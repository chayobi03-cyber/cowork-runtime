# MVP School v0.5.4

## 1. 목적

MVP School은 인하우스 EMC/엔지니어링 자동화 아이디어를 빠르게 선별하고, 작게 검증하고, 회사 PC에서 다시 이어받을 수 있는 MVP로 졸업시키기 위한 로컬 운영 체계다.

한 줄 원칙:

```text
적게 쓰고, 빨리 판단하고, 작게 만들고, evidence로 졸업시킨다.
```

## 2. 사용 대상

1차 사용자는 미래의 나다.

즉, 사내 다수 담당자에게 넘기는 조직형 문서팩이 아니라 회사 PC에서 내가 다시 이어받아 실행, 검증, 수정할 수 있게 만드는 개인 로컬 인수인계 체계다.

## 3. 운영 흐름

```text
1. Idea Card 작성
2. Admit / Hold / Reject 판단
3. 문제 정의
4. MVP 범위 절단
5. MVP Plan 작성
6. 냉정 Audit
7. 제한적 구현 또는 검증
8. Evidence / run_report 정리
9. Local Handoff 작성
10. Performance Scorecard 평가
11. Graduate / Needs changes / Hold / Reject 판정
12. 회사 PC에서 이어받기
```

## 4. 폴더 구조

```text
mvp_school/
  README.md
  GPT_PROJECT_INSTRUCTIONS.md
  PROJECT_UPLOAD_GUIDE.md
  PROJECT_SOURCE_INDEX.md
  NOTE_REGISTRY.md
  SCHOOL_RULES.md
  IDEA_CARD.md
  MVP_PLAN.md
  LOCAL_HANDOFF.md
  PERFORMANCE_SCORECARD.md
  AUDIT_CHECKLIST.md
  EVIDENCE_GUIDE.md
  CURRENT_PROGRESS.md
  MANIFEST_SHA256.txt
  run_report.json
  tools/
    validate_mvp_school.py
  DOMAIN_NOTES/
    EMC_S2P_CST_NOTE.md
    DOC_RAG_KG_NOTE.md
    TOUCHSTONE_SPARAM_NOTE.md
    CST_SCHEMATIC_AUTOMATION_NOTE.md
  TOOL_NOTES/
    README.md
  CONCEPT_NOTES/
    README.md
  examples/
    RUN_REPORT_EXAMPLE.json
    THIN_ORCHESTRATOR_EXAMPLE.md
```

## 5. 핵심 개념

| 개념 | 의미 |
|---|---|
| Idea Card | 아이디어 입학 심사표 |
| MVP Plan | 구현 전 범위 고정 계획 |
| Audit | BLOCKER / MAJOR / LOW / PASS 기준 냉정 검토 |
| Evidence | 실행, 테스트, 제한 사항을 증명하는 기록 |
| Local Handoff | 회사 PC에서 다시 이어받기 위한 문서 |
| Graduation | 미래의 내가 바로 실행, 검증, 수정할 수 있는 상태 |
| Performance Scorecard | 항목별 100점 점수화 평가 |
| Thin Orchestrator | 여러 모듈을 얇게 연결해 E2E smoke test만 검증하는 MVP 형태 |
| Note Registry | 도메인/툴/개념 노트 색인 |
| Project Source Index | ChatGPT Project 업로드 파일과 회사 PC repo 구조의 대응표 |

## 6. 기본 판정

```text
Admit / Hold / Reject
Approve / Reject / Needs changes
Graduate / Needs changes / Hold / Reject
```

## 7. 사용 방법

새 아이디어가 생기면 다음 순서로 작성한다.

1. `IDEA_CARD.md`를 복사해 아이디어 입학 카드 작성
2. Admit이면 `MVP_PLAN.md`로 범위 고정
3. `AUDIT_CHECKLIST.md`로 냉정 검토
4. 구현 또는 검증 후 `EVIDENCE_GUIDE.md` 기준으로 evidence 정리
5. `LOCAL_HANDOFF.md` 작성
6. `PERFORMANCE_SCORECARD.md`로 점수화
7. 졸업 가능하면 회사 PC에서 이어받기

도메인/툴/개념 기준이 필요하면 다음을 우선 확인한다.

```text
NOTE_REGISTRY.md
PROJECT_SOURCE_INDEX.md
DOMAIN_NOTES/
TOOL_NOTES/
CONCEPT_NOTES/
```

## 8. 패키지 검증 방법

회사 PC에서 압축을 푼 뒤 최소 검증을 수행한다.

```bash
python mvp_school/tools/validate_mvp_school.py mvp_school
```

검증 범위는 의도적으로 작게 유지한다.

```text
1. 필수 파일 존재 확인
2. README.md에 언급된 주요 파일 참조 일치 확인
3. 알려진 drift 방지를 위한 최소 콘텐츠 marker 확인
4. NOTE_REGISTRY.md에 등록된 note 파일 실존 확인
5. PROJECT_SOURCE_INDEX.md의 P0/P1 핵심 파일 실존 확인
```

중요한 한계:

```text
Content marker check는 키워드 기반 최소 drift 감지이며, 문서 내용의 의미적 정확성이나 도메인 타당성을 증명하지 않는다.
Validator PASS는 패키지 구조와 최소 marker 존재를 확인한 결과일 뿐, 실제 CST/S2P 구현 가능성 또는 Touchstone 해석 정확성을 보증하지 않는다.
```

secret scan, schema validation, regression fixture, golden cases는 현재 범위에서 제외한다.

## 8-1. GPT 앱 프로젝트 적용

ChatGPT 앱의 이창엽 프로젝트에는 `GPT_PROJECT_INSTRUCTIONS.md`의 본문을 프로젝트 지침으로 복사한다.

프로젝트 reference files에는 `PROJECT_UPLOAD_GUIDE.md`와 `PROJECT_SOURCE_INDEX.md`의 권장 목록을 우선 업로드한다.

세부 템플릿과 운영 기준의 source of truth는 앱 지침이 아니라 업로드된 `mvp_school/` 문서 패키지다.

## 8-2. NOTE 운영 기준

상위 `GPT_PROJECT_INSTRUCTIONS.md`는 거의 고정한다.

업무 중 새로 생긴 툴/개념/도메인 기준은 다음 계층으로 누적한다.

```text
DOMAIN_NOTES/
TOOL_NOTES/
CONCEPT_NOTES/
```

새 note를 추가하거나 기존 note를 수정하는 작업은 R2 Needs approval로 본다.

## 9. 상태

현재 버전: `v0.5.4`

상태:

```text
MVP School v0.5.4 NOTE Structure Patch 완료 / NOTE_REGISTRY, PROJECT_SOURCE_INDEX, Touchstone/CST note, validator 구조 검증 보강
```
