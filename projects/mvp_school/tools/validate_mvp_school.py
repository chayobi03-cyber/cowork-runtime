#!/usr/bin/env python3
"""Minimal validator for MVP School v0.5.4.

Scope is intentionally small:
1. Check required files exist.
2. Check README-referenced package files exist.
3. Check a small set of required content markers that prevent known drift.
4. Check NOTE_REGISTRY.md references registered note files that exist.
5. Check PROJECT_SOURCE_INDEX.md P0/P1 core files exist.

Important limitation:
Content marker checks are keyword-based drift checks only. They do not prove
semantic correctness, domain validity, CST/S2P execution readiness, or physical
accuracy.

This validator intentionally does not perform secret scanning, schema validation,
regression testing, parser validation, physics validation, or enterprise-grade
governance checks.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "GPT_PROJECT_INSTRUCTIONS.md",
    "PROJECT_UPLOAD_GUIDE.md",
    "PROJECT_SOURCE_INDEX.md",
    "NOTE_REGISTRY.md",
    "SCHOOL_RULES.md",
    "IDEA_CARD.md",
    "MVP_PLAN.md",
    "LOCAL_HANDOFF.md",
    "PERFORMANCE_SCORECARD.md",
    "AUDIT_CHECKLIST.md",
    "EVIDENCE_GUIDE.md",
    "CURRENT_PROGRESS.md",
    "MANIFEST_SHA256.txt",
    "run_report.json",
    "DOMAIN_NOTES/EMC_S2P_CST_NOTE.md",
    "DOMAIN_NOTES/DOC_RAG_KG_NOTE.md",
    "DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md",
    "DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md",
    "TOOL_NOTES/README.md",
    "CONCEPT_NOTES/README.md",
    "examples/RUN_REPORT_EXAMPLE.json",
    "examples/THIN_ORCHESTRATOR_EXAMPLE.md",
    "tools/validate_mvp_school.py",
]

PROJECT_SOURCE_CORE_FILES = [
    "GPT_PROJECT_INSTRUCTIONS.md",
    "SCHOOL_RULES.md",
    "AUDIT_CHECKLIST.md",
    "IDEA_CARD.md",
    "MVP_PLAN.md",
    "LOCAL_HANDOFF.md",
    "EVIDENCE_GUIDE.md",
    "PERFORMANCE_SCORECARD.md",
]

PATH_PATTERN = re.compile(
    r"(?:^|[`\s])((?:[A-Za-z0-9_./-]+/)?[A-Za-z0-9_.-]+\.(?:md|json|py|txt))(?:[`\s]|$)",
    re.IGNORECASE,
)

NOTE_PATH_PATTERN = re.compile(
    r"\b((?:DOMAIN_NOTES|TOOL_NOTES|CONCEPT_NOTES)/[A-Za-z0-9_.-]+\.md)\b"
)

CONTENT_MARKERS = {
    "SCHOOL_RULES.md": [
        "작업 위험도 기준: R0~R3",
        "R0",
        "R1",
        "R2",
        "R3",
        "Auto",
        "Post-review",
        "Needs approval",
        "Blocked",
        "L0~L3",
    ],
    "GPT_PROJECT_INSTRUCTIONS.md": [
        "파일 내용을 안다고 가정하지 않는다",
        "mvp_school/SCHOOL_RULES.md",
        "mvp_school/AUDIT_CHECKLIST.md",
    ],
    "NOTE_REGISTRY.md": [
        "NOTE_REGISTRY",
        "DOMAIN_NOTES",
        "TOOL_NOTES",
        "CONCEPT_NOTES",
        "active",
        "draft",
    ],
    "PROJECT_SOURCE_INDEX.md": [
        "PROJECT_SOURCE_INDEX",
        "ChatGPT Project",
        "company PC",
        "P0",
        "P1",
        "P2",
        "P3",
    ],
    "DOMAIN_NOTES/TOUCHSTONE_SPARAM_NOTE.md": [
        "not a Touchstone/S-parameter parser implementation specification",
        "O/X checklist",
        "Reference impedance",
        "S11",
        "S21",
        "not_checked",
    ],
    "DOMAIN_NOTES/CST_SCHEMATIC_AUTOMATION_NOTE.md": [
        "CST",
        "schematic",
        "automation",
        "smoke test",
        "evidence",
        "CST execution not verified",
    ],
}


def extract_readme_references(readme_text: str) -> set[str]:
    refs: set[str] = set()
    for match in PATH_PATTERN.finditer(readme_text):
        ref = match.group(1).strip()
        if ref.startswith("mvp_school/"):
            ref = ref.removeprefix("mvp_school/")
        if ref in {"README.md"} or "/" in ref or ref.endswith((".md", ".json", ".py", ".txt")):
            refs.add(ref)
    refs = {r for r in refs if not r.startswith("python")}
    return refs


def file_exists_or_unique_basename(root: Path, rel: str) -> bool:
    candidate = root / rel
    if candidate.is_file():
        return True
    matches = [path for path in root.rglob(Path(rel).name) if path.is_file()]
    return len(matches) == 1


def validate_required_files(root: Path) -> list[str]:
    failures: list[str] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            failures.append(f"Missing required file: {rel}")
    return failures


def validate_readme_references(root: Path) -> list[str]:
    readme_path = root / "README.md"
    if not readme_path.is_file():
        return ["Cannot check README references because README.md is missing"]

    failures: list[str] = []
    refs = extract_readme_references(readme_path.read_text(encoding="utf-8"))
    for rel in sorted(refs):
        if rel == "README.md":
            continue
        if not file_exists_or_unique_basename(root, rel):
            failures.append(f"Missing README reference: {rel}")
    return failures


def validate_content_markers(root: Path) -> list[str]:
    failures: list[str] = []
    for rel, markers in CONTENT_MARKERS.items():
        path = root / rel
        if not path.is_file():
            continue
        body = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in body:
                failures.append(f"Missing content marker in {rel}: {marker}")
    return failures


def validate_note_registry_references(root: Path) -> list[str]:
    registry_path = root / "NOTE_REGISTRY.md"
    if not registry_path.is_file():
        return ["Cannot check NOTE_REGISTRY references because NOTE_REGISTRY.md is missing"]

    failures: list[str] = []
    body = registry_path.read_text(encoding="utf-8")
    refs = sorted(set(NOTE_PATH_PATTERN.findall(body)))
    if not refs:
        failures.append("NOTE_REGISTRY.md contains no registered note file paths")
        return failures
    for rel in refs:
        if not (root / rel).is_file():
            failures.append(f"Missing NOTE_REGISTRY reference: {rel}")
    return failures


def validate_project_source_index(root: Path) -> list[str]:
    index_path = root / "PROJECT_SOURCE_INDEX.md"
    if not index_path.is_file():
        return ["Cannot check PROJECT_SOURCE_INDEX because PROJECT_SOURCE_INDEX.md is missing"]

    failures: list[str] = []
    body = index_path.read_text(encoding="utf-8")
    for rel in PROJECT_SOURCE_CORE_FILES:
        if rel not in body:
            failures.append(f"Missing PROJECT_SOURCE_INDEX core entry: {rel}")
        if not (root / rel).is_file():
            failures.append(f"Missing PROJECT_SOURCE_INDEX core file: {rel}")
    return failures


def print_section_status(name: str, failures: list[str], prefix: str) -> None:
    print(f"{name}:", "PASS" if not any(f.startswith(prefix) or prefix in f for f in failures) else "FAIL")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()

    required_failures = validate_required_files(root)
    readme_failures = validate_readme_references(root)
    marker_failures = validate_content_markers(root)
    registry_failures = validate_note_registry_references(root)
    project_source_failures = validate_project_source_index(root)

    failures = (
        required_failures
        + readme_failures
        + marker_failures
        + registry_failures
        + project_source_failures
    )

    print("MVP School validation result")
    print(f"Root: {root}")
    print("Required files:", "PASS" if not required_failures else "FAIL")
    print("README references:", "PASS" if not readme_failures else "FAIL")
    print("Content markers:", "PASS" if not marker_failures else "FAIL")
    print("NOTE_REGISTRY references:", "PASS" if not registry_failures else "FAIL")
    print("PROJECT_SOURCE_INDEX core files:", "PASS" if not project_source_failures else "FAIL")
    print("Validator limitation: content markers are minimum drift checks only; they are not semantic or domain validation.")

    if failures:
        print("Final status: FAIL")
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Final status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
