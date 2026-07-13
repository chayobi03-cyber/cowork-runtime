# CLAUDE_MAINTENANCE_LOG.md — Part Work Whitepaper v1

## 2026-07-12 — v1 착수 패키지 생성

**변경 사항**
- 외부 감사(2026-07-12, NEEDS CHANGES) 결과 반영, 섹션별 점검(SECTION_BY_SECTION_REVIEW.md)
  기준으로 v1 최소 구조 9개 파일 신규 작성
- 인수인계 문서 2개(PART_WORK_WHITEPAPER_HANDOFF_PLAN.md, SECTION_BY_SECTION_REVIEW.md) 패키지에
  포함

**의도적으로 하지 않은 것**
- Role/Workstream/Subpart/Context Registry 미생성 (v1 범위 제외, 근거: STRUCTURE_DECISION_
  OPTIONS.md)
- Input Card 6종 중 Topic Card 1종만 생성
- ADR 템플릿 미생성 (Stable Spine 변경은 Decision Log 한 줄 기록으로 대체, Decision Log 파일
  자체도 아직 미생성 — 회의 후 착수 예정)
- 실제 운영 위치(공유폴더/Git/문서시스템) 미확정 — 사내 시스템 확인 전

**다음 세션에서 확인할 것**
- 부서 회의 결과 (판정 주체, 사내 시스템 가용 범위)
- 위 결과에 따라 STRUCTURE_DECISION_OPTIONS.md의 "결정 필요 사항" 갱신
- 승격 트리거(문서 10개 초과, 번복 2회 등) 발생 여부는 매 세션 재확인

## 2026-07-12 — WRITING_METHODOLOGY.md 신설

**변경 사항**
- 백서 작성 방법론 문서 신설: A(문서 갱신 원칙)/B(조직 채택 저항 최소화)/C(입력 방식 마찰 제거)
  3개 고정 절 + append-only 근거 표(A-01~A-05, B-01~B-05, C-01~C-05) 구조로 설계
- 외부 사례 조사(Evergreen Notes, arc42, PARA, Fogg Behavior Model, Tiny Habits, Nielsen
  heuristics, AI SOP 생성 도구 카테고리 등) 반영
- 입력 방식 스펙트럼(텍스트→음성→스크린샷→화면녹화) 정리 — 마찰은 감소하나 처리 부담은 증가
  한다는 트레이드오프 명시
- AI_CONTEXT.md에 참고 문서로 연결

**설계 의도**
- 새 아이디어가 나올 때마다 절 구조를 새로 만들지 않고 표에 행만 추가하는 방식 — Stable Spine
  원칙과 동일한 패턴을 방법론 문서 자체에도 적용
- 각 항목에 고유 ID(A-xx/B-xx/C-xx) 부여해 Topic Card나 향후 Decision Log에서 인용 가능하게 함

**의도적으로 하지 않은 것**
- 화면녹화 처리를 위한 전용 도구(Scribe/Loom 등) 도입 결정 — v1 범위 밖, 필요 시 PC 기본
  녹화기능 + Claude 직접 업로드 분석으로 시범 진행 권장(C-05 참고)
- 항목이 각 절 10개를 넘어설 때의 재구조화 방식은 아직 미정 (그 시점에 결정)

## 2026-07-12 — C-06 신설: 캡처 범위 선택 + PC/휴대폰 환경 분리

**변경 사항**
- WRITING_METHODOLOGY.md C절에 C-06 추가: 다중 모니터/창 단위 캡처 범위 선택 규칙, PC를
  분석 메인으로 두고 휴대폰은 텍스트/음성메모만 우선 지원(사진·영상은 PC로 옮긴 뒤 처리)
- EXPORT_SAFETY_CHECKLIST.md에 "캡처 시점에 원천 차단" 원칙 추가 (6~7번 문항의 사전 조치)
- SAMPLE_RECORDING_TO_CARD.md, AI_CONTEXT.md에 C-06 규칙 반영

**설계 의도**
- Export Safety를 "사후 확인"에서 "캡처 시점 원천 차단"으로 한 단계 앞당김 — 담기지 않으면
  체크리스트 확인 자체가 불필요해짐
