# Recursive Introspection: Teaching Language Model Agents How to Self-Improve

> 方法论文 · 2024 · `wf_6265b745e845c2b4f1`

**作者**：Yuxiao Qu, Tianjun Zhang, Naman Garg, Aviral Kumar  
**原文**：https://arxiv.org/abs/2407.18219  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：离线迭代训练的策略与累积多轮数据；具体更新过程为：当前策略产生on-policy轨迹，重标注后训练，更新策略参与下一轮数据收集；通常从base在累积数据上重训；更新状态的保留与后继使用为：跨训练轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_rise
core只指训练配置；单问题测试时rollout另列adjacent，oracle与非oracle模式不混合

**适用版本**：v2；**原文定位**：S3.p1；S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS4.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_rise_test_rollout
当前答案被修订，不跨最终输出保留，oracle模式与非oracle另列

**适用版本**：v2；**原文定位**：S4.SS3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_rise
`cfg_rise` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 离线迭代训练的策略与累积多轮数据 |
| 改进过程与下一轮参与 | 当前策略产生on-policy轨迹，重标注后训练，更新策略参与下一轮数据收集；通常从base在累积数据上重训 |
| 保留的状态及时间尺度 | 跨训练轮次 |
| 外部固定部分 | 验证奖励、加权SFT、教师或自蒸馏重标注方法 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：离线迭代训练的策略与累积多轮数据（状态：`supported`；定位：S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS3.p1；S4.SS4.p1）。
- **更新由什么过程产生**：当前策略产生on-policy轨迹，重标注后训练，更新策略参与下一轮数据收集；通常从base在累积数据上重训（状态：`supported`；定位：S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS3.p1；S4.SS4.p1）。
- **状态怎样持久保留**：跨训练轮次（状态：`supported`；定位：S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS3.p1；S4.SS4.p1）。
- **更新怎样进入后续改进**：当前策略产生on-policy轨迹，重标注后训练，更新策略参与下一轮数据收集；通常从base在累积数据上重训（状态：`supported`；定位：S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS3.p1；S4.SS4.p1）。

**配置判定**：core只指训练配置；单问题测试时rollout另列adjacent，oracle与非oracle模式不混合

来源：https://arxiv.org/html/2407.18219v2；版本：v2；定位：S3.p1；S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS4.p1。

### cfg_rise_test_rollout
`cfg_rise_test_rollout` · split_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单问题测试rollout |

**配置判定**：当前答案被修订，不跨最终输出保留，oracle模式与非oracle另列

来源：https://arxiv.org/html/2407.18219v2；版本：v2；定位：S4.SS3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e3_w_rise`**：当前策略产生on-policy轨迹，重标注后训练，更新策略参与下一轮数据收集；通常从base在累积数据上重训
  - 来源版本：v2；定位：S4.SS2.p3；S4.SS2.p4；S4.SS2.p5；S4.SS3.p1；S4.SS4.p1；深度：`未单列`。

- **`e3_training_p2b1_rise_spin`**：RISE将包含SPIN的自生成训练工作与自身多回合改进目标作分组对照；双端方法核查显示，RISE训练对历史错误作下一回合修订，SPIN用人类SFT回答对抗前轮模型输出并更新下一轮对手。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`oct15_agents_ev_p2b1_rise_self_correction_limit`**：RISE明确引用现成模型内生自纠正常失败的研究，以额外多轮训练诱导顺序修订能力；被引用研究把intrinsic self-correction限定为没有外部或人类反馈的部署纠正，并另检验oracle停止、调用成本和初始提示公平性。训练条件改变使两项结论适用范围不同。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_explicit_plus_two_endpoint_method_check`。

- **`oct15_agents_ev_p2b1_rise_self_refine`**：RISE以多轮on-policy轨迹、教师或best-of-N重标注及加权回归训练单一模型，使其学会逐轮修订；Self-Refine原方法固定同一LM及生成/反馈/修订提示，在单输入内保留反馈历史、迭代改写输出。RISE附录另明确实现Self-Refine式评测基线。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_explicit_plus_two_endpoint_method_check`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- distillation与self-distillation是两种数据重标注变体。
- 离线训练关系不能赋予部署单问题rollout持续跨题学习。
- 与Self-Refine的横向对照限指定训练/推理边界，不能认定原任务与RISE适配基线完全同配置。
- RISE的非oracle测试模式不表示离线训练数据构造不使用正确性奖励或教师。
- c
- o
- r
- e
- 只
- 指
- 训
- 练
- 配
- 置
- ；
- 单
- 问
- 题
- 测
- 试
- 时
- l
- u
- t
- 另
- 列
- a
- d
- j
- n
- ，
- 与
- 非
- 模
- 式
- 不
- 混
- 合
- RISE引用SPIN是在分组背景中，支持目标与训练数据/轮次机制的横向对照，不支持由SPIN派生。RISE本端限定离线训练配置，单问题部署rollout为另列配置；SPIN跨训练轮次自博弈不能误写成部署多轮自纠正。
- 没有在目标研究的相同模型、提示、预算及样本上独立重做其全部实验。RISE训练数据与奖励可使用正确性信号，不能因其非oracle测试模式而改写为训练也无监督；目标文主要结论限其已测推理设置，原文已承认其他领域可能有效。关系不是直接反驳、失败复现或消除原研究结论。
- 主边比较RISE离线训练配置与Self-Refine单输入提示配置，不混入RISE单问题部署rollout。原Self-Refine数学推理附录A15.p5使用正确标签控制迭代；不可笼统声称其全部原实验无外部标签。RISE的Self-Refine适配基线与原Self-Refine各任务、后端、预算不等同；不推出公平统一性能排名、代码复用或历史继承。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_spin` · SPIN · v3
  - https://arxiv.org/html/2401.01335v3；阅读深度：`未单列`。
- `oct15_agents_src_w_rise` · 已存来源 · v2
  - https://arxiv.org/html/2407.18219v2；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `oct15_agents_src_w_self_correction_limit` · 已存来源 · v2
  - https://arxiv.org/html/2310.01798v2；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `oct15_agents_src_w_self_refine` · 已存来源 · v2
  - https://arxiv.org/html/2303.17651v2；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `stage1_src_w_rise` · 已存来源 · v2
  - https://arxiv.org/html/2407.18219v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6265b745e845c2b4f1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
