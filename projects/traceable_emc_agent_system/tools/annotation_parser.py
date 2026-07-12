#!/usr/bin/env python3
"""Human-guided EDA annotation parser.

Reads one annotation JSON or a directory of annotation JSON files and builds a
minimal Parsed EDA Context artifact compatible with
schemas/annotation/parsed_eda_context.schema.json.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


INTENT_MAP = {
    "signal_path": "analyze_signal_path_for_emi_risk",
    "return_path": "check_return_path_continuity",
    "component_of_interest": "inspect_component_role",
    "filter_candidate": "compare_filter_candidates",
    "connector_or_cable": "check_connector_cable_radiation_risk",
    "risk_region": "inspect_layout_or_schematic_risk_region",
    "initial_routing_hint": "capture_initial_routing_intent",
    "ground_reference": "check_ground_reference_or_shielding",
    "unknown_needs_ai_parse": "needs_human_or_ai_parse",
}


def load_annotations(path: Path) -> list[dict]:
    if path.is_dir():
        files = sorted(path.glob("ANN-*.json"))
    else:
        files = [path]
    annotations = []
    for file in files:
        with file.open("r", encoding="utf-8") as f:
            annotations.append(json.load(f))
    return annotations


def build_context(annotations: list[dict], context_id: str) -> dict:
    source_ids = []
    nets: set[str] = set()
    components: set[str] = set()
    intents: set[str] = set()
    tags: set[str] = set()
    labels: list[str] = []

    for ann in annotations:
        source_ids.append(ann.get("annotation_id", "UNKNOWN"))
        ann_type = ann.get("annotation_type", "unknown_needs_ai_parse")
        intents.add(INTENT_MAP.get(ann_type, "needs_review"))
        labels.append(ann.get("label_ko") or ann.get("label") or ann_type)
        for tag in ann.get("emc_tags", []):
            tags.add(str(tag))
        linked = ann.get("linked_objects", {}) or {}
        for net in linked.get("nets", []) or []:
            nets.add(str(net))
        for comp in linked.get("components", []) or []:
            components.add(str(comp))

    summary = "사람 표시 기반 EDA 맥락: " + "; ".join(labels)
    if tags:
        summary += " / EMC tags: " + ", ".join(sorted(tags))

    return {
        "eda_context_id": context_id,
        "source_annotation_ids": source_ids,
        "summary": summary,
        "emc_intent": sorted(intents),
        "candidate_nets": sorted(nets),
        "candidate_components": sorted(components),
        "created_at": utc_now(),
        "review_status": "human_review_required",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse EDA annotation JSON into parsed EDA context.")
    parser.add_argument("--input", required=True, help="Annotation JSON path or directory")
    parser.add_argument("--output", required=True, help="Output parsed context JSON")
    parser.add_argument("--context-id", default="EDA-CTX-0002")
    args = parser.parse_args()

    annotations = load_annotations(Path(args.input))
    result = build_context(annotations, args.context_id)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