- 휴대폰 사진/영상을 처리 대상에서 제외한 이유: 화면 제약으로 정교한 범위 선택이 어려워
  Export Safety 원칙과 충돌 위험이 있다고 판단

**다음 세션 확인할 것**
- 실제 다중 모니터 환경에서 범위 선택이 Claude 업로드 인터페이스상 어떻게 동작하는지는
  아직 미검증(개념 반영만 완료, 실물 검증 아님)

## 2026-07-12 — PC 입력방식 실제 지원여부 검증 (오류 정정)

**변경 사항**
- `file-reading` 스킬 디스패치 표 직접 확인 결과, **오디오/영상 파일을 Claude가 직접
  재생·분석하는 기능이 없음**을 확인 (지원 확장자 목록에 오디오/비디오 없음, 이미지만 vision
  input으로 직접 지원)
- 기존 WRITING_METHODOLOGY.md C-03(음성), C-05(화면녹화)의 "Claude에 업로드해서 분석"이라는
  표현이 **부정확했음** — 각 항목에 실제 제약 경고 추가, "PC 환경에서 실제 지원 여부" 표 신설
- 정정 내용: 음성은 사람이 먼저 텍스트로 전사해야 함, 화면녹화는 사람이 핵심 장면을 스크린샷
  여러 장으로 미리 추출해야 함(영상 통째 분석 불가) — 두 경우 다 "Claude가 직접 처리"가 아니라
  "사람이 한 단계를 먼저 거친 뒤 이미지/텍스트로 전달"
- SAMPLE_RECORDING_TO_CARD.md 실행 조건을 프레임 추출 방식으로 정정, AI_CONTEXT.md에도
  이 제약 명시 추가

**왜 중요한가**
- 이 정정 없이 진행했으면 다음 세션에서 "녹화 파일을 그냥 업로드하면 되는 줄 알았는데
  안 된다"는 실패를 실제로 겪었을 것 — 방법론 문서 자체가 실행 불가능한 전제를 담고 있었음
- 5가지 입력 방식 중 완전 지원은 텍스트/스크린샷/범위선택 3개뿐, 음성/화면녹화 2개는 조건부
  지원(사람의 사전 작업 필요)이라는 게 이번 검증의 핵심 결론

## 2026-07-12 — TOPIC-0002 등록: 입력 전처리 자동화 도구 (v1 범위 밖, hold)

**변경 사항**
- TOPIC_REGISTRY.yaml에 TOPIC-0002 신규 등록: 음성 전사·화면녹화 프레임 추출을 자동화하는
  도구. status=hold로 명시 — v1 MVP에서는 미진행, 회의 이후 별도 프로젝트로 분리 착수 여부 판단
- STRUCTURE_DECISION_OPTIONS.md "v1의 트레이드오프"에 이 보류 항목과 근거 추가

**설계 의도**
- 지금 방법론 문서에 발견된 제약(음성/화면녹화 조건부 지원)을 "나중에 도구로 자동화하면
  해결될 문제"로 인식하되, 이를 v1 백서 작업과 섞지 않고 **별도 Topic으로 격리**함 — 원안이
  실패했던 "본문에 새 아이디어를 바로 섞는" 패턴을 반복하지 않기 위함
- Track 미지정(Registry 등록 시점에는 Research도 Main도 아님) — 실제 착수 시점에 재판단

## 2026-07-12 — ROADMAP.md 신설 및 v1 목표 재정의

**변경 사항**
- v1 MVP 목표 명확화: **v1은 AI agent를 만들지 않는다.** 업무를 원자 단위(Topic Card)로
  쪼개서 AI가 접근·검색·수정·재사용하기 쉬운 구조를 만드는 것이 v1의 실제 목표
- `ROADMAP.md` 신설 — M0(원자화, 현재)→M1(지식그래프 연결)→M2(입력 전처리 자동화,
  TOPIC-0002와 연결)→M3(업무 효율화 agent 생성, 장기 목표) 4단계 마일스톤
- 지식그래프 스키마 초안을 ROADMAP.md에 포함하되 **M1 착수 전까지는 채우지 않음**(Topic
  5개 이상 쌓이는 시점이 착수 조건)
