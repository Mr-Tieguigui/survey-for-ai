# AI reading and query guide

## Authority order

1. `catalog/` is the factual source of record, including `sources.jsonl` and `evidence.jsonl` restored from the final saved Stage-2 ledgers. These ledgers preserve mixed evidence depths and historical records; only explicitly admitted claims grant technical citation permission.
2. `screening/` preserves candidate routing, abstract-level decisions, exclusions, and identity actions. It supports audit and discovery, not technical claims.
3. `indexes/` routes IDs to canonical records; it does not grant claim permission.
4. In the full repository, `website/assets/data/` and generated `docs/assets/data/` are bounded display projections, not primary evidence. These presentation files are deliberately excluded from the standalone Survey knowledge ZIP; all canonical data and 808 Markdown dossiers remain included.
5. `metadata/provenance.json` explains stage lineage and completion boundaries.

## Recommended retrieval path

Start with `papers/index.json` for one paper, or `indexes/by_question.json`, `by_module.json`, or `by_branch.json` for a topic. Every one of the 808 families has a role-classified Markdown dossier under `papers/`; these are deterministic reading views, not new reviews. Use `scripts/dossier.py WORK_FAMILY_ID` to retrieve one complete neighborhood: work, configurations, admitted claims, relations, sources and evidence. Add `--excerpts` only when a particular interpretation needs the saved selected source passages. `indexes/primary_lookup.json` maps evidence/source IDs to one-based JSONL row numbers, which must not be confused with source-document line numbers.

For a technical answer, return the admitted record ID, source version, source locator, bounded claim and material limits. The existence of a dossier, source row, quote, old review or cached hash does not grant new citation permission. If a field is unknown or pending, preserve that state.

## Citation permissions

- `works.jsonl`: identity, role, navigation, and the explicitly listed role claims only.
- `configurations.jsonl`: the named configuration boundary and reviewed fields only.
- `claims.jsonl`: the exact admitted claim and limits for the recorded version.
- `relations.jsonl`: only the recorded predicate, endpoints, evidence level, and scope limit.
- `frontiers.jsonl`: latest within the frozen corpus and cutoff, never global-latest certification.

Do not infer inheritance from chronology, citation, or similarity. Do not treat a fixed optimizer as proof that feedback is absent. Do not call rounds or generated candidates accepted improvements. Do not force method configurations onto surveys, theory, background, or benchmark records.

## Query examples

`python scripts/query.py "recursive self-improvement" --type works`

`python scripts/query.py "fixed evaluator" --type configurations`

`python scripts/query.py "DGM" --type relations`

`python scripts/query.py "bilevel" --type candidates`

The query script defaults to compact paper routing records. `--full` explicitly returns complete search records. Prefer one-paper retrieval over loading every JSONL table into model context:

```bash
python scripts/query.py "Darwin" --type papers --limit 3
python scripts/dossier.py "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
python scripts/dossier.py WORK_FAMILY_ID --excerpts
```

Read the dossier first, then the exact admitted claim, then only its relevant primary evidence. Reuse this result for comparisons; do not re-download every PDF. Full PDFs remain external source links. Six version-specific selected-body descriptive updates are separately stored in `catalog/reading_supplements.jsonl` and returned by the dossier tool; these are not newly admitted numerical results, independent replication, or whole-paper certification. The Markdown and generated HTML use the same content. The expanded package is local and contains selected saved quotations; its public redistribution status is distinct from the earlier metadata-only release.
