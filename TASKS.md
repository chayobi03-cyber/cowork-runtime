# Coworkai — 진행과제 (TASKS)

> **갱신 시 반드시 push까지 완료할 것.** 로컬 수정만 하고 push 전이면, Claude는 세션 시작 시
> git 최신 커밋만 읽으므로 그 수정 내용을 못 본다(구버전으로 오인). (MAJOR-2 대응)

> Track이 `School`인 항목은 상세 진행 상황이 School Roster(Google Sheets, 4.8)에 있다.
> 이 표에는 요약과 링크만 두고, 상세 갱신은 roster 쪽에서 한다. (MAJOR-1 대응)

| 프로젝트 | Track | 상태 | 다음 액션 | 우선순위 | 마지막 업데이트 |
|---|---|---|---|---|---|
| traceable_emc_agent_system | Non-School | 안정(known_open_items 없음, v0.4.2) | 신규 이슈 없음 — 관찰만 | 중 | 2026-07-12 |
| doc-rag-converter | Non-School | MAJOR 오픈 | dead code(`infer_approval_candidate`/`detect_version_candidate_from_filename`) 파이프라인 연결 또는 README 정정 | 상 | 2026-07-12 |
| MVP School 패키지 v0.5.4 | Non-School | MAJOR 3건 오픈 | run_report.json 스키마 정합, EMC_S2P_CST_NOTE 표준 인용, PROJECT_UPLOAD_GUIDE 갱신 | 상 | 2026-07-12 |
| KG Viewer MVP v0.2 | School (Graduate) | Post-grad backlog | 회사 PC Streamlit smoke evidence, negative test, 오프라인 설치 가이드, 부분 그래프 export → 상세는 School roster 참조 | 하 | 2026-07-12 |
| 사내 AI 경진대회 출품작 | Non-School | 진행 중 | PCB/EMI Engineering Copilot 계열 완성 | 상 | 2026-07-12 |
| Part Work Whitepaper / AI Context | Non-School | 보류(팀 미팅 전제) | v1 scope 축소 권고 후속 — 팀 미팅 후 재개 | 하 | 2026-07-12 |
| AIOS/LCY (Living Canon for You) | Non-School | 진행 중 | 컨텍스트 보존 프로젝트 계속 발전 | 중 | 2026-07-12 |

## 신규 항목 추가 방법

창엽님이 명시적으로 요청할 때만 이 표에 반영한다(트리거는 아직 미확정 — 반복되면 5절 사다리 기준으로
자동 반영 트리거를 검토).

## 이 파일의 위치

- School 재학 프로젝트의 상세 상태·Scorecard·BLOCKER 여부는 이 파일이 아니라 School Roster
  (Google Sheets, `coworkai_detailed_rules.md` 4.8)가 source of truth다.
- 이 파일은 School 밖 진행과제 + School 항목의 요약 포인터만 다룬다.
