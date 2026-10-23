# Automatic Prompt Optimization with "Gradient Descent" and Beam Search

> 方法论文 · 2023 · `wf_97c595829770a700ec`

**作者**：Reid Pryzant, Dan Iter, Jerry Li, Yin Lee, Chenguang Zhu, Michael Zeng  
**原文**：https://aclanthology.org/2023.emnlp-main.494.pdf  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在提示优化系统边界下满足项目四条件；作为TextGrad文本梯度谱系的直接前作

## 2. 论文的核心内容与贡献

### configuration:cfg_protegi
在提示优化系统边界下满足项目四条件；作为TextGrad文本梯度谱系的直接前作

**适用版本**：EMNLP-2023-version-of-record；**原文定位**：P0:L11-L28；P1:L52-L68；P1-2:L75-L167；P2:L168-L221；Algorithms 1-2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_protegi
`cfg_protegi` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 提示候选、数据小批量、文本梯度生成器、编辑器、beam search与候选选择器 |
| 改进过程与下一轮参与 | LLM根据错误生成自然语言梯度，再沿相反语义方向编辑当前提示并筛选后继候选 |
| 保留的状态及时间尺度 | beam中的提示跨优化步保留，并进入下一轮评估、诊断和扩展 |
| 外部固定部分 | 黑盒LLM、训练数据、评价指标、梯度/编辑模板与搜索预算 |

**配置判定**：在提示优化系统边界下满足项目四条件；作为TextGrad文本梯度谱系的直接前作

来源：https://aclanthology.org/2023.emnlp-main.494.pdf；版本：EMNLP-2023-version-of-record；定位：P0:L11-L28；P1:L52-L68；P1-2:L75-L167；P2:L168-L221；Algorithms 1-2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_2ba4e1dd13f80ecd` · 已存来源 · EMNLP-2023-version-of-record
  - https://aclanthology.org/2023.emnlp-main.494.pdf；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_97c595829770a700ec --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