- 00_PART_CONTEXT.md, AI_CONTEXT.md에 "v1이 실제로 만드는 것" 절 추가 — AI가 agent 구현
  요청과 원자화 작업 요청을 혼동하지 않도록 명시
- WRITING_METHODOLOGY.md 한 줄 요약에 "백서 제작 자체가 agentic 방식이어야 한다"는 4번째
  원칙 추가 (기존 B/C절 원칙들의 상위 목표로 명문화)
- TOPIC-0002의 next_action을 ROADMAP M2 착수 조건과 상호 참조하도록 갱신

**설계 의도**
- "마일스톤화나 지식그래프화"라는 요청을 기존 문서(TOPIC_REGISTRY, ATOMIC_PLAN)에 억지로
  끼워넣지 않고 **별도 문서로 분리** — 두 문서의 책임(실행 단위 vs 시간순 계획)이 다르기 때문
- 지식그래프는 스키마만 미리 정하고 실제 데이터는 채우지 않음 — Topic이 2개뿐인 지금 채우면
  과설계(5절 사다리 원칙 위반)

**다음 세션 확인할 것**
- Topic이 5개 이상 등록되면 M1(지식그래프 연결) 착수 여부 재검토
- M3(agent 생성)는 이번 세션에서 구현하지 않음 — 향후 별도 요청 시에도 M1/M2 선행 여부 먼저 확인

## 2026-07-12 — 전체 구조 리뷰 및 정리 (18개→17개 파일)

**변경 사항**
- `PART_WORK_WHITEPAPER_HANDOFF_PLAN.md` 삭제 — `SECTION_BY_SECTION_REVIEW.md`와 내용
  중복(둘 다 "v1 산출물 목록+다음 액션" 담당), 후자가 더 상세·최신이라 후자만 유지
- `ATOMIC_PLAN.md`에 "13/13 완료, 이력 참고용" 헤더 추가 — 더 이상 살아있는 실행 계획이
  아님을 명시, 새 계획은 별도 문서로 생성하도록 안내
- `SECTION_BY_SECTION_REVIEW.md`에 "1회성 감사 기록" 배너 추가 — 이 문서가 계속 참조되며
  사실상 두 번째 본문처럼 취급되는 걸 막고, 최신 원칙은 WRITING_METHODOLOGY.md/ROADMAP.md로
  안내. 문서 끝의 "다음 액션"도 삭제된 HANDOFF_PLAN 참조를 완료 이력으로 정정

**설계 의도**
- 파트원 노출 문서(AI_CONTEXT/00/01/TOPIC_CARD_TEMPLATE 4개)는 그대로 작음 — 이번 정리는
  창엽님/AI용 운영 문서 14개 중 중복·역할모호 3곳만 겨냥
- 삭제 전 다른 살아있는 문서(AI_CONTEXT, ROADMAP 등)가 HANDOFF_PLAN을 참조하지 않는지 grep으로
  확인 후 진행 — 참조는 로그성 기록(SECTION_REVIEW 자기 자신, MAINTENANCE_LOG)뿐이었음

## 2026-07-12 — D절 신설: 카드 입력 보조 절차 (M0 범위의 "작은 agent")

**배경**
- "agentic한 입력을 받기 위한 방법론"을 요청받아 범위를 확인한 결과, M2(입력 전처리 자동화,
  TOPIC-0002)나 M3(업무효율화 agent)가 아니라 **M0 단계에 필요한 더 작은 도구 — 카드 입력을
  도와주는 수준**임을 확인
- 소프트웨어 agent를 새로 만드는 게 아니라, **Claude 자신이 매번 같은 방식으로 카드 입력을
  돕는 고정 절차를 명문화**하는 것으로 범위 확정

**변경 사항**
- `WRITING_METHODOLOGY.md`에 D절 신설(D-01~D-05): 원본확인→Export Safety 선확인→Level A
  필드채움→불확실지점표시→결과제시후대기, 5단계 고정 절차
- 문서 상단 구조안내를 3절(A/B/C)에서 4절(A/B/C/D)로 갱신, "A/B/C는 왜, D는 무엇을" 구분 명시
- AI_CONTEXT.md에 "카드 입력 도와달라는 요청 시 D절을 그대로 따른다" 연결 추가
- ROADMAP.md M0 설명에 D절이 M0의 실행 수단임을 명시 (M2/M3와 다른 층위임을 재확인)

