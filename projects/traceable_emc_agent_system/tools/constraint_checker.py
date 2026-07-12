#!/usr/bin/env python3
"""Minimal component/design constraint checker.

Produces JSON compatible with schemas/tools/constraint_check_result.schema.json.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def check_le(name: str, value: float | None, limit: float | None, unit: str) -> dict[str, Any]:
    if value is None or limit is None:
        return {"check_name": name, "passed": False, "value": value, "limit": limit, "notes": f"missing {unit} value or limit"}
    return {"check_name": name, "passed": value <= limit, "value": value, "limit": limit, "notes": unit}


def check_ge(name: str, value: float | None, limit: float | None, unit: str) -> dict[str, Any]:
    if value is None or limit is None:
        return {"check_name": name, "passed": False, "value": value, "limit": limit, "notes": f"missing {unit} value or limit"}
    return {"check_name": name, "passed": value >= limit, "value": value, "limit": limit, "notes": unit}


def build_result(args: argparse.Namespace) -> dict:
    checks = [
        check_ge("rated_current_margin", args.rated_current_a, args.required_current_a, "A"),
        check_le("dcr_limit", args.dcr_ohm, args.max_dcr_ohm, "ohm"),
        check_le("height_limit", args.height_mm, args.max_height_mm, "mm"),
    ]
    if args.package and args.allowed_package:
        allowed = [p.strip() for p in args.allowed_package.split(",") if p.strip()]
        checks.append(
            {
                "check_name": "package_allowed",
                "passed": args.package in allowed,
                "value": args.package,
                "limit": allowed,
                "notes": "package code must be in allowed list",
            }
        )
    return {
        "run_id": args.run_id,
        "candidate_id": args.candidate_id,
        "checks": checks,
        "passed": all(c["passed"] for c in checks),
        "created_at": utc_now(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run simple design/component constraint checks.")
    parser.add_argument("--output", required=True)
    parser.add_argument("--run-id", default="CONSTRAINT-RUN-0002")
    parser.add_argument("--candidate-id", default="CAND-0001")
    parser.add_argument("--rated-current-a", type=float, default=1.0)
    parser.add_argument("--required-current-a", type=float, default=0.5)
    parser.add_argument("--dcr-ohm", type=float, default=0.1)
    parser.add_argument("--max-dcr-ohm", type=float, default=0.5)
    parser.add_argument("--height-mm", type=float, default=0.6)
    parser.add_argument("--max-height-mm", type=float, default=1.0)
    parser.add_argument("--package", default="0402")
    parser.add_argument("--allowed-package", default="0402,0603,1005,1608")
    args = parser.parse_args()

    result = build_result(args)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
