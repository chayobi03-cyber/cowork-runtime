#!/usr/bin/env python3
"""Run the MVP Traceable EMC Agent case.

Pipeline:
1. Parse human-guided EDA annotation.
2. Retrieve simple RAG evidence candidates.
3. Analyze S2P file.
4. Run simple constraint checks.
5. Build report draft.
6. Run file-level evaluator.
7. Append minimal event ledger and write run case summary.

This is a harness skeleton, not a full autonomous Agent.

Patch note (managed by Claude, see docs/CLAUDE_MAINTENANCE_LOG.md):
    Sub-artifact IDs (EDA-CTX-*, RAGQ-*, S2P-RUN-*, CONSTRAINT-RUN-*, EVT-*) used to be
    hardcoded to the literal "0002" suffix regardless of --run-id, so two different runs
    silently collided on the same files. IDs are now derived from --run-id's own numeric
    suffix so each run gets distinct, schema-valid, traceable artifact IDs.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RUN_ID_PATTERN = re.compile(r"^RUN-([0-9]{4,})$")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def run(cmd: list[str]) -> None:
    print("[RUN]", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def derive_suffix(run_id: str) -> str:
    """Extract the numeric suffix from a RUN-#### style run_id.

    Fails loudly (instead of silently falling back to a hardcoded value) if
    run_id does not match the schema-required pattern, since every downstream
    sub-artifact ID is derived from it.
    """
    match = RUN_ID_PATTERN.match(run_id)
    if not match:
        raise SystemExit(
            f"--run-id must match ^RUN-[0-9]{{4,}}$ (schemas/harness/run_case.schema.json), "
            f"got: {run_id!r}"
        )
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run MVP traceable EMC case.")
    parser.add_argument("--scenario", default="data/sample/scenarios/SCN-0001.json")
    parser.add_argument("--annotation", default="data/sample/annotations/ANN-0001.json")
    parser.add_argument("--s2p", default="data/sample/inputs/s2p_real/BLM18SG221TN1_series.s2p.txt")
    parser.add_argument("--rag-corpus", default="data/sample/rag/corpora")
    parser.add_argument("--query", default="SPK 라인 EMI 필터 시험법 불량현상 설계사양 ferrite bead speaker cable")
    parser.add_argument("--out-dir", default="data/sample/generated")
    parser.add_argument("--run-id", default="RUN-0002")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    run_id = args.run_id
    suffix = derive_suffix(run_id)
    started_at = utc_now()

    eda_ctx_id = f"EDA-CTX-{suffix}"
    ragq_id = f"RAGQ-{suffix}"
    s2p_run_id = f"S2P-RUN-{suffix}"
    constraint_run_id = f"CONSTRAINT-RUN-{suffix}"
    evt_start_id = f"EVT-{suffix}1"
    evt_finish_id = f"EVT-{suffix}2"

    generated = {
        "eda_context": out_dir / "annotations" / f"{eda_ctx_id}.json",
        "evidence": out_dir / "rag" / f"evidence_candidates_{suffix}.jsonl",
        "s2p": out_dir / "tool_outputs" / f"{s2p_run_id}.json",
        "constraint": out_dir / "tool_outputs" / f"{constraint_run_id}.json",
        "report_json": out_dir / "reports" / f"REPORT-DATA-{suffix}.json",
        "report_md": out_dir / "reports" / f"emc_report_draft_{suffix}.md",
        "evaluation": out_dir / "evaluation" / f"EVAL-{suffix}.json",
        "run_case": out_dir / "harness" / f"{run_id}.json",
        "event_ledger": out_dir / "ledgers" / "event_ledger.jsonl",
    }

    append_jsonl(
        ROOT / generated["event_ledger"],
        {
            "event_id": evt_start_id,
            "timestamp": started_at,
            "event_type": "run_started",
            "actor": "scripts/run_case.py",
            "target": run_id,
            "summary": "MVP case run started",
            "related_run_id": run_id,
            "related_scenario_id": "SCN-0001",
            "severity": "info",
        },
    )

    run([sys.executable, "tools/annotation_parser.py", "--input", args.annotation, "--output", str(generated["eda_context"]), "--context-id", eda_ctx_id])
    run([sys.executable, "tools/simple_rag_retriever.py", "--corpus", args.rag_corpus, "--query", args.query, "--output", str(generated["evidence"]), "--query-id", ragq_id, "--limit", "5"])
    run([
        sys.executable,
        "tools/s2p_analyzer.py",
        "--input",
        args.s2p,
        "--output",
        str(generated["s2p"]),
        "--run-id",
        s2p_run_id,
        "--band",
        "EMI_LOW:30000000:300000000",
        "--band",
        "EMI_HIGH:300000000:1000000000",
    ])
    run([
        sys.executable,
        "tools/constraint_checker.py",
        "--output",
        str(generated["constraint"]),
        "--run-id",
        constraint_run_id,
        "--candidate-id",
        "BLM18SG221TN1",
        "--rated-current-a",
        "1.0",
        "--required-current-a",
        "0.5",
        "--dcr-ohm",
        "0.05",
        "--max-dcr-ohm",
        "0.5",
        "--height-mm",
        "0.6",
        "--max-height-mm",
        "1.0",
        "--package",
        "0603",
        "--allowed-package",
        "0402,0603,1005,1608",
    ])
    run([
        sys.executable,
        "tools/report_data_builder.py",
        "--scenario",
        args.scenario,
        "--eda-context",
        str(generated["eda_context"]),
        "--s2p-result",
        str(generated["s2p"]),
        "--constraint-result",
        str(generated["constraint"]),
        "--evidence-jsonl",
        str(generated["evidence"]),
        "--output-json",
        str(generated["report_json"]),
        "--output-md",
        str(generated["report_md"]),
    ])
    run([
        sys.executable,
        "tools/simple_evaluator.py",
        "--target-id",
        run_id,
        "--s2p-result",
        str(generated["s2p"]),
        "--constraint-result",
        str(generated["constraint"]),
        "--evidence-jsonl",
        str(generated["evidence"]),
        "--report-md",
        str(generated["report_md"]),
        "--output",
        str(generated["evaluation"]),
    ])

    finished_at = utc_now()
    output_paths = [str(p) for k, p in generated.items() if k not in {"event_ledger", "run_case"}]
    run_case = {
        "run_id": run_id,
        "scenario_id": "SCN-0001",
        "run_mode": "full_case",
        "started_at": started_at,
        "finished_at": finished_at,
        "nodes_to_run": [
            "02_04_annotation_parser",
            "03_04_rag_retriever",
            "04_01_s2p_tools",
            "04_03_constraint_tools",
            "08_01_tool_evaluation",
        ],
        "input_bundle_path": args.scenario,
        "output_paths": output_paths,
        "status": "completed",
    }
    run_case_path = ROOT / generated["run_case"]
    run_case_path.parent.mkdir(parents=True, exist_ok=True)
    run_case_path.write_text(json.dumps(run_case, ensure_ascii=False, indent=2), encoding="utf-8")

    append_jsonl(
        ROOT / generated["event_ledger"],
        {
            "event_id": evt_finish_id,
            "timestamp": finished_at,
            "event_type": "run_finished",
            "actor": "scripts/run_case.py",
            "target": run_id,
            "summary": "MVP case run completed",
            "related_run_id": run_id,
            "related_scenario_id": "SCN-0001",
            "related_artifacts": output_paths,
            "severity": "info",
        },
    )
    print(f"[OK] wrote {run_case_path}")
    print(f"[OK] report: {ROOT / generated['report_md']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