**설계 의도**
- 기존 SAMPLE_VOICE/SCREENSHOT/RECORDING_TO_CARD.md의 개별 시범들이 사실 D-01~D-05를 매번
  암묵적으로 밟고 있었음 — 이번에 그 절차를 명시적 순서로 승격
- D-04(불확실 지점 표시, 자동 등록 금지)는 TOPIC-0001 가상 시범에서 이미 적용했던 원칙을
  절차화한 것 — 새 원칙이 아니라 기존 관행의 명문화

## 2026-07-12 — D절 역할 오해 정정 (중요)

**문제**
- 방금 만든 D절이 "Claude가 카드 입력을 도와준다"는 표현으로 쓰여 있었는데, 이는 **이 대화의
  Claude(Coworkai 세션)와 백서 자체(WP-0001)의 역할을 혼동**한 것이었음
- 창엽님이 명확히 정정: **백서 실제 제작(운영)은 이 세션의 Claude가 하는 게 아니다. 백서
  자체가 School 재학생(Work Package)이고, 이 세션의 Claude는 그 백서 설계·정비를 돕는 입장.**
  "바로 구현 가능하게 준비"가 핵심 — 즉 문서가 이 대화 없이도 실행 가능해야 함

**변경 사항**
- D절 제목을 "카드 입력 보조 절차(M0 범위의 작은 agent)"에서 **"카드 입력 처리 절차서(이식형)"**
  로 변경, 목적 문장을 "Claude가 ~한다"에서 "수행자(사람/AI 무관)가 ~한다"로 전면 재작성
- 표의 "설명" 열을 "수행자가 하는 일"로 바꾸고, 각 단계에 필요한 참조 문서를 별도 열로 명시
  (D-01~D-05가 세 참조문서: EXPORT_SAFETY_CHECKLIST, TOPIC_CARD_TEMPLATE, TOPIC_REGISTRY만
  있으면 완결되도록)
- "이식성 확인 기준" 신설: "이 대화의 맥락"이 추가로 필요하면 이식성이 깨진 것이라는 자가진단
  기준 추가
- "지금 이 대화에서의 역할" 절 신설: 이 세션 Claude=설계자, 실제 수행자=이 문서를 들고 있는
  누군가(사람/다른 AI 세션)임을 명시적으로 분리
- AI_CONTEXT.md, ROADMAP.md M0 설명도 같은 관점으로 정정 (실행 주체 오해 제거)

**왜 중요한가**
- 이 오해를 안 잡았으면, 다음에 "카드 입력 도와줘"라는 요청이 왔을 때 이 세션의 Claude가
  스스로 실행 주체라고 착각해서 계속 의존성을 만들었을 것 — 백서가 실제로 School을 졸업해서
  독립 운영될 때 이 문서만으로는 안 돌아가는 구조가 됐을 위험
- 앞으로 이 프로젝트의 모든 절차형 문서(D절 같은)는 "이 세션 밖에서도 통하는가"를 항상
  자가진단해야 함 — 이번 정정이 그 기준(이식성 확인 기준)을 만든 계기

## 2026-07-12 — STAKEHOLDER_COMMUNICATION.md, SHARED_FOLDER_AUTOMATION.md 신설

**변경 사항**
- `STAKEHOLDER_COMMUNICATION.md` 신설: 역할(파트장/일반파트원/챔피언/판정관여자) × 소파트별
  전달 매트릭스. 안내 문구는 원본 문서(TOPIC_CARD_TEMPLATE.md 등)를 가리키기만 하고 재작성
  안 함 — 이중 관리 방지
- `SHARED_FOLDER_AUTOMATION.md` 신설: 공유폴더 기반 자동화 설계(축1: 파일→D절 자동트리거,
  축2: 폴더구조↔백서구조 동기화). **설계까지만 v1**, 실행은 사내 시스템 확인 후 M2에서
  진행하도록 명시
- 두 문서 다 AI_CONTEXT.md 참고문서 목록에 연결, ROADMAP.md M2에 SHARED_FOLDER_AUTOMATION
  설계 연결, DEPARTMENT_MEETING_AGENDA.md 회의후 액션에 두 문서 반영 시점 추가

