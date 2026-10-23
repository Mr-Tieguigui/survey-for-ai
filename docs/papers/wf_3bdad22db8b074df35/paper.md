# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

> 背景/相邻基础 · 2023 · `wf_3bdad22db8b074df35`

**作者**：Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn  
**原文**：https://arxiv.org/html/2305.18290  
**研究分支**：偏好、自奖励与对齐训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
对齐基础方法，不将DPO本身标为RSI；它为SPIN等迭代自训练方法提供关键目标函数对照

## 2. 论文的核心内容与贡献

### configuration:cfg_dpo
对齐基础方法，不将DPO本身标为RSI；它为SPIN等迭代自训练方法提供关键目标函数对照

**适用版本**：2305.18290v3；**原文定位**：abstract；S3；S4；Eq.7；web:L54-L64;L113-L133。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### cfg_dpo
`cfg_dpo` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定离线偏好对、参考策略与一次策略优化流程 |
| 改进过程与下一轮参与 | 外部梯度优化器按DPO损失提高偏好回答概率并降低非偏好回答概率 |
| 保留的状态及时间尺度 | 训练后参数持久化；论文方法本身没有跨代自生成反馈闭环 |
| 外部固定部分 | 离线偏好数据、参考策略、损失函数、优化器与超参数 |

**配置判定**：对齐基础方法，不将DPO本身标为RSI；它为SPIN等迭代自训练方法提供关键目标函数对照

来源：https://arxiv.org/html/2305.18290；版本：2305.18290v3；定位：abstract；S3；S4；Eq.7；web:L54-L64;L113-L133。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_ea7008970695e894` · 已存来源 · 2305.18290v3
  - https://arxiv.org/html/2305.18290；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3bdad22db8b074df35 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
