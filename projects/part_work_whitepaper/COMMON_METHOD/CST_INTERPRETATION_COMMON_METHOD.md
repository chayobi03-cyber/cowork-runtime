# CST_INTERPRETATION_COMMON_METHOD.md — CST 해석법 공통부분 (뼈대)

> **범위 안내**: 이 문서는 TOPIC-0003(CST 해석법 — 공통부분)의 **뼈대**다. CST 원문
> (`3D Simulation Help.pdf` 50MB, `CST Online Help PDF Documents.zip` 73MB) 전체를 대조한
> 상세 방법론이 아니다 — 그 작업은 WP-0001이 School 졸업(4.4 Scorecard/4.5 BLOCKER 판정 통과)
> 하는 시점에 별도 AI에게 위임한다 (`CLAUDE_MAINTENANCE_LOG.md` 2026-07-13 항목 참조).
>
> 이 뼈대의 목적은 **지금 당장 업무별 특화 카드(parent_topic_id: TOPIC-0003)를 쓰기 시작할 수
> 있을 만큼**은 되는 것이다. 원문 전체 반영 여부가 완성 기준이 아니라, "이 뼈대만 보고 실제
> 카드 1건이라도 나올 수 있는가"가 완성 기준이다 (`TOPIC_REGISTRY.yaml` next_action 참조).
>
> **완성 기준 정교화 — 암묵지(暗默知) 점검**: "카드 1건이 나올 수 있는가"보다 더 중요한 건
> **AI(다른 세션의 Claude/GPT 등)나 신입사원이 이 문서만 읽었을 때, 경력자가 당연히 아는
> 암묵지가 빠져서 오판단하지 않는가**이다. 각 단계의 "흔한 실수" 칸이 바로 이 암묵지를 담는
> 자리다 — 표면적 절차(무엇을 클릭하는지)만 있고 "왜 그렇게 판단하는지/뭘 모르면 위험한지"가
> 없으면 이 완성 기준을 만족하지 못한 것으로 본다. 업무별 특화 카드 작성 시에도 동일 기준을
> 적용한다.
>
> 근거: `DOMAIN_NOTES/CST_REFERENCE_SOURCES.md`(외부 참조자료), CST Overview Help.pdf(전체
> 확보) + 3D Simulation Help.pdf TOC(목차만 확보, 본문은 페이지 219까지만 확보) + CST
> Workflow & Solver Overview 매뉴얼(2008판, rose-hulman.edu 미러, 솔버선택·포트선택 확인용,
> 2026-07-13 조사) — 확인 안 된 항목은 "확인 필요"로 명시하고 임의로 채우지 않는다.

---

## 구조: CST 자체 Ribbon 워크플로우를 뼈대로 사용

CST Overview Help.pdf의 "Perform an Electromagnetic Simulation" 8단계와 4개 Ribbon 탭
(Modeling / Mesh / Simulation / Post-Processing) 구조를 그대로 5단계로 재구성했다. 비중은
모델링~솔버설정(1~4단계)이 Post-Processing(5단계)보다 높다 — 창엽님 확인 사항.

각 단계는 4개 필드로 정리한다.
- **핵심 항목**: 이 단계에서 다루는 CST 기능/설정
- **판단 기준**: 엔지니어가 무엇을 근거로 결정하는지 (확인 필요 시 명시)
- **흔한 실수**: 이 단계에서 반복되는 오류 패턴
- **업무별 특화 슬롯**: 개별 업무 카드가 채워야 할 빈 자리

---

## 1단계 — 모델링

