# RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges

> 方法论文 · 2026 · `wf_daf5985a2e817ebbf3`

**作者**：Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng, Jieping Ye  
**原文**：https://arxiv.org/abs/2608.24231  
**研究分支**：奖励、评价者与偏好信号  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：同步judge/checker的共享策略；具体更新过程为：judge参数更新后同步checker，更新checker产生下一轮训练奖励；更新状态的保留与后继使用为：跨同步RL更新。

## 2. 论文的核心内容与贡献

### configuration:cfg_recurse_qwen9b
训练奖励不使用外部gold，但早停使用一次人工验证holdout；接口解耦未证明消除所有shortcut

**适用版本**：v1；**原文定位**：S2.SS0.SSS0.Px2.p1；S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_recurse_qwen9b
`cfg_recurse_qwen9b` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 同步judge/checker的共享策略 |
| 改进过程与下一轮参与 | judge参数更新后同步checker，更新checker产生下一轮训练奖励 |
| 保留的状态及时间尺度 | 跨同步RL更新 |
| 外部固定部分 | 固定rubrics、接口、PolicyUpdate和PAV停止机制 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：同步judge/checker的共享策略（状态：`supported`；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1）。
- **更新由什么过程产生**：judge参数更新后同步checker，更新checker产生下一轮训练奖励（状态：`supported`；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1）。
- **状态怎样持久保留**：跨同步RL更新（状态：`supported`；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1）。
- **更新怎样进入后续改进**：judge参数更新后同步checker，更新checker产生下一轮训练奖励（状态：`supported`；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1）。

**配置判定**：训练奖励不使用外部gold，但早停使用一次人工验证holdout；接口解耦未证明消除所有shortcut

来源：https://arxiv.org/html/2608.24231v1；版本：v1；定位：S2.SS0.SSS0.Px2.p1；S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_recurse`**：judge参数更新后同步checker，更新checker产生下一轮训练奖励
  - 来源版本：v1；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 训
- 练
- 奖
- 励
- 不
- 使
- 用
- 外
- 部
- g
- o
- l
- d
- ，
- 但
- 早
- 停
- 一
- 次
- 人
- 工
- 验
- 证
- h
- u
- t
- ；
- 接
- 口
- 解
- 耦
- 未
- 明
- 消
- 除
- 所
- 有
- s
- r
- c

## 7. 与其他论文的具体关系

### [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](../r03_method/wf_593038e29fd9e78185.md)
关系：`disagrees_with` · `r2_recurse_meta_rewarding_8` · 当前展示权限：`retracted_separate`。
RecurSE将Meta-Rewarding描述为有外部meta-judge；Meta-Rewarding S2明确三角色共享同一模型。该外部性对照不能直接接受，需按具体参考模型/版本复核

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- expand_src_w_recurse：https://arxiv.org/html/2608.24231v1；版本：v1；定位：S3.SS1.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px2.p1；S2.SS0.SSS0.Px2.p1。
- expand_src_w_meta_rewarding：https://arxiv.org/html/2407.19594v2；版本：v2；定位：S1.p2；S2.p1；S2.p3；S2.p4；S2.SS1.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_recurse` · RecurSE · v1
  - https://arxiv.org/html/2608.24231v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_daf5985a2e817ebbf3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
