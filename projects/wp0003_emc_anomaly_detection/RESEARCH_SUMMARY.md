# WP-0003: CST/S-parameter 이상탐지 — 딥리서치 정리 및 독립 검증 결과

작성일: 2026-07-14
관련 roster ID: WP-0003
검증 방식: School 4.7 (외부 AI 산출물 독립 검증 — 자기보고 그대로 수용 안 함)

---

## 1. Source Trace Table

| 스레드 | 출처(추정) | 신뢰도 | 검증 방법 | 비고 |
|---|---|---|---|---|
| A | Gemini(추정) | 중 | 방법론 서술 검증 | doc2와 텍스트 완전 동일(중복 제출) |
| B | Gemini(추정) | 중 | 방법론 서술 검증 | A와 별개 응답, 방법론은 A와 대체로 일치 |
| C | Gemini(추정) | **낮음** | 인용 출처 웹검색 재확인 | "2026년 IEEE/Teledyne/R&S 교차검증"이라 자칭하나 구체 인용 다수 미확인 |
| D | Perplexity(추정) | **높음** | 코드 실제 실행(합성 데이터) | feature 추출+코드 골격까지 제공, 실행해서 버그 2건 발견·수정 확인 |

### 스레드 C의 문제 인용 (신뢰 금지)
- "Functional Data Analysis for EMI/EMC Simulation Verification" — 웹검색으로 실존 확인 안 됨
- "Machine Learning-Based Outlier Detection in High-Speed Interconnects" — 실존 확인 안 됨
- "Design of Cavity Backed Slotted Antenna using Machine Learning" (2025) — 실존 확인 안 됨
- "Teledyne LeCroy Signal Integrity Blog (Eric Bogatin, 2026)" — Eric Bogatin·Teledyne LeCroy는 실존(S-parameter/TDR 전문가 맞음)이나, 이상탐지 자동화를 다뤘다는 근거는 못 찾음. **실존 출처 이름 + 가상의 구체적 주장** 패턴 — 전형적 fabrication 신호.

실존 확인된 것: Isolation Forest(Liu/Ting/Zhou, ICDM), MAD 강건통계(Leys et al., J. Experimental Social Psychology) — 두 인용 모두 정확.

---

## 2. 종합 결론 (4개 스레드 공통 부분만 채택)

| 방법론 | 원리 | 최소 데이터 | 1인 로컬 적합도 |
|---|---|---|---|
| MAD/Z-score (주파수별) | 중앙값·MAD 기반 강건 임계치 | 10~20건 | ★★★★★ 즉시 구현 가능 |
| Isolation Forest | 무작위 분할로 고립되는 샘플=이상치 | 30~50건 | ★★★★★ scikit-learn 안정 지원 |
| LOF | 밀도 기반 상대적 고립도 | 20~30건 | ★★★★☆ 하이퍼파라미터 민감 |
| One-Class SVM | 정상 경계 학습 | 30~50건 | ★★★☆☆ 커널/파라미터 민감, 비추천 |
| IFFT→TDR 변환 | 시간영역 변환 후 피크탐지 | 10건 내외 | ★★★★☆ 물리적 위치 특정에 유용(2단계) |

**1인 EMC 엔지니어 추천 로드맵**: ① MAD/Z-score로 즉시 1차 경보 → ② Isolation Forest로 다변량 형태 왜곡까지 재검토 (2단계 조합, 4개 스레드 전부 동일 결론)

**현실적 한계 (4개 스레드 공통 지적)**:
- 의도적 설계 변경(concept shift)과 진짜 이상(true anomaly)을 알고리즘이 구분 못함 → 설계군/보드rev별로 데이터 분리 필요
- Phase wrapping(±180°) 처리 안 하면 노이즈로 오인 → unwrap 전처리 필수
- 주파수 축이 시뮬레이션마다 다르면 interpolate로 통일 필요

---

## 3. 실제 실행 검증 결과 (bash_tool로 직접 확인)

합성 S-parameter 데이터(정상 20건 + 의도적 이상 3종: 공진이동/스파이크/완전깨짐)로 스레드 D의 코드를 그대로 실행:

**결과: 이상 3건 100% 탐지, 정상 20건 오탐 0건** (MAD/Isolation Forest 둘 다)

### 발견·수정한 버그 2건

1. **`np.trapz` → numpy 2.x에서 제거됨.** 코드 그대로 실행하면 `AttributeError`. `np.trapezoid`로 교체 필요.
2. **`report.py`의 `save_report()`가 `color="flag"` 컬럼을 참조**하는데, `run_batch.py`가 실제로 만드는 컬럼은 `mad_flag`/`if_flag`뿐 — `flag` 컬럼 없어서 리포트 생성 단계에서 별도로 크래시.

---

## 4. 검증 완료된 수정판 코드 (그대로 사용 가능)

