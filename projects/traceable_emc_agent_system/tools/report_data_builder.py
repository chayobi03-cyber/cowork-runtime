#!/usr/bin/env python3
"""Build a minimal EMC report draft from generated artifacts."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: str | None):
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def load_jsonl(path: str | None) -> list[dict]:
    if not path:
        return []
    p = Path(path)
    if not p.exists():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def build_markdown(scenario, eda_context, s2p, constraint, evidence) -> str:
    title = scenario.get("title_ko") or scenario.get("title") if scenario else "EMC 분석 보고서 초안"
    lines = [f"# {title}", "", "## 1. 시나리오", ""]
    if scenario:
        lines.append(f"- Scenario ID: `{scenario.get('scenario_id')}`")
        lines.append(f"- Type: `{scenario.get('scenario_type')}`")
    if eda_context:
        lines += ["", "## 2. 회로도/ODB 표시 기반 맥락", "", eda_context.get("summary", "")]
        if eda_context.get("candidate_nets"):
            lines.append(f"- Candidate nets: {', '.join(eda_context['candidate_nets'])}")
        if eda_context.get("candidate_components"):
            lines.append(f"- Candidate components: {', '.join(eda_context['candidate_components'])}")
    if s2p:
        m = s2p.get("metrics", {})
        lines += ["", "## 3. S2P 분석 요약", ""]
        lines.append(f"- Input: `{s2p.get('input_file')}`")
        lines.append(f"- S21 avg: `{m.get('s21_avg_db')}` dB")
        lines.append(f"- S21 min/max: `{m.get('s21_min_db')}` / `{m.get('s21_max_db')}` dB")
        if s2p.get("band_metrics"):
            lines.append("- Band metrics:")
            for band in s2p["band_metrics"]:
                bm = band.get("metrics", {})
                lines.append(f"  - {band.get('band_id')}: S21 avg {bm.get('s21_avg_db')} dB, points {bm.get('point_count')}")
    if constraint:
        lines += ["", "## 4. 제약조건 점검", ""]
        lines.append(f"- Overall passed: `{constraint.get('passed')}`")
        for check in constraint.get("checks", []):
            lines.append(f"- {check.get('check_name')}: passed={check.get('passed')}, value={check.get('value')}, limit={check.get('limit')}")
    if evidence:
        lines += ["", "## 5. RAG 근거 후보", ""]
        for row in evidence:
            lines.append(f"- `{row.get('evidence_candidate_id')}` {row.get('summary')} / relevance={row.get('relevance_score')}")
    lines += ["", "## 6. 검토 필요", "", "- 본 보고서는 MVP 자동 생성 초안이다.", "- RAG 결과는 Evidence Candidate이며, 사람 검토 후 Evidence Ledger에 승격해야 한다.", "- S2P 결과는 입력 Touchstone 파일과 타겟 대역 조건을 재확인해야 한다."]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build minimal EMC report data and Markdown draft.")
    parser.add_argument("--scenario")
    parser.add_argument("--eda-context")
    parser.add_argument("--s2p-result")
    parser.add_argument("--constraint-result")
    parser.add_argument("--evidence-jsonl")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args()

    scenario = load_json(args.scenario)
    eda_context = load_json(args.eda_context)
    s2p = load_json(args.s2p_result)
    constraint = load_json(args.constraint_result)
    evidence = load_jsonl(args.evidence_jsonl)
    md = build_markdown(scenario, eda_context, s2p, constraint, evidence)
    report_data = {
        "report_id": "REPORT-DATA-0001",
        "created_at": utc_now(),
        "scenario_id": scenario.get("scenario_id") if scenario else None,
        "sections": ["scenario", "eda_context", "s2p_analysis", "constraint_check", "rag_evidence_candidates", "review_needed"],
        "source_artifacts": {
            "scenario": args.scenario,
            "eda_context": args.eda_context,
            "s2p_result": args.s2p_result,
            "constraint_result": args.constraint_result,
            "evidence_jsonl": args.evidence_jsonl,
        },
        "review_status": "human_review_required",
    }
    out_json = Path(args.output_json)
    out_md = Path(args.output_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report_data, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(md, encoding="utf-8")
    print(f"[OK] wrote {out_json}")
    print(f"[OK] wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