| 필드 | 내용 |
|---|---|
| 핵심 항목 | 형상(Shape) 생성/import, 재질(Material) 정의, Boundary Condition 설정 |
| 판단 기준 | **[확정 — 출처: CST 공식 help 원문(다수 CST 사용자 포럼에 인용된 공식 문구로 교차검증, 2026-07-15), 신뢰도: 중]** Boundary Condition은 해석 대상의 물리적 외부 환경을 그대로 반영하도록 선택한다. `Open (PML)`: 자유공간처럼 동작, 파가 최소 반사로 통과 — 방사/개방 문제 기본 선택. `Open (add space)`: Open과 동일하되 farfield 계산용 추가 공간 포함 — 안테나 문제에 권장. `PEC`: 이상도체 벽 가정이 타당한 경우에만 사용. `Periodic`: 주기 구조(unit cell)에 적용. — 재질 물성값 출처(데이터시트 vs 라이브러리 기본값)는 여전히 **확인 필요**(공식 문서상 우선순위 규칙 미확인, 2026-07-15 조사에서도 미확보 — 사내 실무 판단으로 채우는 게 ROI상 더 맞다는 기존 판단 유지) |
| 흔한 실수 | 재질 오할당, Boundary Condition 누락/과다 지정 (CAD import 단계의 단위 불일치도 포함 가능 — 확인 필요) |
| 업무별 특화 슬롯 | 이 업무에서 자주 쓰는 형상/재질 조합, 이 업무 특유의 BC 설정 |

## 2단계 — 메쉬

| 필드 | 내용 |
|---|---|
| 핵심 항목 | Hexahedral Mesh, Tetrahedral/Surface Mesh, 적응형 메쉬 리파인 |
| 판단 기준 | **메쉬 수렴(convergence) 확인** — 메쉬를 계속 세분화해도 관심 결과(주로 S-parameter)가 더 이상 유의미하게 변하지 않는 지점까지 확인 (출처: Microwave Journal 가이드, `DOMAIN_NOTES` 참조). **[확정 — 출처: mweda.com CST2013 미러, Time Domain Solver Overview 원문 직접 대조, 신뢰도: 상, 2026-07-15]** Hexahedral 메쉬는 Transient(FIT)/TLM 두 시간영역 솔버가 공유하지만 세부 타입이 `Hexahedral`(Transient/FIT용)과 `Hexahedral TLM`(TLM용)으로 구분됨. TLM은 EMC/EMI/E3 계열 문제에 특히 적합하며 octree 기반 메쉬로 셀 수를 효율화. **[확정 — 출처: CST2013 공식 Adaptive Mesh Refinement 설정문서, 신뢰도: 상, 2026-07-15]** Transient solver의 adaptive mesh refinement는 "Minimum" 패스 설정값이 기본 2회 — S-parameter가 두 패스 사이 유의미하게 변하지 않을 때까지 반복하되 최소 2회는 항상 수행. (Frequency Domain solver의 최소 pass 기본값은 이번 조사에서 미확인 — **확인 필요**로 유지) |
| 흔한 실수 | 수렴 확인 없이 기본 메쉬로 결과 확정, tetrahedral 솔버에서 mesh adaptation이 형상 근사 자체는 개선하지 못한다는 점 간과 |
| 업무별 특화 슬롯 | 이 업무에서 메쉬 밀도를 특히 신경 써야 하는 영역(좁은 간격, 얇은 도체 등) |

## 3단계 — 소스/포트

| 필드 | 내용 |
|---|---|
| 핵심 항목 | Excitation Source, Waveguide Port, Discrete Port, Multipin Port, Field Source 등 |
| 판단 기준 | **[잠정 — 웹 검색 스니펫(포럼/블로그) 기반, 구버전이라 최신문서 재검증 필요 — 신뢰도: 중간(원문 직접 확인 아님, 4단계보다 낮음)]** **Discrete Port**: 임피던스를 미리 아는 경우(예: 50Ω 마이크로스트립)에 적합, 정의가 간단. **Waveguide Port**: 임피던스를 모르거나 실제 전파모드 기반 여기가 필요할 때 우선 선택 — Hexahedral 솔버는 포트가 좌표축(X/Y/Z)에 정렬돼야 하고, Tetrahedral 솔버는 비정렬(회전된) 포트도 지원. **Multipin Port**: 여러 도체가 가까이 붙어 개별 포트로 분리 안 되는 경우(차동쌍, 신호선+그라운드 있는 CPW 등) — 신호선(+)/그라운드(-)로 극성 지정 |
| 흔한 실수 | Discrete↔Waveguide Port를 바꿨을 때 S11 결과가 달라지는 이유를 모르고 임의 선택함 — Discrete Port 주변 필드는 실제 전파모드와 달라 원치 않는 고차모드까지 함께 여기되기 때문. Hexahedral 솔버에서 포트를 축에 정렬하지 않고 사용(회전된 구조에서 특히 발생). Multipin 정의 시 포트 면적을 너무 크거나 작게 잡음 |
| 업무별 특화 슬롯 | 이 업무에서 주로 쓰는 Port 종류와 그 이유 |

