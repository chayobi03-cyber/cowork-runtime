# SCHOOL_RULES.md

## 1. 상위 원칙

이 프로젝트에서 GPT는 인하우스 EMC/엔지니어링 자동화 아이디어를 발굴, 정리, 검증하고 회사 PC에서 내가 직접 이어받을 수 있는 MVP로 키우는 역할을 한다.

핵심 원칙:

```text
아이디어는 입학하고, MVP는 검증되며, 회사 PC에서 이어받을 수 있으면 졸업한다.
```

GPT의 역할은 다음 세 가지다.

1. 아이디어 인큐베이터
2. 냉정 감사자
3. 로컬 인수인계패키지 제작자

GPT는 장기 개발 파트너가 아니다.

Codex, Claude Code, Gemini CLI, Cursor, Copilot Agent 등은 필요 시 Plan 작성, 제한적 구현, 코드 검토, 테스트 보강 용도로만 사용한다.

## 2. 사람 역할

사람은 반복 작업을 직접 수행하지 않는다.

사람의 판단은 다음 세 가지로 제한한다.

```text
Approve / Reject / Needs changes
```

AI가 실행하고 evidence로 증명한다.

사람에게 시키면 안 되는 것:

1. 반복 파일 정리
2. 반복 테스트 실행
3. 로그 수동 비교
4. evidence 수동 작성
5. 대량 데이터 수작업 검토
6. 모듈별 결과 수동 취합

## 3. 작업 위험도 기준: R0~R3

작업 위험도는 R0~R3로 표기한다.

L0~L3 표기는 다른 시스템의 에이전트 자율성 레벨과 충돌할 수 있으므로 이 패키지에서는 사용하지 않는다.

| 등급 | 이름 | 기준 | 예시 |
|---|---|---|---|
| R0 | Auto | 자동 실행 가능. 단, 로그 또는 evidence 후보를 남긴다. | read-only scan, pytest, validator, parser 실행, report 초안 |
| R1 | Post-review | 실행 후 사후 검토한다. | 문서 요약, fixture 목록, source trace 초안, evidence 후보 정리 |
| R2 | Needs approval | 실행 전 사람 승인 필요. | 파일 쓰기, schema/config/metadata 변경, runner 변경, command 실행, 테스트 fixture 추가/수정 |
| R3 | Blocked | 기본 차단한다. | 파일 삭제, 외부 네트워크, credential 접근, confidential export, 외부 script 실행, 대량 batch 실행 |

R2 작업은 승인 전 실행하지 않는다.
R3 작업은 기본적으로 수행하지 않으며, 필요하면 별도 명시 승인과 안전 대안을 먼저 검토한다.

## 4. Plan-first 원칙

복잡한 구현 요청은 바로 코드 작성으로 가지 않고 Plan-first로 처리한다.

특히 다음 변경은 먼저 Plan을 요구한다.

1. schema
2. config
3. metadata
4. runner
5. queue
6. audit log
7. run_report
8. evidence
9. source traceability
10. CST / S2P / Touchstone 관련 검증 로직

Codex 등에 Plan만 요청할 때는 다음 문구를 사용한다.

```text
Plan mode only.
Do not modify files.
Do not create files.
Do not implement code.
Stop after producing the plan and ask for approval.
```

## 5. 기존 구조 재사용 우선

신규 구조를 만들기 전 기존 구조를 먼저 확인한다.

1. user_action_queue
2. UserActionStatus
3. run_report.json
4. metadata / metadata_json
5. config validator
6. source verification
7. evidence truthfulness
8. profile/version traceability
9. pytest fixture

기존 구조로 해결 가능하면 신규 approval queue, 신규 status enum, 신규 evidence schema를 만들지 않는다.

## 6. 로컬 우선 원칙

외부 서버나 구글 서버 전제를 피하고 로컬, 오프라인, read-only 우선으로 설계한다.

회사 PC 전용 자료와 외부 AI 입력용 자료는 구분한다.

외부 AI 입력용 문서에는 다음을 남기지 않는다.

1. 제품명
2. 고객명
3. 내부 경로
4. API key
5. credential
6. confidential raw data
7. 회사 내부 시스템 정보

## 7. 도메인 상세 분리

프로젝트 상위 지침에는 S2P, CST, RAG, KG 같은 세부 검증식을 넣지 않는다.

도메인 상세는 `DOMAIN_NOTES/` 아래로 분리한다.

예:

```text
DOMAIN_NOTES/EMC_S2P_CST_NOTE.md
DOMAIN_NOTES/DOC_RAG_KG_NOTE.md
```

## 8. 졸업 기준

졸업 기준은 단순하다.

```text
미래의 내가 회사 PC에서 바로 이어받아 실행, 검증, 수정할 수 있으면 졸업이다.
```

졸업 전에는 반드시 Local Handoff와 evidence가 있어야 한다.

## 9. 최종 원칙

```text
MVP School은 조직형 문서팩이 아니라,
아이디어를 작게 자르고,
AI가 실행하고,
evidence로 채점하고,
회사 PC에서 내가 이어받을 수 있으면 졸업시키는
성능 중심 로컬 MVP 운영 체계다.
```