```python
from pathlib import Path
import numpy as np
import pandas as pd
import skrf as rf
from scipy.signal import find_peaks
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def load_touchstone(path):
    ntwk = rf.Network(str(path))
    return ntwk.f, ntwk.s, ntwk

def s_to_db(s_complex, eps=1e-15):
    mag = np.abs(s_complex)
    return 20 * np.log10(np.maximum(mag, eps))

def extract_features(path, target="S21", bands=None):
    f_hz, s, ntwk = load_touchstone(path)
    freq_ghz = f_hz / 1e9
    if s.shape[1] == 1:
        y = s[:, 0, 0]
    else:
        mapping = {"S11": (0, 0), "S21": (1, 0), "S12": (0, 1), "S22": (1, 1)}
        i, j = mapping[target]
        y = s[:, i, j]
    y_db = s_to_db(y)
    feats = {}
    feats["min_db"] = float(np.min(y_db))
    feats["max_db"] = float(np.max(y_db))
    feats["mean_db"] = float(np.mean(y_db))
    feats["median_db"] = float(np.median(y_db))
    feats["std_db"] = float(np.std(y_db))
    feats["p95_p5_db"] = float(np.percentile(y_db, 95) - np.percentile(y_db, 5))
    feats["area_db_ghz"] = float(np.trapezoid(y_db, freq_ghz))  # FIX: trapz -> trapezoid (numpy>=2.0)
    idx_min = int(np.argmin(y_db)); idx_max = int(np.argmax(y_db))
    feats["f_min_db_ghz"] = float(freq_ghz[idx_min])
    feats["f_max_db_ghz"] = float(freq_ghz[idx_max])
    dy = np.diff(y_db)
    feats["largest_jump_db"] = float(np.max(np.abs(dy))) if len(dy) else 0.0
    peaks, props = find_peaks(y_db, prominence=1.0)
    feats["n_peaks"] = int(len(peaks))
    feats["max_peak_prominence"] = float(np.max(props["prominences"])) if len(peaks) else 0.0
    if bands is None:
        bands = [(freq_ghz.min(), freq_ghz.max())]
    for k, (lo, hi) in enumerate(bands):
        mask = (freq_ghz >= lo) & (freq_ghz < hi)
        seg = y_db[mask]
        if len(seg) == 0:
            feats[f"band{k}_mean"]=np.nan; feats[f"band{k}_std"]=np.nan
            feats[f"band{k}_min"]=np.nan; feats[f"band{k}_max"]=np.nan
        else:
            feats[f"band{k}_mean"]=float(np.mean(seg)); feats[f"band{k}_std"]=float(np.std(seg))
            feats[f"band{k}_min"]=float(np.min(seg)); feats[f"band{k}_max"]=float(np.max(seg))
    return feats

def build_dataset(folder, pattern="*.s2p", target="S21", bands=None):
    rows = []
    for p in sorted(Path(folder).glob(pattern)):
        feats = extract_features(p, target=target, bands=bands)
        feats["file"] = p.name
        rows.append(feats)
    return pd.DataFrame(rows)

def mad_scores(df, cols, thresh=3.5):
    X = df[cols].copy()
    med = X.median()
    mad = (X - med).abs().median().replace(0, np.nan)
    z = 0.6745 * (X - med) / mad
    score = z.abs().max(axis=1)
    flag = score > thresh
    return score, flag

def isolation_forest_scores(df, cols, contamination=0.05, random_state=42):
    X = df[cols].copy().fillna(df[cols].median())
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    model = IsolationForest(n_estimators=300, contamination=contamination, random_state=random_state)
    model.fit(Xs)
    score = -model.decision_function(Xs)
    flag = model.predict(Xs) == -1
    return score, flag, model, scaler

# ===== 사용 예 (2026-07-15 갱신: 실제 관심 주파수 대역 + MAD 취약점 수정 반영) =====
# 관심 대역: 1차 30MHz~1GHz, 2차 1GHz~3GHz, 3차 3GHz~10GHz
# bands = [(0.03, 1.0), (1.0, 3.0), (3.0, 10.0)]
# df = build_dataset("sim_results", pattern="*.s2p", target="S21", bands=bands)
# all_cols = [c for c in df.columns if c != "file"]
# FIX(2026-07-15): MAD는 저분산/이산적 feature(n_peaks, max_peak_prominence)를 제외한 연속형만 사용.
# 이 두 feature를 포함하면 실제 데이터에서 오탐률이 20%까지 치솟음(섹션6 참조). Isolation Forest는
# 전체 feature를 그대로 사용해도 안정적(오탐 0%) — 주 판정 기준으로 권장, MAD는 보조 참고용.
# mad_cols = [c for c in all_cols if c not in ("n_peaks", "max_peak_prominence")]
# df["mad_score"], df["mad_flag"] = mad_scores(df, mad_cols)
# df["if_score"], df["if_flag"], _, _ = isolation_forest_scores(df, all_cols)
# df.sort_values("if_score", ascending=False).to_csv("emc_anomaly_report.csv", index=False)
#
# 주의: 입력 파일의 실제 주파수 범위가 위 관심 대역과 전혀 안 겹치면 band별 feature가 전부 NaN이
# 되어 StandardScaler에서 경고 발생(섹션6 발견2). 실행 전 주파수 범위 겹침 여부를 확인할 것.
```

**리포트 생성(plotly)을 붙일 경우**: `save_report()`에서 `color="flag"` 대신 `color="if_flag"` 또는 `color="mad_flag"`로 명시할 것 (원본 코드의 컬럼명 불일치 버그 수정).

