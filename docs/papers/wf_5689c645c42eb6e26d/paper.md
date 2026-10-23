# Large Language Models have Intrinsic Self-Correction Ability

> 方法论文 · 2024 · `wf_5689c645c42eb6e26d`

**作者**：Dancheng Liu, Amir Nassereldine, Ziming Yang, Chenhui Xu, Yuting Hu, Jiajie Li, Utkarsh Kumar, Changjae Lee, Ruiyang Qin, Yiyu Shi, Jinjun Xiong  
**原文**：https://arxiv.org/abs/2406.15673  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：not_fully_inspected；具体更新过程为：no persistent cross-task improvement-state update established in checked method；更新状态的保留与后继使用为：within one answer-correction context。

## 2. 论文的核心内容与贡献

### configuration:cfg_intrinsic_correction
Single-answer reasoning/correction context is distinct from a retained improvement system.

**适用版本**：v1；**原文定位**：Section 2.2 Eq.4。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_intrinsic_correction
`cfg_intrinsic_correction` · method_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | not_fully_inspected |
| 改进过程与下一轮参与 | no persistent cross-task improvement-state update established in checked method |
| 保留的状态及时间尺度 | within one answer-correction context |

**配置判定**：Single-answer reasoning/correction context is distinct from a retained improvement system.

来源：https://arxiv.org/abs/2406.15673v1；版本：v1；定位：Section 2.2 Eq.4。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口

**证据深度**：original_abstract, primary_abstract_or_official_summary_review。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5689c645c42eb6e26d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
