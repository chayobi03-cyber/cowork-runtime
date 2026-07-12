#!/usr/bin/env python3
from __future__ import annotations
from _validate_utils import ROOT, load_json, print_result, validate_instance


def main() -> int:
    errors: list[str] = []
    schema = load_json(ROOT / 'schemas/tools/tool_contract.schema.json')
    for path in sorted((ROOT / 'data/sample/tool_contracts').glob('TOOL-*.json')):
        try:
            instance = load_json(path)
        except Exception as exc:
            errors.append(f'{path}: invalid JSON: {exc}')
            continue
        errors.extend(validate_instance(instance, schema, path))
    return print_result(errors, 'tool contracts validated')

if __name__ == '__main__':
    raise SystemExit(main())
