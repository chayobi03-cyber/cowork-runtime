# OFFLINE_ENV_GUIDE.md — 사내(외부 git 접근 불가) 환경에서 이 저장소 쓰는 법

> 1차 인수인계 패키지(zip) 안내문. 사내 PC로 이 폴더를 그대로 옮겨서 로컬 git 저장소로
> 계속 쓸 때 참고한다.

## 이 zip에 뭐가 들어있나

`cowork-runtime` 저장소 **전체**의 사본이다. `.git` 폴더가 그대로 포함돼 있어서, 이 폴더
안에서는 원격(GitHub) 없이도 로컬 git 명령이 정상 동작한다.

- `rules/coworkai_detailed_rules.md` — Coworkai 운영 규칙 (거버넌스, source of truth)
- `templates/base_instructions.md`, `bindings/coworkai.md` — 실행 원칙 연결
- `projects/` — 모든 프로젝트(part_work_whitepaper 등)
- `.git/` — 커밋 이력 전체 (패키지 생성 시점까지)
- `README.md`, `DECISIONS.md`, `.cowork/runtime.yaml` — 저장소 구조/결정 근거

## 사내 PC에서 할 수 있는 것

- `git log`, `git diff`, `git show` 등 이력 조회 — 정상 동작 (네트워크 불필요)
- `git commit` — 로컬 커밋 쌓기 가능 (원격 push는 안 됨, 나중에 동기화)
- `git checkout -b <branch>` — 로컬 브랜치로 작업 격리 가능

## 사내 PC에서 할 수 없는 것 (원격 접근 필요)

- `git pull` / `git push` — GitHub(origin) 접근 불가
- 최신 원격 상태 확인 (이 패키지 생성 시점 이후 원격에 추가된 커밋은 반영 안 됨)

## 나중에 동기화할 때 (외부 접근 가능해지면)

1. 이 폴더에서 쌓인 로컬 커밋들을 확인: `git log origin/main..HEAD` (이 패키지의 origin/main
   기준 — 실제 원격의 최신 상태와는 다를 수 있으니 먼저 `git fetch`로 갱신 후 비교할 것)
2. 원격이 그 사이 변경됐다면 `git fetch && git rebase origin/main` (충돌 시 수동 해결)
3. 문제없으면 `git push origin main`

## 패키지 생성 시점 기록

- 생성일: 2026-07-13
- 마지막 커밋: f83a771e8199662bbdbd05023eed050a1ddd85b2 2026-07-13 21:11:56 +0000 LOW 4건 반영: representative_output/next_action 정리, 왜 질문 재명명, 커밋메시지 한국어 정책
