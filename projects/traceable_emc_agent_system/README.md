# Traceable EMC Agent System v0.4

작게 시작하되 지속 발전 가능한 EMC Workflow Agent / Agent Harness 골격입니다.

## 핵심 구성

- `schemas/`: Artifact JSON Schema
- `nodes/`: Tree Node Contract 정의
- `data/sample/`: 샘플 Scenario, Annotation, RAG, S2P 입력, Generated Output
- `tools/`: MVP 실행 도구
- `scripts/`: 검증 및 Harness 실행 스크립트
- `docs/`: Tree, Schema, Codex 작업 메모

## v0.4 추가 내용

- `tools/s2p_analyzer.py`: Touchstone S2P 파싱 및 S11/S21 dB metric 생성
- `tools/annotation_parser.py`: 사람 표시 기반 EDA Annotation을 Parsed EDA Context로 변환
- `tools/simple_rag_retriever.py`: 시험법/불량현상/설계사양 문서에 대한 키워드 RAG
- `tools/constraint_checker.py`: 전류/DCR/높이/패키지 제약조건 점검
- `tools/report_data_builder.py`: 분석 결과를 EMC 보고서 초안 Markdown으로 생성
- `tools/simple_evaluator.py`: 생성 산출물 존재/형식 기반 MVP 평가
- `scripts/run_case.py`: Annotation → RAG → S2P → Constraint → Report → Evaluation 실행
- `scripts/validate_generated_artifacts.py`: 생성 산출물 Schema 검증

## 실행 방법

```bash
python scripts/validate_json_schema.py
python scripts/validate_node_registry.py
python scripts/validate_artifacts.py
python scripts/run_case.py
python scripts/validate_generated_artifacts.py
python scripts/build_manifest.py
```

## 생성 결과

`python scripts/run_case.py` 실행 후 주요 결과는 아래에 생성됩니다.

```text
data/sample/generated/annotations/EDA-CTX-0002.json
data/sample/generated/rag/evidence_candidates.jsonl
data/sample/generated/tool_outputs/S2P-RUN-0002.json
data/sample/generated/tool_outputs/CONSTRAINT-RUN-0002.json
data/sample/generated/reports/emc_report_draft.md
data/sample/generated/evaluation/EVAL-0002.json
data/sample/generated/harness/RUN-0002.json
```

## 운영 원칙

- Workflow(업무 흐름)는 아직 확정하지 않고 `workflow_backlog`에 둡니다.
- 계산은 Python Tool이 수행하고, AI는 해석/요약/보고서/판단 보조를 담당합니다.
- RAG 결과는 Evidence Candidate이며, 사람 검토 후 Evidence Ledger로 승격합니다.
- Event Ledger는 원본 기록이고, Graph/Index는 파생 뷰입니다.
- 사용자 승인 없는 공식 PASS/DONE/Script Library 등록은 금지합니다.
