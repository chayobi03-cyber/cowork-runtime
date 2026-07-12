# Part Work Whitepaper — 섹션별 감사 요청 개별 점검

> 원본 외부 감사 의뢰 프롬프트(2026-07-12)의 섹션 3~15에 명시된 "감사 요청" 질문을 하나씩
> 점검한다. 전체 요약 판정(NEEDS CHANGES)은 이미 나왔으므로, 이 문서는 그 판정의 근거를
> 섹션 단위로 분해해 어떤 항목을 살리고 어떤 항목을 버릴지 명확히 한다.

---

## 섹션 5. 전체 백서 구조 점검

**Q: 20명/3소파트 기준 과한가?** → 과하다. 11개 본문 + 5개 레지스트리 + 8개 템플릿 + 7개 폴더는
문서 수 기준으로 봐도 30개 이상의 유지 대상이 동시에 생긴다.

**Q: 꼭 필요한 최소 구조는?** → 본문 2개(PART_CONTEXT, WHITEPAPER 요약) + Topic Registry 1개 +
Topic Card 템플릿 1개 + AI_CONTEXT.md 1개. 총 5개.

**Q: 나중으로 미룰 폴더/파일은?** → ROLE_REGISTRY, WORKSTREAM_REGISTRY, SUBPART_REGISTRY,
CONTEXT_REGISTRY, COMMON_METHOD 내 8개 템플릿 중 Topic Card 제외 7개, ROLES/, WORKSTREAMS/,
SUBPARTS/, DECISIONS/ 폴더.

**Q: 아예 제거해야 하는 항목은?** → 지금 시점에는 "제거"보다 "보류"가 맞다. 다만 AGENTS.md와
CONTEXT_INDEX.yaml은 문서 수가 10개를 넘기 전까지는 만들 근거 자체가 없으므로 계획에서
아예 빼는 것을 권한다(보류 목록에도 안 올림 — 필요해지면 그때 새로 설계).

**Q: 처음부터 세분화하면 운영자 부담은?** → 매우 높음. 이 구조 전체를 하루 만에 세팅하면
그 자체로 며칠 소요되는 작업이 되고, 실제 회의나 파트원 입력 이전에 지침 관리가 본업이 된다.
→ **판정: 5개 파일로 축소, 나머지는 보류 목록에 남겨두되 착수하지 않음.**

---

## 섹션 6. Stable Spine 개념 점검

**Q: 개념이 적절한가?** → 개념 자체(변화는 흡수하고 중심은 안 흔든다)는 타당하다.

**Q: 20명 파트 기준 너무 무거운가?** → 개념은 안 무겁지만 **ADR 의무화**가 무겁다.

**Q: Spine 안에 넣을 것 / appendix로 내릴 것?**
- Spine에 남길 것: 목적(1), 소파트 운영 원칙(2), 사람/역할/업무/주제/도구 분리 원칙(3),
  evidence-first 원칙(7), Approve/Reject/Needs changes 판정 원칙(9)
- Appendix로 내릴 것: 업무 role 추가 절차(4), 자동화 후보 topic 추가 절차(5), 사내실증/외부AI
  분리 원칙(6), Local Handoff 원칙(8), R0~R3 위험도 원칙(10) — 이 5개는 "원칙 요약 1줄 + 상세는
  별도 문서 링크" 형태로 Spine 밖에 두는 게 맞다. Spine은 "왜"를 담고, 실행 절차는 appendix가
  담는다.

**Q: 변경 시 ADR이 필요한 구조가 과한가?** → 과하다. 대신 08_DECISION_LOG.md에 한 줄 기록
(날짜/변경내용/이유)만으로 시작하고, 실제로 "번복이 잦아 추적이 안 되는" 문제가 2회 이상
발생하면 그때 ADR 형식을 도입한다(coworkai 5절 사다리 원칙과 동일한 패턴).
→ **판정: Spine 5원칙만 유지, ADR 의무 제거, 변경 이력은 Decision Log 한 줄 기록으로 대체.**

---

## 섹션 7. Role / Workstream / Topic 모델 점검

**Q: 분리가 실무적으로 맞는가?** → 개념은 맞지만 3개를 동시에 굴리는 건 초기엔 과하다.

**Q: 현장 엔지니어가 이해하기 쉬운가?** → Topic(자동화 주제)은 이해하기 쉽다. Role/Workstream
구분은 "책임 단위 vs 반복 업무 흐름"의 차이가 현장 언어로는 모호하게 느껴질 수 있다 — 실제
회의에서 검증 필요(Top 5 Questions 1번과 연결).

