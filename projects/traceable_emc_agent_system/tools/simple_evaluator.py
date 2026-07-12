#!/usr/bin/env python3
"""Minimal evaluator for generated MVP run outputs.

v0.4.2: criteria now read each upstream tool's own judgment output
(constraint's `passed`, s2p's `warnings`, evidence's `relevance_score`)
instead of only checking "does the file exist and parse". A tool
producing a file that itself reports failure (constraint not passed,
s2p warnings present, no relevant evidence found) must now fail the
corresponding criterion here too — file existence alone is no longer
treated as success. See docs/CLAUDE_MAINTENANCE_LOG.md MAJOR-2.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def exists(path: str | None) -> bool:
    return bool(path) and Path(path).exists()


def load_json(path: str | None) -> dict | None:
    if not exists(path):
        return None
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def load_jsonl(path: str | None) -> list[dict]:
    if not exists(path):
        return []
    rows: list[dict] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def derive_eval_id(target_id: str) -> str:
    """Derive EVAL-<suffix> from a RUN-<suffix> style target_id.

    Mirrors scripts/run_case.py's derive_suffix() intent: fail loudly
    instead of silently falling back to a hardcoded id, since a wrong
    evaluation_id breaks traceability back to the run it evaluated.
    """
    match = re.search(r"(\d+)\s*$", target_id or "")
    if not match:
        raise ValueError(
            f"cannot derive evaluation_id: target_id {target_id!r} has no numeric suffix"
        )
    return f"EVAL-{match.group(1)}"


def check_s2p(path: str | None) -> tuple[bool, str]:
    data = load_json(path)
    if data is None:
        return False, "s2p result missing or unparseable"
    warnings = data.get("warnings")
    if warnings is None:
        return False, "s2p result has no 'warnings' field (unexpected schema)"
    if warnings:
        return False, f"s2p analysis reported {len(warnings)} warning(s): {warnings}"
    return True, "s2p result exists and reports no warnings"


def check_constraint(path: str | None) -> tuple[bool, str]:
    data = load_json(path)
    if data is None:
        return False, "constraint result missing or unparseable"
    if "passed" not in data:
        return False, "constraint result has no 'passed' field (unexpected schema)"
    if not data["passed"]:
        failed = [c["check_name"] for c in data.get("checks", []) if not c.get("passed", True)]
        return False, f"constraint checks failed: {failed or 'unknown'}"
    return True, "constraint result exists and all checks passed"


def check_evidence(path: str | None) -> tuple[bool, str]:
    rows = load_jsonl(path)
    if not rows:
        return False, "no evidence candidates found"
    scores = [r.get("relevance_score", 0) for r in rows]
    if not any(s and s > 0 for s in scores):
        return False, f"evidence candidates exist but none have relevance_score > 0 ({scores})"
    return True, f"at least one evidence candidate has relevance_score > 0 (max={max(scores)})"


def check_report(path: str | None) -> tuple[bool, str]:
    if not exists(path):
        return False, "report markdown missing"
    if Path(path).stat().st_size == 0:
        return False, "report markdown is empty"
    return True, "report markdown exists and is non-empty"


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate MVP generated outputs.")
    parser.add_argument("--target-id", default="RUN-0002")
    parser.add_argument("--s2p-result")
    parser.add_argument("--constraint-result")
    parser.add_argument("--evidence-jsonl")
    parser.add_argument("--report-md")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    s2p_passed, s2p_notes = check_s2p(args.s2p_result)
    constraint_passed, constraint_notes = check_constraint(args.constraint_result)
    evidence_passed, evidence_notes = check_evidence(args.evidence_jsonl)
    report_passed, report_notes = check_report(args.report_md)

    criteria = [
        ("s2p_result_valid", s2p_passed, "S2P analysis result exists and reports no warnings", s2p_notes),
        ("constraint_result_valid", constraint_passed, "Constraint check result exists and all checks passed", constraint_notes),
        ("evidence_candidates_relevant", evidence_passed, "RAG evidence has at least one candidate with relevance_score > 0", evidence_notes),
        ("report_markdown_exists", report_passed, "Report markdown exists and is non-empty", report_notes),
    ]
    passed_count = sum(1 for _, passed, _, _ in criteria if passed)
    score = 100.0 * passed_count / len(criteria)
    result = {
        "evaluation_id": derive_eval_id(args.target_id),
        "target_type": "run_case",
        "target_id": args.target_id,
        "score": score,
        "passed": score >= 75.0,
        "criteria_results": [
            {
                "criterion_id": cid,
                "description": desc,
                "passed": passed,
                "score": 25.0 if passed else 0.0,
                "notes": notes,
            }
            for cid, passed, desc, notes in criteria
        ],
        "created_at": utc_now(),
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
