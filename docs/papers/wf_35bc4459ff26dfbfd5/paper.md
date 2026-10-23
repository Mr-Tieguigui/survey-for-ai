# Reflective Oracles: A Foundation for Classical Game Theory

> 概念/理论/立场 · 2015 · `wf_35bc4459ff26dfbfd5`

**作者**：Benja Fallenstein, Jessica Taylor, Paul F. Christiano  
**原文**：https://arxiv.org/abs/1508.04145  
**研究分支**：定义、理论与系统边界  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Reflective oracles answer probability-threshold queries about machines sharing the oracle; at equality they may randomize. Queries require almost-sure halting and binary outputs, and Theorem 2.3 asserts existence. Direct conceptual context for reflective agents that model other agents and themselves within the same formal environment.

### 与 RSI 的具体关系

- Direct conceptual context for reflective agents that model other agents and themselves within the same formal environment.

## 2. 论文的核心内容与贡献

### role:b570_01_role_1508_04145
Reflective oracles answer probability-threshold queries about machines sharing the oracle; at equality they may randomize. Queries require almost-sure halting and binary outputs, and Theorem 2.3 asserts existence.

**适用版本**：1508.04145v1；**原文定位**：§2 query/reflection definitions and Theorem 2.3 tool L62–85；Assumptions / boundaries: §2 query/reflection definitions and Theorem 2.3 tool L87–102。
**引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`。

### 已存角色解释 · `r4_role_review_wf_35bc4459ff26dfbfd5`
Reflective Oracles以随机化避免对角化并构造决策/博弈基础；属于反思代理形式语境，不是已实现自改性能证据。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_35bc4459ff26dfbfd5`**：Reflective Oracles以随机化避免对角化并构造决策/博弈基础；属于反思代理形式语境，不是已实现自改性能证据。
  - 来源版本：1508.04145v1；定位：Atom entry http://arxiv.org/abs/1508.04145v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_01_ev_1508_04145`**：Reflective oracles answer probability-threshold queries about machines sharing the oracle; at equality they may randomize. Queries require almost-sure halting and binary outputs, and Theorem 2.3 asserts existence.
  - 来源版本：1508.04145v1；定位：§2 query/reflection definitions and Theorem 2.3 tool L62–85；Assumptions / boundaries: §2 query/reflection definitions and Theorem 2.3 tool L87–102；深度：`selected_primary_theorem_assumptions_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- The decision-theoretic construction assumes oracle-computable world programs and almost-surely halting action counterfactuals with rational bounded utilities. Existence does not provide an efficient, measured recursive improver.
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_01_src_1508_04145` · Reflective Oracles: A Foundation for Classical Game Theory · 1508.04145v1
  - https://arxiv.org/html/1508.04145v1；阅读深度：`selected_primary_theorem_assumptions_and_limits`。
- `r4_role_src_d6f9c35358996ce4` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22intelligence+explosion%22+OR+ti%3A%22recursive+self-improvement%22+OR+ti%3A%22reflective+oracle%22+OR+ti%3A%22self+modification%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_theorem_assumptions_and_limits。
**当前引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_35bc4459ff26dfbfd5 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
