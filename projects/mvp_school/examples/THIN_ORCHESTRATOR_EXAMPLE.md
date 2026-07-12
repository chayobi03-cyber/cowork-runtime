# THIN_ORCHESTRATOR_EXAMPLE.md

## 1. 예시 목적

여러 모듈을 통합하더라도 MVP가 너무 커지지 않도록 Thin Orchestrator 방식으로 자르는 예시다.

## 2. 좋은 통합 MVP 예시

```text
S2P sample files
→ parser
→ validator
→ scorecard
→ report_writer
→ run_report.json
```

이번 MVP 목표:

```text
대표 S2P fixture 1~3개를 넣었을 때 parser, validator, scorecard, report_writer가 순서대로 실행되고 실패 위치와 결과가 run_report.json에 남는지 검증한다.
```

## 3. 포함 범위

1. 얇은 runner
2. 모듈 간 adapter
3. 대표 fixture 1~3개
4. E2E smoke test
5. run_report 생성
6. 실패 위치 trace

## 4. 제외 범위

1. 각 모듈 내부 대규모 개선
2. 대량 batch 처리
3. UI
4. DB
5. CST 실제 실행
6. RAG 연동
7. 부품 추천 알고리즘
8. 권한/승인 시스템

## 5. 좋은 판정

```text
이 MVP는 전체 EMC 분석 플랫폼이 아니라, 기존 모듈들이 최소 경로로 연결되고 evidence가 남는지를 검증하는 Thin Orchestrator MVP다.
```

## 6. 나쁜 통합 예시

```text
S2P parser 개선
+ 부품 DB 설계
+ CST 자동 실행
+ RAG 검색
+ UI 대시보드
+ 승인 workflow
+ 보고서 자동 생성
+ 사내 배포 구조
```

판정:

```text
플랫폼 기획에 가깝다. MVP School에서는 여러 작은 MVP로 분리해야 한다.
```
