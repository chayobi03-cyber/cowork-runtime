# 01_PART_WORK_WHITEPAPER — 본문 요약

## Stable Spine (흔들리지 않는 중심축, v1 축소판 — 5원칙)

1. **목적**: 이 백서는 파트 업무와 자동화 주제의 운영 기준팩이다. 특정 기술 MVP의 완료 보고서가
   아니다.
2. **소파트 운영 원칙**: 3개 소파트 세부 업무는 다르되, 등록·판정 방식은 공통(Topic Card →
   Registry)으로 통일한다.
3. **분리 원칙**: Person ≠ Role, Role ≠ Workstream, Workstream ≠ Topic, Candidate Topic ≠
   Candidate MVP, Candidate MVP ≠ Implemented. (v1은 Topic 단일 모델로 시작하며, 이 구분은
   개념적 원칙으로만 유지하고 별도 ID 체계는 회의 후 도입 여부 결정)
4. **evidence-first 원칙**: 실증 완료를 백서 단계에서 주장하지 않는다. 사내 실증은 회사 PC에서
   하고, evidence 없이는 상태를 "검증됨"으로 표기하지 않는다.
5. **판정 원칙**: 사람 역할은 Approve / Reject / Needs changes 세 가지로 제한한다. 판정 주체
   (창엽님 단독 vs 파트장 협의)는 부서 회의에서 확정한다 (`DEPARTMENT_MEETING_AGENDA.md` 참조).

> Spine 변경은 정식 ADR 없이 `08_DECISION_LOG.md`(후속 산출물)에 한 줄 기록으로 관리한다.
> 번복이 반복되는 문제가 실제로 2회 이상 발생하면 그때 ADR 형식 도입을 재검토한다.

## Topic 모델 (v1 단일 모델)

새 자동화/개선 주제는 `TOPIC_CARD_TEMPLATE.md`로 접수하고 `TOPIC_REGISTRY.yaml`에 등록한다.
Role/Workstream은 별도 ID 체계 없이 Topic Card 내 서술 필드로 흡수한다.

## 운영 위치

미확정. 검토 순서: 공유폴더 → 사내 문서시스템(있는 경우) → 사내 Git → 정적 문서 사이트.
Authoritative/Published/AI Export/Evidence 4분리 대신, 공유폴더 내 2폴더 구조(원본용 / export용)
로 시작한다.

## 보안 경계

외부 AI 입력 전 반드시 `EXPORT_SAFETY_CHECKLIST.md`를 통과시킨다. Topic Card의
`external_ai_safety`, `company_only_validation` 필드는 체크리스트 통과 후에만 표시한다.

## 이번 버전에서 보류한 것

Role/Workstream/Subpart/Context Registry, Input Card 6종, AGENTS.md/CONTEXT_INDEX.yaml,
Stable Spine 정식 ADR 절차, Hybrid 4분리 구조 정식 문서화. 상세 근거는
`SECTION_BY_SECTION_REVIEW.md` 참조.