**Q: 3개 소파트 관리에 적절한가?** → Topic Card 필드에 "관련 소파트"를 넣는 것으로 충분히
흡수 가능. 별도 Subpart Registry는 불필요.

**Q: 더 단순한 모델이 있는가?** → 있다. v1은 **Topic만** 굴리고, Role/Workstream은 "이 Topic이
어떤 반복 업무를 자동화하는가"라는 Topic Card의 서술 필드로 흡수한다. 별도 ID 체계
(ROLE-0001 등)는 회의 후 실제로 role이 여러 topic에 걸쳐 재사용되는 사례가 쌓이면 그때 분리.

**Q: Person mapping은 언제 추가하는가?** → 트리거 기준 신설 필요: "동일 Role이 3개 이상 Topic에
걸쳐 반복 등장" 또는 "실제 인력 배정 결정이 필요한 시점". 지금 문서에는 이 트리거가 없었음
(MAJOR-1 대응).
→ **판정: v1은 Topic 단일 모델. Role/Workstream ID 체계는 회의 후 재검토.**

---

## 섹션 8. Topic Extension System 점검

**Q: Card/Registry/Research Log/Plan/Evidence Plan 모두 필요한가?** → 아니다. 5단계는 School의
12단계 운영흐름을 그대로 옮겨온 것인데, School은 이미 "재학중 프로젝트" 단위라 무거운 게
정당화되지만, Topic은 아직 "아이디어 후보" 단계라 그 정도 무게가 안 맞는다.

**Q: 초기에는 Card+Registry만으로 충분한가?** → 충분하다. Research Log/Implementation
Plan/Evidence Plan은 해당 Topic이 실제로 "구현 후보"로 승격된 뒤에 추가한다.

**Q: 백서 본문 보호 방식으로 적절한가?** → 적절하다. 이 원칙(본문에 직접 안 섞고 Card로 받는다)은
살릴 핵심 원칙 중 하나.

**Q: 과도한 process로 주제 입력이 줄어들 가능성은?** → 5단계 전체를 요구하면 매우 높음. Card 1장
+ Registry 등록 2단계로 줄이면 낮음.
→ **판정: 1~2단계(Card 작성 → Registry 등록)만 v1에 적용. 3~6단계는 승격 시점에 추가.**

---

## 섹션 9. AI-Readable Context Layer 점검

**Q: AI_CONTEXT.md/AGENTS.md/CONTEXT_INDEX.yaml 모두 필요한가?** → 아니다. 문서 수가 적은
초기 단계에서 라우팅 인덱스(CONTEXT_INDEX.yaml)는 인덱싱할 대상 자체가 적어 무의미하다.

**Q: CONTEXT_REGISTRY.yaml은 과설계인가?** → 그렇다. doc_type/ai_role/update_policy/
confidentiality를 관리할 문서가 아직 4개뿐인 단계에서는 이 메타데이터를 유지보수하는 비용이
얻는 이득보다 크다.

