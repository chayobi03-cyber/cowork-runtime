# Department Meeting Agenda — Part Work Whitepaper v1

## 배경 (1분 설명용)

파트 업무·자동화 주제를 계속 접수·조사·실증·인수인계할 수 있는 최소 운영 구조(v1)를 만들었다.
이건 확정안이 아니라 회의에서 다듬을 초안이다.

## 핵심 질문 (Top 5)

1. 소파트별로 실제 반복 업무가 뭔지 파트장들이 3개씩만 먼저 말해줄 수 있는가? — *(미정, 회의 전 파트장 사전 문의 필요)*
2. 사내에서 LLM/인트라 검색을 어디까지 쓸 수 있는가 (완전 금지 / 사내 LLM만 / 외부 AI 일부 허용)? — *(미정, 사내 시스템 확인 필요 — STRUCTURE_DECISION_OPTIONS.md 결정 필요 사항과 동일)*
3. 공유폴더 외에 이미 쓰고 있는 문서 도구(SharePoint 등)가 있는가? — *(미정, 사내 확인 필요)*
4. Topic 판정(Approve/Reject/Needs changes)을 창엽님 혼자 할 것인가, 파트장 협의를 거칠 것인가? — *(미정, 회의에서 확정 필요 — 가장 우선순위 높은 질문)*
5. 파트원들에게 "1분 카드 작성"을 실제로 요청할 채널/타이밍이 있는가(정기 회의, 슬랙 등)? — *(미정, WRITING_METHODOLOGY.md B-02/B-03 원칙상 "기존 루틴에 anchor" 방식 권장)*

## 검증이 필요한 가정 (Top 5)

1. 파트원이 자발적으로 Topic Card를 채울 유인이 있다.
2. 사내 공유폴더가 최소한의 버전 관리(파일명 규칙만으로도)를 견딘다.
3. 외부 AI를 사내 업무 맥락에 실제로 쓸 수 있다 — 법무/보안 승인 여부 미확인.
4. 창엽님 1인이 이 구조 전체의 유지보수를 감당할 수 있다.
5. "새 role/topic 추가돼도 spine이 안 흔들린다"는 것이 실제 조직 변화 속도에서도 유효하다.

## 회의에서 보여줄 것

- `AI_CONTEXT.md`, `00_PART_CONTEXT.md`, `01_PART_WORK_WHITEPAPER.md` (요약본)
- `TOPIC_CARD_TEMPLATE.md` (직접 하나 같이 써보는 것을 권장 — 1분 소요 확인용)
- `STRUCTURE_DECISION_OPTIONS.md` (v1 축소판 vs 원안 비교)

## 회의에서 다루지 않을 것

운영 위치 최종 확정, Role/Workstream 정식 체계, ADR 절차 — 전부 이번 회의 이후 사안.

## 회의 후 액션

1. 판정 주체 확정 (질문 4)
2. 사내 시스템 확인 담당·일정 배정
3. 확정된 내용으로 `STRUCTURE_DECISION_OPTIONS.md` → Decision Log로 전환
