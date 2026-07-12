# External Structure Benchmark Report (압축판)

> 파트장급 청중 기준. 벤치마크당 2~3문장. 상세 원본 검토는 감사 결과(섹션별 점검 12절) 참조.

## 핵심 반영 (2개)

**GitLab Handbook-first** — 모든 운영 지식을 한 곳(single source of truth)에 문서로 남기고,
그 문서를 기준으로 업무를 굴리는 방식. 이 백서의 "본문+Registry+Card" 구조가 이 철학을
그대로 따른다.

**Diátaxis** — 문서를 설명(explanation)/방법(how-to)/참고(reference)/튜토리얼로 역할 분리하는
프레임워크. 이 백서의 "본문 요약(설명) vs Topic Card(방법) vs Registry(참고)" 구분이 이
프레임워크의 축소 적용판이다.

## 검토했으나 직접 채택 안 함 (3개, 한 줄 요약)

- **MADR/ADR**: 중요 결정을 정형 문서로 기록하는 방식. v1에서는 Decision Log 한 줄 기록으로
  대체하고, 번복이 반복되면 재검토.
- **Kubernetes KEP**: proposal/registry/stage 기반 관리. 이미 스스로도 "과함"을 인정한 벤치마크이며,
  축소해도 남는 개념이 Topic Card+Registry와 중복돼 별도 채택 안 함.
- **The Turing Way**: reproducibility/evidence 참고. Public reproducibility가 아니라 local
  reproducibility로 이미 evidence-first 원칙에 축소 반영됨(별도 구조 불필요).

## 운영 위치 관련 참고

- **Git**: 변경 이력 관리 후보지만 비개발자 비중 고려해 후순위.
- **SharePoint**: 비개발자 접근성 좋음, 사내 가용 여부 확인 필요.
- **MkDocs**: Markdown 기반 published view 후보, 나중 단계.
- **AGENTS.md / Copilot instructions / llms.txt / MCP**: AI-readable context 구조 참고 대상.
  v1에서는 AI_CONTEXT.md 1개로 축소 적용, 문서 수 10개 넘으면 확장 검토.

## 결론

원안이 참고한 8개 벤치마크 중 2개(GitLab Handbook-first, Diátaxis)만 v1 구조에 직접 반영,
나머지는 "검토했음" 수준으로 기록만 남기고 채택 보류.
