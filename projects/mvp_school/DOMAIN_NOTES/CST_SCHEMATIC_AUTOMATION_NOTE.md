# DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md

## 1. Scope guard

This document is not CST VBA/Python implementation code and not a CST API reference replacement.

It defines MVP boundaries, evidence expectations, and failure reporting for CST schematic automation ideas.

Actual CST automation code, CST batch runs, macro execution, external scripts, and company model export require a separate MVP Plan and approval.

## 2. Purpose

Use this note before starting a CST schematic automation MVP.

The goal is to avoid jumping directly from "CST can be automated" to a broad automation system without proving a small local path.

## 3. Representative input

Possible representative inputs:

```text
one simple circuit/schematic description
one S2P fixture path
one manually defined port/component list
one local CST help reference excerpt
```

Do not use confidential product models or internal customer files in external AI sessions.

## 4. Representative output

Allowed MVP-level outputs:

```text
planned schematic object list
planned connection list
manual run checklist
failure location summary
run_report entry
```

This note does not require actual CST execution.

## 5. Not in scope

```text
CST batch execution
licensed environment automation
full macro generation
full CST project generation
confidential model export
external server execution
database or UI integration
large batch conversion
```

## 6. Minimum smoke test idea

A valid first CST schematic automation MVP should be small enough to explain as:

```text
one representative input
one thin adapter or runner
one planned schematic/output summary
one run_report result
one failure location if it does not execute
```

If CST is not available on the current machine, the MVP may stop at a dry-run plan and evidence package, but it must clearly say "actual CST execution not verified".

## 7. Evidence criteria

Minimum evidence:

```text
input description or file list
CST availability status
exact command or manual step attempted, if any
output artifact or dry-run summary
failure log or limitation
run_report entry
company PC recheck requirement
```

## 8. Failure locations to separate

When CST automation fails, separate the failure location.

```text
input parse failure
mapping failure
script generation failure
CST environment unavailable
CST API/macro execution failure
license/runtime failure
output verification failure
```

## 9. Risk tier examples

```text
R0: read-only CST help review or local file inventory
R1: draft CST automation plan or dry-run checklist
R2: creating/modifying macro, runner, adapter, fixture, or run_report output
R3: CST batch execution without approval, external script execution, confidential export, credential access, or large batch run
```

## 10. Required wording discipline

Allowed wording:

```text
CST execution not verified
CST dry-run plan prepared
representative input only
company PC recheck required
```

Avoid wording:

```text
CST validated
automation complete
model physically verified
production-ready
```

unless evidence proves that exact claim.
