# Self-Rewarding Language Models

> 方法论文 · 2024 · `wf_35a65d9aba7dd5b532`

**作者**：Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston  
**原文**：https://arxiv.org/abs/2401.10020  
**研究分支**：奖励、评价者与偏好信号  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：生成回答和自评的同一模型＋偏好训练数据；具体更新过程为：M2由M1自评分偏好训练，M3由M2生成偏好继续训练；更新模型继续承担生成和评价；更新状态的保留与后继使用为：跨DPO训练轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_rewarding
不能把同一模型自评等同于独立真值；主实验与附录用更新模型出题的变体分开

**适用版本**：v3；**原文定位**：S2.I2.i2.p1.1；S2.I2.i3.p1.1；S2.SS3.SSS0.Px1.p2.1；S2.I3.ix3.p1.1；S2.I3.ix4.p1.1；S3.SS1.SSS3.Px2.p1.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_self_rewarding
`cfg_self_rewarding` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 生成回答和自评的同一模型＋偏好训练数据 |
| 改进过程与下一轮参与 | M2由M1自评分偏好训练，M3由M2生成偏好继续训练；更新模型继续承担生成和评价 |
| 保留的状态及时间尺度 | 跨DPO训练轮次 |
| 外部固定部分 | 人类IFT/EFT种子、DPO、评分提示；主实验提问生成器固定 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：生成回答和自评的同一模型＋偏好训练数据（状态：`supported`；定位：S2.p1；S2.p3；S2.SS2.p3；S2.SS4.SSS0.Px1.p1；S2.SS4.SSS0.Px2.p2）。
- **更新由什么过程产生**：M2由M1自评分偏好训练，M3由M2生成偏好继续训练；更新模型继续承担生成和评价（状态：`supported`；定位：S2.p1；S2.p3；S2.SS2.p3；S2.SS4.SSS0.Px1.p1；S2.SS4.SSS0.Px2.p2）。
- **状态怎样持久保留**：跨DPO训练轮次（状态：`supported`；定位：S2.p1；S2.p3；S2.SS2.p3；S2.SS4.SSS0.Px1.p1；S2.SS4.SSS0.Px2.p2）。
- **更新怎样进入后续改进**：M2由M1自评分偏好训练，M3由M2生成偏好继续训练；更新模型继续承担生成和评价（状态：`supported`；定位：S2.p1；S2.p3；S2.SS2.p3；S2.SS4.SSS0.Px1.p1；S2.SS4.SSS0.Px2.p2）。

**配置判定**：不能把同一模型自评等同于独立真值；主实验与附录用更新模型出题的变体分开

来源：https://arxiv.org/html/2401.10020v3；版本：v3；定位：S2.I2.i2.p1.1；S2.I2.i3.p1.1；S2.SS3.SSS0.Px1.p2.1；S2.I3.ix3.p1.1；S2.I3.ix4.p1.1；S3.SS1.SSS3.Px2.p1.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_self_rewarding`**：M2由M1自评分偏好训练，M3由M2生成偏好继续训练；更新模型继续承担生成和评价
  - 来源版本：v3；定位：S2.p1；S2.p3；S2.SS2.p3；S2.SS4.SSS0.Px1.p1；S2.SS4.SSS0.Px2.p2；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_p2c_spin_selfrewarding_boundary`**：SPIN将Self-Rewarding称为同期工作，并明确对照隐式自评与显式奖励：SPIN以人类SFT回答为正样本、旧模型回答为对手负样本；Self-Rewarding由同模型生成并评分候选后构造DPO偏好。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`e3_training_r2_meta_rewarding_self_rewarding_1`**：Meta-Rewarding明确沿用Self-Rewarding的回答生成—同模型评分—偏好优化流程，并加入判断偏好训练、meta-judge和长度控制；共享同一模型的三个角色。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 主实验prompts由固定Llama2-Chat70B生成；responses和评分使用更新中的模型。
- M2从M1、M3从M2初始化；人类IFT/EFT种子固定。
- 不
- 能
- 把
- 同
- 一
- 模
- 型
- 自
- 评
- 等
- 于
- 独
- 立
- 真
- 值
- ；
- 主
- 实
- 验
- 与
- 附
- 录
- 用
- 更
- 新
- 出
- 题
- 的
- 变
- 体
- 分
- 开
- 原文明确同期方法比较，不是历史继承；SPIN无需新偏好标注不等于无人类示范，Self-Rewarding无外部奖励模型不等于无IFT/EFT人类种子。不得由这种机制对照推出统一性能优劣。
- 方法扩展有作者明确陈述；Meta-Rewarding不是由独立外部meta-judge训练。两文种子模型、数据与长度控制不同，不能据此比较原论文全局性能；Self-Rewarding主实验出题模型固定，其附录更新出题模型变体不并入本配置。

## 7. 与其他论文的具体关系

### [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](../r03_method/wf_593038e29fd9e78185.md)
关系：`extends_configuration_of` · `r2_meta_rewarding_self_rewarding_1` · 当前展示权限：`primary_supported`。
Meta-Rewarding明确沿用Self-Rewarding的回答生成—同模型评分—偏好优化流程，并加入判断偏好训练、meta-judge和长度控制；共享同一模型的三个角色。

**关系边界**：方法扩展有作者明确陈述；Meta-Rewarding不是由独立外部meta-judge训练。两文种子模型、数据与长度控制不同，不能据此比较原论文全局性能；Self-Rewarding主实验出题模型固定，其附录更新出题模型变体不并入本配置。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2407.19594v2；版本：v2；定位：S2.p3.1；S2.p4.1；S2.SS1.p1.1；S2.SS2.p3.1。
- object：https://arxiv.org/html/2401.10020v3；版本：v3；定位：S2.I2.i2.p1.1；S2.I2.i3.p1.1；S2.SS3.SSS0.Px1.p2.1；S2.I3.ix3.p1.1；S2.I3.ix4.p1.1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_meta_rewarding` · Meta-Rewarding Language Models · v2
  - https://arxiv.org/html/2407.19594v2；阅读深度：`未单列`。
- `expand_src_w_self_rewarding` · Self-Rewarding Language Models · v3
  - https://arxiv.org/html/2401.10020v3；阅读深度：`未单列`。
- `expand_src_w_spin` · SPIN · v3
  - https://arxiv.org/html/2401.01335v3；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_35a65d9aba7dd5b532 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
