#!/usr/bin/env python3
"""Validate artifact instances (curated samples + generated outputs +
tool contracts) against their JSON Schemas.

Consolidated (2026-07-14, Claude, see docs/CLAUDE_MAINTENANCE_LOG.md) from
three previously separate scripts that shared the same load->validate->collect
skeleton and only differed in which directory/pattern they scanned:
  - validate_artifacts.py           (hardcoded fixed sample file paths)
  - validate_generated_artifacts.py (glob patterns under data/sample/generated/)
  - validate_tool_contracts.py      (glob pattern under data/sample/tool_contracts/)

Consolidating also closes a latent coverage gap: the old validate_artifacts.py
hardcoded exactly one tool_contracts fixture (TOOL-S2P-ANALYZER.json) while five
other TOOL-*.json fixtures existed unchecked under data/sample/tool_contracts/
(TOOL-ANNOTATION-PARSER, TOOL-CONSTRAINT-CHECKER, TOOL-REPORT-DATA-BUILDER,
TOOL-SIMPLE-EVALUATOR, TOOL-SIMPLE-RAG-RETRIEVER). Using glob patterns
everywhere (not just for generated/) closes this same class of gap for every
group, not only tool_contracts.
"""
from __future__ import annotations

import json
from pathlib import Path

from _validate_utils import ROOT, load_json, print_result, validate_instance

# (glob pattern relative to ROOT, schema path relative to ROOT, required)
# required=True: at least one match must exist, or this is a FAIL (protects
#   against a fixture being silently deleted/renamed).
# required=False: zero matches is OK (e.g. generated/ outputs from runs that
#   simply haven't happened yet in this environment).
JSON_GLOBS: list[tuple[str, str, bool]] = [
    ('data/sample/context/*.json', 'schemas/context/context_bundle.schema.json', True),
    ('data/sample/scenarios/*.json', 'schemas/context/scenario_card.schema.json', True),
    ('data/sample/annotations/ANN-*.json', 'schemas/annotation/annotation.schema.json', True),
    ('data/sample/annotations/EDA-CTX-*.json', 'schemas/annotation/parsed_eda_context.schema.json', True),
    ('data/sample/rag/documents/*.json', 'schemas/rag/rag_document.schema.json', True),
    ('data/sample/rag/queries/*.json', 'schemas/rag/rag_query.schema.json', True),
    ('data/sample/tool_outputs/S2P-RUN-*.json', 'schemas/tools/s2p_analysis_result.schema.json', True),
    ('data/sample/tool_outputs/CONSTRAINT-RUN-*.json', 'schemas/tools/constraint_check_result.schema.json', True),
    ('data/sample/harness/RUN-*.json', 'schemas/harness/run_case.schema.json', True),
    ('data/sample/evaluation/EVAL-*.json', 'schemas/evaluation/evaluation_score.schema.json', True),
    ('data/sample/tool_fit/*.json', 'schemas/tool_fit/tool_fit_review.schema.json', True),
    ('data/sample/workflow_backlog/*.json', 'schemas/workflow/workflow_backlog.schema.json', True),
    ('data/sample/tool_contracts/TOOL-*.json', 'schemas/tools/tool_contract.schema.json', True),
    ('data/sample/generated/annotations/EDA-CTX-*.json', 'schemas/annotation/parsed_eda_context.schema.json', False),
    ('data/sample/generated/tool_outputs/S2P-RUN-*.json', 'schemas/tools/s2p_analysis_result.schema.json', False),
    ('data/sample/generated/tool_outputs/CONSTRAINT-RUN-*.json', 'schemas/tools/constraint_check_result.schema.json', False),
    ('data/sample/generated/harness/RUN-*.json', 'schemas/harness/run_case.schema.json', False),
    ('data/sample/generated/evaluation/EVAL-*.json', 'schemas/evaluation/evaluation_score.schema.json', False),
]

JSONL_GLOBS: list[tuple[str, str, bool]] = [
    ('data/sample/rag/evidence_candidates.jsonl', 'schemas/rag/evidence_candidate.schema.json', True),
    ('data/sample/ledgers/event_ledger.jsonl', 'schemas/ledger/event_ledger_event.schema.json', True),
    ('data/sample/ledgers/tool_selection_log.jsonl', 'schemas/ledger/tool_selection_entry.schema.json', True),
    ('data/sample/generated/rag/evidence_candidates*.jsonl', 'schemas/rag/evidence_candidate.schema.json', False),
    ('data/sample/generated/ledgers/event_ledger.jsonl', 'schemas/ledger/event_ledger_event.schema.json', False),
]


def _validate_json_glob(pattern: str, schema_rel: str, required: bool, errors: list[str]) -> int:
    schema = load_json(ROOT / schema_rel)
    matches = sorted(ROOT.glob(pattern))
    if not matches:
        if required:
            errors.append(f'no artifact matched required pattern: {pattern}')
        return 0
    checked = 0
    for path in matches:
        checked += 1
        try:
            instance = load_json(path)
        except Exception as exc:
            errors.append(f'{path.relative_to(ROOT)}: invalid JSON: {exc}')
            continue
        errors.extend(validate_instance(instance, schema, path))
    return checked


def _validate_jsonl_glob(pattern: str, schema_rel: str, required: bool, errors: list[str]) -> int:
    schema = load_json(ROOT / schema_rel)
    matches = sorted(ROOT.glob(pattern))
    if not matches:
        if required:
            errors.append(f'no jsonl artifact matched required pattern: {pattern}')
        return 0
    checked = 0
    for path in matches:
        with path.open('r', encoding='utf-8') as f:
            for idx, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                checked += 1
                try:
                    instance = json.loads(line)
                except Exception as exc:
                    errors.append(f'{path.relative_to(ROOT)}:{idx}: invalid JSON line: {exc}')
                    continue
                errors.extend(validate_instance(instance, schema, Path(f'{path}:{idx}')))
    return checked


def main() -> int:
    errors: list[str] = []
    checked_count = 0
    for pattern, schema_rel, required in JSON_GLOBS:
        checked_count += _validate_json_glob(pattern, schema_rel, required, errors)
    for pattern, schema_rel, required in JSONL_GLOBS:
        checked_count += _validate_jsonl_glob(pattern, schema_rel, required, errors)
    return print_result(errors, f'artifacts validated ({checked_count} files/lines checked)')


if __name__ == '__main__':
    raise SystemExit(main())
