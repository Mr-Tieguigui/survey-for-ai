# Linear Transformers Are Secretly Fast Weight Programmers

> 方法论文 · 2021 · `wf_7d5c8c3617e9f1f28d`

**作者**：Imanol Schlag, Kazuki Irie, Jürgen Schmidhuber  
**原文**：https://proceedings.mlr.press/v139/schlag21a.html  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
是SRWM的关键机制基础；主要主张是序列内快速记忆编程，未把自身表述为跨任务递归系统改进，因此保持adjacent

## 2. 论文的核心内容与贡献

### configuration:cfg_deltanet
是SRWM的关键机制基础；主要主张是序列内快速记忆编程，未把自身表述为跨任务递归系统改进，因此保持adjacent

**适用版本**：PMLR-139-version-of-record；**原文定位**：abstract；S2-S3；Eq.24-25；PMLR method text。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_deltanet
`cfg_deltanet` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 慢速控制网络、序列内快速权重矩阵、动态学习率和delta更新规则 |
| 改进过程与下一轮参与 | 慢速网络根据输入生成key/value/学习率，以delta规则纠正快速记忆中的键值映射 |
| 保留的状态及时间尺度 | 快速权重在单序列/episode内部跨时间步保留，通常在新序列重置 |
| 外部固定部分 | 训练后的慢速网络参数、delta规则、结构与外部训练过程 |

**配置判定**：是SRWM的关键机制基础；主要主张是序列内快速记忆编程，未把自身表述为跨任务递归系统改进，因此保持adjacent

来源：https://proceedings.mlr.press/v139/schlag21a.html；版本：PMLR-139-version-of-record；定位：abstract；S2-S3；Eq.24-25；PMLR method text。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_48a91309d8294bc3` · 已存来源 · PMLR-139-version-of-record
  - https://proceedings.mlr.press/v139/schlag21a.html；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7d5c8c3617e9f1f28d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
