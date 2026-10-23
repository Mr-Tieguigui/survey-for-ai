# R-Zero: Self-Evolving Reasoning LLM from Zero Data

> 方法论文 · 2025 · `wf_d82ab8edb1ee6dcab2`

**作者**：Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, Dong Yu  
**原文**：https://arxiv.org/abs/2508.05004  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Separate Challenger and Solver policies, initialized from the same base model, alternate GRPO training on self-generated mathematical questions；具体更新过程为：The current Solver answers generated questions multiple times. Majority answers become pseudo-labels; an uncertainty reward trains the Challenger, and a filtered informative-band curriculum trains the Solver against those pseudo-labels；更新状态的保留与后继使用为：Both policy checkpoints persist across alternating training rounds; generated filtered datasets train the next Solver。

## 2. 论文的核心内容与贡献

### configuration:cfg_r_zero
Agreement with a majority pseudo-label is not independent ground-truth verification.

**适用版本**：v4；**原文定位**：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_r_zero
`cfg_r_zero` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Separate Challenger and Solver policies, initialized from the same base model, alternate GRPO training on self-generated mathematical questions. |
| 改进过程与下一轮参与 | The current Solver answers generated questions multiple times. Majority answers become pseudo-labels; an uncertainty reward trains the Challenger, and a filtered informative-band curriculum trains the Solver against those pseudo-labels. |
| 保留的状态及时间尺度 | Both policy checkpoints persist across alternating training rounds; generated filtered datasets train the next Solver. |
| 外部固定部分 | - Base model initialization - GRPO and filtering rules - Majority-vote pseudo-label mechanism - Question prompt and mathematical task domain |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Separate Challenger and Solver policies, initialized from the same base model, alternate GRPO training on self-generated mathematical questions.（状态：`supported`；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）。
- **更新由什么过程产生**：The current Solver answers generated questions multiple times. Majority answers become pseudo-labels; an uncertainty reward trains the Challenger, and a filtered informative-band curriculum trains the Solver against those pseudo-labels.（状态：`supported`；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）。
- **状态怎样持久保留**：Both policy checkpoints persist across alternating training rounds; generated filtered datasets train the next Solver.（状态：`supported`；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）。
- **更新怎样进入后续改进**：The current Solver answers generated questions multiple times. Majority answers become pseudo-labels; an uncertainty reward trains the Challenger, and a filtered informative-band curriculum trains the Solver against those pseudo-labels.（状态：`supported`；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）。

**已核对的公式、算法或任务定义**：

- Uncertainty reward: 1 - 2 * abs(p_hat - 1/2), where p_hat is agreement with the majority pseudo-label.
- Curriculum admits question/pseudo-label pairs satisfying abs(p_hat - 1/2) <= delta.
- Solver binary reward tests equality to the majority pseudo-label, not Python execution truth.

**配置判定**：Agreement with a majority pseudo-label is not independent ground-truth verification.

来源：https://arxiv.org/html/2508.05004v4；版本：v4；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_r_zero`**：当前Solver响应定义Challenger不确定性奖励；更新Challenger生成下一批Solver训练题
  - 来源版本：v4；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1；深度：`AI_primary_method_passage_recheck`。

- **`oct15_training_ev_w_r_zero`**：R-Zero co-trains separate Challenger and Solver policies. Repeated Solver samples provide majority pseudo-labels, an uncertainty-based Challenger reward, and Solver training targets.
  - 来源版本：v4；定位：S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Agreement with a majority pseudo-label is not independent ground-truth verification.
- The two-role parameterization differs from AZR shared-role policy training.
- Author wording that the framework is fully automated is not a certification of unrestricted autonomy.
- 伪
- 标
- 签
- 一
- 致
- 性
- 不
- 等
- 于
- 独
- 立
- 正
- 确
- ；
- 借
- 用
- A
- b
- s
- o
- l
- u
- t
- e
- 
- Z
- r
- 代
- 码
- 执
- 行
- 器
- 作
- 其
- 证
- 据

## 7. 与其他论文的具体关系

### [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](../r03_method/wf_8cffd9d9c1aba22093.md)
关系：`contrasts_system_boundary_with` · `r2_r_zero_absolute_zero_11` · 当前展示权限：`primary_supported`。
Both adapt generated training tasks to current solver behavior. R-Zero alternately trains separate Challenger/Solver policies using majority-vote pseudo-labels and an uncertainty band. AZR jointly trains proposer/solver roles in one policy and grounds code-task labels and rewards in execution.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2508.05004v4（v4；S2.SS1.p1；S2.SS2.SSS0.Px1.p1；S2.SS3.p1；S2.SS4.p1）；https://arxiv.org/html/2505.03335v3（v3；S3.SS1；S3.SS2；S3.SS3.SSS1；S3.SS3.SSS2.p1；S3.SS3.SSS2.p2）。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_r_zero` · R-Zero · v4
  - https://arxiv.org/html/2508.05004v4；阅读深度：`未单列`。
- `oct15_training_src_w_r_zero` · 已存来源 · v4
  - https://arxiv.org/html/2508.05004v4；阅读深度：`targeted_primary_method_and_configuration_crosscheck`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d82ab8edb1ee6dcab2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
