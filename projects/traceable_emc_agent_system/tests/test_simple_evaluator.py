"""Regression tests for tools/simple_evaluator.py (v0.4.2, MAJOR-2 fix).

Covers the core claim of the fix: a criterion must fail when the upstream
tool's own judgment says fail, even if the file exists and parses fine.
Pure "file exists" is no longer sufficient for a pass.
"""
import json

from simple_evaluator import (
    check_constraint,
    check_evidence,
    check_report,
    check_s2p,
    derive_eval_id,
)


def write_json(tmp_path, name, data):
    path = tmp_path / name
    path.write_text(json.dumps(data), encoding="utf-8")
    return str(path)


def write_jsonl(tmp_path, name, rows):
    path = tmp_path / name
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    return str(path)


# --- s2p: file exists but tool itself reports warnings -> must fail ---


def test_s2p_fails_when_file_missing():
    passed, _ = check_s2p(None)
    assert passed is False


def test_s2p_fails_when_warnings_present_even_though_file_exists(tmp_path):
    path = write_json(tmp_path, "s2p.json", {"warnings": ["gap in frequency sweep"]})
    passed, notes = check_s2p(path)
    assert passed is False
    assert "warning" in notes


def test_s2p_passes_when_file_exists_and_no_warnings(tmp_path):
    path = write_json(tmp_path, "s2p.json", {"warnings": []})
    passed, _ = check_s2p(path)
    assert passed is True


# --- constraint: file exists but passed=False -> must fail ---


def test_constraint_fails_when_passed_is_false_even_though_file_exists(tmp_path):
    path = write_json(
        tmp_path,
        "constraint.json",
        {"passed": False, "checks": [{"check_name": "dcr_limit", "passed": False}]},
    )
    passed, notes = check_constraint(path)
    assert passed is False
    assert "dcr_limit" in notes


def test_constraint_passes_when_passed_is_true(tmp_path):
    path = write_json(tmp_path, "constraint.json", {"passed": True, "checks": []})
    passed, _ = check_constraint(path)
    assert passed is True


# --- evidence: rows exist but all relevance_score == 0 -> must fail ---


def test_evidence_fails_when_all_relevance_scores_are_zero(tmp_path):
    path = write_jsonl(
        tmp_path,
        "evidence.jsonl",
        [{"relevance_score": 0}, {"relevance_score": 0.0}],
    )
    passed, notes = check_evidence(path)
    assert passed is False
    assert "relevance_score" in notes


def test_evidence_passes_when_at_least_one_relevance_score_is_positive(tmp_path):
    path = write_jsonl(
        tmp_path,
        "evidence.jsonl",
        [{"relevance_score": 0}, {"relevance_score": 0.42}],
    )
    passed, _ = check_evidence(path)
    assert passed is True


def test_evidence_fails_when_file_missing():
    passed, _ = check_evidence(None)
    assert passed is False


# --- report: unchanged existence/non-empty behavior ---


def test_report_fails_when_missing():
    passed, _ = check_report(None)
    assert passed is False


def test_report_fails_when_empty(tmp_path):
    path = tmp_path / "report.md"
    path.write_text("", encoding="utf-8")
    passed, _ = check_report(str(path))
    assert passed is False


def test_report_passes_when_nonempty(tmp_path):
    path = tmp_path / "report.md"
    path.write_text("# report", encoding="utf-8")
    passed, _ = check_report(str(path))
    assert passed is True


# --- evaluation_id derivation: must not silently fall back to a hardcoded id ---


def test_derive_eval_id_extracts_numeric_suffix():
    assert derive_eval_id("RUN-0002") == "EVAL-0002"


def test_derive_eval_id_works_for_other_suffixes():
    assert derive_eval_id("RUN-9999") == "EVAL-9999"


def test_derive_eval_id_raises_on_missing_suffix():
    try:
        derive_eval_id("RUN-")
        assert False, "expected ValueError"
    except ValueError:
        pass