## 4단계 — 솔버 설정

| 필드 | 내용 |
|---|---|
| 핵심 항목 | "Which Solver to Use" 판단, Time Domain / Frequency Domain / Eigenmode / Integral Equation / Multilayer / Asymptotic Solver 중 선택 |
| 판단 기준 | **[잠정 — 공식 매뉴얼 원문 확인, 구버전(2008판)이라 최신문서 재검증 필요 — 신뢰도: 높음(원문 직접 fetch)]** **"Which Solver to Use" 가이드라인표** (출처: CST Workflow & Solver Overview 매뉴얼, rose-hulman.edu 미러, 2026-07-13 확인 — "규칙이 아니라 가이드라인"으로 명시됨):<br>· 커넥터/PCB/디지털회로/EMI/방사문제 → Transient<br>· 스트립라인/패치안테나/필터 → Transient 또는 General Purpose Frequency Domain<br>· 공진기(cavity)/진행파 구조 → Eigenmode<br>· 전기적으로 큰 구조(안테나 배치, RCS) → Integral Equation 또는 Transient<br>**강제 규칙(예외 아님, 반드시 지켜야 함)**:<br>1. 비선형 다이오드 포함 → Frequency Domain 불가, 반드시 Transient<br>2. 메쉬 수백만 셀 이상(전기적으로 매우 큼) → Frequency Domain은 급격히 느려짐, Transient 또는 Integral Equation<br>3. 위상차 있는 주기구조 → Transient는 위상차 0인 주기구조만 가능, 반드시 Frequency Domain<br>4. 손실 있는 도파관 포트의 S-parameter → Frequency Domain (손실 포트 모드 계산 가능) |
| 흔한 실수 | 표를 "규칙"으로 오인해 예외 상황(원문에 "구조에 따라 표에 없는 솔버가 더 효율적일 수 있음"이라고 명시됨)을 고려 안 함. 강제 규칙 4가지(비선형/대형구조/위상차 주기구조/손실포트) 위반 — 예: 비선형 다이오드 구조에 Frequency Domain 솔버를 시도해 계산 자체가 성립하지 않음 |
| 업무별 특화 슬롯 | 이 업무에서 표준으로 쓰는 솔버 + 그 이유 |

## 5단계 — Post-Processing (결과 해석)

| 필드 | 내용 |
|---|---|
| 핵심 항목 | S-Parameter, Farfield Calculation(2D/3D/gain/RCS), SAR, Force/Torque, Loss/Q, AR-Filter, TDR, Polarization |
| 판단 기준 | **일부 확보**: Farfield는 Huygens box 기반 near-field→far-field 변환이 표준 방법(`DOMAIN_NOTES` IntechOpen 항목 참조). S-Parameter 판독 기준(반사/삽입손실 등)은 `DOMAIN_NOTES`의 Altium/Cadence/NWES 자료 참고 가능. 나머지(SAR/Force-Torque/TDR 등)는 확인 필요 |
| 흔한 실수 | S-Parameter를 측정과 직접 비교 시 de-embedding 누락(`DOMAIN_NOTES` AllPCB 항목 참조), Farfield 계산 시 근접장 조건 미충족 상태에서 원거리장으로 오판 |
| 업무별 특화 슬롯 | 이 업무에서 최종 판정에 쓰는 결과 지표와 합격/불합격 기준 |

