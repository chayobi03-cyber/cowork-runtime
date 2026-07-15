# GIT_AUTH_TROUBLESHOOTING.md — 이 저장소에 git push할 때 인증 실패사례/해결법

> Claude(또는 다른 AI/사람)가 샌드박스·컨테이너 환경에서 이 저장소에 git push를 시도할 때
> 참고하는 운영 가이드다. OFFLINE_ENV_GUIDE.md와 같은 성격의 "환경/도구 사용법" 문서다.

## 실패사례 (2026-07-14)

`gh auth login --hostname github.com --git-protocol https --web`을 백그라운드로 띄우는 방식
(`setsid nohup gh auth login ... < /dev/null > logfile 2>&1 &`)이 **2026-07-12 세션에서는 2회
성공**했으나, **2026-07-14 세션에서는 3회 연속 실패**했다.

- 증상: device code 발급 직후 프로세스가 `ps`에서 사라짐. `~/.config/gh/hosts.yml`도 생성 안 됨.
- 추정 원인(미확정): 사람이 브라우저에서 코드를 입력하는 몇 분 사이, 샌드박스가 tool call 사이의
  detached 백그라운드 프로세스를 정리하는 것으로 보임. 확정된 원인은 아니다.
- 결론: 이 방식은 같은 환경 안에서도 성공/실패가 오락가락해 **신뢰할 수 없다**. "백그라운드
  프로세스가 사람의 승인 대기 시간(수 분) 동안 생존해야 한다"는 전제 자체가 위험하다.

## 권장 방식 (2026-07-14 성공 확인, 백그라운드 프로세스 불필요)

gh CLI의 `auth login`을 쓰지 않고 GitHub Device Flow API를 직접 curl로 호출한다. 이 방식은
승인 대기 중에 아무 프로세스도 살아있을 필요가 없어, 세션 중간에 다른 대화가 끼어들어도 안전하다.

**1단계 — device code 발급 (1회 호출)**

```bash
curl -s -X POST https://github.com/login/device/code \
  -H "Accept: application/json" \
  -d "client_id=178c6fc778ccc68e1d6a" \
  -d "scope=repo"
```

- `client_id=178c6fc778ccc68e1d6a`는 GitHub CLI(`gh`)의 공개 OAuth 클라이언트 ID다. Device flow는
  public client 방식이라 client secret이 필요 없다.
- 응답에서 `user_code`(사람에게 보여줄 코드)와 `device_code`(다음 단계에서 쓸 값)를 받는다.
- 사람에게: `https://github.com/login/device` 접속 → `user_code` 입력 → 승인 요청.

**2단계 — 사람이 승인 완료했다고 확인하면 토큰 발급 (1회 호출)**

```bash
curl -s -X POST https://github.com/login/oauth/access_token \
  -H "Accept: application/json" \
  -d "client_id=178c6fc778ccc68e1d6a" \
  -d "device_code=$DEVICE_CODE" \
  -d "grant_type=urn:ietf:params:oauth:grant-type:device_code"
```

- `authorization_pending` 응답이면 아직 승인 전 — 사람에게 재확인 후 같은 명령 재시도.
- 성공하면 `access_token`(`gho_`로 시작) 반환.

**3단계 — 주의: `gh auth login --with-token`은 이 토큰으로 실패할 수 있음**

`scope=repo`만 요청한 토큰을 `gh auth login --with-token`에 넣으면 다음 에러가 난다:

```text
error validating token: missing required scope 'read:org'
```

gh CLI 자체의 로그인 검증이 `repo` 스코프만으로는 통과되지 않는다. **git push만 되면 되는 경우**
gh CLI 로그인 자체를 우회하고 git에 토큰을 직접 물리는 게 더 간단하고 확실하다.

```bash
git remote set-url origin "https://x-access-token:${TOKEN}@github.com/chayobi03-cyber/cowork-runtime.git"
git push origin main
# push 끝나면 보안 위생상 토큰 없는 URL로 되돌린다
git remote set-url origin "https://github.com/chayobi03-cyber/cowork-runtime.git"
```

토큰을 담은 임시 파일(있다면)도 push 후 바로 삭제한다.

## 우선순위 갱신 (2026-07-16) — Fine-grained PAT를 1안으로

Device flow(위 "권장 방식")는 `scope=repo`라 계정이 접근 가능한 **모든** 저장소에 대한 읽기/쓰기
권한을 가지며, 만료(`expires_in`)도 설정돼 있지 않아 폐기하지 않는 한 무기한 유효하다. 창엽님이
"매번 재발급 승인하는 번거로움 대신, 저장소 하나로 범위를 좁히고 만료 기한도 직접 정할 수 있는
방식"을 요청해(2026-07-16) 다음으로 우선순위를 재정렬한다.

**1안 (다음 세션부터 먼저 안내할 것) — Fine-grained Personal Access Token**

창엽님이 GitHub Settings → Developer settings → Fine-grained tokens에서 직접 발급:
- Repository access: `cowork-runtime` 저장소 하나로 제한
- Permissions: `Contents: Read and write`만 (그 이상 불필요)
- Expiration: 원하는 주기로 직접 지정(예: 7일/30일/90일/커스텀) — 매 세션 재인증 없이 만료 전까지
  재사용 가능
- 발급된 토큰 값은 Claude의 memory에 저장하지 않는다(credential은 memory 대상 아님) — 창엽님이
  보관했다가 세션 시작 시 대화에 붙여넣으면, 그 값으로 바로 `git remote set-url`에 물려서 push한다
  (아래 "권장 방식" 3단계와 동일한 방식, device flow 단계만 생략)

**2안 (완전히 폐기하지 않음, 창엽님이 PAT 없이 즉석에서 인증하고 싶을 때)** — 위 "권장 방식"의
curl 기반 device flow. 매번 새로 발급받아야 하고 스코프가 넓지만, 별도 사전 설정 없이 그 자리에서
바로 인증 가능하다는 장점이 있어 대안으로 유지한다.

**3안 (fallback)** — `setsid nohup gh auth login ...` 방식. 신뢰도가 낮아(성공/실패가 오락가락)
1·2안이 모두 막혔을 때만 시도한다.

> 앞으로 Claude가 이 저장소에 push해야 할 때는, **먼저 창엽님께 1안(Fine-grained PAT)을 쓸지
> 2안(device flow)을 쓸지 물어보고**, 답이 없거나 "아무거나"면 1안을 우선 안내한다.

## 앞으로의 순서 (기존 device flow 진행 시 — 위 1안 미사용 시에만 해당)

1. **먼저**: 위 "권장 방식"(curl 기반 device flow, 백그라운드 프로세스 없음)을 시도한다.
2. 이게 막히면(예: device flow API 자체가 네트워크 정책으로 차단된 환경) `setsid nohup gh auth
   login ...` 방식을 fallback으로 시도한다 — 완전히 폐기하지는 않는다, 우연히 될 수도 있다.
3. gh CLI가 컨테이너에 기본 설치돼 있지 않으면 릴리즈 tarball을 직접 받는다:
   `curl -sL https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_amd64.tar.gz -o gh.tar.gz && tar xzf gh.tar.gz`
   (`github.com`, `codeload.github.com`, `release-assets.githubusercontent.com`이 보통 네트워크
   허용 도메인에 포함돼 있어 이 다운로드 방식이 대체로 가능하다.)

## 실제 성공 사례

- 2026-07-14, commit `60a30ba` — School 프로젝트 간 기능 중복 정리 push. 위 curl 기반 방식으로
  인증 → git remote에 토큰 직접 설정 → push → GitHub API로 원격 반영 독립검증까지 완료.
