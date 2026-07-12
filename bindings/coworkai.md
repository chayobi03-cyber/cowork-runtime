# Binding — Coworkai

> 이 문서는 `templates/base_instructions.md`(범용) 위에 얹는 Coworkai 전용 5~7줄이다.
> 실제 Claude Project 커스텀 지침 칸에는 아래 "붙여넣을 내용"만 넣는다.

## 프로젝트 개요

Coworkai — PCB/EMI 엔지니어링 실무자(창엽님)의 AI 보조 워크플로우. EMC 자동화, 문서 관리,
지식 그래프 탐색 등을 GPT/Claude 병행 사용으로 체계화. GPT 산출물은 항상 Claude가 독립 검증.

## Detailed rules 위치

`rules/coworkai_detailed_rules.md` (이 저장소, 현재 v10) — source of truth.
세션 시작 시 이 저장소를 clone해서 최신본을 확인한다. Claude Project 지식파일에 detailed rules
사본이 있다면 그건 폴백용이며, 이 저장소와 내용이 다르면 저장소가 우선한다.

## 용어 매핑 (base_instructions.md 대응)

| base_instructions 용어 | Coworkai 대응 |
|---|---|
| Work Package | MVP School 재학 프로젝트 1개 (Roster 행 1개) |
| RFC | Idea Card 접수 단계 |
| Main Track | 실제 참조/실행되고 있는 산출물 (detailed rules 4.10) |
| Research Track | 참조 지식·조사 자료, 아직 미사용 (Main으로 승급 가능) |
| self-audit | detailed rules 섹션 1의 14개 항목 (Full/Quick 구분은 4.10) |

## ROI 맥락

16인 규모 조직. 과도한 자동화·테스트 프레임워크·엔터프라이즈급 확장은 기본적으로 거부(ROI 근거
없이 추가하지 않음).

---

## Claude Project 커스텀 지침 칸에 붙여넣을 내용 (그대로 복사)

```
Coworkai 프로젝트 — PCB/EMI 엔지니어링 실무자(창엽님)의 AI 보조 워크플로우.
GPT/Claude 병행 사용, GPT 산출물은 항상 Claude가 독립 검증.

Detailed rules source of truth: https://github.com/chayobi03-cyber/cowork-runtime
  → rules/coworkai_detailed_rules.md (현재 v10). 세션 시작 시 git clone으로 최신본 확인.
  프로젝트 지식파일의 detailed rules 사본은 폴백용이며, 저장소와 다르면 저장소 우선.

Base 실행원칙: 같은 저장소의 templates/base_instructions.md 참조
  (Evidence-first, Work Package=School 프로젝트, RFC=Idea Card, Main/Research Track,
  self-audit=detailed rules 섹션1 14개 항목).

ROI 맥락: 16인 조직, 과도한 자동화/프레임워크 확장 지양.
```
