# ReAct: Synergizing Reasoning and Acting in Language Models

> 方法论文 · 2022 · `wf_e504ba1ba9c3fffc74`

**作者**：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao  
**原文**：https://arxiv.org/abs/2210.03629  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
冻结模型的任务内思考-动作-观察基础配置；提供代理规划背景，跨任务经验自改四条件不成立。

## 2. 论文的核心内容与贡献

### configuration:cfg_react_prompting
仅任务内推理/规划基础配置；不认证跨任务RSI。

**适用版本**：2210.03629v3；**原文定位**：§2 ReAct；§3.2 ReAct Prompting。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_react_prompting
`cfg_react_prompting` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结语言模型、固定少样本示例、任务环境和当前轨迹 |
| 改进过程与下一轮参与 | 任务内交替思考、动作、观察并更新当前计划 |
| 保留的状态及时间尺度 | 当前问题轨迹；不提供跨问题自写经验池 |
| 外部固定部分 | 模型参数、示例、环境接口和代理协议 |

**配置判定**：仅任务内推理/规划基础配置；不认证跨任务RSI。

来源：https://arxiv.org/html/2210.03629v3；版本：2210.03629v3；定位：§2 ReAct；§3.2 ReAct Prompting。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `intake_src_w_react` · 已存来源 · 2210.03629v3
  - https://arxiv.org/html/2210.03629v3；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e504ba1ba9c3fffc74 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
