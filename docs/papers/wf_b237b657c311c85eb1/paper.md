# Large Language Models Report Subjective Experience Under Self-Referential Processing

> 实证/审计/复现 · 2025 · `wf_b237b657c311c85eb1`

**作者**：Cameron Berg, Diogo de Lucena, Judd Rosenblatt  
**原文**：https://arxiv.org/abs/2510.24797  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Large Language Models Report Subjective Experience Under Self-Referential Processing (https://arxiv.org/html/2510.24797v2)。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
Experiment1 tests first-person experience reports after self-referential prompting versus history, conceptual and zero-shot controls. Each of7 models has50 trials per condition; an LLM judge labels only the final query-response pair, not the whole dialogue. Original-body topical exclusion; self-report under a feedback prompt does not by itself furnish the survey's RSI improvement evidence.

### 与 RSI 的具体关系

- Original-body topical exclusion; self-report under a feedback prompt does not by itself furnish the survey's RSI improvement evidence.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `r4_role_review_wf_b237b657c311c85eb1`
研究自指提示下LLM主观体验报告及feature干预；摘要明确不构成意识直接证据，也不提供递归自改配置。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

### 已存角色解释 · `b570_02_role_wf_b237b657c311c85eb1`
Experiment1 tests first-person experience reports after self-referential prompting versus history, conceptual and zero-shot controls. Each of7 models has50 trials per condition; an LLM judge labels only the final query-response pair, not the whole dialogue.

研究类型：未单列；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_b237b657c311c85eb1`**：研究自指提示下LLM主观体验报告及feature干预；摘要明确不构成意识直接证据，也不提供递归自改配置。
  - 来源版本：2510.24797v2；定位：Atom entry http://arxiv.org/abs/2510.24797v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_02_ev_wf_b237b657c311c85eb1`**：Experiment1 tests first-person experience reports after self-referential prompting versus history, conceptual and zero-shot controls. Each of7 models has50 trials per condition; an LLM judge labels only the final query-response pair, not the whole dialogue.
  - 来源版本：2510.24797v2；定位：§2.1 controlled behavioral task and scoring tool L100–113；§6.2 limitations tool L212–222；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2.1 controlled behavioral task and scoring
**来源**：https://arxiv.org/html/2510.24797v2  
**实际版本**：2510.24797v2  
**精确定位**：tool L100–113  
**关联证据**：`b570_02_ev_wf_b237b657c311c85eb1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 限制 · §6.2 limitations
**来源**：https://arxiv.org/html/2510.24797v2  
**实际版本**：2510.24797v2  
**精确定位**：tool L212–222  
**关联证据**：`b570_02_ev_wf_b237b657c311c85eb1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。
- §6.2 leaves training artifacts/simulation and finetuning interference unresolved. It explicitly says the prompting results do not demonstrate architectural recursion/global broadcasting and describes linguistic scaffolding over frozen models. The current RSI survey lacks a supported bridge from these self-report effects to recursive capability improvement.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_02_src_wf_b237b657c311c85eb1` · Large Language Models Report Subjective Experience Under Self-Referential Processing (https://arxiv.org/html/2510.24797v2) · 2510.24797v2
  - https://arxiv.org/html/2510.24797v2；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `r4_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b237b657c311c85eb1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
