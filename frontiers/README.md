# Frontier Surveys · Open Direction Directory

[English](README.md) · [简体中文](README_CN.md) · [Registry](registry.json)

These are unassigned research proposals, not completed surveys. RSI remains the worked example with its own fixed corpus. Discovery links carry navigation permission only; this directory does not enlarge RSI membership.

| ID | Proposed survey | Research question | Status | Directory |
|---|---|---|---|---|
| F01 | Agent memory & continual learning | How does external memory affect later tasks, and how is transfer evaluated? | ○ Proposed | [agent-memory](agent-memory/) |
| F02 | Test-time compute, reasoning & adaptation | What changes with inference compute versus test-time updates? | ○ Proposed | [test-time-adaptation](test-time-adaptation/) |
| F03 | Scientific discovery & research agents | Which steps from a research question to a candidate result are verifiable? | ○ Proposed | [scientific-discovery](scientific-discovery/) |
| F04 | World models & embodied interaction | What do generative, predictive and interactive environment models support? | ○ Proposed | [world-models](world-models/) |
| F05 | Agent evaluation & reliability | How can model, environment, harness and protocol contributions be separated? | ○ Proposed | [agent-evaluation](agent-evaluation/) |
| F06 | Multi-agent coordination & organization | How does coordination affect decomposition, communication and outcomes? | ○ Proposed | [multi-agent-systems](multi-agent-systems/) |
| ＋ | **Your domain** | Define the scope and reader questions | Open slot | [_template](_template/) |

## How to contribute

1. Choose a direction, or copy `_template/` to a new domain-ID folder.
2. Edit its `scope.json`: name, questions, comparison axes, first-party entry points and maintainer.
3. Register the ID and relative scope path in `registry.json` under `directions`.
4. Run the commands below to synchronize this index and both project README tables.
5. Follow the [project onboarding](../README.md#build-a-survey-in-another-domain) to initialize actual research inside the direction's `survey/` child.
6. Change status only after the corresponding work exists. `ready` refers to the declared scope and retains evidence-depth and exception disclosures.

```bash
python scripts/build_frontier_index.py
python scripts/build_frontier_index.py --check
```

Run from the repository root, without a model or network. `registry.json` registers locations; each `scope.json` owns the proposal content. README files are generated views. Never count unread sources as primary reviews.
