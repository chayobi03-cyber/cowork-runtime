# CLAUDE_MAINTENANCE_LOG.md

Claude가 개발자 역할로 직접 관리한 변경 이력. 각 항목은 독립 audit(2026-07-11)에서
발견된 findings에 대응한다.

## 2026-07-11 — v0.4 patch (파일 내 버전 번호는 올리지 않음, 로직만 수정)

### MAJOR-1: 하드코딩된 ID (`scripts/run_case.py`)

- 문제: `--run-id`를 받으면서도 `EDA-CTX-0002`, `RAGQ-0002`, `S2P-RUN-0002`,
  `CONSTRAINT-RUN-0002` 등이 코드에 리터럴로 박혀 있어, 다른 run-id로 실행해도
  같은 파일을 덮어씀.
- 수정: `derive_suffix()`로 `--run-id`의 숫자 부분을 실제로 추출해 모든 하위
  산출물 ID/파일명에 반영. run-id가 schema 패턴(`^RUN-[0-9]{4,}$`)에 안 맞으면
  조용히 기본값으로 넘어가지 않고 즉시 에러.
- 부수 수정: `scripts/validate_generated_artifacts.py`도 동일한 하드코딩
  (`*-0002` 경로 고정) 문제가 있어 glob 기반 검증으로 교체.
- 검증: `RUN-0002`와 `RUN-9999`를 둘 다 실행해 파일이 충돌 없이 공존하는 것을
  직접 확인. `tests/test_run_case_id_derivation.py` 4개 회귀 테스트 추가.

### MAJOR-2: 고정 점수 계산 (`tools/simple_evaluator.py`)

- 수정하지 않음. 각 criterion에 이미 `"notes": "MVP file-level evaluation"`이
  명시돼 있어 은폐가 아니라고 판단, 그리고 "파일 존재/파싱 여부"만 보는 평가기를
  실제 품질 평가기로 바꾸는 것은 이번 패치 범위를 넘는 R2급 설계 변경(신규
  criteria 정의 필요)이라 별도 Plan 승인 없이 진행하지 않음.
- 남은 조치: 다음에 evaluator 로직을 실제로 바꾸려면 별도 MVP_PLAN이 필요함.

### MAJOR-3: jsonschema 미설치 시 무음 통과 (`scripts/_validate_utils.py`)

- 문제: jsonschema가 없으면 `validate_instance`가 `[]`를 반환해 항상 `[OK]`,
  exit code 0으로 보였음 — "검증 안 함"과 "검증해서 통과"가 구분 안 됐음.
- 수정: jsonschema 미설치 시 명시적으로 `RuntimeError` 발생, 호출부가 그대로
  실패(exit 1)하도록 변경. "조용히 통과"를 "시끄럽게 실패"로 바꿈.
- 검증: jsonschema 없는 새 venv에서 `validate_artifacts.py` 실행 → exit 1
  (트레이스백으로 원인 명시)까지 직접 재현. 있는 venv에서는 기존과 동일하게 통과.

### MAJOR-4: 단위테스트 부재

- 추가: `tests/test_constraint_checker.py`(7개), `tests/test_s2p_analyzer.py`(8개),
  `tests/test_run_case_id_derivation.py`(4개) = 19개, 전부 실제 로직 대상,
  전부 이 세션에서 직접 실행해 19/19 PASS 확인.
- 남은 조치: `annotation_parser.py`, `simple_rag_retriever.py`,
  `report_data_builder.py`, `simple_evaluator.py`는 아직 단위테스트 없음.

### LOW-1: S2P 데이터 출처 불명

- 수정하지 않음(값 자체를 임의로 바꾸는 것은 위험). 대신
  `data/sample/inputs/s2p_real/PROVENANCE_NOTE.md`로 문제를 문서화하고
  사람 확인이 필요한 항목으로 남김.

## 의도적으로 건드리지 않은 것

- `project_config.json`, `schemas/`, `nodes/` 등 계약(contract) 레벨 파일은
  이번 패치 범위 밖. 계약 변경은 Plan-first 대상(SCHOOL_RULES.md §4/§9).
- confidentiality gate 개념 추가하지 않음 — v1.5.6에서 나온 개념이고 v0.4
  범위 밖.

---

# v0.4.2 (2026-07-12) — MAJOR-2 재설계

> **재구성 경위**: v0.4.2는 2026-07-11 세션에서 한 차례 완성됐던 이력이 있으나, 산출물이
> `/tmp/emc_final.zip`(세션 종료 시 소실되는 임시 경로)에만 저장되어 실제로는 어디에도
> 남지 않았음이 2026-07-12 확인 결과 드러남. 이번 항목은 v0.4.1을 기준으로 **처음부터
> 다시 구현**한 것이며, 이전 세션의 산출물을 복원한 것이 아니다. 테스트 개수(29개 vs
> 이번 33개)가 이전 기록과 다른 것도 이 때문 — 같은 목표를 다른 구현으로 재작성한 결과다.

### MAJOR-2: 고정 점수 계산 (`tools/simple_evaluator.py`) — 이번 세션에서 해결

- **문제**: 기존 evaluator는 "파일이 존재하고 파싱되는가"만 확인했다. 업스트림 도구가
  자체적으로 실패를 보고해도(constraint의 `passed: false`, s2p의 `warnings` 존재,
  evidence 전부 `relevance_score: 0`) 파일 자체는 만들어지므로 evaluator는 "성공"으로
  잘못 판정했다.
- **수정**: 4개 기준 전부를 업스트림 도구의 실제 판정값을 읽도록 재작성.
  - `s2p_result_valid`: 파일 존재 + `warnings` 리스트가 비어있어야 함
  - `constraint_result_valid`: 파일 존재 + 최상위 `passed`가 true여야 함
  - `evidence_candidates_relevant`: 파일 존재 + 최소 1개 row의 `relevance_score > 0`
  - `report_markdown_exists`: 기존과 동일(존재+비어있지 않음) — 이 항목은 자유 텍스트라
    도구 자체 판정 필드가 없어 파일 기준 유지
- **evaluation_id 하드코딩 잔존분도 함께 수정**: `"EVAL-0002"` 리터럴을
  `derive_eval_id(target_id)`로 교체 — `target_id`의 숫자 접미사를 못 찾으면 예외를
  던지도록 해서(조용히 기본값으로 폴백하지 않음) `scripts/run_case.py`의
  `derive_suffix()`와 동일한 "실패 시 침묵하지 않는다" 원칙을 적용.
- **검증**: `tests/test_simple_evaluator.py` 14개 신규(기존 19개 + 신규 14개 = 33개,
  전부 이 세션에서 직접 실행해 33/33 PASS 확인). 추가로 `scripts/run_case.py` 전체
  파이프라인을 실제 샘플 데이터로 end-to-end 실행해 `EVAL-0002.json`이 정상 생성되고
  4개 기준 전부 실제 계산값(예: evidence relevance_score=0.273)을 근거로 판정되는 것을
  직접 확인.
- **known_open_items (v0.4.2 기준)**: 없음.

