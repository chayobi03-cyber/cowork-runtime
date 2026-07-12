# DOMAIN_NOTES/DOC_RAG_KG_NOTE.md

## 1. 목적

이 문서는 문서 변환, RAG, KG, 로컬 viewer 관련 MVP를 만들 때 참고하는 도메인 노트다.

상위 지침에는 RAG/KG 세부 구조를 넣지 않고 이 문서로 분리한다.

## 2. 기본 원칙

1. 로컬/오프라인/read-only 우선
2. 원본 파일 직접 수정 금지
3. 복사본 또는 export 기반 분석
4. source trace 보존
5. evidence truthfulness 우선
6. 기밀 가능 정보 외부 입력 금지
7. 초기 MVP에서는 cloud, Google server, 사내 인증 연동을 기본 제외

## 3. 문서 변환 MVP 검토 항목

1. 입력 파일 형식
2. 출력 파일 형식
3. 원본 보존 여부
4. 변환 실패 처리
5. source path trace
6. hash 또는 version trace
7. metadata 보존 여부
8. run_report 생성 여부
9. malformed 문서 처리
10. 빈 문서 처리

## 4. RAG MVP 검토 항목

초기 RAG MVP는 답변 품질보다 traceability를 먼저 본다.

검토 항목:

1. chunk 기준
2. source file reference
3. page/section/table reference
4. retrieval evidence
5. rejected source 분리
6. hallucination 방지 문구
7. 검색 실패 처리
8. 외부 서버 의존 여부

## 5. KG / Viewer MVP 검토 항목

초기 KG viewer는 read-only 기준으로 시작한다.

검토 항목:

1. node/edge schema
2. source trace
3. local file loading
4. read-only 보장
5. graph rendering 여부
6. 검색/필터 가능성
7. 원본 수정 금지
8. export 가능 여부

## 6. Thin Orchestrator 예시

허용 가능한 초기 MVP:

```text
문서 샘플
→ metadata extractor
→ chunk/source trace generator
→ local json export
→ read-only viewer 또는 summary report
```

제외 범위:

1. 사내 검색 시스템 연동
2. Google Drive/Sheet 필수 연동
3. cloud vector DB
4. 권한 관리
5. 다중 사용자 workflow
6. 자동 승인 시스템

## 7. Evidence 기준

1. 입력 문서 목록
2. source trace
3. output json/report
4. 변환 실패 목록
5. skipped file reason
6. run_report
7. known limitation
8. 회사 PC 재검증 필요 여부
