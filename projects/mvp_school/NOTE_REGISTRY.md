# NOTE_REGISTRY.md

## 1. Purpose

This file is the index for reusable notes in MVP School.

Notes are supporting references. They do not replace the source-of-truth files for admission, planning, audit, evidence, scorecard, or local handoff.

Source-of-truth priority remains:

```text
GPT_PROJECT_INSTRUCTIONS.md: project behavior guardrail only
SCHOOL_RULES.md: common operating rules and R0~R3 definitions
AUDIT_CHECKLIST.md: BLOCKER / MAJOR / LOW / PASS audit criteria
PERFORMANCE_SCORECARD.md: scoring criteria
EVIDENCE_GUIDE.md: evidence requirements
IDEA_CARD.md / MVP_PLAN.md / LOCAL_HANDOFF.md: working templates
```

## 2. Note status values

| Status | Meaning |
|---|---|
| active | Can be used as a current reference note |
| draft | Working note; use with caution |
| reference | Background note only; not a gate |
| deprecated | Kept for history; do not use for new work |

## 3. Registered notes

| Note file | Class | Purpose | Applies to | Status | Source-of-truth role |
|---|---|---|---|---|---|
| DOMAIN_NOTES/EMC_S2P_CST_NOTE.md | Domain | Existing minimum EMC/S2P/CST domain principles | EMC, S2P, CST MVPs | active | supporting note |
| DOMAIN_NOTES/DOC_RAG_KG_NOTE.md | Domain | Existing doc/RAG/KG domain principles | doc-rag, KG MVPs | active | supporting note |
| DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md | Domain | Touchstone/S-parameter pre-MVP checklist and evidence boundaries | S2P, Touchstone, CST import prep | active | supporting note |
| DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md | Domain | CST schematic automation boundaries and evidence checklist | CST automation MVPs | draft | supporting note |
| TOOL_NOTES/README.md | Tool | Template and rules for tool-specific notes | future tool notes | active | note authoring guide |
| CONCEPT_NOTES/README.md | Concept | Template and rules for reusable concept notes | future concept notes | active | note authoring guide |

## 4. When to add a new note

Add a note only when at least one condition is true.

```text
1. The same mistake or decision repeats at least twice.
2. The criterion is reusable across more than one MVP.
3. The criterion is domain-specific and too detailed for GPT_PROJECT_INSTRUCTIONS.md.
4. The criterion helps future local handoff or evidence interpretation.
```

Do not add a note for one-off conversation context.

## 5. Update rule

New note files are R2 Needs approval because they change the package.

Before adding or changing a note:

```text
1. State why the note is needed.
2. Confirm it does not duplicate source-of-truth gates.
3. Add it to this registry.
4. Update README.md if the folder structure changes.
5. Update MANIFEST_SHA256.txt and run_report.json.
6. Run tools/validate_mvp_school.py.
```
