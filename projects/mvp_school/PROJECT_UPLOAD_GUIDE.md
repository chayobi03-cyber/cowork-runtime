# PROJECT_UPLOAD_GUIDE.md

## 목적

이 문서는 `mvp_school/` 패키지를 ChatGPT 앱의 **이창엽 프로젝트**와 회사 PC 작업 폴더에 적용하는 방법을 설명한다.

## 1. GPT 앱 프로젝트 지침 적용

1. `GPT_PROJECT_INSTRUCTIONS.md`를 연다.
2. `---` 아래 내용을 복사한다.
3. ChatGPT 앱의 이창엽 프로젝트 전용 지침에 붙여넣는다.

## 2. GPT 앱 프로젝트 파일 업로드 권장 목록

프로젝트 sources/reference files에는 아래 파일을 우선 업로드한다.

```text
GPT_PROJECT_INSTRUCTIONS.md
SCHOOL_RULES.md
IDEA_CARD.md
MVP_PLAN.md
LOCAL_HANDOFF.md
PERFORMANCE_SCORECARD.md
AUDIT_CHECKLIST.md
EVIDENCE_GUIDE.md
CURRENT_PROGRESS.md
NOTE_REGISTRY.md
PROJECT_SOURCE_INDEX.md
```

도메인 작업을 진행할 때만 아래 파일을 추가 업로드한다.

```text
DOMAIN_NOTES/EMC_S2P_CST_NOTE.md
DOMAIN_NOTES/DOC_RAG_KG_NOTE.md
```

## 3. 회사 PC / repo 적용

회사 PC 작업 폴더 또는 Git repo 루트에 `mvp_school/` 폴더째 추가한다.

권장 구조:

```text
your_project/
  mvp_school/
  src/
  tests/
  data/
```

`mvp_school/`은 소스코드가 아니라 운영 지침, 템플릿, 검증 기준 폴더다.

## 4. 최소 검증

압축을 푼 뒤 다음을 실행한다.

```bash
python mvp_school/tools/validate_mvp_school.py mvp_school
```

v0.5.2 validator는 의도적으로 작게 유지한다.

검증 범위:

1. 필수 파일 존재 확인
2. README.md에 언급된 주요 파일 참조 일치 확인

## 5. 주의

회사 PC 전용 raw 자료는 ChatGPT 앱, Claude, Coworkai, Codex 등 외부 AI 세션에 그대로 붙여넣지 않는다.

외부 AI에 넣을 내용은 제품명, 고객명, 내부 경로, API key, credential 등 기밀 가능 정보를 제거한 정제본이어야 한다.
