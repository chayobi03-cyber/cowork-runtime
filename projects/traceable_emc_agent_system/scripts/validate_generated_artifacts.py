#!/usr/bin/env python3
"""Validate generated case artifacts against their JSON Schemas.

Patch note (managed by Claude, see docs/CLAUDE_MAINTENANCE_LOG.md):
    This used to hardcode the single default run's filenames (the "0002"
    suffix), so it silently ignored any artifact produced by a different
    --run-id passed to scripts/run_case.py. It now glob-discovers artifacts
    by pattern so every generated run is actually checked, not just the
    default demo run.
"""
from __future__ import annotations

import json
from pathlib import Path

from _validate_utils import ROOT, load_json, print_result, validate_instance

# glob pattern (relative to ROOT) -> schema path (relative to ROOT)
ARTIFACT_SCHEMA_GLOBS = {
    'data/sample/generated/annotations/EDA-CTX-*.json': 'schemas/annotation/parsed_eda_context.schema.json',
    'data/sample/generated/tool_outputs/S2P-RUN-*.json': 'schemas/tools/s2p_analysis_result.schema.json',
    'data/sample/generated/tool_outputs/CONSTRAINT-RUN-*.json': 'schemas/tools/constraint_check_result.schema.json',
    'data/sample/generated/harness/RUN-*.json': 'schemas/harness/run_case.schema.json',
    'data/sample/generated/evaluation/EVAL-*.json': 'schemas/evaluation/evaluation_score.schema.json',
}

JSONL_SCHEMA_GLOBS = {
    'data/sample/generated/rag/evidence_candidates*.jsonl': 'schemas/rag/evidence_candidate.schema.json',
    'data/sample/generated/ledgers/event_ledger.jsonl': 'schemas/ledger/event_ledger_event.schema.json',
}


def main() -> int:
    errors: list[str] = []
    checked_count = 0

    for pattern, schema_rel in ARTIFACT_SCHEMA_GLOBS.items():
        schema = load_json(ROOT / schema_rel)
        matches = sorted(ROOT.glob(pattern))
        if not matches:
            errors.append(f'no generated artifact matched: {pattern}')
            continue
        for path in matches:
            checked_count += 1
            try:
                instance = load_json(path)
            except Exception as exc:
                errors.append(f'{path.relative_to(ROOT)}: invalid JSON: {exc}')
                continue
            errors.extend(validate_instance(instance, schema, path))

    for pattern, schema_rel in JSONL_SCHEMA_GLOBS.items():
        schema = load_json(ROOT / schema_rel)
        matches = sorted(ROOT.glob(pattern))
        if not matches:
            errors.append(f'no generated jsonl artifact matched: {pattern}')
            continue
        for path in matches:
            checked_count += 1
            with path.open('r', encoding='utf-8') as f:
                for idx, line in enumerate(f, start=1):
                    if not line.strip():
                        continue
                    try:
                        instance = json.loads(line)
                    except Exception as exc:
                        errors.append(f'{path.relative_to(ROOT)}:{idx}: invalid JSON line: {exc}')
                        continue
                    errors.extend(validate_instance(instance, schema, Path(f'{path}:{idx}')))

    return print_result(errors, f'generated artifacts validated ({checked_count} files checked)')


if __name__ == '__main__':
    raise SystemExit(main())
