# PROJECT_SOURCE_INDEX.md

## 1. Purpose

This file maps the `mvp_school/` repo package to ChatGPT Project reference files.

ChatGPT Project sources may be uploaded as flat individual files, while the company PC/repo package keeps a folder structure. This index prevents confusion between those two modes.

## 2. Priority definitions

| Priority | Definition |
|---|---|
| P0 | Directly affects GPT behavior or graduation/audit judgment |
| P1 | Required to write Idea Card, MVP Plan, Local Handoff, Evidence, or Scorecard artifacts |
| P2 | Useful for current state tracking, note discovery, or domain-specific reference |
| P3 | Supporting evidence, examples, validator, manifest, or run report; useful in repo but not always needed in ChatGPT Project sources |

## 3. Project source upload index

| Priority | File | Repo path | Upload to ChatGPT Project? | Missing impact | Notes |
|---|---|---|---|---|---|
| P0 | GPT_PROJECT_INSTRUCTIONS.md | mvp_school/GPT_PROJECT_INSTRUCTIONS.md | Yes | GPT may not follow the intended project behavior | Copy body into project instructions and upload as reference if useful |
| P0 | SCHOOL_RULES.md | mvp_school/SCHOOL_RULES.md | Yes | R0~R3 and common rules may be unavailable | Source of truth for R0~R3 definitions |
| P0 | AUDIT_CHECKLIST.md | mvp_school/AUDIT_CHECKLIST.md | Yes | BLOCKER/MAJOR/LOW/PASS gate may be unavailable | Source of truth for audit judgment |
| P1 | IDEA_CARD.md | mvp_school/IDEA_CARD.md | Yes | New ideas may not be admitted consistently | Template source of truth |
| P1 | MVP_PLAN.md | mvp_school/MVP_PLAN.md | Yes | Plan-first workflow may lose structure | Template source of truth |
| P1 | LOCAL_HANDOFF.md | mvp_school/LOCAL_HANDOFF.md | Yes | Graduation handoff may be incomplete | Template source of truth |
| P1 | EVIDENCE_GUIDE.md | mvp_school/EVIDENCE_GUIDE.md | Yes | Completion claims may lack evidence criteria | Evidence source of truth |
| P1 | PERFORMANCE_SCORECARD.md | mvp_school/PERFORMANCE_SCORECARD.md | Yes | Graduation scoring may be inconsistent | Scorecard source of truth |
| P2 | CURRENT_PROGRESS.md | mvp_school/CURRENT_PROGRESS.md | Recommended | Current package state may be unclear | Useful during ongoing project work |
| P2 | NOTE_REGISTRY.md | mvp_school/NOTE_REGISTRY.md | Recommended | Note files may be hard to discover | Upload when using domain/tool/concept notes |
| P2 | PROJECT_SOURCE_INDEX.md | mvp_school/PROJECT_SOURCE_INDEX.md | Recommended | Flat upload vs repo structure may drift | This file |
| P2 | PROJECT_UPLOAD_GUIDE.md | mvp_school/PROJECT_UPLOAD_GUIDE.md | Recommended | Upload workflow may be unclear | Operational guide |
| P2 | DOMAIN_NOTES/EMC_S2P_CST_NOTE.md | mvp_school/DOMAIN_NOTES/EMC_S2P_CST_NOTE.md | When relevant | EMC/S2P/CST domain boundaries may be unavailable | Supporting note |
| P2 | DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md | mvp_school/DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md | When relevant | Touchstone pre-MVP checklist may be unavailable | Checklist only, not parser spec |
| P2 | DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md | mvp_school/DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md | When relevant | CST automation boundaries may be unavailable | Draft supporting note |
| P3 | run_report.json | mvp_school/run_report.json | Optional | Latest package validation evidence may be unavailable | Evidence record, not source of truth |
| P3 | MANIFEST_SHA256.txt | mvp_school/MANIFEST_SHA256.txt | Optional | Package integrity cannot be checked from uploaded sources alone | Repo/package evidence |
| P3 | tools/validate_mvp_school.py | mvp_school/tools/validate_mvp_school.py | Optional | Local validation command unavailable | Company PC/repo use |
| P3 | examples/RUN_REPORT_EXAMPLE.json | mvp_school/examples/RUN_REPORT_EXAMPLE.json | Optional | Example evidence shape unavailable | Example only |
| P3 | examples/THIN_ORCHESTRATOR_EXAMPLE.md | mvp_school/examples/THIN_ORCHESTRATOR_EXAMPLE.md | Optional | Example thin orchestrator unavailable | Example only |

## 4. Important limitation

If a file is not uploaded to the current ChatGPT Project or attached in the conversation, GPT must not assume it can read the file contents.

Use this statement when uncertain:

```text
I do not have the referenced mvp_school file in the current conversation/project sources. Please upload it or paste the relevant section.
```

## 5. Company PC rule

For company PC or repo work, keep the folder structure intact.

```text
your_project/
  mvp_school/
    DOMAIN_NOTES/
    TOOL_NOTES/
    CONCEPT_NOTES/
    examples/
    tools/
```

For ChatGPT Project sources, flat upload of selected markdown files is acceptable, but source-of-truth relationships must still follow this index.
