# DOMAIN_NOTES/EMC_S2P_CST_NOTE.md — deprecated (2026-07-14)

## 상태

이 문서는 deprecated다. 새 작업에서 참조하지 않는다. NOTE_REGISTRY.md의 상태 정의를 그대로
따른다: "Kept for history; do not use for new work."

## 왜 deprecated인가

이 문서(요약형, 한국어)는 아래 두 특화 노트의 내용을 다른 형식으로 반복하고 있었다:

- S2P/Touchstone 관련 전체 → `DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md`
- CST 관련 전체 → `DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md`
- Thin Orchestrator 파이프라인 예시 → `examples/THIN_ORCHESTRATOR_EXAMPLE.md`

2026-07-14 기능 중복 점검에서 이 세 문서를 항목별로 대조한 결과, 이 문서에만 있는 고유 내용이
없다고 판단해 통합했다.

## 예외: 통합하지 않고 뺀 항목

이 문서 3절("S2P / Touchstone 검토 항목")에는 "reciprocity 가능성", "passivity 가능성" 판단이
포함돼 있었으나, `TOUCHSTONE_SPARAM_NOTE.md` 1절(Scope guard)은 passivity correction/causality
fitting을 명시적으로 범위 제외 대상으로 규정한다. 두 문서가 상충할 여지가 있어 Claude가 임의로
병합하지 않고 사용자에게 확인했고, **범위 제외 방향으로 확정**했다(TOUCHSTONE_SPARAM_NOTE.md의
기존 제외 범위를 그대로 유지, 별도 추가 없음). 이 판단 근거를 기록으로 남기기 위해 이 문서를
완전히 삭제하지 않고 deprecated 상태로 보존한다.

## 새 작업에서 할 일

1. S2P/Touchstone 관련 MVP → `DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md` 참조
2. CST schematic automation 관련 MVP → `DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md` 참조
3. 여러 모듈 통합(Thin Orchestrator) 예시 → `examples/THIN_ORCHESTRATOR_EXAMPLE.md` 참조
