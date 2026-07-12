from __future__ import annotations

import sys
from pathlib import Path

from _validate_utils import ROOT, iter_json_files, load_json, print_result


def main() -> int:
    errors: list[str] = []
    schema_dir = ROOT / 'schemas'
    for path in iter_json_files(schema_dir):
        try:
            data = load_json(path)
        except Exception as exc:
            errors.append(f'{path}: invalid JSON: {exc}')
            continue
        if '$schema' not in data:
            errors.append(f'{path}: missing $schema')
        if 'title' not in data:
            errors.append(f'{path}: missing title')
        if 'type' not in data:
            errors.append(f'{path}: missing type')
    return print_result(errors, 'all schema files are valid JSON and include basic schema fields')


if __name__ == '__main__':
    raise SystemExit(main())
