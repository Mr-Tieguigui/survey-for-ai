# Evaluation protocol

Freeze the source manifest, domain split, cases, answer rubric, cost accounting and stop rules before comparing conditions.

Required conditions:

1. no-Skill baseline using the same model, sources and budget;
2. full Skill;
3. identity/version resolution ablated;
4. role-specific evidence schema ablated;
5. two-endpoint relationship rule ablated;
6. dependency impact index ablated;
7. reader-question routing ablated.

Evaluate a development domain separately from held-out transfer. Do not tune on held-out cases. Include an incremental update that changes a source version and a simulated fault that corrupts a relationship or identity join; label them separately.

Score identity/version accuracy, claim-to-source citation fidelity, relationship direction, scope/abstention correctness, membership conservation, reader utility, update impact localization, input/output tokens, source reads and elapsed time. Preserve failures and confidence. Deterministic schema checks establish contract compliance only; they do not establish language-model effectiveness.

Promote the candidate to stable only when the full Skill improves the preregistered primary outcomes without a material citation or scope regression, held-out results follow the same direction, and maintenance repairs do not silently alter unaffected records.
