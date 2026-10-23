# MedForge: Interpretable Medical Deepfake Detection via Forgery-aware Reasoning

> 方法论文 · 2026 · `wf_56066c1b83df3075b9`

**作者**：Zhihui Chen, Kai He, Qingyuan Lei, Bin Pu, Jian Zhang, Yuling Xu, Mengling Feng  
**原文**：https://arxiv.org/html/2603.18577  
**研究分支**：多模态、医疗与视觉  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
MedForge本身是静态基础检测系统和数据/模型资源；MedForge-RSI在其冻结模型之上增加部署期持久经验与工具闭环

## 2. 论文的核心内容与贡献

### configuration:cfg_medforge_reasoner
MedForge本身是静态基础检测系统和数据/模型资源；MedForge-RSI在其冻结模型之上增加部署期持久经验与工具闭环

**适用版本**：2603.18577v2；**原文定位**：S3.1；S4.1-S4.3；web:L146-L199；Appendix D.4。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_medforge_reasoner
`cfg_medforge_reasoner` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | MedForge-90K数据、SFT冷启动与Forgery-aware GSPO训练得到的检测/推理模型 |
| 改进过程与下一轮参与 | 外部训练流程用定位、格式与分类奖励更新模型参数 |
| 保留的状态及时间尺度 | 训练后模型参数持久化；部署时原论文未给出递归自改循环 |
| 外部固定部分 | 数据集划分、奖励函数、SFT/GSPO算法、训练基础设施与评测协议 |

**配置判定**：MedForge本身是静态基础检测系统和数据/模型资源；MedForge-RSI在其冻结模型之上增加部署期持久经验与工具闭环

来源：https://arxiv.org/html/2603.18577；版本：2603.18577v2；定位：S3.1；S4.1-S4.3；web:L146-L199；Appendix D.4。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_86239974c524c14f` · 已存来源 · 2603.18577v2
  - https://arxiv.org/html/2603.18577；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_56066c1b83df3075b9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
