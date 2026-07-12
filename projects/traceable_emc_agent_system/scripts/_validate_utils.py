from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

try:
    import jsonschema  # type: ignore
except Exception:  # pragma: no cover
    jsonschema = None


def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def iter_json_files(base: Path) -> Iterable[Path]:
    return sorted(p for p in base.rglob('*.json') if p.is_file())


def iter_jsonl_files(base: Path) -> Iterable[Path]:
    return sorted(p for p in base.rglob('*.jsonl') if p.is_file())


def validate_instance(instance, schema, path: Path) -> list[str]:
    """Validate instance against schema.

    Patch note (managed by Claude, see docs/CLAUDE_MAINTENANCE_LOG.md):
        Previously returned [] silently when the jsonschema package was not
        installed, so callers always printed "[OK]" even though zero real
        schema validation happened (only JSON parsing). That is indistinguishable
        from a genuine pass in the printed output and in the exit code.
        This now raises so the caller cannot accidentally treat "not checked"
        as "checked and passed". Scripts must have jsonschema installed to run.
    """
    if jsonschema is None:
        raise RuntimeError(
            "jsonschema package is not installed. Real schema validation cannot run. "
            "Install it first: pip install jsonschema"
        )
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    return [f"{path}: {err.message}" for err in errors]


def print_result(errors: list[str], ok_message: str) -> int:
    if errors:
        print('[FAIL] validation errors:')
        for err in errors:
            print(' -', err)
        return 1
    print('[OK]', ok_message)
    return 0
