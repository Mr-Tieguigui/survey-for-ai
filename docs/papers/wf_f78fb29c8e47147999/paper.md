# Dataflow matrix machines as programmable, dynamically expandable, self-referential generalized recurrent neural networks

> 方法论文 · 2016 · `wf_f78fb29c8e47147999`

**作者**：Michael Bukatin, Steve Matthews, Andrey Radul  
**原文**：https://arxiv.org/abs/1605.05296  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Dataflow matrix machines 以多类型线性流和高阶神经元在运行时更新网络权重及拓扑矩阵，并讨论可编程构造；摘要未核实评价驱动的持续能力改进或改进器自身升级。

## 2. 论文的核心内容与贡献

### configuration:cfg_dmm_self_accumulator_architecture
原文给可编程自修改计算架构和运行状态反馈；未定义评价驱动的改进选择或证明变得更善改进，作为RSI邻接形式基础，不认证能力增益。

**适用版本**：1605.05296v2；**原文定位**：PDF v2 physical p3 §1.4 tool L79–99；PDF v2 physical p6 §3.3 tool L243–248；PDF v2 physical p8 §3.7 and conclusion tool L319–354。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_f78fb29c8e47147999`
Dataflow matrix machines 以多类型线性流和高阶神经元在运行时更新网络权重及拓扑矩阵，并讨论可编程构造；摘要未核实评价驱动的持续能力改进或改进器自身升级。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### DMM: Self accumulator controls recurrent topology
`cfg_dmm_self_accumulator_architecture` · protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 有限非零稀疏连接矩阵A与流类型/神经元signature，Self累积器的输出描述当前运行网络。 |
| 改进过程与下一轮参与 | 高阶神经元读取A并发出加性矩阵更新；down movement用A计算所有输入，包括Self，up movement把A更新为A+contributions。 |
| 保留的状态及时间尺度 | A在连续时步累积，变更后A决定下一时步计算和后续矩阵更新。 |
| 外部固定部分 | - signature和built-in neuron transforms - 同步两阶段解释器 - 没有提供任务reward或择优验证器 |

**配置判定**：原文给可编程自修改计算架构和运行状态反馈；未定义评价驱动的改进选择或证明变得更善改进，作为RSI邻接形式基础，不认证能力增益。

来源：https://arxiv.org/pdf/1605.05296；版本：1605.05296v2；定位：PDF v2 physical p3 §1.4 tool L79–99；PDF v2 physical p6 §3.3 tool L243–248；PDF v2 physical p8 §3.7 and conclusion tool L319–354。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_f78fb29c8e47147999`**：Dataflow matrix machines 以多类型线性流和高阶神经元在运行时更新网络权重及拓扑矩阵，并讨论可编程构造；摘要未核实评价驱动的持续能力改进或改进器自身升级。
  - 来源版本：1605.05296v2；定位：Atom entry http://arxiv.org/abs/1605.05296v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_dmm_self_accumulator_architecture`**：原文给可编程自修改计算架构和运行状态反馈；未定义评价驱动的改进选择或证明变得更善改进，作为RSI邻接形式基础，不认证能力增益。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- A反馈改变网络不自动是性能改进；后续程序学习被写为研究愿景。
- 原网页无版本地址实际PDF页眉为1605.05296v2(2018-06-21)，未把v2内容归给2016v1。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_dmm_programmable` · 已存来源 · 1605.05296v2
  - https://arxiv.org/pdf/1605.05296；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f78fb29c8e47147999 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