**Q: 구조로서 충분한가?** → AI_CONTEXT.md 1개(1페이지, "이 파트가 뭘 하는 곳이고 지금 뭘 하고
있는지 + 절대 하면 안 되는 추론 목록")면 지금 단계에는 충분하다.

**Q: 필요한 metadata / 너무 복잡한 metadata는?**
- 필요: 각 Topic Card의 `company_only_validation`(Y/N), `external_ai_safety`(Y/N) 두 필드 —
  AI가 과대해석하지 않도록 하는 핵심 안전장치이므로 유지.
- 과함: doc_type, ai_role, update_policy, confidentiality의 4필드 메타데이터 체계(문서별) —
  문서가 4개뿐이면 사람이 그냥 알고 있는 정보라 별도 필드로 관리할 이유가 없음.
→ **판정: AI_CONTEXT.md 1개 + "금지 추론 목록"만 유지. AGENTS.md/CONTEXT_INDEX/CONTEXT_REGISTRY
전부 보류.**

---

## 섹션 10. Human Input & Tacit Knowledge Capture 점검

**Q: 입력 카드 방식이 현실적인가?** → 카드라는 형식 자체는 맞다. 개수가 문제.

**Q: 카드 종류가 너무 많은가?** → 6종은 많다. Topic Input Card 1종으로 시작.

**Q: 1분/5분/15분 구조가 적절한가?** → 구조 자체(입력 난이도를 계단식으로)는 좋은 설계지만,
처음부터 3단계를 다 제시하면 "어느 레벨로 써야 하지"라는 선택 부담이 생긴다. v1은 **Level A
(1분)만** 제시하고, Level B/C는 해당 Topic이 실제로 구현 후보로 승격될 때 자연스럽게 요구한다
(승격 = 더 자세히 써야 하는 시점이라는 게 직관적으로 연결됨).

**Q: 암묵지 제거 질문이 충분한가?** → 12개 질문 자체는 좋은 목록이나, 카드 한 장에 12개 질문을
다 넣으면 그것만으로 15분이 넘는다. Level A 카드에는 이 중 핵심 5개만
(무엇을 받아서 무엇을 만드는가 / 좋은 결과와 나쁜 결과의 차이 / 자주 틀리는 부분 / AI가 판단하면
안 되는 부분 / 하면 안 되는 작업)만 넣고 나머지는 Level B/C로 미룬다.

**Q: Approve/Reject/Needs changes만 하게 하는 원칙이 가능한가?** → 가능하나 판정 주체가
불명확한 채로는 작동 안 함(Top 5 Questions 4번과 동일 이슈) — 회의에서 확정 필요.
→ **판정: Topic Input Card 1종, Level A만, 핵심 질문 5개로 축소.**

---

## 섹션 11. 운영 위치 및 시스템 구조 점검

**Q: 지금 확정 안 하는 판단이 맞는가?** → 맞다.

**Q: 외부 벤치마크 리포트로 먼저 정리하는 방식이 적절한가?** → 적절하다. 단, 리포트 자체가
너무 길면 회의에서 안 읽힌다 — A4 1~2장 요약 권장.

**Q: 검토 순서는?** → 접근장벽 낮은 순: 공유폴더 → 사내 문서시스템(있다면) → 사내 Git →
정적 사이트. Git을 상위에 둘 이유 없음(비개발자 비중 고려).

**Q: 원본/조회본/AI export/evidence 분리 구조가 적절한가?** → 개념은 맞지만 지금은 4분리 전체를
문서화할 필요 없이, 공유폴더 안에 **폴더 2개(원본용 / export용)**로 시작. Evidence는 원본
폴더의 하위 폴더로 충분(별도 최상위 분리 불필요, 사내이므로 애초에 외부 유출 경로가 export
폴더 하나뿐).

**Q: 20명 파트 기준 너무 복잡한가?** → 4분리 정식 구조는 복잡함. 2폴더 구조는 적정.
→ **판정: 운영 위치 미확정 유지, 검토 순서만 확정, 4분리는 2폴더로 축소.**

---

## 섹션 12. 외부 벤치마크 참고 점검

**Q: 20명 파트 기준 축소 적용이 타당한가?** → 대체로 타당하나 벤치마크 5개(GitLab Handbook,
Diátaxis, MADR/ADR, Kubernetes KEP, Turing Way)를 전부 리포트에 녹이면 리포트 자체가 길어진다.

**Q: 제외해야 할 참고 구조는?** → Kubernetes KEP는 이미 스스로 "과하므로 축소 적용"이라고
밝혔는데, 축소해도 남는 개념(proposal/registry/stage)이 이미 Topic Card + Registry 구조와
중복된다 — 벤치마크 리포트에서 KEP는 "참고했으나 직접 채택 안 함" 한 줄로 축소.

**Q: 더 강하게 반영해야 할 구조는?** → GitLab Handbook-first(single source of truth)와
Diátaxis(문서 역할 분리)는 실제로 지금 구조(본문 요약 vs 상세 vs 카드)에 이미 자연스럽게
녹아 있으므로, 이 둘만 벤치마크 리포트의 핵심으로 남기고 나머지는 부록 처리.

**Q: 외부 근거를 리포트에 어느 정도 넣을 것인가?** → 파트장급 청중 기준, 벤치마크당 2~3문장
요약이면 충분. 원본 문서처럼 각 벤치마크마다 상세 설명을 넣으면 회의 자료로 안 맞음.
→ **판정: 벤치마크 리포트는 GitLab Handbook-first + Diátaxis 중심으로 압축, 나머지 3개는
"검토했음" 수준으로만 언급.**

---

## 섹션 13. 보안 / 사내 사용 경계 점검

**Q: 이 정도 보안 경계가 충분한가?** → 원칙 목록은 충분하나 **강제 절차가 없다**는 게 지난
감사에서 지적한 BLOCKER-4. 원칙만 있고 체크리스트가 없으면 실수로 뚫린다.

**Q: 과도한 보안 구조 없이 최소 위험을 막는 방법은?** → export 직전 1회, Y/N 5문항 체크리스트
(고객명/제품명/경로/이름/credential/raw데이터 포함 여부)만으로 충분. 별도 승인 프로세스나
자동 필터링 시스템은 지금 단계에서 과함.

**Q: 외부AI-safe/company-only 구분을 어떻게 단순화하는가?** → Topic Card의 필드 2개
(`external_ai_safety`, `company_only_validation`)만으로 충분 — 이미 원본 설계에 있던 필드를
그대로 쓰되, 이걸 "선언"이 아니라 "체크리스트 통과 후 표시"로 운영 방식만 바꾼다.
→ **판정: 체크리스트 1개 신설(v1 필수 산출물에 추가), 나머지 보안 구조는 지금 그대로 유지.**

---

## 섹션 14. 리스크 자체 진단 점검

**Q: 자체 진단이 충분한가? 빠진 BLOCKER는?** → 지난 감사에서 이미 지적: **"1인 유지보수"
리스크가 빠져 있었음.** 이 문서 자체 진단의 BLOCKER 6개, MAJOR 7개, LOW 5개는 대부분 타당하나
전부 "구조/조직" 관점이고 "이걸 관리할 사람이 창엽님 한 명"이라는 제약이 리스크로 명시되지
않았다. → 이번 점검에서 BLOCKER 후보 8번으로 추가 권고: **"백서 유지보수가 창엽님 1인에게
집중되어, 파트원 입력이 늘어날수록 병목이 된다."**
→ **판정: 원본 BLOCKER/MAJOR/LOW 목록 유지 + BLOCKER 8번 추가.**

---

## 섹션 15. 현재 단계 산출물 범위 점검

**Q: 지금 산출물 범위가 적절한가?** → 7개 예정 산출물(EXTERNAL_STRUCTURE_BENCHMARK_REPORT 등)
중 일부는 지난 감사 결과로 대체 가능. 예를 들어 STRUCTURE_DECISION_OPTIONS.md는 이번 섹션별
점검 결과 자체가 초안이 된다.

**Q: 바로 만들면 안 되는 항목이 더 있는가?** → ADR_TEMPLATE_FOR_STRUCTURE_DECISION.md는 섹션 6
판정(ADR 보류)에 따라 지금 만들 필요 없음 — 7개 목록에서 제외 권고.

**Q: 반대로 지금 빠뜨리면 나중에 문제되는 항목은?** → **export 안전 체크리스트**(섹션 13에서
신설 권고)가 원본 7개 목록에 없었음 — 추가 필요.
→ **판정: 원본 7개 중 ADR_TEMPLATE 제외, EXPORT_SAFETY_CHECKLIST.md 추가 → 총 7개 유지.**

---

## 종합: v1 최종 산출물 목록 (이번 점검 결과 반영)

| # | 파일명 | 근거 섹션 |
|---|---|---|
| 1 | AI_CONTEXT.md (1페이지) | 9 |
| 2 | 00_PART_CONTEXT.md (요약) | 5 |
| 3 | 01_PART_WORK_WHITEPAPER.md (요약) | 5 |
| 4 | TOPIC_REGISTRY.yaml | 5, 7 |
| 5 | TOPIC_CARD_TEMPLATE.md (Level A만) | 8, 10 |
| 6 | EXPORT_SAFETY_CHECKLIST.md | 13, 14 |
| 7 | DEPARTMENT_MEETING_AGENDA.md | 전체 |
| 8 | STRUCTURE_DECISION_OPTIONS.md | 5, 6, 11 |
| 9 | EXTERNAL_STRUCTURE_BENCHMARK_REPORT.md (압축판, GitLab+Diátaxis 중심) | 12 |

ADR_TEMPLATE, INTERNAL_SYSTEM_CHECKLIST, HUMAN_INPUT_SYSTEM_PROPOSAL, AI_CONTEXT_STRUCTURE_
PROPOSAL은 회의 이후 또는 사내 시스템 확인 이후로 이동.

## 다음 액션

기존 Plan 문서(`PART_WORK_WHITEPAPER_HANDOFF_PLAN.md`)의 "다음 액션" 섹션을 이 9개 목록 기준으로
갱신하고, 1번부터 순서대로 실제 파일 작성을 시작한다.
