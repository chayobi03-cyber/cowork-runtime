# CURRENT_PROGRESS.md

## 1. 현재 상태

```text
MVP School 설계 v0.5 확정 / 파일 패키지 생성 완료
```

## 2. 핵심 변경 이력

기존 방향:

```text
사내 여러 담당자에게 넘기는 조직형 인수인계패키지
```

현재 방향:

```text
회사 PC에서 내가 직접 이어받을 수 있는 성능 중심 로컬 MVP School
```

## 3. 변경 이유

1. 실제 사용자는 미래의 나다.
2. 조직형 approval 문서가 현재 목적에 비해 과했다.
3. 문서 수가 많으면 운영 속도가 떨어진다.
4. MVP School의 핵심은 문서 완성도가 아니라 졸업 성능이다.
5. 회사 PC에서 바로 실행, 검증, 수정할 수 있어야 가치가 있다.

## 4. 확정 원칙

1. Plan-first
2. Evidence-first
3. 사람은 Approve / Reject / Needs changes만 판단
4. AI가 실행하고 evidence로 증명
5. BLOCKER / MAJOR / LOW / PASS audit
6. Performance Scorecard는 항목별 100점
7. 최종 점수는 가중 평균
8. Local Handoff 기준으로 졸업 판단
9. 도메인 상세는 DOMAIN_NOTES로 분리
10. 로컬/오프라인/read-only 우선

## 5. 여러 모듈 통합 판단

여러 모듈을 통합하는 것 자체는 너무 큰 MVP가 아니다.

허용되는 경우:

```text
기존 모듈을 얇게 묶고 E2E smoke test와 run_report만 검증하는 Thin Orchestrator MVP
```

위험한 경우:

```text
모듈 내부 구현, 통합, UI, DB, approval workflow, report 자동화를 한 번에 모두 하려는 경우
```

## 6. 8축 scorecard 확정

| 항목 | 가중치 |
|---|---:|
| 문제/효과 명확성 | 12% |
| MVP 범위 절단 성능 | 13% |
| AI 실행 가능성 | 13% |
| 검증/evidence 가능성 | 17% |
| Trajectory / 과정 품질 | 12% |
| 로컬 인수인계 가능성 | 15% |
| 안전/기밀/오프라인 적합성 | 12% |
| 비용/속도/재사용성 | 6% |

## 7. 다음 단계

추천 다음 단계:

```text
실제 아이디어 1개에 MVP School을 시범 적용한다.
```

후보:

1. S2P parser / validator Thin Orchestrator
2. 로컬 KG viewer read-only MVP
3. 공유폴더 scanner report generator
4. doc-rag-converter Phase 0~1 검증

## 8. 현재 패키지 한계

1. 실제 MVP에 적용한 scoring 결과는 아직 없다.
2. Domain Notes는 최소 지침 수준이다.
3. 예시 run_report는 샘플이며 실제 실행 evidence가 아니다.
4. 회사 PC에서 실제 재검증이 필요하다.

## 9. 최종 기록

```text
MVP School은 조직형 문서팩이 아니라,
아이디어를 작게 자르고,
AI가 실행하고,
evidence로 채점하고,
회사 PC에서 내가 이어받을 수 있으면 졸업시키는
성능 중심 로컬 MVP 운영 체계다.
```

---

## v0.5.1 Evidence Integrity Patch

### 목적

Claude 1차 감사와 GPT 재검토 결과, v0.5 패키지는 운영 철학은 타당하지만 evidence 무결성에서 실제 결함이 확인되었다. v0.5.1은 엔터프라이즈 eval harness 확장이 아니라 P0 최소 무결성 패치로 제한한다.

### 반영 항목

1. `run_report.json`의 자기 hash evidence 제거
2. `MANIFEST_SHA256.txt` 재생성
3. `README.md` 파일 구조 drift 수정
4. `examples/RUN_REPORT_EXAMPLE.json` 추가
5. `tools/validate_mvp_school.py` 추가

### 의도적으로 제외한 항목

1. `AGENTS.md`
2. `TRAJECTORY_LOG_TEMPLATE.md`
3. `scorecard_schema.json`
4. `golden_cases/`와 `bad_cases/`
5. `RISK_REGISTER.md`
6. secret scan / schema validation / enterprise governance harness

### 판단근거

MVP School은 개인 로컬 재참조용 졸업 시스템이다. 따라서 v0.5.1은 “적게 쓰고, 빨리 판단하고, 작게 만들고, evidence로 졸업시킨다”는 원칙에 맞게 P0 결함만 수정한다.

