# Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models

> 方法论文 · 2024 · `wf_52c244d3fdd75d0080`

**作者**：Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, Quanquan Gu  
**原文**：https://arxiv.org/abs/2401.01335  
**研究分支**：偏好、自奖励与对齐训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：新旧轮次策略及自生成对手响应；具体更新过程为：上轮LLM产生对手响应，当前轮训练后复制参数成为下一轮对手；更新状态的保留与后继使用为：跨自博弈微调轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_spin
不需要新增人类数据不代表没有人类示范锚点

**适用版本**：v3；**原文定位**：S4.SS1.p1.1；S4.SS1.p2.1；S4.SS1.p5.1；S4.SS1.p5.3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_spin
`cfg_spin` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 新旧轮次策略及自生成对手响应 |
| 改进过程与下一轮参与 | 上轮LLM产生对手响应，当前轮训练后复制参数成为下一轮对手 |
| 保留的状态及时间尺度 | 跨自博弈微调轮次 |
| 外部固定部分 | 人类SFT数据分布、目标公式与KL约束 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：新旧轮次策略及自生成对手响应（状态：`supported`；定位：S4.SS1.p1；S4.SS1.p2；S4.SS1.p5）。
- **更新由什么过程产生**：上轮LLM产生对手响应，当前轮训练后复制参数成为下一轮对手（状态：`supported`；定位：S4.SS1.p1；S4.SS1.p2；S4.SS1.p5）。
- **状态怎样持久保留**：跨自博弈微调轮次（状态：`supported`；定位：S4.SS1.p1；S4.SS1.p2；S4.SS1.p5）。
- **更新怎样进入后续改进**：上轮LLM产生对手响应，当前轮训练后复制参数成为下一轮对手（状态：`supported`；定位：S4.SS1.p1；S4.SS1.p2；S4.SS1.p5）。

**配置判定**：不需要新增人类数据不代表没有人类示范锚点

来源：https://arxiv.org/html/2401.01335v3；版本：v3；定位：S4.SS1.p1.1；S4.SS1.p2.1；S4.SS1.p5.1；S4.SS1.p5.3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_spin`**：上轮LLM产生对手响应，当前轮训练后复制参数成为下一轮对手
  - 来源版本：v3；定位：S4.SS1.p1；S4.SS1.p2；S4.SS1.p5；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_p2b1_rise_spin`**：RISE将包含SPIN的自生成训练工作与自身多回合改进目标作分组对照；双端方法核查显示，RISE训练对历史错误作下一回合修订，SPIN用人类SFT回答对抗前轮模型输出并更新下一轮对手。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`e3_training_p2c_spin_selfrewarding_boundary`**：SPIN将Self-Rewarding称为同期工作，并明确对照隐式自评与显式奖励：SPIN以人类SFT回答为正样本、旧模型回答为对手负样本；Self-Rewarding由同模型生成并评分候选后构造DPO偏好。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 人类SFT目标分布仍为正样本锚点。
- 隐式自评不训练显式奖励模型，旧轮模型作为下一轮对手。
- 不
- 需
- 要
- 新
- 增
- 人
- 类
- 数
- 据
- 代
- 表
- 没
- 有
- 示
- 范
- 锚
- 点
- RISE引用SPIN是在分组背景中，支持目标与训练数据/轮次机制的横向对照，不支持由SPIN派生。RISE本端限定离线训练配置，单问题部署rollout为另列配置；SPIN跨训练轮次自博弈不能误写成部署多轮自纠正。
- 原文明确同期方法比较，不是历史继承；SPIN无需新偏好标注不等于无人类示范，Self-Rewarding无外部奖励模型不等于无IFT/EFT人类种子。不得由这种机制对照推出统一性能优劣。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_self_rewarding` · Self-Rewarding Language Models · v3
  - https://arxiv.org/html/2401.10020v3；阅读深度：`未单列`。
- `expand_src_w_spin` · SPIN · v3
  - https://arxiv.org/html/2401.01335v3；阅读深度：`未单列`。
- `stage1_src_w_rise` · 已存来源 · v2
  - https://arxiv.org/html/2407.18219v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_52c244d3fdd75d0080 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
