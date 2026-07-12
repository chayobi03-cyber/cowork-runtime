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
