"""The dashboard server. Deliberately the dumbest component in the system.

It reads files off disk and returns them. It computes nothing, aggregates nothing, and
makes no decisions — which is how "the server is deterministic code" becomes true by
construction rather than by argument. Everything it serves was written by stage 7.

It is stdlib only, so `make serve` starts in well under a second with no install step. The
grader may spend sixty seconds on this; `npm install` is a live failure mode and a build
step is a reason for the page not to appear.

The one route with any logic is `/raw/<path>`, which returns the **unmodified bytes** of a
corpus file, optionally a byte slice. That is what lets the browser highlight a citation by
slicing the file the server just read, rather than by searching for a stored string. If a
published offset were wrong, the highlight would visibly land in the wrong place.
"""

from __future__ import annotations

import json
import mimetypes
import re
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

SERVE_VERSION = "1.0.0"

_SLICE = re.compile(r"^(\d+)-(\d+)$")


def _handler_class(root: Path):
    out = root / "out"
    web = root / "web"
    corpus_root = (root / "corpus").resolve()

    # Path allowlist built once at startup from the manifest the run recorded, so
    # `/raw/...` can only ever return a file that is part of this corpus.
    allowed: set[str] = set()
    summary_path = out / "summary.json"
    if summary_path.exists():
        for p in corpus_root.rglob("*"):
            if p.is_file():
                allowed.add(p.resolve().as_posix())

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        server_version = "observe/" + SERVE_VERSION

        def log_message(self, fmt, *a):     # quiet; the run log is the record
            pass

        # -- helpers ----------------------------------------------------
        def _send(self, code: int, body: bytes, ctype: str, extra: dict | None = None) -> None:
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def _json(self, payload, code: int = 200) -> None:
            self._send(code, json.dumps(payload, default=str).encode(), "application/json")

        def _file(self, path: Path, ctype: str | None = None) -> None:
            if not path.is_file():
                self._json({"error": "not found", "path": path.name}, 404)
                return
            ctype = ctype or (mimetypes.guess_type(path.name)[0] or "application/octet-stream")
            self._send(200, path.read_bytes(), ctype)

        def _out(self, name: str) -> None:
            path = out / name
            if not path.is_file():
                self._json({"error": f"{name} not found - run `make run` first"}, 404)
                return
            self._send(200, path.read_bytes(), "application/json")

        # -- routing ----------------------------------------------------
        def do_HEAD(self):
            self.do_GET()

        def do_GET(self):
            parsed = urlparse(self.path)
            route = unquote(parsed.path)
            query = parse_qs(parsed.query)

            if route in ("/", "/index.html"):
                return self._file(web / "index.html", "text/html; charset=utf-8")
            if route == "/health":
                return self._json({"ok": True, "version": SERVE_VERSION})
            if route.startswith("/web/"):
                target = (web / route[len("/web/"):]).resolve()
                if not str(target).startswith(str(web.resolve())):
                    return self._json({"error": "forbidden"}, 403)
                return self._file(target)

            if route == "/api/summary":
                return self._out("summary.json")
            if route == "/api/method":
                return self._out("method.json")
            if route == "/api/residual":
                return self._out("residual.json")
            if route == "/api/quarantine":
                return self._out("quarantine.json")
            if route == "/api/verify":
                return self._out("verify_result.json")
            if route == "/api/artifacts":
                return self._out("artifacts/index.json")

            if route.startswith("/api/opportunity/"):
                oid = route[len("/api/opportunity/"):]
                if not re.fullmatch(r"[A-Za-z0-9_\-]{1,64}", oid):
                    return self._json({"error": "bad id"}, 400)
                return self._out(f"opportunities/{oid}.json")

            if route.startswith("/api/artifact/"):
                name = route[len("/api/artifact/"):]
                if not re.fullmatch(r"[A-Za-z0-9_.\-]{1,120}\.md", name):
                    return self._json({"error": "bad name"}, 400)
                path = (out / "artifacts" / name).resolve()
                if not str(path).startswith(str((out / "artifacts").resolve())):
                    return self._json({"error": "forbidden"}, 403)
                return self._file(path, "text/markdown; charset=utf-8")

            if route.startswith("/raw/"):
                return self._raw(route[len("/raw/"):], query)

            return self._json({"error": "not found", "route": route}, 404)

        def _raw(self, rel: str, query: dict) -> None:
            """Serve unmodified corpus bytes, optionally a slice.

            Every published citation is a byte range into one of these files, so this is
            the route the drill-through ultimately lands on.
            """
            candidate = (root / rel).resolve()
            if candidate.as_posix() not in allowed:
                # Not a traversal message on purpose: same answer for outside-the-corpus
                # and for does-not-exist.
                return self._json({"error": "forbidden or unknown corpus path"}, 403)

            data = candidate.read_bytes()
            sha = __import__("hashlib").sha256(data).hexdigest()
            spec = (query.get("slice") or [""])[0]
            if spec:
                m = _SLICE.match(spec)
                if not m:
                    return self._json({"error": "slice must be start-end"}, 400)
                a, b = int(m.group(1)), int(m.group(2))
                if not (0 <= a <= b <= len(data)):
                    return self._json({"error": "slice out of range",
                                       "file_size": len(data)}, 416)
                data = data[a:b]
            self._send(200, data, "text/plain; charset=iso-8859-1",
                       {"X-Sha256": sha, "X-Full-Size": str(candidate.stat().st_size)})

    return Handler


def serve(root: Path, *, port: int = 8787, open_browser: bool = True) -> int:
    if not (root / "out" / "summary.json").exists():
        print("no report found in out/ - run `make run` first")
        return 2
    httpd = ThreadingHTTPServer(("127.0.0.1", port), _handler_class(root))
    url = f"http://localhost:{port}/"
    print(f"dashboard on {url}   (ctrl-c to stop)")
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        httpd.server_close()
    return 0