# Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge

> 方法论文 · 2024 · `wf_593038e29fd9e78185`

**作者**：Tianhao Wu, Weizhe Yuan, Olga Golovneva, Jing Xu, Yuandong Tian, Jiantao Jiao, Jason Weston, Sainbayar Sukhbaatar  
**原文**：https://arxiv.org/abs/2407.19594  
**研究分支**：奖励、评价者与偏好信号  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：同模型actor/judge/meta-judge及偏好训练；具体更新过程为：同模型产生回答和判断偏好，DPO更新后作为下一轮生成器和训练初始化；更新状态的保留与后继使用为：跨偏好训练轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_meta_rewarding
meta-judge角色不等于外部模型；原文明确共享模型，不能接受另一论文对它的外部性概括

**适用版本**：v2；**原文定位**：S2.p3.1；S2.p4.1；S2.SS1.p1.1；S2.SS2.p3.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_meta_rewarding
`cfg_meta_rewarding` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 同模型actor/judge/meta-judge及偏好训练 |
| 改进过程与下一轮参与 | 同模型产生回答和判断偏好，DPO更新后作为下一轮生成器和训练初始化 |
| 保留的状态及时间尺度 | 跨偏好训练轮次 |
| 外部固定部分 | 种子模型、rubric、偏好构造和DPO |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：同模型actor/judge/meta-judge及偏好训练（状态：`supported`；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1）。
- **更新由什么过程产生**：同模型产生回答和判断偏好，DPO更新后作为下一轮生成器和训练初始化（状态：`supported`；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1）。
- **状态怎样持久保留**：跨偏好训练轮次（状态：`supported`；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1）。
- **更新怎样进入后续改进**：同模型产生回答和判断偏好，DPO更新后作为下一轮生成器和训练初始化（状态：`supported`；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1）。

**配置判定**：meta-judge角色不等于外部模型；原文明确共享模型，不能接受另一论文对它的外部性概括

来源：https://arxiv.org/html/2407.19594v2；版本：v2；定位：S2.p3.1；S2.p4.1；S2.SS1.p1.1；S2.SS2.p3.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_meta_rewarding`**：同模型产生回答和判断偏好，DPO更新后作为下一轮生成器和训练初始化
  - 来源版本：v2；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_r2_meta_rewarding_self_rewarding_1`**：Meta-Rewarding明确沿用Self-Rewarding的回答生成—同模型评分—偏好优化流程，并加入判断偏好训练、meta-judge和长度控制；共享同一模型的三个角色。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 同模型actor/judge/meta-judge，三个角色并非三个外部模型。
- 长度控制是本方法新增配置。
- m
- e
- t
- a
- -
- j
- u
- d
- g
- 角
- 色
- 不
- 等
- 于
- 外
- 部
- 模
- 型
- ；
- 原
- 文
- 明
- 确
- 共
- 享
- ，
- 能
- 接
- 受
- 另
- 一
- 论
- 对
- 它
- 的
- 性
- 概
- 括
- 方法扩展有作者明确陈述；Meta-Rewarding不是由独立外部meta-judge训练。两文种子模型、数据与长度控制不同，不能据此比较原论文全局性能；Self-Rewarding主实验出题模型固定，其附录更新出题模型变体不并入本配置。

## 7. 与其他论文的具体关系

### [Self-Rewarding Language Models](../r03_method/wf_35a65d9aba7dd5b532.md)
关系：`extends_configuration_of` · `r2_meta_rewarding_self_rewarding_1` · 当前展示权限：`primary_supported`。
Meta-Rewarding明确沿用Self-Rewarding的回答生成—同模型评分—偏好优化流程，并加入判断偏好训练、meta-judge和长度控制；共享同一模型的三个角色。

**关系边界**：方法扩展有作者明确陈述；Meta-Rewarding不是由独立外部meta-judge训练。两文种子模型、数据与长度控制不同，不能据此比较原论文全局性能；Self-Rewarding主实验出题模型固定，其附录更新出题模型变体不并入本配置。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2407.19594v2；版本：v2；定位：S2.p3.1；S2.p4.1；S2.SS1.p1.1；S2.SS2.p3.1。
- object：https://arxiv.org/html/2401.10020v3；版本：v3；定位：S2.I2.i2.p1.1；S2.I2.i3.p1.1；S2.SS3.SSS0.Px1.p2.1；S2.I3.ix3.p1.1；S2.I3.ix4.p1.1。

### [RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges](../r03_method/wf_daf5985a2e817ebbf3.md)
关系：`disagrees_with` · `r2_recurse_meta_rewarding_8` · 当前展示权限：`retracted_separate`。
RecurSE将Meta-Rewarding描述为有外部meta-judge；Meta-Rewarding S2明确三角色共享同一模型。该外部性对照不能直接接受，需按具体参考模型/版本复核

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- expand_src_w_recurse：https://arxiv.org/html/2608.24231v1；版本：v1；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1。
- expand_src_w_meta_rewarding：https://arxiv.org/html/2407.19594v2；版本：v2；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_meta_rewarding` · Meta-Rewarding Language Models · v2
  - https://arxiv.org/html/2407.19594v2；阅读深度：`未单列`。
- `expand_src_w_self_rewarding` · Self-Rewarding Language Models · v3
  - https://arxiv.org/html/2401.10020v3；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_593038e29fd9e78185 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
