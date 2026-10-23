# Domain adaptation, synthesis and answering

## Domain adapter

Define the intellectual unit (work family), scope/cutoff, sources, role-specific evidence fields, relation predicates, comparison axes, reader profiles and questions. Preserve a separate source manifestation for each observed URL/version. Keep the domain vocabulary out of universal acceptance rules. For example, intervention/outcome fields and algorithm/input fields are alternative adapter choices, not evidence about an actual paper.

Use `scripts/init_domain.py` to initialize an empty local project. The scaffold is intentionally not release-ready: it contains no works and requires a completed adapter. Map legacy exports to the logical entities in `data-contract.md` rather than rewriting an established corpus. `method/workflow.json` in the project distribution is the machine-readable lifecycle and answer contract.

## Lifecycle and gates

| Stage | Produce | Check before advancing |
|---|---|---|
| Scope | operational definition, roles, sources, cutoff, membership lock and budget | inclusions/exclusions and acceptance unit are explicit |
| Identity | canonical works, aliases, exact source manifestations | no title-only identity merge; ambiguous links remain pending |
| Evidence | role dossiers, bounded claims, optional protocol/configuration views | primary-body support and locators for admitted technical claims |
| Field | branch navigation and typed relationships | both endpoints resolve; evidence matches the specific predicate |
| Synthesis | vertical, horizontal, mechanism, frontier and reader modules | each statement resolves to admitted claims or labeled curator synthesis |
| Answer | minimal evidence packet for a reader request | comparison compatibility, citations, limits and gaps are present |
| Maintain | dependency repair, versioned release, manifest | membership conserved; current inputs; unresolved gates disclosed |

Organization-ready, primary-review-complete, and cross-domain-method-validated are different states. Keep their gates and denominators separate.

## Multi-view knowledge

The tree is a primary navigation structure, not a proof that research has a single parent. Add typed cross-links for extension, alternative mechanism, shared evaluation, contradiction, application and curator comparison. A genuine lineage projection should not acquire a cycle from chronology alone; a non-lineage comparison graph may contain cycles.

Vertical modules explain problem shifts, mechanisms, evidence changes and open constraints. Horizontal modules select adapter-defined dimensions, state missing cells, and compare numerical results only when task, split, metric, budget and selection conditions are compatible. Mechanism modules connect inputs, process, outputs, assumptions and failure modes; add retained state and feedback only when appropriate. Frontier modules include multiple leaves and a search cutoff; a missing successor does not certify global novelty.

Each reader module has an ID, reader goal, question, included work IDs, admitted claim IDs, comparison conditions, bounded synthesis, limitations and unresolved questions. Modules may overlap; primary branch membership should follow the project's explicit policy.

## Minimal answer packet

Route intent to an existing question and module. Load the module summary, selected admitted claims and exact source locators. Expand the relevant dossier or selected passage only if the question requires it. Return:

```json
{
  "question": "the reader request",
  "corpus_version": "the actual frozen release",
  "answer": "a bounded conclusion, or an explicit evidence gap",
  "claim_ids": [],
  "citations": [],
  "comparison_conditions": [],
  "limits": [],
  "gaps": [],
  "status": "insufficient_evidence"
}
```

This empty example illustrates abstention; it is not an answer to a research question. Citations in real answers contain source URL, observed version and page/section/paragraph locator. Do not upgrade an abstract, a draft extraction, or a retrieved source into an admitted claim. Expose curator interpretation as such.

## Cost and updates

Use one extraction per source/version/needed passage and reuse it across views. Index and query before reading. Let deterministic code handle joins, membership, hashes, graph references and exports. Let semantic judgment handle role, mechanism, conflicting interpretations and relationship meaning. Review changed fields and their support instead of repeating the full paper. Reserve model escalation for unresolved decisions; do not assume a provider or model is installed.

For a new source version, traverse reverse dependencies from source → evidence → claims/configurations → relations/modules/answers. Mark affected consumers stale, repair that set, run referential checks across the corpus, and update the manifest last. Keep earlier versions and failures. Measure source reads and actual token/time usage when evaluating efficiency; do not estimate a speedup from design alone.
