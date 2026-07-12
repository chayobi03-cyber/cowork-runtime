# Export Safety Checklist

> 외부 AI(Claude/GPT 등)에 어떤 내용이든 입력하기 **직전**, 매번 1분 내로 아래 5문항을 확인한다.
> 하나라도 "포함됨"이면 export하지 않고 먼저 제거·치환한다.
>
> 이 체크리스트는 원칙 선언이 아니라 **강제 절차**다 — 통과 없이는 Topic Card의
> `external_ai_safety` 필드를 Y로 표시하지 않는다.

| # | 확인 항목 | 포함 여부 (Y/N) |
|---|---|---|
| 1 | 고객명이 포함되어 있는가 | |
| 2 | 제품명(사내 고유 명칭)이 포함되어 있는가 | |
| 3 | 사내 경로/파일 위치가 포함되어 있는가 | |
| 4 | 개인 이름이 포함되어 있는가 | |
| 5 | credential 또는 실제 raw 시험 결과 수치가 포함되어 있는가 | |

- 전부 N → export 가능, `external_ai_safety = Y`
- 하나라도 Y → 제거/치환 후 재확인, 그 전까지 `external_ai_safety = N` 유지

## company_only_validation 표기 기준

사내 회사 PC에서 실제로 돌려보거나 확인한 내용(raw data, 실제 시험 결과)은
`company_only_validation = Y`로 표기하고, 이 내용은 **애초에 위 체크리스트 대상이 아니라
export 자체를 하지 않는다** (사내 원본 폴더에만 보관).
