# Generative Agents: Interactive Simulacra of Human Behavior

> 综合系统/智能体 · 2023 · `wf_6e953134a3c044025f`

**作者**：Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein  
**原文**：https://arxiv.org/abs/2304.03442  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在代理记忆边界内，反思被持久写回且能再作为反思输入；属于核心持久记忆配置，不能外推为改进器自改或无限能力增长。

## 2. 论文的核心内容与贡献

### configuration:cfg_generative_agents_reflection
在记忆系统边界满足四条件；实验衡量行为可信度，未检验递归能力增幅。

**适用版本**：2304.03442v2；**原文定位**：§4.1；§4.2；Fig.7。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_generative_agents_reflection
`cfg_generative_agents_reflection` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LLM、记忆流、重要度触发、检索与规划 |
| 改进过程与下一轮参与 | 观察写入记忆，反思抽象化并写回，未来反思可读取既有反思 |
| 保留的状态及时间尺度 | 模拟跨时间步持久记忆 |
| 外部固定部分 | LLM、提示、反思阈值、检索评分与模拟环境 |

**配置判定**：在记忆系统边界满足四条件；实验衡量行为可信度，未检验递归能力增幅。

来源：https://arxiv.org/html/2304.03442v2；版本：2304.03442v2；定位：§4.1；§4.2；Fig.7。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_d19623ba6dc0dadd` · 已存来源 · 2304.03442v2
  - https://arxiv.org/html/2304.03442v2；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6e953134a3c044025f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
