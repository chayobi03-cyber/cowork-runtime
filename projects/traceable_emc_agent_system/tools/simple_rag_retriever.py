#!/usr/bin/env python3
"""Simple keyword RAG retriever for MVP.

This is intentionally lightweight: no vector DB, no external dependency.
It scans Markdown files, scores token overlap, and writes Evidence Candidate
JSONL compatible with schemas/rag/evidence_candidate.schema.json.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

TOKEN_RE = re.compile(r"[A-Za-z0-9가-힣_+\-/]+")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def tokenize(text: str) -> set[str]:
    return {t.lower() for t in TOKEN_RE.findall(text) if len(t) >= 2}


def summarize(text: str, query_tokens: set[str], max_chars: int = 420) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    scored = []
    for line in lines:
        score = len(tokenize(line) & query_tokens)
        scored.append((score, line))
    scored.sort(key=lambda x: x[0], reverse=True)
    chosen = [line for score, line in scored[:3] if score > 0]
    if not chosen:
        chosen = lines[:3]
    summary = " / ".join(chosen)
    if len(summary) > max_chars:
        summary = summary[: max_chars - 3] + "..."
    return summary


def doc_type_from_path(path: Path) -> str:
    parts = set(path.parts)
    if "test_methods" in parts:
        return "test_method"
    if "failure_cases" in parts:
        return "failure_case"
    if "design_specs" in parts:
        return "design_spec"
    if "vendor_guides" in parts:
        return "vendor_guide"
    if "standards" in parts or "standard_summaries" in parts:
        return "standard_summary"
    return "other"


def retrieve(corpus_dir: Path, query: str, query_id: str, limit: int) -> list[dict]:
    query_tokens = tokenize(query)
    docs = sorted(corpus_dir.rglob("*.md"))
    scored_docs = []
    for doc in docs:
        text = doc.read_text(encoding="utf-8", errors="ignore")
        doc_tokens = tokenize(text + " " + doc.name)
        overlap = len(query_tokens & doc_tokens)
        if overlap == 0:
            continue
        relevance = min(1.0, overlap / max(1, len(query_tokens)))
        scored_docs.append((relevance, overlap, doc, text))

    scored_docs.sort(key=lambda item: (item[0], item[1], str(item[2])), reverse=True)
    candidates: list[dict] = []
    for idx, (relevance, overlap, doc, text) in enumerate(scored_docs[:limit], start=1):
        doc_stem = re.sub(r"[^A-Za-z0-9]+", "-", doc.stem).strip("-").upper() or f"DOC-{idx:04d}"
        candidates.append(
            {
                "evidence_candidate_id": f"EVC-{idx:04d}",
                "source_doc_id": doc_stem,
                "query_id": query_id,
                "matched_text_ref": str(doc),
                "summary": summarize(text, query_tokens),
                "relevance_score": round(float(relevance), 3),
                "source_quality_score": 0.7 if doc_type_from_path(doc) in {"test_method", "design_spec"} else 0.6,
                "applicability_note": f"keyword overlap={overlap}; doc_type={doc_type_from_path(doc)}; human review required before evidence ledger promotion",
                "limitations": ["MVP keyword retrieval only", "semantic similarity is not yet implemented"],
                "linked_scenario_id": "SCN-0001",
                "review_status": "needs_human_review",
                "created_at": utc_now(),
            }
        )
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser(description="Run simple keyword RAG retrieval.")
    parser.add_argument("--corpus", required=True, help="Corpus root directory")
    parser.add_argument("--query", required=True, help="Query text")
    parser.add_argument("--output", required=True, help="Output JSONL path")
    parser.add_argument("--query-id", default="RAGQ-0002")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    candidates = retrieve(Path(args.corpus), args.query, args.query_id, args.limit)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for row in candidates:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"[OK] wrote {len(candidates)} candidates to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
