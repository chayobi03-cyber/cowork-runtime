# cowork-runtime

Evidence-first AI Runtime

## 구조

- `templates/base_instructions.md` — 범용 실행 원칙 (프로젝트/AI 무관)
- `bindings/<project>.md` — 프로젝트별 5~7줄 연결 정보 (base_instructions 위에 얹음)
- `rules/coworkai_detailed_rules.md` — Coworkai 프로젝트 세부 운영 규칙 (source of truth)
- `DECISIONS.md` — 이 저장소 구조/운영 방식에 대한 결정 근거 기록
- `OFFLINE_ENV_GUIDE.md` — 사내(외부 git 접근 불가) 환경에서 이 저장소 쓰는 법
- `GIT_AUTH_TROUBLESHOOTING.md` — 이 저장소에 git push할 때 인증 실패사례/해결법
- `.cowork/runtime.yaml` — 머신 판독용 설정 요약