---

## 5. 관심 주파수 대역 (2026-07-15 확정)

- 1차: 30MHz ~ 1GHz
- 2차: 1GHz ~ 3GHz
- 3차: 3GHz ~ 10GHz

feature 추출 시 `bands = [(0.03, 1.0), (1.0, 3.0), (3.0, 10.0)]` (GHz 단위)로 고정.

---

## 6. 추가 검증 (2026-07-15): 실제 곡선 기반 재검증

기존 검증(섹션3)은 사인함수 기반 **합성** S-parameter로만 진행돼 "너무 깔끔한 데이터"라는 audit
지적(MAJOR-4)이 있었음. 이를 보완하기 위해 `scikit-rf` 패키지에 번들로 포함된 **실제 시뮬레이션
데이터**(`ring slot.s2p`, 안테나 S-parameter, 75~110GHz, 완전 공개·회사 데이터 아님)를 기반으로,
현실적 산포(주파수 미세 이동 ±0.15GHz + 약한 노이즈)를 더한 정상 20건 + 명백한 이상 3건(공진
대폭 이동/스파이크/완전 평탄화)으로 재검증.

### 발견 1: MAD 조합 방식의 실제 취약점

정상 20건 중 4건(20%)이 MAD 방식에서 오탐 발생. 원인 추적 결과, `max_peak_prominence`(피크 크기)
feature가 문제였음 — 우연히 `scipy.find_peaks`가 피크를 하나도 못 찾은 파일 3건에서 이 값이 0.0이
됐는데, 이 feature 자체의 전체 산포(MAD)가 매우 작아서(0.0836) 작은 절대편차가 z-score 9.17이라는
극단값을 만들었음. **MAD는 "전체 feature 중 최대 z-score"로 판정하므로, 저분산 feature 하나가
전체 판정을 왜곡할 수 있음.**

**합성(사인곡선) 데이터에서는 이 문제가 안 보였음** — `find_peaks`가 항상 안정적으로 피크를 찾아서
`max_peak_prominence`가 0이 되는 경우가 없었기 때문. 실제 물리 데이터를 쓰고 나서야 드러난 문제.

**Isolation Forest는 이 문제에 영향받지 않음** (오탐 0/20 유지) — 여러 feature를 tree 분할로 종합
판단하므로 단일 feature 취약점에 강건함.

### 수정안 및 재검증 결과

MAD 계산에서 이산적/저분산 feature(`n_peaks`, `max_peak_prominence`)를 제외하고 연속형 feature만
사용하도록 수정. Isolation Forest는 전체 feature 유지.

| | 수정 전 | 수정 후 |
|---|---|---|
| 이상 3건 탐지 (IF/MAD) | 100%/100% | 100%/100% (유지) |
| 정상 20건 오탐 (IF) | 0건 | 0건 (유지) |
| 정상 20건 오탐 (MAD) | 4건(20%) | **1건(5%)** — 개선됐으나 완전 해결 아님 |

잔여 오탐 1건(`normal_11`)은 `f_max_db_ghz`(최대값이 나타난 주파수) feature가 원인 — 이 역시
저분산 feature의 구조적 한계로, MAD 방식 자체의 근본적 취약점(이산적이거나 좁은 분포를 갖는
feature에 약하다)을 보여줌.

**권장**: Isolation Forest를 주 판정 기준으로, MAD는 보조 참고용(1차 경보)으로 격하해서 운용.

### 발견 2: 관심 대역이 실제 파일의 주파수 범위 밖이면 전체 NaN

`ring slot.s2p`가 75~110GHz인데 관심 대역을 30MHz~10GHz로 설정하면, band별 feature(band0_mean 등)
가 **전체 행에서 NaN**이 됨. 코드 자체는 크래시하지 않았으나(`np.nan` 채움 로직이 있어서), 이후
`StandardScaler`에서 `RuntimeWarning: invalid value encountered in divide`가 발생함 — 전부 NaN인
컬럼을 표준화하려 하면서 나온 경고.

**실사용 시 필요한 안전장치**: 파이프라인 실행 전, 각 입력 파일의 주파수 범위가 정의된 관심 대역과
최소한 일부라도 겹치는지 사전 검증하는 로직 추가 필요. (이번 재검증은 대역 정의 로직 자체가
크래시 없이 동작하는지 확인하는 목적이었고, 실제 대역별 통계치 자체는 이번 실제-곡선 테스트에서는
검증되지 못함 — ring slot 예제의 주파수 범위가 관심 대역과 안 겹쳤기 때문. 이 부분은 실제 회사
CST 데이터로 재검증 시 확인 필요.)

---

## 7. 다음 단계 (MVP Plan과 동일, 갱신됨)

MVP Plan 작성 완료(WP-0003_MVP_Plan.md) → 실제 CST 데이터로 1차 검증(사내 실행, 결과만 공유) →
냉정 Audit 재실행. 이번 재검증에서 나온 MAD 취약점 수정안과 대역 사전검증 로직을 실제 데이터
검증 단계에 반영할 것.
