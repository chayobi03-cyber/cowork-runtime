import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest
from run_case import derive_suffix


def test_derive_suffix_extracts_numeric_part():
    assert derive_suffix("RUN-0002") == "0002"


def test_derive_suffix_extracts_from_different_run_id():
    assert derive_suffix("RUN-9999") == "9999"


def test_derive_suffix_rejects_malformed_run_id():
    with pytest.raises(SystemExit):
        derive_suffix("NOT-A-VALID-ID")


def test_different_run_ids_produce_different_suffixes():
    # Regression test for the hardcoded-ID bug: two different run-ids must
    # never collapse to the same suffix (which previously happened because
    # the suffix was a literal "0002" regardless of --run-id).
    assert derive_suffix("RUN-0002") != derive_suffix("RUN-9999")