### 상태

```text
v0.5: Concept PASS / Package integrity FAIL
v0.5.1: Evidence integrity patch applied / validation pending at package generation time
```



---

## v0.5.2 Project Instruction Alignment Patch

### 목적

GPT 앱 이창엽 프로젝트 전용 지침과 `mvp_school/` 파일 패키지의 역할을 분리했다.

### 반영 사항

1. `GPT_PROJECT_INSTRUCTIONS.md` 추가
   - GPT 앱 프로젝트 지침에 복사할 최소 행동 기준
   - 세부 기준은 `mvp_school/` 문서 패키지를 source of truth로 참조
2. `PROJECT_UPLOAD_GUIDE.md` 추가
   - ChatGPT 프로젝트 reference file 업로드 권장 목록
   - 회사 PC/repo 적용 방법
3. L0~L3 작업 위험도 표기를 R0~R3로 정리
   - v0.5.2 생성 시 문서상 의도는 있었으나 실제 표 누락이 Claude 독립검증에서 발견됨
   - 다른 시스템의 자율성 레벨과 충돌 방지
4. 프로젝트 지침에서 BLOCKER, Idea Card, Local Handoff 세부 항목 중복을 줄이고 파일 참조 방식으로 전환
5. 도메인 세부 검증 기준은 `DOMAIN_NOTES/`에 둔다는 원칙 재확인

### 의도적으로 하지 않은 것

- enterprise eval harness 추가
- schema/golden cases/risk register 추가
- secret scan 추가
- 대규모 문서 재작성

### 상태

```text
v0.5.2: Project instruction alignment PASS / 실제 아이디어 적용 전
```


---

## v0.5.3 Risk Tier Definition Patch

### 목적

Claude 독립검증 결과, v0.5.2 보고에는 `SCHOOL_RULES.md`에 R0~R3 기준표가 있다고 되어 있었으나 실제 파일에는 해당 정의가 없었다. 이 결함은 GPT 보고 내용과 파일 내용이 불일치한 실제 drift로 판단한다.

### 반영 사항

1. `SCHOOL_RULES.md`에 R0~R3 작업 위험도 기준표를 실제 추가
2. `AUDIT_CHECKLIST.md`에 R0~R3 source of truth 위치와 audit 적용 기준 추가
3. `GPT_PROJECT_INSTRUCTIONS.md`에서 R0~R3 상세 정의의 source of truth를 `SCHOOL_RULES.md`로 명확화
4. `tools/validate_mvp_school.py`에 최소 콘텐츠 marker 검사 추가
   - `SCHOOL_RULES.md`의 R0/R1/R2/R3, Auto/Post-review/Needs approval/Blocked marker 확인
   - `GPT_PROJECT_INSTRUCTIONS.md`의 파일 미확인 방어 문구 확인

### 의도적으로 하지 않은 것

- secret scan 추가
- schema validation 추가
- enterprise eval harness 추가
- golden cases / bad cases 추가

### 판단근거

이번 패치는 프로덕션급 validator 확장이 아니라, 이미 발견된 source-of-truth drift를 막기 위한 최소 콘텐츠 검증이다. MVP School의 개인 로컬 운영 목적과 과설계 방지 원칙을 유지한다.

### 상태

```text
v0.5.3: Risk tier definition PASS / Minimal content marker validation added / 실제 아이디어 적용 전
```

---

## v0.5.4 NOTE Structure Patch

### 목적

v0.5.3까지 확정된 MVP School 운영 기준을 유지하면서, 개별 툴 조사, 개념 조사, EMC/S2P/CST 같은 도메인 기준이 늘어날 때 상위 `GPT_PROJECT_INSTRUCTIONS.md`를 계속 키우지 않도록 NOTE 계층을 정식화했다.

### 반영 사항

1. `NOTE_REGISTRY.md` 추가
   - 도메인/툴/개념 note 색인
   - note의 상태와 source-of-truth 역할을 구분
2. `PROJECT_SOURCE_INDEX.md` 추가
   - ChatGPT Project flat upload와 회사 PC repo 구조의 차이를 관리
   - P0~P3 업로드 우선순위 정의 추가
3. `DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md` 추가
   - Touchstone/S-parameter parser 구현 사양이 아니라 O/X 체크리스트와 evidence 경계로 제한
4. `DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md` 추가
   - CST schematic automation 구현 전 범위, evidence, 실패 위치 기준 정리
5. `TOOL_NOTES/README.md` 추가
   - 툴별 note 작성 템플릿
6. `CONCEPT_NOTES/README.md` 추가
   - 개념 note 작성 템플릿
