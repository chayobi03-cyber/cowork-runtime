# AUDIT_CHECKLIST.md

판정 등급:

```text
BLOCKER / MAJOR / LOW / PASS
```

## 0. 작업 위험도 기준

작업 위험도 R0~R3의 source of truth는 `SCHOOL_RULES.md`의 "작업 위험도 기준: R0~R3" 섹션이다.

Audit 시 R2 작업이 승인 없이 실행됐거나 R3 작업이 기본 허용된 경우 BLOCKER로 본다.

## 1. BLOCKER

다음 중 하나라도 있으면 승인 불가다.

1. 목적이 불명확하다.
2. 문제 정의가 없다.
3. MVP 범위가 너무 크다.
4. 실행 방법이 없다.
5. 테스트 방법이 없다.
6. evidence가 없다.
7. 사람이 반복 작업을 직접 해야 한다.
8. 기밀 가능 정보가 외부 입력용 자료에 포함되어 있다.
9. 회사 PC에서 이어받을 수 없다.
10. Plan 없이 schema/config/metadata/runner/queue/evidence를 바꾸려 한다.
11. 기존 구조 재사용 검토 없이 새 구조를 만든다.
12. 외부 네트워크, credential, 파일 삭제, batch 실행을 기본 허용한다.

## 2. MAJOR

수정 후 승인 가능하다.

1. 제외 범위가 약하다.
2. 테스트 fixture가 부족하다.
3. 오류/malformed 케이스가 없다.
4. run_report 또는 evidence가 불완전하다.
5. known limitation이 부족하다.
6. backlog가 추상적이다.
7. 실패 시 확인 위치가 불명확하다.
8. 도메인 상세가 상위 지침을 잠식한다.
9. 여러 모듈 통합 시 실패 위치 trace가 없다.
10. 과정 품질 또는 trajectory 기록이 없다.

## 3. LOW

졸업에는 치명적이지 않지만 정리 권장이다.

1. 파일명 일관성이 부족하다.
2. README 설명이 짧다.
3. 예시가 부족하다.
4. 용어가 혼용된다.
5. 문서 순서가 어색하다.
6. scorecard 세부 기준 보강 필요.

## 4. PASS

통과 조건이다.

1. 목적과 문제 정의가 명확하다.
2. MVP 범위가 작고 테스트 가능하다.
3. 제외 범위가 명확하다.
4. 실행 방법이 있다.
5. 테스트 방법이 있다.
6. evidence가 있다.
7. known limitation이 있다.
8. backlog가 있다.
9. 기밀 가능 정보가 정리됐다.
10. 미래의 내가 회사 PC에서 이어받을 수 있다.
11. 사람 반복 작업이 없다.
12. scorecard와 BLOCKER gate가 적용됐다.

## 5. Plan Audit Questions

1. 목적이 명확한가?
2. 현재 구조 요약이 있는가?
3. 수정/생성 파일 목록이 있는가?
4. 기존 구조 재사용 가능성을 검토했는가?
5. 제외 범위가 명확한가?
6. 테스트 계획이 있는가?
7. evidence 기준이 있는가?
8. BLOCKER / MAJOR / LOW 리스크가 있는가?
9. 구현 순서가 작은 단위인가?
10. 사람 승인 전 구현하지 않는가?

## 6. Handoff Audit Questions

1. 왜 만들었는지 알 수 있는가?
2. 어디까지 했는지 알 수 있는가?
3. 실행 방법이 있는가?
4. 테스트 방법이 있는가?
5. 실패 시 어디를 봐야 하는가?
6. evidence가 있는가?
7. known limitation이 있는가?
8. backlog가 있는가?
9. 기밀정보가 제거됐는가?
10. GPT 없이도 회사 PC에서 이어받을 수 있는가?
