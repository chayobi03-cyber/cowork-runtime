from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    files = []
    for path in sorted(ROOT.rglob('*')):
        if path.is_file():
            files.append(str(path.relative_to(ROOT)).replace('\\', '/'))
    manifest = {
        'project': 'Traceable EMC Agent System',
        'file_count': len(files),
        'files': files,
    }
    out = ROOT / 'data/sample/manifest.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'[OK] wrote {out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
