# DOMAIN_NOTES/EMC_S2P_CST_NOTE.md

## 1. 목적

이 문서는 EMC, S2P, Touchstone, CST 관련 MVP를 만들 때 상위 지침과 분리해 참고하는 도메인 노트다.

상위 `SCHOOL_RULES.md`에는 도메인 세부식을 넣지 않는다.

## 2. 기본 원칙

1. 물리 타당성과 검증 가능성을 우선한다.
2. fixture는 승인된 라이브러리가 아니다.
3. 공식 문서는 실행 evidence가 아니다.
4. 샘플 S2P는 parser/validator fixture로 먼저 사용한다.
5. CST batch 또는 외부 네트워크 실행은 초기 MVP에서 제외한다.
6. 로컬 read-only 분석부터 시작한다.

## 3. S2P / Touchstone 검토 항목

최소 검토 항목:

1. Touchstone header
2. frequency unit
3. parameter type
4. data format
5. reference impedance
6. frequency range
7. point count
8. S11/S21/S12/S22 column integrity
9. reciprocity 가능성
10. passivity 가능성
11. S21 dB 변환 가능성
12. malformed line 처리
13. duplicate frequency 처리
14. unsupported extension 처리

## 4. CST 관련 원칙

1. CST help 문서는 reference로 분류한다.
2. CST 실제 실행 evidence와 문서 reference는 구분한다.
3. CST batch 실행은 초기 MVP에서 기본 제외한다.
4. CST 자동화는 Plan-first 대상이다.
5. 외부 script 실행, credential, confidential export는 R3 Blocked로 본다.

## 5. Thin Orchestrator 예시

허용 가능한 초기 MVP:

```text
S2P sample files
→ parser
→ format validator
→ simple scorecard
→ run_report.json
```

제외 범위:

1. CST 실제 실행
2. 부품 추천 알고리즘
3. 대량 라이브러리 구축
4. UI 대시보드
5. 외부 서버 연동
6. 사내 DB 연동

## 6. Evidence 기준

EMC/S2P/CST MVP의 evidence에는 다음을 포함한다.

1. 입력 S2P 목록
2. header parse 결과
3. frequency range
4. point count
5. validation result
6. failure reason
7. run_report
8. known limitation
9. 회사 PC 재검증 필요 여부

## 7. 주의 표현

사용 금지 또는 제한 표현:

```text
CST 검증 완료
물리적으로 정확함
부품 라이브러리 승인 완료
운영 적용 가능
```

실제 evidence가 있을 때만 사용한다.

권장 표현:

```text
fixture 기준 parser 통과
format validation 통과
실제 CST 실행 미검증
vendor raw source trace 미완료
회사 PC에서 재검증 필요
```
