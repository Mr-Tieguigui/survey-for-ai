#!/usr/bin/env python3
"""Validate the generic exported survey-domain contract without reading source papers."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("domain_data", type=Path, help="Directory containing exported domain data files")
    args = parser.parse_args()
    root = args.domain_data
    works = load_jsonl(root / "works.jsonl")
    configs = load_jsonl(root / "configurations.jsonl")
    relations = load_jsonl(root / "relations.jsonl")
    claims = load_jsonl(root / "claims.jsonl")
    branches = load_json(root / "branches.json")
    modules = load_json(root / "modules.json")
    questions = load_json(root / "questions.json")
    profiles = load_json(root / "reader_profiles.json")
    deps = load_json(root / "dependency_index.json")

    work_ids = {row["work_family_id"] for row in works}
    config_ids = {row["configuration_id"] for row in configs}
    claim_ids = {row["record_id"] for row in claims}
    relation_ids = {row["relation_id"] for row in relations}
    checks = {
        "unique_work_ids": len(work_ids) == len(works),
        "unique_configuration_ids": len(config_ids) == len(configs),
        "unique_claim_ids": len(claim_ids) == len(claims),
        "unique_relation_ids": len(relation_ids) == len(relations),
        "configuration_work_refs": all(row["work_family_id"] in work_ids for row in configs),
        "claim_work_refs": all(row["work_family_id"] in work_ids for row in claims),
        "relation_endpoint_refs": all(
            (not ep.get("work_family_id") or ep["work_family_id"] in work_ids)
            and (not ep.get("configuration_id") or ep["configuration_id"] in config_ids)
            for row in relations for ep in (row.get("subject", {}), row.get("object", {}))
        ),
        "claim_dependency_coverage": set(deps["claim_consumers"]) == claim_ids,
        "work_dependency_coverage": set(deps["work_family_consumers"]) == work_ids,
        "reader_structures_present": bool(branches and modules and questions and profiles),
    }
    result = {"passed": all(checks.values()), "checks": checks, "counts": {"works": len(works), "configurations": len(configs), "relations": len(relations), "claims": len(claims), "branches": len(branches), "modules": len(modules), "questions": len(questions), "reader_profiles": len(profiles)}}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
