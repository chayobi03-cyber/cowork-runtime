from __future__ import annotations

from pathlib import Path

from _validate_utils import ROOT, iter_json_files, load_json, print_result, validate_instance


def main() -> int:
    errors: list[str] = []
    schema_path = ROOT / 'schemas/common/node_contract.schema.json'
    schema = load_json(schema_path)
    node_dir = ROOT / 'nodes'
    seen: set[str] = set()
    for path in iter_json_files(node_dir):
        try:
            node = load_json(path)
        except Exception as exc:
            errors.append(f'{path}: invalid JSON: {exc}')
            continue
        errors.extend(validate_instance(node, schema, path))
        node_id = node.get('node_id')
        if node_id in seen:
            errors.append(f'{path}: duplicate node_id {node_id}')
        seen.add(node_id)
        for schema_ref in node.get('schemas', []):
            if not (ROOT / schema_ref).exists():
                errors.append(f'{path}: referenced schema does not exist: {schema_ref}')
    return print_result(errors, f'{len(seen)} node files validated')


if __name__ == '__main__':
    raise SystemExit(main())
