# SPK 라인 필터 비교 + 주석 + RAG 샘플

## 1. 시나리오

- Scenario ID: `SCN-0001`
- Type: `s2p_filter_compare`

## 2. 회로도/ODB 표시 기반 맥락

사람 표시 기반 EDA 맥락: SPK 양극 신호 경로 / EMC tags: filter_candidate, radiation_risk, speaker_line
- Candidate nets: SPK_P
- Candidate components: CN301, FB101

## 3. S2P 분석 요약

- Input: `data/sample/inputs/s2p_real/BLM18SG221TN1_series.s2p.txt`
- S21 avg: `-5.946914157524381` dB
- S21 min/max: `-11.711313372138646` / `-0.018246801489932674` dB
- Band metrics:
  - EMI_LOW: S21 avg -9.722703112172708 dB, points 115
  - EMI_HIGH: S21 avg -10.651622156598847 dB, points 61

## 4. 제약조건 점검

- Overall passed: `True`
- rated_current_margin: passed=True, value=1.0, limit=0.5
- dcr_limit: passed=True, value=0.05, limit=0.5
- height_limit: passed=True, value=0.6, limit=1.0
- package_allowed: passed=True, value=0603, limit=['0402', '0603', '1005', '1608']

## 5. RAG 근거 후보

- `EVC-0001` SPK 라인 EMI 비교 시 변경 전후 측정 조건, 케이블 배치, 부하 조건, 측정 대역을 동일하게 유지해야 한다. / relevance=0.273
- `EVC-0002` 필터 후보는 DCR, 정격전류, 패키지 크기, 높이, 승인 부품 여부를 확인해야 한다. / relevance=0.091

## 6. 검토 필요

- 본 보고서는 MVP 자동 생성 초안이다.
- RAG 결과는 Evidence Candidate이며, 사람 검토 후 Evidence Ledger에 승격해야 한다.
- S2P 결과는 입력 Touchstone 파일과 타겟 대역 조건을 재확인해야 한다.
