# A Formulation of Recursive Self-Improvement and Its Possible Efficiency

> 概念/理论/立场 · 2018 · `wf_bac225dc07b9227462`

**作者**：Wenyi Wang  
**原文**：https://arxiv.org/abs/1805.06610  
**研究分支**：定义、理论与系统边界  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
对一类 RSI 给形式定义，在受限版本主张可计算有效系统存在，并报告搜索空间大小相关的对数运行时间仿真；必须保留受限设定，不能外推一般真实系统无限加速。

## 2. 论文的核心内容与贡献

### role:r5_role_w_wang_rsi_formulation
有限程序集合及固定总序下，当前程序定义候选生成分布并严格择优替换；Markov简化及预先构造的吸收时间评分是关键假设。§4的对数步骤趋势来自随机抽象程序仿真；§5承认预计算评分比枚举全部程序更费时，实用oracle评分仍待解决。

**适用版本**：1805.06610v1；**原文定位**：PDF pp2–4 §§2–3, tool lines26–128；PDF pp6–8 §§4–5, tool lines237–287。
**引用权限**：`selected_definition_and_assumption_claims_only`。

### 已存角色解释 · `s18ctx_role_review_wf_bac225dc07b9227462`
对一类 RSI 给形式定义，在受限版本主张可计算有效系统存在，并报告搜索空间大小相关的对数运行时间仿真；必须保留受限设定，不能外推一般真实系统无限加速。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_bac225dc07b9227462`**：对一类 RSI 给形式定义，在受限版本主张可计算有效系统存在，并报告搜索空间大小相关的对数运行时间仿真；必须保留受限设定，不能外推一般真实系统无限加速。
  - 来源版本：1805.06610v1；定位：Atom entry http://arxiv.org/abs/1805.06610v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5_role_ev_w_wang_rsi_formulation`**：有限程序集合及固定总序下，当前程序定义候选生成分布并严格择优替换；Markov简化及预先构造的吸收时间评分是关键假设。§4的对数步骤趋势来自随机抽象程序仿真；§5承认预计算评分比枚举全部程序更费时，实用oracle评分仍待解决。
  - 来源版本：1805.06610v1；定位：PDF pp2–4 §§2–3, tool lines26–128；PDF pp6–8 §§4–5, tool lines237–287；深度：`selected_primary_theory_definition_assumptions_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 对数趋势不包含评分预计算总成本，不是一般实际RSI计算加速保证。
- 没有真实源代码自主改写系统或现代LLM实验。
- 本文构造和证明未做独立形式验证，限定为定义/假设/作者报告仿真核查。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 对数趋势不包含评分预计算总成本，不是一般实际RSI计算加速保证。；没有真实源代码自主改写系统或现代LLM实验。；本文构造和证明未做独立形式验证，限定为定义/假设/作者报告仿真核查。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5_root_src_wang2018` · 已存来源 · 1805.06610v1
  - https://arxiv.org/pdf/1805.06610v1；阅读深度：`selected_primary_definitions_assumptions_and_limits`。
- `s18ctx_role_src_d65411d60f3e40c6` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22recursive+self-improvement%22+OR+abs%3A%22recursive+self-improvement%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract。
**当前引用权限**：`selected_definition_and_assumption_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bac225dc07b9227462 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
