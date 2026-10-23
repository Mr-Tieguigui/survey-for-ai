# Absolute Zero: Reinforced Self-play Reasoning with Zero Data

> 方法论文 · 2025 · `wf_8cffd9d9c1aba22093`

**作者**：Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang  
**原文**：https://arxiv.org/abs/2505.03335  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：A single shared policy serves as both task proposer and solver, together with validated task buffers and a Python execution environment；具体更新过程为：The shared policy proposes code tasks, receives a learnability reward derived from solver rollouts, and receives execution-grounded solver rewards. Proposer and solver roles are jointly trained; validated generated tasks enter persistent buffers used by subsequent proposals；更新状态的保留与后继使用为：Policy parameters persist across RL updates; validated task buffers persist across online self-play iterations。

### 定点原文补充：具体问题与执行过程
同一个模型兼任出题者和解题者，通过自生成代码任务与执行反馈共同训练，课程随模型状态变化。

1. 围绕程序、输入、输出三元组构造演绎、归纳和溯因任务；执行器检查有效性与答案。
2. 有效任务进入持久缓冲区，后续采样与任务提议复用这些内容；TRR++ 更新共享策略。

**实验与选择协议**：

- 主实验基于 Qwen2.5-7B 与其 Coder 版本；训练批次 64×6，学习率 1e-6，采用 AdamW。
- 评价区分代码执行类同分布任务与数学/代码生成类分布外任务；不把两类分数混为一项。

**解释边界**：

- 零外部任务数据不等于没有预训练、种子提示、执行器或人工奖励规则。
- 执行正确性只覆盖规定的代码任务，不支持任意自然语言事实正确性。

来源：[2505.03335v3](https://arxiv.org/html/2505.03335v3)；定位：§3.1–3.3 Absolute Zero Reasoner；Algorithm 1；§4.1 Training Details and Evaluation Protocol。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_absolute_zero
No externally supplied task dataset does not mean no pretrained knowledge, seed prompt, evaluator, or human designed algorithm.

**适用版本**：v3；**原文定位**：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_absolute_zero
`cfg_absolute_zero` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | A single shared policy serves as both task proposer and solver, together with validated task buffers and a Python execution environment. |
| 改进过程与下一轮参与 | The shared policy proposes code tasks, receives a learnability reward derived from solver rollouts, and receives execution-grounded solver rewards. Proposer and solver roles are jointly trained; validated generated tasks enter persistent buffers used by subsequent proposals. |
| 保留的状态及时间尺度 | Policy parameters persist across RL updates; validated task buffers persist across online self-play iterations. |
| 外部固定部分 | - Pretrained model initialization - Python executor and task validation - Deduction, induction, and abduction task interfaces - TRR++ optimization and reward/format rules |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：A single shared policy serves as both task proposer and solver, together with validated task buffers and a Python execution environment.（状态：`supported`；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。
- **更新由什么过程产生**：The shared policy proposes code tasks, receives a learnability reward derived from solver rollouts, and receives execution-grounded solver rewards. Proposer and solver roles are jointly trained; validated generated tasks enter persistent buffers used by subsequent proposals.（状态：`supported`；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。
- **状态怎样持久保留**：Policy parameters persist across RL updates; validated task buffers persist across online self-play iterations.（状态：`supported`；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。
- **更新怎样进入后续改进**：The shared policy proposes code tasks, receives a learnability reward derived from solver rollouts, and receives execution-grounded solver rewards. Proposer and solver roles are jointly trained; validated generated tasks enter persistent buffers used by subsequent proposals.（状态：`supported`；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

**已核对的公式、算法或任务定义**：

- Eq. 4: proposer reward = 0 when mean solver success is 0; otherwise 1 - mean solver success.
- Eq. 5: solver reward is Python-checked answer correctness.
- Task triplet: o = p(i); deduction predicts o, abduction predicts a compatible i, induction synthesizes p.

**配置判定**：No externally supplied task dataset does not mean no pretrained knowledge, seed prompt, evaluator, or human designed algorithm.

来源：https://arxiv.org/html/2505.03335v3；版本：v3；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_absolute_zero`**：提出与求解都训练；缓冲样例条件化后续提案，更新模型继续出题和求解
  - 来源版本：v3；定位：S3.SS1.p1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2；深度：`AI_primary_method_passage_recheck`。

- **`oct15_training_ev_w_absolute_zero`**：AZR jointly trains one policy in proposer and solver roles using execution-validated code tasks. Valid triplets survive in buffers that condition subsequent proposals and fill incomplete batches.
  - 来源版本：v3；定位：S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- No externally supplied task dataset does not mean no pretrained knowledge, seed prompt, evaluator, or human designed algorithm.
- The executed truth concerns code reasoning task triplets; it does not establish truth of arbitrary natural language claims.
- The proposer reward is zero for zero solver success and otherwise one minus mean solver success; it is not R-Zero majority-vote uncertainty.
- 零
- 外
- 部
- 任
- 务
- 训
- 练
- 数
- 据
- 不
- 等
- 于
- 无
- 预
- 、
- 执
- 行
- 器
- 或
- 人
- 工
- 设
- 计

## 7. 与其他论文的具体关系

### [COEVO: Co-Evolving Context and Parameters for Recursive Self-Improvement](../r03_method/wf_3c776c3fd8713d0d43.md)
关系：`contrasts_system_boundary_with` · `r2_coevo_absolute_zero_10` · 当前展示权限：`primary_supported`。
COEVO changes the subsequent learning experience by accepting editable strategy-prompt revisions; AZR changes it by self-proposing execution-validated code tasks. Both couple current model state to later training data, but prompt-scaffold adaptation and task-proposal self-play are different update mechanisms.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2609.33398v1（v1；S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）；https://arxiv.org/html/2505.03335v3（v3；S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

### [R-Zero: Self-Evolving Reasoning LLM from Zero Data](../r03_method/wf_d82ab8edb1ee6dcab2.md)
关系：`contrasts_system_boundary_with` · `r2_r_zero_absolute_zero_11` · 当前展示权限：`primary_supported`。
Both adapt generated training tasks to current solver behavior. R-Zero alternately trains separate Challenger/Solver policies using majority-vote pseudo-labels and an uncertainty band. AZR jointly trains proposer/solver roles in one policy and grounds code-task labels and rewards in execution.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2508.05004v4（v4；S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）；https://arxiv.org/html/2505.03335v3（v3；S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

### [Recursive Self-Improvement in Unified Multimodal Models](../r03_method/wf_27e4243aa4b5eee002.md)
关系：`contrasts_system_boundary_with` · `r2_multimodal_rsi_absolute_zero_15` · 当前展示权限：`primary_supported`。
Both use program execution to ground self-produced training material. The multimodal configuration verifies rendered chart targets/labels and merges separate generation/understanding updates under a fixed diagnosis-to-curriculum rule. AZR uses execution-validated code reasoning triplets for shared-policy proposer/solver RL.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2610.03002v1（v1；S2.SS1；S2.SS2；S2.SS3；S2.SS4；S2.SS5.p1；S2.SS5.p2；S4.SS5.p1）；https://arxiv.org/html/2505.03335v3（v3；S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_absolute_zero` · Absolute Zero · v3
  - https://arxiv.org/html/2505.03335v3；阅读深度：`未单列`。
- `oct15_training_src_w_absolute_zero` · 已存来源 · v3
  - https://arxiv.org/html/2505.03335v3；阅读深度：`targeted_primary_method_and_configuration_crosscheck`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8cffd9d9c1aba22093 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
