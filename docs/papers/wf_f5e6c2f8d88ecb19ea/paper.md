# Self-Modification of Policy and Utility Function in Rational Agents

> 概念/理论/立场 · 2016 · `wf_f5e6c2f8d88ecb19ea`

**作者**：Tom Everitt, Daniel Filan, Mayank Daswani, Marcus Hutter  
**原文**：https://arxiv.org/abs/1605.03142  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Theorem 16 preserves original realistic expected-utility optimality along the realized policy sequence when belief and initial utility are modification-independent and the initial policy is optimal for the realistic value function. Direct formal context for evaluating self-modification using the current goal and explicit assumptions, without promoting the paper to a runnable configuration.

### 与 RSI 的具体关系

- Direct formal context for evaluating self-modification using the current goal and explicit assumptions, without promoting the paper to a runnable configuration.

## 2. 论文的核心内容与贡献

### role:b570_01_role_1605_03142
Theorem 16 preserves original realistic expected-utility optimality along the realized policy sequence when belief and initial utility are modification-independent and the initial policy is optimal for the realistic value function.

**适用版本**：1605.03142v1；**原文定位**：§5 Theorem 16 and selected proof setup tool L235–245；§3 policy-modification definition and ordinary RL boundary tool L102–118；Assumptions / boundaries: §5 Theorem 16 and selected proof setup tool L261–278。
**引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_f5e6c2f8d88ecb19ea`
在一般强化学习中形式化目标保持，条件涉及价值函数预见自修改后果并用当前效用评价未来；其无害结论是理论条件命题，不保证有界理性或现实代理自改安全。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_f5e6c2f8d88ecb19ea`**：在一般强化学习中形式化目标保持，条件涉及价值函数预见自修改后果并用当前效用评价未来；其无害结论是理论条件命题，不保证有界理性或现实代理自改安全。
  - 来源版本：1605.03142v1；定位：Atom entry http://arxiv.org/abs/1605.03142v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_01_ev_1605_03142`**：Theorem 16 preserves original realistic expected-utility optimality along the realized policy sequence when belief and initial utility are modification-independent and the initial policy is optimal for the realistic value function.
  - 来源版本：1605.03142v1；定位：§5 Theorem 16 and selected proof setup tool L235–245；§3 policy-modification definition and ordinary RL boundary tool L102–118；Assumptions / boundaries: §5 Theorem 16 and selected proof setup tool L261–278；深度：`selected_primary_theorem_assumptions_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- The guarantee is on-policy. It does not prevent changing the percept input to the utility function, and preserving an incorrectly specified goal can resist correction, value learning or exploration. It is not empirical RSI evidence.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_01_src_1605_03142` · Self-Modification of Policy and Utility Function in Rational Agents · 1605.03142v1
  - https://arxiv.org/html/1605.03142v1；阅读深度：`selected_primary_theorem_assumptions_and_limits`。
- `s18ctx_role_src_d6f9c35358996ce4` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22intelligence+explosion%22+OR+ti%3A%22recursive+self-improvement%22+OR+ti%3A%22reflective+oracle%22+OR+ti%3A%22self+modification%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_theorem_assumptions_and_limits。
**当前引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f5e6c2f8d88ecb19ea --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
