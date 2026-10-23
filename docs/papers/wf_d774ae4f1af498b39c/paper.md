# Self-Evolving Agent Harness

> 概念/理论/立场 · 2026 · `wf_d774ae4f1af498b39c`

**作者**：Chuyang Wei, Haoxiang Guan, Minghang Zhu, Kexin Zhou, Jiyan He, Xiren Zhou, Huanhuan Chen, Yifei Shen  
**原文**：https://arxiv.org/abs/2610.18813v1  
**研究分支**：定义、理论与系统边界  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Definition, taxonomy and conditional theory; formal lifecycle is not counted as a separately demonstrated empirical self-improving system.

## 2. 论文的核心内容与贡献

### configuration:cfg_harness_rsi_formal_lifecycle
Formal lifecycle satisfies the stated four-condition design at specification level. Kept adjacent as a conceptual/theoretical framework, not counted as a demonstrated empirical self-improving implementation.

**适用版本**：v1；**原文定位**：S2；S3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### cfg_harness_rsi_formal_lifecycle
`cfg_harness_rsi_formal_lifecycle` · protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Formal protocol for a frozen model M, mutable harness H, operational feedback and persistent accepted revisions; final assessor J is outside the editable boundary. |
| 改进过程与下一轮参与 | An Update operator diagnoses, proposes, assesses and admits harness revisions; the incumbent survives when admission fails. Later runs execute the retained harness and retain the updater. |
| 保留的状态及时间尺度 | Formal requirement that accepted revisions are stored and loaded in subsequent runs. |
| 外部固定部分 | - Task model weights - Final assessor J - Stated sampling/stability/admission assumptions |
| 实验实现状态 | formal_protocol_and_conditional_theory_not_new_empirical_system |

**保证成立的条件**：

- Fixed model/evaluator and bounded loss
- Exogenous independently drawn tasks for stability analysis
- Historical regression budgets for retention
- At most K candidates fixed before fresh independent validation at each of T rounds
- Historical-mixture target; evaluator discrepancy bound needed for target-risk claims

**保证的限制**：

- Expected gap control is not an individual-run bound.
- Retention budgets are separate assumptions; stability alone does not establish them.
- Candidate construction must precede independent fresh validation; reused adaptive holdouts do not satisfy that premise.
- A historical-mixture certificate does not cover arbitrary future distributions; evaluator-target discrepancy requires additional evidence.

**配置判定**：Formal lifecycle satisfies the stated four-condition design at specification level. Kept adjacent as a conceptual/theoretical framework, not counted as a demonstrated empirical self-improving implementation.

来源：https://arxiv.org/html/2610.18813v1；版本：v1；定位：S2；S3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`oct15_intake_ev_harness_lifecycle`**：The formal harness lifecycle keeps model weights and final assessor fixed. Feedback proposes and admits persistent harness revisions; later executions load them and retain an updater. Taxonomy separates interpreted state from executable/runtime changes.
  - 来源版本：v1；定位：S2；S3；深度：`未单列`。

- **`oct15_intake_ev_harness_conditional_theory`**：The theory bounds expected generalization via replace-one stability, retention via separately assumed historical-risk budgets, and admission on a historical task mixture via fresh validation and Hoeffding/union bounds.
  - 来源版本：v1；定位：PDF p.3 Section 2 Eqs.(1)-(3)；PDF pp.6-8 Section 4.2 Eqs.(4)-(9)；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- A formal lifecycle does not certify that every cited method implements it.
- This is a framework/taxonomy, not evidence of a new independently benchmarked optimizer.
- Expected gap control is not an individual-run bound.
- Retention budgets are separate assumptions; stability alone does not establish them.
- Candidate construction must precede independent fresh validation; reused adaptive holdouts do not satisfy that premise.
- A historical-mixture certificate does not cover arbitrary future distributions; evaluator-target discrepancy requires additional evidence.

## 7. 与其他论文的具体关系

### [ExpeL: LLM Agents Are Experiential Learners](../r03_method/wf_984256074226b209d4.md)
关系：`contrasts_system_boundary_with` · `oct15_harness_expel_interpreted_boundary` · 当前展示权限：`primary_supported`。
The harness framework distinguishes interpreted memory/insight updates from executable runtime mutation around fixed weights. Original ExpeL concretely updates natural-language insights and retrieved trajectories during construction, then uses a fixed pool at evaluation. This illustrates an interpreted-state boundary, not general executable self-rewriting.

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- oct15_intake_src_2610_18813v1_html：https://arxiv.org/html/2610.18813v1；版本：v1；定位：S2；S3。
- oct15_training_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。
- oct15_intake_src_2610_18813v1_html：https://arxiv.org/html/2610.18813v1；版本：v1；定位：S2；S3。
- oct15_training_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

## 8. 来源清单、复查入口与解析缺口
- `oct15_intake_src_2610_18813v1_html` · 已存来源 · v1
  - https://arxiv.org/html/2610.18813v1；阅读深度：`未单列`。
- `oct15_intake_src_2610_18813v1_pdf` · 已存来源 · v1
  - https://arxiv.org/pdf/2610.18813v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_fulltext_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d774ae4f1af498b39c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
