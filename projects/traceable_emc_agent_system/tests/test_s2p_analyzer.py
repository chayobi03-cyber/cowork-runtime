import math
from pathlib import Path

from s2p_analyzer import _to_complex, db20, parse_s2p


def test_db20_unity_magnitude_is_zero_db():
    assert db20(complex(1.0, 0.0)) == 0.0


def test_db20_half_magnitude_is_about_minus_6db():
    assert math.isclose(db20(complex(0.5, 0.0)), -6.0206, abs_tol=0.01)


def test_db20_zero_magnitude_returns_sentinel_not_crash():
    assert db20(complex(0.0, 0.0)) == -999.0


def test_to_complex_ri_format():
    c = _to_complex(3.0, 4.0, "RI")
    assert c == complex(3.0, 4.0)


def test_to_complex_ma_format_matches_expected_magnitude_angle():
    c = _to_complex(1.0, 90.0, "MA")
    assert math.isclose(abs(c), 1.0, abs_tol=1e-9)
    assert math.isclose(c.real, 0.0, abs_tol=1e-9)
    assert math.isclose(c.imag, 1.0, abs_tol=1e-9)


def test_to_complex_db_format_zero_db_is_unity_magnitude():
    c = _to_complex(0.0, 0.0, "DB")
    assert math.isclose(abs(c), 1.0, abs_tol=1e-9)


def test_to_complex_rejects_unknown_format():
    import pytest

    with pytest.raises(ValueError):
        _to_complex(1.0, 1.0, "XY")


def test_parse_s2p_reads_minimal_touchstone_file(tmp_path):
    content = (
        "! test fixture\n"
        "# Hz S RI R 50\n"
        "1000000.0 0.1 0.0 0.9 0.0 0.9 0.0 0.1 0.0\n"
        "2000000.0 0.2 0.0 0.8 0.0 0.8 0.0 0.2 0.0\n"
    )
    f = tmp_path / "sample.s2p"
    f.write_text(content, encoding="utf-8")

    points, meta, warnings = parse_s2p(f)

    assert len(points) == 2
    assert points[0].freq_hz == 1000000.0
    assert points[0].s21 == complex(0.9, 0.0)
    assert meta["frequency_unit"] == "HZ"
    assert meta["data_format"] == "RI"