7. `tools/validate_mvp_school.py` 보강
   - marker 검사는 최소 drift 감지라는 한계를 명시
   - README reference, NOTE_REGISTRY reference, PROJECT_SOURCE_INDEX P0/P1 핵심 파일 존재 검증 추가

### 독립 audit 반영

Claude 독립 audit에서 지적된 다음 사항을 반영했다.

1. content marker 검사는 의미 검증이 아니라 최소 drift 감지임을 README와 run_report에 명시
2. Touchstone note는 parser spec으로 변질되지 않도록 문서 서두에 scope guard 추가
3. PROJECT_SOURCE_INDEX의 P0~P3 우선순위 기준 명시
4. Gate 실패 시 재시도는 최대 1회로 제한한다는 운영 기준을 run_report known limitations에 기록

### 의도적으로 하지 않은 것

- `GPT_PROJECT_INSTRUCTIONS.md` 변경
- `SCHOOL_RULES.md` R0~R3 의미 변경
- `AUDIT_CHECKLIST.md` BLOCKER 기준 변경
- `PERFORMANCE_SCORECARD.md` 점수 체계 변경
- 실제 Touchstone/S2P parser 구현
- 실제 CST automation code 작성
- CST batch 실행
- 외부 서버 연동
- 회사 raw 자료 포함

### 상태

```text
v0.5.4: NOTE Structure Patch PASS / validator structural checks added / 실제 아이디어 적용 전
```

## v0.5.5 Domain Note Consolidation Patch

Coworkai School(별개 시스템, Google Sheets roster 기반)의 창엽님이 "지금까지 진행된 School
산출물들 기능이 비슷한데 통합 가능한가"라고 질의한 것을 계기로, Claude가 mvp_school/DOMAIN_NOTES/
전체를 항목별로 대조했다.

### 발견

`EMC_S2P_CST_NOTE.md`(요약형, 한국어)가 `TOUCHSTONE_SPARAM_NOTE.md`(S2P/Touchstone 특화),
`CST_SCHEMATIC_AUTOMATION_NOTE.md`(CST automation 특화), `examples/THIN_ORCHESTRATOR_EXAMPLE.md`
(파이프라인 예시) 세 문서의 내용을 다른 형식으로 반복하고 있었다. 고유 내용이 사실상 없었다.

### 상충 지점 발견 및 처리

`EMC_S2P_CST_NOTE.md` 3절의 "reciprocity/passivity 가능성" 체크 항목이 `TOUCHSTONE_SPARAM_NOTE.md`
의 명시적 범위 제외(passivity correction/causality fitting)와 상충 여지가 있었다. Claude는 이걸
임의로 병합/판단하지 않고 사용자에게 확인을 요청했고, **범위 제외로 확정**됐다(추가 항목 없이
TOUCHSTONE_SPARAM_NOTE.md의 기존 제외 범위 유지).

### 조치

1. `EMC_S2P_CST_NOTE.md`: 내용을 deprecated 안내 + 대체 문서 pointer로 교체 (파일 자체는 유지 —
   NOTE_REGISTRY.md의 "deprecated: kept for history" 상태 활용, 삭제하지 않음)
2. `NOTE_REGISTRY.md`: 해당 행 상태 active → deprecated
3. `SCHOOL_RULES.md`, `PROJECT_UPLOAD_GUIDE.md`: 예시/업로드 목록에서 deprecated 파일을
   TOUCHSTONE_SPARAM_NOTE.md + CST_SCHEMATIC_AUTOMATION_NOTE.md로 교체
4. `PROJECT_SOURCE_INDEX.md`: 우선순위 P2 → P3, upload 권장 여부 No로 변경
5. `README.md`: 파일트리에 deprecated 표기 추가

### 의도적으로 하지 않은 것

- `TOUCHSTONE_SPARAM_NOTE.md`, `CST_SCHEMATIC_AUTOMATION_NOTE.md` 내용 수정 (두 문서는 도메인이
  달라 병합하지 않음 — School 4.3 "하나의 입력/하나의 출력/하나의 테스트 경로" 원칙과 정합)
- `EMC_S2P_CST_NOTE.md` 물리 삭제 (deprecated 상태로 이력 보존)
- reciprocity/passivity 항목을 TOUCHSTONE_SPARAM_NOTE.md에 추가 (사용자가 범위 제외로 확정)

### 상태

```text
v0.5.5: Domain Note Consolidation PASS / EMC_S2P_CST_NOTE.md deprecated / 5개 참조 문서 갱신 완료
```
