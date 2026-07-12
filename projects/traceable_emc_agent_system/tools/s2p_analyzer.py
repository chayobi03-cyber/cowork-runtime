#!/usr/bin/env python3
"""Minimal Touchstone S2P analyzer for Traceable EMC Agent System.

Purpose:
- Parse simple 2-port Touchstone v1 files.
- Support RI, MA, and DB data formats.
- Compute basic S11/S21 dB metrics for target bands.
- Produce JSON compatible with schemas/tools/s2p_analysis_result.schema.json.

This tool intentionally avoids external dependencies for MVP portability.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

UNIT_FACTORS = {
    "HZ": 1.0,
    "KHZ": 1e3,
    "MHZ": 1e6,
    "GHZ": 1e9,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


@dataclass
class S2PPoint:
    freq_hz: float
    s11: complex
    s21: complex
    s12: complex
    s22: complex


def _to_complex(a: float, b: float, fmt: str) -> complex:
    fmt = fmt.upper()
    if fmt == "RI":
        return complex(a, b)
    if fmt == "MA":
        return cmath.rect(a, math.radians(b))
    if fmt == "DB":
        mag = 10 ** (a / 20.0)
        return cmath.rect(mag, math.radians(b))
    raise ValueError(f"unsupported S-parameter format: {fmt}")


def db20(value: complex) -> float:
    mag = abs(value)
    if mag <= 0:
        return -999.0
    return 20.0 * math.log10(mag)


def parse_s2p(path: Path) -> tuple[list[S2PPoint], dict[str, str], list[str]]:
    warnings: list[str] = []
    unit = "HZ"
    parameter = "S"
    data_format = "RI"
    reference = "50"
    points: list[S2PPoint] = []

    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("!"):
            continue
        if line.startswith("#"):
            tokens = line[1:].strip().upper().split()
            if tokens:
                unit = tokens[0]
            if len(tokens) >= 2:
                parameter = tokens[1]
            if len(tokens) >= 3:
                data_format = tokens[2]
            if "R" in tokens:
                r_index = tokens.index("R")
                if r_index + 1 < len(tokens):
                    reference = tokens[r_index + 1]
            continue

        # Strip inline comment if present.
        if "!" in line:
            line = line.split("!", 1)[0].strip()
        parts = line.split()
        if len(parts) < 9:
            warnings.append(f"skipped short data line: {raw_line[:80]}")
            continue
        try:
            values = [float(p) for p in parts[:9]]
        except ValueError:
            warnings.append(f"skipped non-numeric data line: {raw_line[:80]}")
            continue

        factor = UNIT_FACTORS.get(unit.upper(), 1.0)
        if unit.upper() not in UNIT_FACTORS:
            warnings.append(f"unknown frequency unit '{unit}', treated as Hz")
        freq_hz = values[0] * factor
        s11 = _to_complex(values[1], values[2], data_format)
        s21 = _to_complex(values[3], values[4], data_format)
        s12 = _to_complex(values[5], values[6], data_format)
        s22 = _to_complex(values[7], values[8], data_format)
        points.append(S2PPoint(freq_hz=freq_hz, s11=s11, s21=s21, s12=s12, s22=s22))

    if parameter.upper() != "S":
        warnings.append(f"parameter type is '{parameter}', expected S")
    if not points:
        raise ValueError(f"no valid S2P data points parsed from {path}")

    meta = {
        "frequency_unit": unit,
        "parameter": parameter,
        "data_format": data_format,
        "reference_ohm": reference,
    }
    return points, meta, warnings


def parse_band(text: str) -> dict[str, float | str]:
    """Parse band expression like '100e6:1e9' or 'EMI:100e6:1e9'."""
    parts = text.split(":")
    if len(parts) == 2:
        band_id = f"BAND-{parts[0]}-{parts[1]}"
        start, stop = parts
    elif len(parts) == 3:
        band_id, start, stop = parts
    else:
        raise ValueError("band must be START:STOP or ID:START:STOP")
    return {"band_id": band_id, "f_start_hz": float(start), "f_stop_hz": float(stop)}


def select_points(points: Iterable[S2PPoint], f_start: float, f_stop: float) -> list[S2PPoint]:
    return [p for p in points if f_start <= p.freq_hz <= f_stop]


def summarize(points: list[S2PPoint]) -> dict[str, float | int | str]:
    if not points:
        return {
            "point_count": 0,
            "s21_min_db": 0.0,
            "s21_max_db": 0.0,
            "s21_avg_db": 0.0,
            "s11_min_db": 0.0,
            "s11_max_db": 0.0,
            "notes": "no points in selected band",
        }
    s21 = [db20(p.s21) for p in points]
    s11 = [db20(p.s11) for p in points]
    return {
        "point_count": len(points),
        "s21_min_db": min(s21),
        "s21_max_db": max(s21),
        "s21_avg_db": sum(s21) / len(s21),
        "s11_min_db": min(s11),
        "s11_max_db": max(s11),
        "notes": "computed from parsed S2P data",
    }


def build_result(input_file: Path, bands: list[dict[str, float | str]], run_id: str) -> dict:
    points, meta, warnings = parse_s2p(input_file)
    if not bands:
        bands = [{"band_id": "FULL", "f_start_hz": points[0].freq_hz, "f_stop_hz": points[-1].freq_hz}]

    band_metrics = []
    for band in bands:
        selected = select_points(points, float(band["f_start_hz"]), float(band["f_stop_hz"]))
        metrics = summarize(selected)
        band_metrics.append({**band, "metrics": metrics})

    full_metrics = summarize(points)
    result = {
        "run_id": run_id,
        "input_file": str(input_file),
        "frequency_unit": "Hz",
        "port_count": 2,
        "target_bands": bands,
        "metrics": {
            "s21_min_db": full_metrics["s21_min_db"],
            "s21_max_db": full_metrics["s21_max_db"],
            "s21_avg_db": full_metrics["s21_avg_db"],
            "s11_min_db": full_metrics["s11_min_db"],
            "s11_max_db": full_metrics["s11_max_db"],
            "notes": f"format={meta['data_format']}, reference={meta['reference_ohm']} ohm, points={len(points)}",
        },
        "band_metrics": band_metrics,
        "warnings": warnings,
        "created_at": utc_now(),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a Touchstone S2P file.")
    parser.add_argument("--input", required=True, help="Path to .s2p or .s2p.txt file")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--run-id", default="S2P-RUN-0001")
    parser.add_argument("--band", action="append", default=[], help="Band START:STOP or ID:START:STOP in Hz")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    bands = [parse_band(b) for b in args.band]
    result = build_result(input_path, bands, args.run_id)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
