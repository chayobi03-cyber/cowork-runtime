# Part Work Whitepaper — Local Handoff / Plan (v1 착수용)

> Coworkai 운영 규칙(v10) 4.6 Local Handoff 형식 준용.
> 이 문서는 외부 감사(2026-07-12, NEEDS CHANGES 판정) 결과를 반영한 v1 착수 계획이다.
> Track 분류: **Research Track** (아직 실행 코드 없음, 구조/원칙 설계 단계)

---

## 목적

20명 / 3개 소파트 규모 엔지니어링 파트에서 쓸 "업무+자동화 주제 확장 백서"의 **v1 최소 구조**를
착수하고, 부서 회의 전까지 회의 자료(벤치마크 리포트, 체크리스트, 아젠다, 결정 옵션)를 준비한다.
목표는 완성된 운영 체계가 아니라 **회의에서 논의 가능한 최소 초안**이다.

## 범위 (이번 착수분)

외부 감사 결과의 "지금 당장 만들 것" 4종만 다룬다.

1. `AI_CONTEXT.md` — 1페이지 entrypoint 메모
2. `00_PART_CONTEXT.md` + `01_PART_WORK_WHITEPAPER.md` — 요약 수준 본문 2개
3. `TOPIC_REGISTRY.yaml` — 1개 레지스트리만 (Role/Workstream/Subpart Registry 제외)
4. Topic Card Template — 1종, Level A(1분 입력)만

추가로 감사 산출물 요청 목록(15절) 중 **회의 준비용 2종**을 병행 작성한다.
- `DEPARTMENT_MEETING_AGENDA.md` (Top 5 Questions 기반)
- `STRUCTURE_DECISION_OPTIONS.md` (감사 결과의 Recommended Minimal Structure 기반)

## 제외 범위 (명시적 보류)

감사 BLOCKER/MAJOR 근거로 아래는 이번 착수에서 만들지 않는다.

- Role/Workstream/Subpart/Context Registry (4종) — Topic Registry만 우선
- Input Card 6종 전체 — Topic Card 1종으로 축소
- Stable Spine 정식 문서화 + ADR 절차 — 회의에서 실제 필요성 확인 후 결정
- Hybrid 4분리 구조(Authoritative/Published/AI Export/Evidence) 정식 문서화 — 공유폴더 내 폴더 2단
  구분(원본 vs export)으로 대체
- 운영 위치(공유폴더/Git/문서시스템) 확정 — 사내 시스템 확인 전까지 보류
- RAG/KG/자동화 스크립트/웹앱 등 실제 구현 — 범위 밖

## 핵심 결정과 근거

| 결정 | 근거 |
|---|---|
| Registry 5종 → 1종(Topic)만 우선 | 감사 MAJOR-2: registry 간 정합성 관리 주체 불명확 + 1인 유지보수 한계 |
| Input Card 6종×3레벨 → 1종×Level A만 | 감사 Tacit Knowledge View: 카드 종류·난이도 판단 자체가 입력 장벽 |
| Stable Spine ADR 의무화 보류 | 감사 BLOCKER-2: ADR 요구가 Spine을 경직시키거나 형해화시킬 위험 |
| AI-readable layer(AI_CONTEXT/AGENTS/CONTEXT_INDEX 3종) → AI_CONTEXT.md 1개만 | 감사 AI Context View: 문서 4개 미만 단계에서 routing index는 불필요한 유지보수 부담 |
| 운영 위치 미확정 유지, 검토 순서는 공유폴더→문서시스템→Git→정적사이트 | 감사 Operating Location View: 비개발자 비중 고려, 접근장벽 낮은 순 |
| export 시 회사정보 유출 방지용 강제 체크리스트 신설 | 감사 BLOCKER-4: 선언적 원칙만 있고 강제 절차 부재 지적 |
| 유지보수 인력(1인) 제약을 리스크 목록에 명시 추가 | 감사에서 지적된 "빠진 BLOCKER" — 자체 진단 14절에 없었음 |

## 현재 상태

- 외부 감사 완료 (2026-07-12), 판정: NEEDS CHANGES
- 이 문서(Plan) 작성 시점 기준, 실제 파일(AI_CONTEXT.md 등) 아직 미작성
- 사내 시스템(공유폴더/Git/문서시스템 가용 범위) 확인 전 단계
- Coworkai git 이전 작업(v10)과는 별개 트랙 — 이 프로젝트는 EMC/PCB Copilot과 마찬가지로
  이번 cowork-runtime 저장소 이전에 미포함

## 다음 액션 (실행 순서)

1. **회의 준비용 2종 먼저 작성** — 실제 산출물 없이도 회의를 시작할 수 있게
   - `DEPARTMENT_MEETING_AGENDA.md`
   - `STRUCTURE_DECISION_OPTIONS.md` (v1 최소구조 vs 원래 제안 구조 비교표 포함)
2. **v1 최소 구조 4종 작성**
   - AI_CONTEXT.md (1페이지)
   - 00_PART_CONTEXT.md, 01_PART_WORK_WHITEPAPER.md (요약)
   - TOPIC_REGISTRY.yaml (빈 스키마 + 샘플 1행)
   - Topic Card Template (Level A, 1분 입력 필드만)
3. **export 안전 체크리스트 초안 작성** (감사 BLOCKER-4 대응)
   - 고객명/제품명/경로/이름/credential/raw데이터 포함 여부 Y/N 형식, 1분 내 체크 가능하게
4. **창엽님 리뷰 → Approve/Reject/Needs changes 판정**
   - 이 판정 주체(창엽님 단독 vs 파트장 포함 여부)를 사전에 확인 (Top 5 Questions 중 4번)
5. **회의 이후에만 진행 가능한 항목은 대기**
   - Role/Workstream 문서화, Decision Log, Stable Spine 정식화 — 4단계 승인 후 착수

## 다음 세션 재개 시 확인할 것

- 이 Plan 문서와 감사 결과가 최신인지 (별도 버전이 없으면 그대로 유효)
- 부서 회의 일정/결과가 나왔는지 → 나왔으면 STRUCTURE_DECISION_OPTIONS.md 갱신 필요
- 사내 시스템 확인 결과가 있는지 → 있으면 운영 위치 섹션부터 재작업
