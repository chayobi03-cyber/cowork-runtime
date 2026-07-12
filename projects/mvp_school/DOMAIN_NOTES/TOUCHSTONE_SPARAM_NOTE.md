# DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md

## 1. Scope guard

This document is not a Touchstone/S-parameter parser implementation specification.

This document defines only a pre-MVP human checklist and evidence boundary for Touchstone or S-parameter related MVP work.

The following are explicitly out of scope for this note:

```text
automatic pass/fail algorithms
formula-based acceptance thresholds
interpolation
renormalization
de-embedding
passivity correction
causality fitting
vendor model correction logic
Touchstone v1/v2 full grammar support
CST import automation code
parser column mapping implementation details
```

If any of those become necessary, create a separate MVP Plan first.

## 2. Purpose

Use this note when a project uses `.s2p`, Touchstone, or S-parameter files as representative inputs for EMC, filter, or CST-adjacent MVPs.

The purpose is to prevent false completion claims such as "S2P validated" when only a file was opened or parsed superficially.

## 3. Representative input

Examples of representative inputs:

```text
BLM18SG221TN1_series.s2p.txt
BLM15PX121SN1_series.s2p.txt
LQW15CAR11J00_series.s2p.txt
```

These samples are fixtures or reference inputs. They are not automatically approved part libraries.

## 4. Representative output

Allowed MVP-level outputs:

```text
file_seen: yes/no
header_seen: yes/no
frequency_unit_seen: yes/no
format_seen: yes/no
reference_impedance_seen: yes/no
port_column_hint_seen: yes/no
representative_frequency_order_check: yes/no/not_checked
source_type_recorded: vendor/measured/generated/unknown
known_limitations: text
```

This output is a checklist result, not a physics validation result.

## 5. O/X checklist only

Use only O/X or yes/no/not_checked checks at this note level.

| Check | Allowed values | Evidence example |
|---|---|---|
| Header exists | yes/no | `# Hz S RI R 50` line captured |
| Frequency unit is visible | yes/no | `Hz`, `MHz`, or other unit appears in header or comment |
| S-parameter format is visible | yes/no | `S RI`, `S MA`, or `S DB` appears |
| Reference impedance is visible | yes/no | `R 50` or equivalent appears |
| Port/data column hint is visible | yes/no/not_checked | comments or sample rows show S11/S21/S12/S22-like structure |
| Representative frequency ordering checked | yes/no/not_checked | first few representative rows appear increasing |
| Source type recorded | yes/no | vendor/measured/generated/unknown recorded |

## 6. What not to claim

Do not claim:

```text
Touchstone parser complete
S2P physically valid
passivity validated
reciprocity validated
causality validated
CST import verified
vendor model approved
part library approved
```

unless separate execution evidence proves that exact claim.

## 7. Smoke test boundary

A minimal smoke test may check only that one to three representative files can be read and summarized into the O/X checklist.

A smoke test must not silently convert checklist presence into physical pass/fail judgment.

## 8. Evidence criteria

Minimum evidence for this note:

```text
input filename
file hash or source trace if available
captured header/comment lines
checklist output
known limitations
run_report entry
```

## 9. Risk tier examples

```text
R0: read-only inspection of S2P header/comment lines
R1: draft checklist summary from existing S2P files
R2: modifying parser, validator, test fixture, or run_report schema
R3: external download, company confidential export, CST batch execution, or vendor library approval claim without evidence
```
