# GLoRe: When, Where, and How to Improve LLM Reasoning via Global and Local Refinements

> 方法论文 · 2024 · `wf_5c87c7b33cd09ee672`

**作者**：Alex Havrilla, Sharath Raparthy, Christoforos Nalmpantis, Jane Dwivedi-Yu, Maksym Zhuravinskyi, Eric Hambro, Roberta Raileanu  
**原文**：https://arxiv.org/abs/2402.10963  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
训练期学生自采样与筛选再训练构成闭环；部署时冻结的多模型纠错配置单列为短暂输出修订。

## 2. 论文的核心内容与贡献

### configuration:cfg_glore_ei_training
核心训练闭环；奖励/更新规则固定，不证明改进算法自改。

**适用版本**：2402.10963v2；**原文定位**：§4.1 Step 1；Appendix B。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_glore_refinement_inference
推理期输出修订配置；不得借用训练闭环标签。

**适用版本**：2402.10963v2；**原文定位**：§4.1 Steps 2–3；§4.2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_glore_refiner_training
配对训练的设计适配单独定位；未证明该refiner自行重生成其下一轮训练数据。

**适用版本**：2402.10963v2；**原文定位**：§4.1 Step 3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_glore_ei_training
`cfg_glore_ei_training` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 学生策略、正确答案筛选器、累计训练数据与外部微调器 |
| 改进过程与下一轮参与 | 当前学生采样、过滤正确轨迹、并集训练数据、重新训练后生成下一批 |
| 保留的状态及时间尺度 | 跨EI轮次保留训练数据与学生参数 |
| 外部固定部分 | 答案、筛选、训练程序、采样预算 |

**配置判定**：核心训练闭环；奖励/更新规则固定，不证明改进算法自改。

来源：https://arxiv.org/html/2402.10963v2；版本：2402.10963v2；定位：§4.1 Step 1；Appendix B。

### cfg_glore_refinement_inference
`cfg_glore_refinement_inference` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结学生、ORM/SORM和全局/局部refiner |
| 改进过程与下一轮参与 | 识别需修订的答案和错误位置，再生成候选并排序 |
| 保留的状态及时间尺度 | 当前问题内的草稿与候选 |
| 外部固定部分 | 部署参数、排序器、数据接口 |

**配置判定**：推理期输出修订配置；不得借用训练闭环标签。

来源：https://arxiv.org/html/2402.10963v2；版本：2402.10963v2；定位：§4.1 Steps 2–3；§4.2。

### cfg_glore_refiner_training
`cfg_glore_refiner_training` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 学生生成的固定数据、错/对样本对与可训练refiner |
| 改进过程与下一轮参与 | 合成错误/正确答案配对，监督训练全局/局部refiner |
| 保留的状态及时间尺度 | 训练后refiner参数持久化 |
| 外部固定部分 | 学生数据、标签构造、配对方法和外部优化流程 |

**配置判定**：配对训练的设计适配单独定位；未证明该refiner自行重生成其下一轮训练数据。

来源：https://arxiv.org/html/2402.10963v2；版本：2402.10963v2；定位：§4.1 Step 3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_3b0af33e27939350` · 已存来源 · 2402.10963v2
  - https://arxiv.org/html/2402.10963v2；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5c87c7b33cd09ee672 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
