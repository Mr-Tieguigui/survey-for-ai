# MedForge-RSI: Medical Deepfake Detection via Recursive Self-Improvement

> 方法论文 · 2026 · `wf_f025e1cd4ede05d159`

**作者**：Zhihui Chen, Mengling Feng  
**原文**：https://arxiv.org/abs/2609.36549  
**研究分支**：多模态、医疗与视觉  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：v3经验库/工具及冻结检测模型的反思；具体更新过程为：现有工具读数与指令历史输入反思，形成后续库/工具提案；工具保留用于后续测量与反思；更新状态的保留与后继使用为：部署模拟轮次内。

## 2. 论文的核心内容与贡献

### configuration:cfg_medforge_v3
保留旧结构核心，不等于改进机制代码自改；有验证bug、退化、污染及部分变体无seed复核，非临床有效性认证

**适用版本**：2609.36549v1；**原文定位**：A4.SS0.SSS0.Px1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_medforge_v3
`cfg_medforge_v3` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | v3经验库/工具及冻结检测模型的反思 |
| 改进过程与下一轮参与 | 现有工具读数与指令历史输入反思，形成后续库/工具提案；工具保留用于后续测量与反思 |
| 保留的状态及时间尺度 | 部署模拟轮次内 |
| 外部固定部分 | 模型权重、官方prompt、评分解析、流和接受实现 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：v3经验库/工具及冻结检测模型的反思（状态：`supported`；定位：S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；A4.SS0.SSS0.Px1.p1；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1）。
- **更新由什么过程产生**：现有工具读数与指令历史输入反思，形成后续库/工具提案；工具保留用于后续测量与反思（状态：`supported`；定位：S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；A4.SS0.SSS0.Px1.p1；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1）。
- **状态怎样持久保留**：部署模拟轮次内（状态：`supported`；定位：S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；A4.SS0.SSS0.Px1.p1；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1）。
- **更新怎样进入后续改进**：现有工具读数与指令历史输入反思，形成后续库/工具提案；工具保留用于后续测量与反思（状态：`supported`；定位：S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；A4.SS0.SSS0.Px1.p1；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1）。

**配置判定**：保留旧结构核心，不等于改进机制代码自改；有验证bug、退化、污染及部分变体无seed复核，非临床有效性认证

来源：https://arxiv.org/html/2609.36549v1；版本：2609.36549v1；定位：A4.SS0.SSS0.Px1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_medforge_rsi`**：现有工具读数与指令历史输入反思，形成后续库/工具提案；工具保留用于后续测量与反思
  - 来源版本：v1；定位：S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.p1；S3.SS4.p3；A4.SS0.SSS0.Px1.p1；S6.SS3.SSS0.Px4.p1；S7.SS0.SSS0.Px3.p1；A1.T2.2；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- acceptance_test_not_strictly_monotonic_improvement
- health_check_fallback_is_a_distinct_admission_path
- not_clinical_effectiveness_certification
- 保
- 留
- 旧
- 结
- 构
- 核
- 心
- ，
- 不
- 等
- 于
- 改
- 进
- 机
- 制
- 代
- 码
- 自
- ；
- 有
- 验
- 证
- b
- u
- g
- 、
- 退
- 化
- 污
- 染
- 及
- 部
- 分
- 变
- 体
- 无
- s
- e
- d
- 复
- 非
- 临
- 床
- 效
- 性
- 认

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `hist_src_medforge_abs` · 已存来源 · 2609.36549v1
  - https://arxiv.org/abs/2609.36549；阅读深度：`未单列`。
- `expand_src_w_medforge_rsi` · MedForge-RSI · v1
  - https://arxiv.org/html/2609.36549v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f025e1cd4ede05d159 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
