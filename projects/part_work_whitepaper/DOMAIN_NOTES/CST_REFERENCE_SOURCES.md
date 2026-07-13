# CST_REFERENCE_SOURCES.md — CST 관련 작업 참조 위키

> **구조 안내**: 이 문서는 Topic Card가 아니다. TOPIC-0003(CST 해석법) 같은 특정 작업의 산출물이
> 아니라, **CST/EMC 시뮬레이션 관련 작업을 할 때마다 필요하면 열어보는 참조 자료 모음**이다.
> Track 분류(4.10)상 Research Track — 그 자체로 실행되지 않는 참조 지식이며, 실제 Main Track
> 작업(TOPIC-0003 공통부분 작성 등)에 반영하려면 그때그때 필요한 부분만 인용/발췌한다.
>
> 위키 원칙: 최신 유지보다 **필요할 때 추가**가 우선이다. 새 자료를 찾을 때마다 해당 카테고리에
> 항목만 추가하면 되고, 전체를 재구조화하지 않는다.

---

## 학계/논문 자료

| 자료 | 출처 | 한줄 설명 | 활용처 |
|---|---|---|---|
| EMPossible (CEM 강의) | empossible.net | UTEP Raymond Rumpf 교수의 전산전자기학 강의, 무료 공개, MATLAB 코드 포함 | 방법론 전반의 이론적 근거, 교육자료 톤 참고 |
| A Practical Guide to 3D Electromagnetic Simulation | Microwave Journal | 메쉬 수렴(convergence)·adaptation 실무 가이드, S-parameter 수렴 판단 기준 | 메쉬 단계 판단기준 인용 |
| EMI/EMC and Co-Existence Simulation Methodology (백서) | ANSYS, st.com 호스팅 | 실제 EMI 사례 기반 시뮬레이션-측정 상관관계 방법론 | Post-Processing/결과판정 챕터 근거 |
| EMC Measurement Setup Based on Near-Field Multiprobe System | IntechOpen | Huygens box, Near-field→Far-field 변환 방법론 | CST Farfield Calculation 챕터와 직결 |
| Tensorial Analysis of Networks (TAN) Modelling for PCB SI and EMC Analysis | IET 챕터 | PCB 특화 SI/EMC 해석 방법론 | 업무별 특화카드(PCB 관련) 참고 |
| Experimental near-field method for validating simulation antenna models | IEEE | 시뮬레이션 검증(측정 대비) 방법론 | 결과 신뢰도 판단 기준 |
| S-Parameters for Signal Integrity (책) | academia.edu | S-parameter 해석 전문서, 오픈소스 SignalIntegrity 패키지 동반 | S-Parameter 챕터 심화 근거 |
| EMI/EMC Computational Modeling Handbook | ResearchGate | IEEE Std 1597 기반 검증 교훈 정리 | 시뮬레이션 검증 일반론 |

## 오픈소스

| 자료 | 성격 | 한줄 설명 | 활용처 |
|---|---|---|---|
| openEMS | FDTD 솔버 (GPL, Matlab/Octave/Python) | CST와 나란히 비교검증된 논문 다수(결과 일치 확인 사례 있음) | 교차검증용 대안 솔버, 방법론 비교 |
| gprMax | FDTD (Python, 에딘버러대) | 안테나 시뮬레이션에도 활용, CST 대비 정확도 검증 논문 존재 | 교차검증 참고 |
| Meep / MaxFEM / FEniCS / FEMM / Elmer | FEM/FDTD 오픈소스 대안군 | learnemc.com/free-cem-codes, empossible.net에 목록 정리됨 | 필요시 개념 비교 |
| firegurafiku/microwave-studio-macros | GitHub, CST VBA 매크로 | 안테나 설계용 CST 매크로 모음 (박사과정 산출물) | 업무별 특화카드 스크립트 예시 |
| shimming-toolbox/CST-simulation-macros | GitHub, CST VBA 매크로 | 코일/여기(excitation) 태스크 시퀀스 자동화 매크로 | 반복작업 자동화 참고 |
| hbartle/CSTStudio_NFScanner | GitHub, CST VBA 매크로 | Near-field scanner 구성 + Farfield 결과 후처리 매크로 | Post-Processing 자동화 스크립트 예시 |
| SignalIntegrity (Python 패키지) | 오픈소스 | S-parameter 기반 SI 해석 도구 | S-Parameter 해석 실습/검증용 |

## 실무 사이트 (블로그/벤더 가이드)

| 자료 | 출처 | 한줄 설명 | 활용처 |
|---|---|---|---|
| The Basics of Signal Integrity Analysis and Simulation in PCB Design | Altium | S-parameter/모드변환 등 SI 해석 실무 가이드 | S-Parameter 챕터 실무 예시 |
| Guide to Signal Integrity Analysis in PCB Design | NWES Blog | S11/S21 읽는 법, 아이다이어그램 등 | 결과 판독 기준 |
| Reaffirm Signal Integrity Using S-Parameter Simulation | Cadence | 임피던스 매칭·반사 해석 | S-Parameter 실무 예시 |
| Signal Integrity Testing: Tools for High-Speed PCB Validation | AllPCB | TDR·de-embedding 등 측정-시뮬레이션 상관관계 실무 팁 | 검증 단계 참고 |
| CST VBA Macro Language 미러 | mweda.com | CST 구버전 VBA 레퍼런스 미러(공식 도움말 보완용) | 공식 문서 접근 안 될 때 대체 |

---

## 이 문서를 갱신하는 법

- 새 자료를 찾으면 해당 카테고리(학계/오픈소스/실무사이트) 표에 행만 추가한다. 표 구조나 컬럼을
  바꾸지 않는다.
- 카테고리 자체가 안 맞는 자료가 계속 쌓이면(예: 표준 규격 문서, 특정 업무 전용 자료) 그때 새
  카테고리를 추가한다 — 지금은 3개 카테고리로 충분하다 (5절 사다리 원칙과 동일 패턴).
- 이 문서는 TOPIC-0003 등 특정 작업에 종속되지 않으므로, 특정 Topic이 Graduate/Reject 되어도
  이 문서는 그대로 유지된다.