**설계 의도**
- SHARED_FOLDER_AUTOMATION은 TOPIC-0002/M2와 범위가 겹치는데, 이걸 새 Topic으로 등록하지
  않고 "설계 문서"로만 남김 — 사내 시스템 미확정 상태에서 Registry에 실행 대상처럼 등록하면
  또 다른 형태의 "확정 표현" 과설계가 될 위험(외부 감사 Operating Location View 원칙 재적용)
- STAKEHOLDER_COMMUNICATION은 원본 문서를 복제하지 않는 "필터/라우팅" 역할로만 설계 — A절
  (문서갱신 원칙, 본문vs카드 역할분리)과 동일한 패턴을 부서원 전달에도 적용

**다음 세션 확인할 것**
- 소파트별 절(현재 전부 미정)은 회의에서 파트장 답변이 나오면 채운다
- SHARED_FOLDER_AUTOMATION 실행 주체는 사내 시스템 확인 전까지 결정 보류 상태 유지

## 2026-07-13 — 부서 회의 완료, TOPIC-0003(CST 해석법) 등록

**변경 사항**
- 부서 회의 완료. 대표안건 = CST 해석법(모델링→메쉬→소스/포트→솔버설정→Post-Processing).
  판정 주체는 현재 기준 창엽님(회의에서 일부만 확정) — `STAKEHOLDER_COMMUNICATION.md` 반영
- `TOPIC_REGISTRY.yaml` schema v1→v2: `parent_topic_id` 필드 신설 (소파트가 아니라 업무 단위로
  계속 늘어나는 특화 카드를 공통 카드에 연결하기 위함)
- `TOPIC-0003`(CST 해석법 — 공통부분) 신규 등록, status: under_review
- `DOMAIN_NOTES/CST_REFERENCE_SOURCES.md` 신설 — CST 관련 작업 시 참고할 학계/오픈소스/실무
  사이트 위키형 참조문서 (Research Track, 특정 Topic에 종속되지 않음)

**설계 의도 / 결정 사항**
- CST 원문(Overview Help.pdf 등)의 TOC + Ribbon 구조(Modeling/Mesh/Simulation/Post-Processing)를
  공통부분 방법론의 뼈대로 채택 — CST 자체 UI 워크플로우를 그대로 활용
- **외부 AI 위임 시점 확정**: 원문(50MB+73MB) 전체 대조 기반 상세 방법론 작성은 지금 위임하지
  않는다. WP-0001 자체가 School 졸업(4.4 Scorecard/4.5 BLOCKER 판정 통과)하는 시점에 위임한다.
  그 전까지 방법론 뼈대 작업은 Claude가 계속 이어간다.
- **뼈대만으로 진행 가능한지 검토 결과**: 졸업 판정 자체는 TOPIC-0003 내용 완성도가 아니라 M0
  완료조건(부서회의 통과 + 실제 카드 입력 확인, ROADMAP.md)을 보므로 문제없음. 다만 **뼈대가
  실제 파트원의 업무별 특화 카드 작성을 지원할 만큼은 되는지**는 별도 확인이 필요 — "원문 전체
  반영 여부"가 아니라 "이 뼈대만 보고 실제 카드 1건이라도 나올 수 있는가"가 기준. 이 조건은 M0
  evidence(실제 카드 입력) 확인 시 함께 검증한다.

**의도적으로 하지 않은 것**
- COMMON_METHOD/에 5단계 상세 방법론 문서 아직 작성 안 함 (뼈대만 확정, 본문은 다음 세션)
- 업무별 특화 카드(parent_topic_id: TOPIC-0003) 아직 접수 시작 안 함

**다음 세션 확인할 것**
- COMMON_METHOD/CST_INTERPRETATION_COMMON_METHOD.md 초안 작성 이어가기
- WP-0001 School 졸업 판정(Scorecard/BLOCKER) 진행 상황 — 위임 시점 판단 기준
- 실제 파트원 카드 입력(M0 evidence) 확인 시, 뼈대 수준으로 카드 작성이 실제로 됐는지 함께 확인
  (안 되면 뼈대 보강 필요 — 원문 전체 대조가 아니라 뼈대 자체의 실사용 가능성 문제로 처리)

