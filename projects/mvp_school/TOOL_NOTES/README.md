# TOOL_NOTES/README.md

## 1. Purpose

`TOOL_NOTES/` stores reusable guidance for specific tools or tool-like modules.

A tool note is not an implementation request. It is a local reference for scope, boundaries, validation, and evidence.

## 2. When to create a tool note

Create a tool note when a tool or module will likely be reused across multiple MVPs, or when recurring validation mistakes appear.

Examples:

```text
S2P_VALIDATOR_NOTE.md
TOUCHSTONE_PARSER_NOTE.md
CST_AUTOMATION_NOTE.md
DOC_RAG_CONVERTER_NOTE.md
KG_VIEWER_NOTE.md
```

## 3. Tool note template

```text
# Tool Note: <Tool Name>

## Purpose
## Representative Input
## Representative Output
## Not In Scope
## Execution Boundary
## Validation Criteria
## Evidence Criteria
## Common Failure Modes
## Minimum Smoke Test
## Risk Tier Notes
```

## 4. Boundary rule

Do not put full implementation specs in a tool note unless the user explicitly approves an implementation plan.

If code, schema, config, runner, queue, or evidence structure changes are needed, create an MVP Plan first.

## 5. Evidence rule

A tool note may define what evidence is needed, but it does not prove that the evidence exists.

Evidence must be produced by actual execution, test logs, output files, or run reports.
