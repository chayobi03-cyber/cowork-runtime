# AI_CONTEXT.md

이 문서는 AI(Claude/GPT 등)가 이 파트 백서 작업을 도울 때 가장 먼저 읽는 1페이지 요약이다.

## 이 파트는 무엇을 하는 곳인가

약 20명 규모, 3개 소파트로 구성된 엔지니어링 파트다. 반복 업무·검토 업무·시험/해석 데이터 정리
업무가 존재하며, 이 업무들을 자동화 후보(Topic)로 등록하고 조사·실증해서 이어받을 수 있는
형태로 남기는 것이 목표다.

## 지금 이 백서는 무슨 상태인가 (v1, 착수 단계)

- 완성된 운영 체계가 아니라 **부서 회의 전 최소 초안**이다.
- 실제 사내 시스템(공유폴더/Git/문서시스템 가용 범위)은 아직 미확인 상태다.
- 운영 위치, Role/Workstream 정식 체계, Stable Spine ADR 절차는 전부 회의 이후로 보류돼 있다.
- 지금 존재하는 건 Topic Registry 1개 + Topic Card 템플릿 1개 + 요약 본문 2개뿐이다.

## AI가 절대 하면 안 되는 추론 (금지 목록)

- `candidate_mvp` = 구현 완료로 해석하지 않는다.
- `company_only_validation` = 이미 검증됨으로 해석하지 않는다.
- 백서에 언급됐다 = 승인됐다로 해석하지 않는다.
- Topic Registry 등록 = 진행 중 프로젝트로 해석하지 않는다.
- Fixture 통과 = 프로덕션 준비 완료로 해석하지 않는다.
- Role owner 필드 = 실제 인력 배정 완료로 해석하지 않는다.

## AI가 지켜야 할 것

- 회사 내부 정보(제품명/고객명/경로/개인이름/credential/raw 시험결과)는 외부 AI 입력용 export에
  절대 포함하지 않는다. export 전 `EXPORT_SAFETY_CHECKLIST.md`를 반드시 통과시킨다.
- 새 Topic은 백서 본문에 직접 쓰지 않고 Topic Card로 받아 Registry에 등록한다.
- 이 파트의 자동화 관련 실행 코드/검증은 Coworkai 프로젝트(별도 저장소, cowork-runtime)의
  Track/Audit 규칙을 그대로 준용한다. 이 백서 프로젝트 자체는 아직 Research Track이다
  (실행 코드 없음, 구조·원칙 설계 단계).

## 참고 문서

- 상세 판단 근거: `SECTION_BY_SECTION_REVIEW.md`, `EXTERNAL_STRUCTURE_BENCHMARK_REPORT.md`
- 운영 원칙 요약: `01_PART_WORK_WHITEPAPER.md`