---

## 아직 채우지 못한 것 (다음 세션 또는 위임 시점에 확인)

- 1단계(모델링) Boundary Condition은 2026-07-15 공식 help 원문 교차검증으로 채움. 다만
  재질 물성값 출처(데이터시트 vs 라이브러리 기본값) 우선순위는 CST 문서로 확인할 사안이라기보다
  **사내 실무 판단 기준**에 가까움 — 업무별 특화 카드 작성 시 실제 파트원 답변으로 채우는 게
  맞다 (원문 재조사보다 이쪽이 ROI가 높음)
- 2단계(메쉬) Frequency Domain solver의 adaptive mesh 최소 pass 기본값은 2026-07-15
  조사에서 확인 안 됨 — Transient solver(최소 2회)만 확정, F-solver는 여전히 확인 필요
- 3·4단계는 2026-07-13 웹 조사(CST 구버전 공개 매뉴얼, rose-hulman.edu 미러)로 확인 완료.
  다만 이 매뉴얼은 2008년판이라 최신(2026) 버전과 세부 UI/옵션이 다를 수 있음 — 원문(3D
  Simulation Help.pdf) 전체 대조는 여전히 위임 시점에 확인
- EMC 표준(CISPR/IEC 61000-4 등) 수치 기준은 섹션1 11번 원칙에 따라 여기서도 임의 확정하지
  않는다 — "기준 미정"으로 유지

## 이미지/다이어그램 포함 구조 (MVP 이후 확장 예정)

CST 해석법은 S-Parameter 그래프, Farfield 방사패턴, 메쉬 뷰, 포트 모드 시각화처럼 **텍스트만으로
설명하기 어려운 결과가 많다** — "흔한 실수"·"판단 기준" 칸의 암묵지도 스크린샷 한 장이 문장
여러 줄보다 나은 경우가 많다. 다만 지금(MVP 뼈대 단계)은 이미지 포함 구조를 만들지 않는다 —
4.3 MVP 범위 판정 기준상 UI/저장 구조까지 한 번에 넣으면 범위 초과다.

**MVP 이후 도입 시 고려할 방향** (지금 결정하지 않음, 착수 조건 충족 시 재검토):
- Topic Card 접수 매체가 스크린샷(WRITING_METHODOLOGY.md C-04~C-06)을 이미 지원하므로, 카드
  자체는 이미지 첨부가 가능함 — 부족한 건 **문서(이 COMMON_METHOD류) 안에서 이미지를 인라인으로
  보여주는 저장/참조 구조**임
- 후보안 1: 이미지를 Drive에 별도 보관하고 이 문서에는 링크만 삽입 (git 저장소는 텍스트 위주 유지)
- 후보안 2: git 저장소 내 `assets/` 폴더에 이미지 직접 커밋 (버전관리 이점, 저장소 용량 증가 트레이드오프)
- Export Safety(EXPORT_SAFETY_CHECKLIST.md C-04~C-06)는 이미지에도 그대로 적용 — 사내 정보
  노출 위험이 텍스트보다 크므로 이미지 포함 구조 도입 시 체크리스트를 다시 검토해야 함
- 착수 조건: 업무별 특화 카드가 실제로 몇 건 쌓여 "텍스트만으로는 안 된다"는 사례가 반복 확인될 때
  (5절 사다리 원칙과 동일 패턴 — 아직 필요성이 반복 확인되지 않았으므로 지금 만들지 않는다)

## 이 문서를 갱신하는 법

- "확인 필요" 표시가 있는 칸은 실제 원문 확인 또는 업무별 특화 카드 작성 과정에서 나온 내용으로
  채워지면 그 칸만 갱신한다. 표 구조 자체는 바꾸지 않는다.
- 업무별 특화 카드는 이 문서를 수정하지 않고 `TOPIC_REGISTRY.yaml`에 `parent_topic_id:
  TOPIC-0003`으로 별도 등록한다.
