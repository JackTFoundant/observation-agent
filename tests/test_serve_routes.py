"""The dashboard server: every route, and the ways it must refuse.

`/raw/<path>` hands out corpus bytes, so its refusals matter more than its successes. The
tests below run against a real server on an ephemeral port, with no model involved.
"""

from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

from observe.serve import _handler_class

ROOT = Path(__file__).resolve().parents[1]
HAS_REPORT = (ROOT / "out" / "summary.json").exists()
pytestmark = pytest.mark.skipif(
    not HAS_REPORT, reason="no published report in out/; run `make run` first")


@pytest.fixture(scope="module")
def server():
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), _handler_class(ROOT))
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()
    httpd.server_close()


def get(base: str, path: str):
    with urllib.request.urlopen(base + path, timeout=10) as r:
        return r.status, r.read(), dict(r.headers)


def status_of(base: str, path: str) -> int:
    try:
        with urllib.request.urlopen(base + path, timeout=10) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


# ---------------------------------------------------------------------------
# Success paths
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("path", [
    "/", "/health", "/api/summary", "/api/method", "/api/quarantine",
    "/api/residual", "/api/verify", "/web/app.js", "/web/styles.css",
])
def test_routes_serve(server, path):
    status, body, _headers = get(server, path)
    assert status == 200
    assert body


def test_summary_is_valid_json_with_the_fields_the_ui_needs(server):
    _s, body, _h = get(server, "/api/summary")
    data = json.loads(body)
    for key in ("headline", "opportunities", "attribution", "evidence", "corpus", "scope_line"):
        assert key in data, key
    assert "dollars_per_month" in data["headline"]


def test_opportunity_route_serves_each_listed_opportunity(server):
    _s, body, _h = get(server, "/api/summary")
    for row in json.loads(body)["opportunities"][:4]:
        status, payload, _h2 = get(server, f"/api/opportunity/{row['opportunity_id']}")
        assert status == 200
        opp = json.loads(payload)
        assert opp["opportunity_id"] == row["opportunity_id"]
        assert "derivation" in opp


# ---------------------------------------------------------------------------
# /raw — the drill-through target
# ---------------------------------------------------------------------------

def _first_citation() -> dict:
    summary = json.loads((ROOT / "out" / "summary.json").read_text())
    for row in summary["opportunities"]:
        path = ROOT / "out" / "opportunities" / f"{row['opportunity_id']}.json"
        if path.exists():
            cits = json.loads(path.read_text()).get("citations") or []
            if cits:
                return cits[0]
    pytest.skip("no citations in the published report")


def test_raw_returns_unmodified_bytes_with_a_hash(server):
    cit = _first_citation()
    status, body, headers = get(server, "/raw/" + cit["source_path"])
    assert status == 200
    on_disk = (ROOT / cit["source_path"]).read_bytes()
    assert body == on_disk
    assert headers["X-Sha256"] == cit["source_sha256"]


def test_raw_slice_returns_exactly_the_cited_bytes(server):
    """The whole drill-through rests on this: the published byte range *is* the quote."""
    cit = _first_citation()
    a, b = cit["raw_start"], cit["raw_end"]
    _s, body, _h = get(server, f"/raw/{cit['source_path']}?slice={a}-{b}")
    assert body.decode("latin-1") == cit["quote"]


def test_raw_refuses_a_path_outside_the_corpus(server):
    assert status_of(server, "/raw/NOTES.md") == 403
    assert status_of(server, "/raw/observe/serve.py") == 403


def test_raw_refuses_traversal(server):
    for attempt in (
        "/raw/../../../../etc/passwd",
        "/raw/corpus/../NOTES.md",
        "/raw/%2e%2e%2f%2e%2e%2fetc%2fpasswd",
    ):
        assert status_of(server, attempt) in (403, 404), attempt


def test_raw_refuses_an_out_of_range_slice(server):
    cit = _first_citation()
    assert status_of(server, f"/raw/{cit['source_path']}?slice=0-99999999") == 416


def test_raw_refuses_a_malformed_slice(server):
    cit = _first_citation()
    assert status_of(server, f"/raw/{cit['source_path']}?slice=abc") == 400


# ---------------------------------------------------------------------------
# Rejections elsewhere
# ---------------------------------------------------------------------------

def test_unknown_route_is_404(server):
    assert status_of(server, "/api/nope") == 404


def test_opportunity_id_is_validated(server):
    assert status_of(server, "/api/opportunity/..%2F..%2Fsummary") in (400, 404)
    assert status_of(server, "/api/opportunity/" + "x" * 200) in (400, 404)


def test_artifact_name_is_validated(server):
    assert status_of(server, "/api/artifact/../../summary.json") in (400, 403, 404)
    assert status_of(server, "/api/artifact/not-markdown.py") == 400


def test_web_route_cannot_escape_the_web_directory(server):
    assert status_of(server, "/web/../observe/serve.py") in (403, 404)


def test_server_does_no_computation(server):
    """Two identical requests must return byte-identical bodies.

    The server's job is to read files. If it were aggregating or deriving anything, this
    is where a timestamp or a re-ordered dict would show up — and 'the server is
    deterministic code' would stop being true by construction.
    """
    _s1, a, _h1 = get(server, "/api/summary")
    _s2, b, _h2 = get(server, "/api/summary")
    assert a == b