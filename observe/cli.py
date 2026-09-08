"""One command. `observe run` is the whole system.

    observe doctor    one real model call, to fail fast with a specific remedy
    observe run       the full pipeline
    observe verify    re-verify the published report; no model
    observe serve     the dashboard

`run` is safe to re-run: everything is content-addressed, so an unchanged corpus is a
cache-hit replay in seconds and an interrupted run resumes by simply running it again.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path


def cmd_doctor(args) -> int:
    from observe.claude_cli import doctor
    report = doctor()
    print(json.dumps(report, indent=2))
    if not report.get("ok"):
        print("\nDOCTOR FAILED. " + str(report.get("remedy", "")), file=sys.stderr)
        return 1
    print(f"\nOK - CLI at {report['cli_path']} answered in {report['latency_ms']}ms")
    return 0


def cmd_run(args) -> int:
    from observe.claude_cli import doctor
    from observe.dispatch import AuthenticationFailed
    from observe.pipeline import (
        new_context, stage0, stage1, stage2, stage3, stage45, stage6, stage7)
    from observe.recurring import find_series

    root = Path(args.root).resolve()
    started = time.time()

    if not args.skip_doctor:
        # Before anything expensive, so a run cannot burn twenty minutes discovering the
        # CLI was never authenticated.
        report = doctor()
        if not report.get("ok"):
            print(f"pre-flight failed: {report.get('error')}\n{report.get('remedy','')}",
                  file=sys.stderr)
            return 1
        print(f"[doctor] {report['cli_path']} ok ({report['latency_ms']}ms)")

    ctx = new_context(root, run_id=args.run_id, concurrency=args.concurrency,
                      deadline_s=args.deadline * 60)
    ctx.cache.start_run(ctx.run_id, "")
    print(f"[run {ctx.run_id}] deadline {args.deadline} min, concurrency {args.concurrency}")

    try:
        corpus = stage0(ctx)
        print(f"[0/7] parse       {corpus_line(ctx)}")
        extractions = stage1(ctx, corpus, model=args.extract_model)
        print(f"[1/7] extract     {stage_line(ctx, 'stage1')}")
        clusters, records = stage2(ctx, corpus, extractions, method=args.cluster_method)
        print(f"[2/7] cluster     {stage_line(ctx, 'stage2')}")
        characterizations = stage3(ctx, clusters, records, model=args.characterize_model)
        print(f"[3/7] describe    {stage_line(ctx, 'stage3')}")
        series = find_series(corpus.survivors, corpus.address_to_person)
        opportunities, rejected = stage45(ctx, corpus, clusters, records,
                                          characterizations, series)
        print(f"[4/7] cite+cost   {stage_line(ctx, 'stage45')}")
        artifacts, skipped = stage6(ctx, opportunities, model=args.artifact_model)
        print(f"[5/7] act         {stage_line(ctx, 'stage6')}")
        summary = stage7(ctx, corpus, opportunities, clusters, rejected, artifacts)
        print(f"[6/7] render      out/report.md, out/summary.json")
    except AuthenticationFailed as e:
        ctx.cache.finish_run(ctx.run_id, "auth_failed", str(e))
        print(f"\nAUTHENTICATION FAILED: {e}\nRun `claude auth login`.", file=sys.stderr)
        return 1

    rc = 0
    if not args.no_verify:
        from observe.verify import verify
        rep = verify(root / "out", root / "corpus")
        (root / "out" / "verify_result.json").write_text(json.dumps({
            "verify_version": "1.0.0", "passed": rep.passed, "checks": rep.checks,
            "failures": rep.failures, "warnings": rep.warnings,
            "citation_tiers": rep.tiers,
        }, indent=2) + "\n")
        status = "PASS" if rep.passed else "FAIL"
        print(f"[7/7] verify      {status}: {rep.checks} checks, {len(rep.failures)} failures")
        for f in rep.failures[:8]:
            print(f"        FAIL {f['kind']}: {f['detail'][:140]}")
        rc = 0 if rep.passed else 1

    ctx.cache.finish_run(ctx.run_id, "ok" if rc == 0 else "verify_failed")
    h = summary["headline"]
    d = h["dollars_per_month"]
    print(f"\n  ${d['base']:,.0f}/month  (range ${d['low']:,.0f} - ${d['high']:,.0f})")
    print(f"  {h['counted_opportunities']} opportunities, "
          f"{summary['evidence']['citations_verified']} verified citations, "
          f"{len(artifacts)} artifacts drafted")
    print(f"  {summary['attribution']['share_attributed']:.0%} of operational messages "
          f"attributed to an identified process (the rest is uncosted long tail)")
    print(f"\n  total {time.time() - started:.0f}s   report out/report.md   "
          f"dashboard: observe serve")
    return rc


def corpus_line(ctx) -> str:
    s = ctx.stats["stage0"]
    return (f"{s['files']:,} files -> {s['survivors']:,} unique -> "
            f"{s['task_instances']:,} task instances ({s['seconds']}s)")


def stage_line(ctx, key: str) -> str:
    s = ctx.stats.get(key, {})
    return ", ".join(f"{k}={v}" for k, v in s.items() if not k.startswith("_"))


def cmd_verify(args) -> int:
    from observe.verify import main as verify_main
    argv = ["--out", str(args.out), "--corpus", str(args.corpus)]
    if args.sample:
        argv += ["--sample", str(args.sample), "--seed", str(args.seed)]
    return verify_main(argv)


def cmd_serve(args) -> int:
    from observe.serve import serve
    return serve(Path(args.root).resolve(), port=args.port, open_browser=not args.no_open)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="observe", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("doctor", help="check the CLI is present and authenticated")
    d.set_defaults(func=cmd_doctor)

    r = sub.add_parser("run", help="run the full pipeline")
    r.add_argument("--root", default=".")
    r.add_argument("--run-id", default=None)
    r.add_argument("--concurrency", type=int, default=8)
    r.add_argument("--deadline", type=float, default=25, help="minutes")
    r.add_argument("--extract-model", default="sonnet")
    r.add_argument("--characterize-model", default="opus")
    r.add_argument("--artifact-model", default="opus")
    r.add_argument("--cluster-method", default="tfidf", choices=["tfidf", "components"])
    r.add_argument("--skip-doctor", action="store_true")
    r.add_argument("--no-verify", action="store_true")
    r.set_defaults(func=cmd_run)

    v = sub.add_parser("verify", help="re-verify the published report; no model calls")
    v.add_argument("--out", default="out", type=Path)
    v.add_argument("--corpus", default="corpus", type=Path)
    v.add_argument("--sample", type=int, default=0)
    v.add_argument("--seed", type=int, default=7)
    v.set_defaults(func=cmd_verify)

    s = sub.add_parser("serve", help="serve the dashboard on localhost")
    s.add_argument("--root", default=".")
    s.add_argument("--port", type=int, default=8787)
    s.add_argument("--no-open", action="store_true")
    s.set_defaults(func=cmd_serve)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
