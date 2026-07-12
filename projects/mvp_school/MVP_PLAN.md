# MVP_PLAN.md

## 0. Plan Mode 지시문

Codex, Claude Code, Gemini CLI, Cursor, Copilot Agent 등에 Plan만 요청할 때 다음 문구를 사용한다.

```text
Plan mode only.
Do not modify files.
Do not create files.
Do not implement code.
Stop after producing the plan and ask for approval.
```

## 1. 목적

```text

```

## 2. 현재 구조 요약

현재 파일, 모듈, 데이터, 테스트 구조를 요약한다.

```text

```

## 3. 수정/생성 파일 목록

| 파일 | 작업 | 이유 | 위험도 |
|---|---|---|---|
|  |  |  | R0/R1/R2/R3 |

## 4. 기존 구조 재사용 가능성

먼저 확인할 것:

1. user_action_queue
2. UserActionStatus
3. run_report.json
4. metadata / metadata_json
5. config validator
6. source verification
7. evidence truthfulness
8. profile/version traceability
9. pytest fixture

검토 결과:

```text

```

## 5. MVP 범위

이번 MVP에서 할 것:

```text

```

## 6. 제외 범위

이번 MVP에서 하지 않을 것:

```text

```

## 7. Thin Orchestrator 여부

여러 모듈을 통합하는 경우 작성한다.

| 항목 | 내용 |
|---|---|
| 통합 목표 | 전체 시스템 완성 / 얇은 연결 경로 검증 |
| 연결 모듈 |  |
| 대표 입력 |  |
| 대표 출력 |  |
| E2E smoke test | 있음 / 없음 |
| 실패 위치 trace | 가능 / 불가능 |
| 모듈 내부 개선 포함 여부 | 포함 / 제외 |

## 8. 테스트 계획

| 테스트 | 목적 | 입력 | 기대 출력 |
|---|---|---|---|
| 정상 케이스 |  |  |  |
| 오류 케이스 |  |  |  |
| malformed 케이스 |  |  |  |
| E2E smoke test |  |  |  |

## 9. Evidence 기준

완료 시 남길 evidence:

1. 실행 명령
2. 입력 파일 또는 fixture
3. 출력물
4. 테스트 결과
5. 실패 로그 또는 제한 사항
6. run_report
7. 변경 파일 목록

## 10. 리스크

| 등급 | 리스크 | 대응 |
|---|---|---|
| BLOCKER |  |  |
| MAJOR |  |  |
| LOW |  |  |

## 11. 구현 순서

1. 
2. 
3. 

## 12. Acceptance Criteria

- [ ] 목적이 명확하다.
- [ ] MVP 범위가 작다.
- [ ] 제외 범위가 명확하다.
- [ ] 기존 구조 재사용 가능성을 확인했다.
- [ ] 테스트 방법이 있다.
- [ ] evidence 기준이 있다.
- [ ] Local Handoff로 이어질 수 있다.
- [ ] 사람 반복 작업이 없다.

## 13. 승인 요청

```text
Approve / Reject / Needs changes
```
