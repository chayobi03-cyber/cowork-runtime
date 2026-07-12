from __future__ import annotations

import json
from pathlib import Path

from _validate_utils import ROOT, load_json, print_result, validate_instance

ARTIFACT_SCHEMA_MAP = {
    'data/sample/context/CTX-0001.json': 'schemas/context/context_bundle.schema.json',
    'data/sample/scenarios/SCN-0001.json': 'schemas/context/scenario_card.schema.json',
    'data/sample/annotations/ANN-0001.json': 'schemas/annotation/annotation.schema.json',
    'data/sample/annotations/EDA-CTX-0001.json': 'schemas/annotation/parsed_eda_context.schema.json',
    'data/sample/rag/documents/DOC-0001.json': 'schemas/rag/rag_document.schema.json',
    'data/sample/rag/queries/RAGQ-0001.json': 'schemas/rag/rag_query.schema.json',
    'data/sample/tool_outputs/S2P-RUN-0001.json': 'schemas/tools/s2p_analysis_result.schema.json',
    'data/sample/tool_outputs/CONSTRAINT-RUN-0001.json': 'schemas/tools/constraint_check_result.schema.json',
    'data/sample/harness/RUN-0001.json': 'schemas/harness/run_case.schema.json',
    'data/sample/evaluation/EVAL-0001.json': 'schemas/evaluation/evaluation_score.schema.json',
    'data/sample/tool_fit/TOOLFIT-0001.json': 'schemas/tool_fit/tool_fit_review.schema.json',
    'data/sample/workflow_backlog/WF-0001.json': 'schemas/workflow/workflow_backlog.schema.json',
    'data/sample/tool_contracts/TOOL-S2P-ANALYZER.json': 'schemas/tools/tool_contract.schema.json',
}

JSONL_SCHEMA_MAP = {
    'data/sample/rag/evidence_candidates.jsonl': 'schemas/rag/evidence_candidate.schema.json',
    'data/sample/ledgers/event_ledger.jsonl': 'schemas/ledger/event_ledger_event.schema.json',
    'data/sample/ledgers/tool_selection_log.jsonl': 'schemas/ledger/tool_selection_entry.schema.json',
}


def main() -> int:
    errors: list[str] = []
    for rel, schema_rel in ARTIFACT_SCHEMA_MAP.items():
        path = ROOT / rel
        schema_path = ROOT / schema_rel
        if not path.exists():
            errors.append(f'missing artifact: {rel}')
            continue
        if not schema_path.exists():
            errors.append(f'missing schema: {schema_rel}')
            continue
        try:
            instance = load_json(path)
            schema = load_json(schema_path)
        except Exception as exc:
            errors.append(f'{rel}: invalid JSON: {exc}')
            continue
        errors.extend(validate_instance(instance, schema, path))

    for rel, schema_rel in JSONL_SCHEMA_MAP.items():
        path = ROOT / rel
        schema_path = ROOT / schema_rel
        if not path.exists():
            errors.append(f'missing jsonl artifact: {rel}')
            continue
        schema = load_json(schema_path)
        with path.open('r', encoding='utf-8') as f:
            for idx, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                try:
                    instance = json.loads(line)
                except Exception as exc:
                    errors.append(f'{rel}:{idx}: invalid JSON line: {exc}')
                    continue
                errors.extend(validate_instance(instance, schema, Path(f'{path}:{idx}')))
    return print_result(errors, 'sample artifacts validated')


if __name__ == '__main__':
    raise SystemExit(main())
