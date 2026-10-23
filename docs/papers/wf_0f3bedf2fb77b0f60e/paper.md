# Generating Sequences by Learning to Self-Correct

> 方法论文 · 2023 · `wf_0f3bedf2fb77b0f60e`

**作者**：Sean Welleck, Ximing Lu, Peter West, Faeze Brahman, Tianxiao Shen, Daniel Khashabi, Yejin Choi  
**原文**：https://arxiv.org/abs/2211.00053  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在线训练的校正器生成新数据并重新训练自身；固定校正器在单个样本上多次纠错不等于跨任务持久自改。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_correct_inference
支持多次纠错，原文不存在一般性的两轮上限；无跨独立输出持久参数更新。

**适用版本**：2211.00053v1；**原文定位**：§2 Eq.1；§3.2；§3.5；§3.6。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_self_correct_online_training
在线自校正训练满足四条件；更新对象是校正器。

**适用版本**：2211.00053v1；**原文定位**：§2.1；Algorithm 1；Eq.2–5。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_self_correct_online_training
`cfg_self_correct_online_training` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定生成器、可训练校正器、值函数与数据池 |
| 改进过程与下一轮参与 | 当前校正器生成新修订，形成值改进样本对，梯度更新后重复生成 |
| 保留的状态及时间尺度 | 跨训练迭代保留数据池与校正器参数 |
| 外部固定部分 | 生成器、值/反馈函数、配对和优化规则 |

**配置判定**：在线自校正训练满足四条件；更新对象是校正器。

来源：https://arxiv.org/html/2211.00053v1；版本：2211.00053v1；定位：§2.1；Algorithm 1；Eq.2–5。

### cfg_self_correct_inference
`cfg_self_correct_inference` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结生成器及已训练校正器 |
| 改进过程与下一轮参与 | 校正器对同一输出多次应用 |
| 保留的状态及时间尺度 | 单问题的输出序列 |
| 外部固定部分 | 部署模型参数、反馈和停机规则 |

**配置判定**：支持多次纠错，原文不存在一般性的两轮上限；无跨独立输出持久参数更新。

来源：https://arxiv.org/html/2211.00053v1；版本：2211.00053v1；定位：§2 Eq.1；§3.2；§3.5；§3.6。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_05103e47f07b784d` · 已存来源 · 2211.00053v1
  - https://arxiv.org/html/2211.00053v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0f3bedf2fb77b0f60e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
