# EVIDENCE_GUIDE.md

## 1. 원칙

작업 완료는 코드 작성이 아니라 evidence로 판단한다.

Evidence는 사람이 반복 검증을 하지 않도록 AI/Agent가 생성해야 한다.

## 2. 최소 evidence

1. 실행 명령
2. 입력 자료
3. 출력물
4. 테스트 결과
5. 실패 로그 또는 제한 사항
6. 변경 파일 목록
7. run_report 또는 요약 기록
8. known limitation
9. 다음 조치

## 3. run_report 최소 구조

```json
{
  "mvp_name": "",
  "version": "",
  "status": "pass|fail|partial",
  "inputs": [],
  "outputs": [],
  "commands": [],
  "tests": {
    "passed": 0,
    "failed": 0,
    "skipped": 0
  },
  "trajectory": [],
  "evidence": [],
  "known_limitations": [],
  "next_actions": []
}
```

## 4. Evidence truthfulness

Evidence 없이 다음 표현을 쓰지 않는다.

1. 검증 완료
2. 문제 없음
3. 안전함
4. 정확함
5. 운영 가능
6. 완성됨

권장 표현:

1. fixture 기준 통과
2. pytest 기준 통과
3. smoke test 기준 통과
4. 실제 운영 환경 미검증
5. source trace 미완료
6. reviewer 승인 필요
7. 회사 PC 재검증 필요

## 5. 통합 MVP evidence

여러 모듈을 통합하는 경우 추가로 남긴다.

1. 모듈별 입력 contract
2. 모듈별 출력 contract
3. E2E 실행 경로
4. 실패한 모듈 식별 방식
5. 각 모듈 내부 검증과 통합 검증의 분리 여부
6. run_report의 step별 status

## 6. Source trace 기준

source trace가 필요한 경우 최소 다음을 남긴다.

1. source file
2. source type
3. source origin
4. source hash
5. page/table/section reference
6. extraction confidence
7. reviewer status
8. usage scope

usage scope 예시:

1. official reference
2. parser fixture
3. candidate data
4. source evidence
5. approved library
6. handoff artifact

주의:

```text
fixture는 승인된 라이브러리가 아니다.
공식 문서는 실행 evidence가 아니다.
샘플 데이터는 운영 검증 완료를 의미하지 않는다.
```

## 7. 완료 판단

작업 완료 판단에는 다음이 필요하다.

- [ ] run_report가 있다.
- [ ] 실행 명령이 기록됐다.
- [ ] 입력과 출력이 기록됐다.
- [ ] 테스트 결과가 기록됐다.
- [ ] 실패 또는 제한 사항이 기록됐다.
- [ ] source trace가 필요한 경우 포함됐다.
- [ ] scorecard 또는 audit 판정이 있다.
- [ ] evidence가 과장 없이 작성됐다.
