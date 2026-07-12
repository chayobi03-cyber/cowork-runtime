# Structure Decision Options — v1 축소판 vs 원안

## 비교표

| 항목 | 원안 (초기 설계) | v1 (이번 착수) | 판단 근거 |
|---|---|---|---|
| 본문 문서 | 11개 | 2개 (요약) | 외부 감사 BLOCKER-1 |
| Registry | 5종 | 1종 (Topic만) | 외부 감사 MAJOR-2 |
| Input Card | 6종 × 3레벨 | 1종 × Level A만 | 외부 감사 Tacit Knowledge View |
| Stable Spine 변경 절차 | ADR 의무 | Decision Log 한 줄 기록 | 외부 감사 BLOCKER-2 |
| AI-readable layer | AI_CONTEXT+AGENTS+CONTEXT_INDEX+CONTEXT_REGISTRY (4종) | AI_CONTEXT.md 1개 | 외부 감사 AI Context View |
| 운영 위치 구조 | Authoritative/Published/AI Export/Evidence 4분리 | 공유폴더 내 2폴더 | 외부 감사 Operating Location View |
| 보안 절차 | 원칙 선언만 | Export 전 강제 체크리스트 | 외부 감사 BLOCKER-4 |
| Role/Workstream | 별도 ID 체계(ROLE-xxxx 등) | Topic Card 서술 필드로 흡수 | 섹션별 점검 7절 |

## 왜 v1로 축소했는가

2026-07-12 외부 감사 결과 NEEDS CHANGES 판정. 핵심 사유: 20명/1인 유지관리 체계에서 원안 규모
(11+5+8+7 = 30개 이상 유지 대상)를 처음부터 세팅하면 회의 이전에 구조 관리 자체가 본업이 되고,
파트원 입력 장벽이 높아져 실제 활용도가 낮아질 위험이 큼.

## v1의 트레이드오프 (인지하고 있는 것)

- Role/Workstream 정식 구분이 없어, 동일 Role이 여러 Topic에 걸쳐 나타나도 아직 추적 안 됨
  → 실제로 반복되면 그때 도입 (트리거: 동일 Role 패턴이 3개 이상 Topic에서 반복 확인)
- Level B/C 입력이 없어 깊이 있는 실증 정보는 승격 시점에만 요구됨
  → Topic이 candidate_mvp로 판단될 때 Level B/C 요청

## 승격 트리거 (v1 → 다음 버전)

아래 중 하나라도 실제로 발생하면 해당 항목만 개별적으로 확장한다 (전체 재설계 아님).

- 문서 수가 10개를 넘김 → CONTEXT_INDEX.yaml 도입 검토
- 동일 유형 판단 번복이 2회 이상 → ADR 형식 도입 검토
- 동일 Role 패턴이 3개 이상 Topic에서 반복 → Role Registry 분리 검토
- Topic이 구현 후보로 승격 → 해당 Topic에 한해 Research Log/Implementation Plan/Evidence Plan
  추가

## 결정 필요 사항 (회의에서 확정)

- [ ] Topic 판정 주체 (창엽님 단독 / 파트장 협의)
- [ ] 운영 위치 1순위 후보 (사내 시스템 확인 후)
- [ ] 외부 AI 사용 가능 범위 (법무/보안 확인 후)
