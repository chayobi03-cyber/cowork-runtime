# Schema Guide

## 핵심 구조

- Node 정의는 `schemas/common/node_contract.schema.json`을 따른다.
- 실제 산출물은 Artifact Schema를 따른다.
- 업무 Flow는 아직 확정하지 않고 `data/sample/workflow_backlog/`에 보류한다.

## 검증

```bash
python scripts/validate_json_schema.py
python scripts/validate_node_registry.py
python scripts/validate_artifacts.py
```
