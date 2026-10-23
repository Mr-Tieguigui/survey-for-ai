---
name: survey-evidence-ledger
description: Build, query, or maintain a domain-adapted literature survey for AI readers. Use for evidence-grounded corpus curation, paper dossiers, typed field relationships, reader modules, bounded answers and incremental updates; not an informal reading list.
---

# Survey for AI · evidence ledger

Use saved records as the source of state. Keep corpus membership, evidence admission, synthesis completion, and publication status as separate decisions.

## Start a new domain

Read `method/domain_adapter.json` when it exists. Reuse the project ontology and identifiers; do not replace a working schema with the RSI example. If no project exists, run [scripts/init_domain.py](scripts/init_domain.py) with an explicit output, domain ID, name and scope. It creates an empty **draft**, not a completed survey. Complete inclusions/exclusions, search sources/cutoff, evidence roles, comparison axes, relation predicates, reader questions and budget before freezing corpus membership. New discoveries after a scope lock enter a separate candidate queue unless the user expands the release.

For domain design and reader synthesis, read [references/workflow.md](references/workflow.md). Use [references/data-contract.md](references/data-contract.md) only for schema mapping; [references/rsi-adapter.md](references/rsi-adapter.md) only for RSI. A new domain can add roles and evidence fields; it must retain identity/version traceability and distinguish navigation from admitted claims.

## Working modes

- **Create:** define the domain adapter, scope and completion gates; initialize empty records without inventing papers.
- **Answer:** route a reader request to modules and admitted claim IDs; output the answer contract below.
- **Resume:** read the compact run state, scope lock, last accepted receipt, and current failures. Do not reload completed papers.
- **Curate:** resolve identity and version, assign the body-supported role, and record a bounded claim plus material limits.
- **Relate:** create a typed directed edge only when its endpoints and meaning are supported.
- **Synthesize:** route admitted claims into questions, branches, comparisons, and reader answers; abstain beyond admitted evidence.
- **Maintain:** trace a changed source through the dependency index, repair affected records, rerun relevant checks, and update the manifest last.
- **Prepare release:** export project-authored records and external links; exclude source bytes, private caches, excerpts, secrets, and unverified third-party code.

For a new domain or schema mapping, read [references/data-contract.md](references/data-contract.md). For controlled evaluation or Skill changes, read [references/evaluation-protocol.md](references/evaluation-protocol.md). For the RSI case study, read [references/rsi-adapter.md](references/rsi-adapter.md).

## Identity and source versions

Do not merge by title, project, topic, filename, or chronology alone. Treat those signals as candidate links pending an identity check. Keep distinct reports as distinct work families; after identity is verified, one work family may retain several source manifestations or versions. Never overwrite the earlier manifestation.

## Role-specific evidence

Read only the primary-body passages needed for the decision and record the observed source/version, locator, bounded claim, and limits.

- Method/system: problem, input/output, concrete mechanism, assumptions/resources, evaluation protocol and limits. Add domain-specific fields from the adapter. For iterative/self-improving systems, also record update object, feedback, retained successor state, adoption rule and fixed boundary.
- Benchmark/evaluation: task unit, data/split, scoring, selection, uncertainty, and validity limits.
- Survey/background/theory: definitions, assumptions, coverage, and explicit relevance; distinguish proposals and theorem assumptions from experiments.
- Scope exclusion: body-supported thematic reason, with identity retained and no technical-claim permission.

A survey, report, benchmark, or background paper may support role-specific claims without receiving a method-system configuration. Lack of a method configuration is not evidence for exclusion.

## Configuration boundaries

A configuration is an optional view for a concrete method, intervention or protocol. Its dimensions come from the domain adapter; non-iterative methods do not need an improver or retained successor state. For iterative systems specifically: Create separate configuration views when loops differ materially in update object, feedback, retained state, adoption rule, or system boundary, even when they occur in one paper. A fixed optimizer can participate in bounded feedback. A structural loop does not establish strong recursive self-improvement, monotonic gain, or acceleration. Attempts, rounds, and candidates are not accepted improvements.

## Navigation and evidence permissions

Metadata, abstracts, information cards, and curator notes may support discovery or navigation context only. They support neither a technical claim nor proof of thematic exclusion. Admit a technical claim or scope exclusion only from the corresponding primary-body evidence.

## Relationships

Chronology, citation, topical similarity, or shared task alone is not inheritance and never merges separate works. Use chronology or typed horizontal comparison when dependency evidence is absent.

## Reader answers

Select the reader intent (orientation, historical development, mechanism, comparison, evaluation, frontier or practical entry). Resolve question → module → claim IDs → exact source/version/locator. Read source passages only if needed to settle the requested interpretation. Do not load every dossier or the full ledger. The result contains `question`, `corpus_version`, `answer`, `claim_ids`, `citations` (URL/version/locator), `comparison_conditions`, `limits`, `gaps` and `status` (`supported`, `partial` or `insufficient_evidence`). Empty evidence yields an explicit gap, never an invented answer.

For each answer, return the bounded conclusion, evidence record IDs, applicable versions/locators, material limits, and missing evidence. Label a frontier as local to the documented search scope unless a separate global search supports a stronger statement. Abstain and name the missing evidence when the question exceeds admitted claims.

## Cost and maintenance

Use deterministic scripts for joins, hashes, counts, dependency propagation, export, and validation. Use semantic judgment for role, mechanism, conflict, relationship meaning, and bounded synthesis. Reuse exact source/version caches, read selected passages, combine substantial batches, and rebuild only after accepted changes.

On a source change, use the dependency index to identify consumers, update only affected records, and verify that unaffected records keep their hashes. Preserve unresolved records and earlier manifestations. Do not alter thresholds or delete failures to make a phase appear complete.

## Completion

Report actual scope and remaining gates. A survey package is ready when membership is conserved, evidence references resolve, relations have valid endpoints, reader routes resolve, unsupported questions abstain, source hashes are current, and the build is reproducible. Cross-domain effectiveness is an empirical claim. Mark the current method as a candidate until fixed no-Skill/with-Skill comparisons, ablations, unexposed transfer cases and maintenance tests support stronger claims. Do not invent efficiency or accuracy measurements.

Use `scripts/review_view.py` for compact RSI progress views and `scripts/validate_release.py` for the generic exported-domain contract.
