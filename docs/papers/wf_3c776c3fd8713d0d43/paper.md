# COEVO: Co-Evolving Context and Parameters for Recursive Self-Improvement

> 方法论文 · 2026 · `wf_3c776c3fd8713d0d43`

**作者**：Siwei Chen, Xinping Bao, Xinyu Cai, Yuan Cao, Wan Jiang, Shaohong Chen  
**原文**：https://arxiv.org/abs/2609.33398  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Model parameters theta_t and an editable strategy scaffold s_t co-adapt; the full prompt contains fixed constraints c plus editable scaffold s_t；具体更新过程为：An RL window updates parameters under a fixed prompt. The resulting frozen checkpoint proposes constrained prompt revisions, which are accepted only after policy-state and task-performance checks. An accepted prompt generates the next on-policy training distribution；更新状态的保留与后继使用为：Accepted strategy context and updated policy checkpoints persist across alternating RL windows。

## 2. 论文的核心内容与贡献

### configuration:cfg_coevo
Entropy and attention are intervention signals, not correctness evidence or unrestricted objectives.

**适用版本**：v1；**原文定位**：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_coevo
`cfg_coevo` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Model parameters theta_t and an editable strategy scaffold s_t co-adapt; the full prompt contains fixed constraints c plus editable scaffold s_t. |
| 改进过程与下一轮参与 | An RL window updates parameters under a fixed prompt. The resulting frozen checkpoint proposes constrained prompt revisions, which are accepted only after policy-state and task-performance checks. An accepted prompt generates the next on-policy training distribution. |
| 保留的状态及时间尺度 | Accepted strategy context and updated policy checkpoints persist across alternating RL windows. |
| 外部固定部分 | - Task objective and immutable prompt instructions - Optimizer - Evaluator - Execution interface - Acceptance criteria and editable prompt region |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Model parameters theta_t and an editable strategy scaffold s_t co-adapt; the full prompt contains fixed constraints c plus editable scaffold s_t.（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）。
- **更新由什么过程产生**：An RL window updates parameters under a fixed prompt. The resulting frozen checkpoint proposes constrained prompt revisions, which are accepted only after policy-state and task-performance checks. An accepted prompt generates the next on-policy training distribution.（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）。
- **状态怎样持久保留**：Accepted strategy context and updated policy checkpoints persist across alternating RL windows.（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）。
- **更新怎样进入后续改进**：An RL window updates parameters under a fixed prompt. The resulting frozen checkpoint proposes constrained prompt revisions, which are accepted only after policy-state and task-performance checks. An accepted prompt generates the next on-policy training distribution.（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）。

**已核对的公式、算法或任务定义**：

- State: (theta_t, p_t), with p_t = c concatenated with s_t.
- Dependency: accepted p_(t+1) changes next on-policy D_(t+1), which changes theta_(t+1).

**配置判定**：Entropy and attention are intervention signals, not correctness evidence or unrestricted objectives.

来源：https://arxiv.org/html/2609.33398v1；版本：v1；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_coevo`**：当前checkpoint编辑策略上下文，接受提示改变下一轮on-policy数据；参数更新又改变下一次编辑依据
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8；深度：`AI_primary_method_passage_recheck`。

- **`oct15_training_ev_w_coevo`**：COEVO alternates parameter learning and accepted strategy-prompt adaptation. The revised prompt changes subsequent on-policy experience while later parameter updates change the policy that evaluates the next context revision.
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Entropy and attention are intervention signals, not correctness evidence or unrestricted objectives.
- Only the strategy scaffold is editable; the task specification and output requirements remain fixed.
- The comparison with AZR concerns endogenous changes to subsequent learning experience, not author-certified inheritance.
- 熵
- /
- 注
- 意
- 力
- 是
- 操
- 作
- 性
- 信
- 号
- ；
- 不
- 因
- 果
- 证
- 据
- 或
- 无
- 限
- 增
- 长

## 7. 与其他论文的具体关系

### [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](../r03_method/wf_8cffd9d9c1aba22093.md)
关系：`contrasts_system_boundary_with` · `r2_coevo_absolute_zero_10` · 当前展示权限：`primary_supported`。
COEVO changes the subsequent learning experience by accepting editable strategy-prompt revisions; AZR changes it by self-proposing execution-validated code tasks. Both couple current model state to later training data, but prompt-scaffold adaptation and task-proposal self-play are different update mechanisms.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2609.33398v1（v1；S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS3.p4；S3.SS3.p5；S3.SS3.p8）；https://arxiv.org/html/2505.03335v3（v3；S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_coevo` · COEVO · v1
  - https://arxiv.org/html/2609.33398v1；阅读深度：`未单列`。
- `oct15_training_src_w_coevo` · 已存来源 · v1
  - https://arxiv.org/html/2609.33398v1；阅读深度：`targeted_primary_method_and_configuration_crosscheck`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3c776c3fd8713d0d43 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
