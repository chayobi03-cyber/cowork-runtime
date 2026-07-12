from constraint_checker import build_result, check_ge, check_le
import argparse


def make_args(**overrides):
    defaults = dict(
        output="out.json",
        run_id="CONSTRAINT-RUN-0002",
        candidate_id="CAND-0001",
        rated_current_a=1.0,
        required_current_a=0.5,
        dcr_ohm=0.05,
        max_dcr_ohm=0.5,
        height_mm=0.6,
        max_height_mm=1.0,
        package="0603",
        allowed_package="0402,0603,1005,1608",
    )
    defaults.update(overrides)
    return argparse.Namespace(**defaults)


def test_check_le_passes_when_value_under_limit():
    result = check_le("dcr_limit", 0.1, 0.5, "ohm")
    assert result["passed"] is True


def test_check_le_fails_when_value_over_limit():
    result = check_le("dcr_limit", 0.6, 0.5, "ohm")
    assert result["passed"] is False


def test_check_ge_fails_when_value_under_limit():
    result = check_ge("rated_current_margin", 0.3, 0.5, "A")
    assert result["passed"] is False


def test_check_le_missing_value_is_not_silently_true():
    result = check_le("dcr_limit", None, 0.5, "ohm")
    assert result["passed"] is False
    assert "missing" in result["notes"]


def test_build_result_all_pass():
    result = build_result(make_args())
    assert result["passed"] is True
    assert all(c["passed"] for c in result["checks"])


def test_build_result_fails_when_package_not_allowed():
    result = build_result(make_args(package="9999", allowed_package="0402,0603"))
    assert result["passed"] is False
    package_check = next(c for c in result["checks"] if c["check_name"] == "package_allowed")
    assert package_check["passed"] is False


def test_build_result_fails_when_dcr_exceeds_limit():
    result = build_result(make_args(dcr_ohm=0.9, max_dcr_ohm=0.5))
    assert result["passed"] is False
