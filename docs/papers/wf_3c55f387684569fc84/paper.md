# On The Statistical Limits of Self-Improving Agents

> 失败/限制/风险 · 2025 · `wf_3c55f387684569fc84`

**作者**：Charles L. Wang, Keir Dorchen, Peter Jin  
**原文**：https://arxiv.org/abs/2510.04399  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Utility-Learning Tension in Self-Modifying Agents (https://arxiv.org/html/2510.04399v1)。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
For representational self-modification, the paper states distribution-free learnability iff policy-reachable representation classes have a uniform finite VC bound. Its Two-Gate rule combines an independent-validation improvement margin with membership in an ex-ante capacity-capped reference family. Direct formal self-modification limit; role corrected from empirical to limitation on the selected mathematical assumptions.

### 与 RSI 的具体关系

- Direct formal self-modification limit; role corrected from empirical to limitation on the selected mathematical assumptions.

## 2. 论文的核心内容与贡献

### role:b570_02_role_wf_3c55f387684569fc84
For representational self-modification, the paper states distribution-free learnability iff policy-reachable representation classes have a uniform finite VC bound. Its Two-Gate rule combines an independent-validation improvement margin with membership in an ex-ante capacity-capped reference family.

**适用版本**：2510.04399v1；**原文定位**：§4 policy-reachable capacity boundary and Two-Gate rule tool L299–339；Standing assumptions A1–A7 tool L272–298。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_02_ev_wf_3c55f387684569fc84`**：For representational self-modification, the paper states distribution-free learnability iff policy-reachable representation classes have a uniform finite VC bound. Its Two-Gate rule combines an independent-validation improvement margin with membership in an ex-ante capacity-capped reference family.
  - 来源版本：2510.04399v1；定位：§4 policy-reachable capacity boundary and Two-Gate rule tool L299–339；Standing assumptions A1–A7 tool L272–298；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §4 policy-reachable capacity boundary and Two-Gate rule
**来源**：https://arxiv.org/html/2510.04399v1  
**实际版本**：2510.04399v1  
**精确定位**：tool L299–339  
**关联证据**：`b570_02_ev_wf_3c55f387684569fc84`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 限制 · Standing assumptions A1–A7
**来源**：https://arxiv.org/html/2510.04399v1  
**实际版本**：2510.04399v1  
**精确定位**：tool L272–298  
**关联证据**：`b570_02_ev_wf_3c55f387684569fc84`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The stated result assumes fixed-distribution i.i.d. data, independent train/validation, bounded loss, a valid capacity measure/proxy, isolated modification axes and sample-complexity rather than runtime scope. It is an author-stated formal boundary, not an empirical RSI performance law or an independently verified proof.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_02_src_wf_3c55f387684569fc84` · Utility-Learning Tension in Self-Modifying Agents (https://arxiv.org/html/2510.04399v1) · 2510.04399v1
  - https://arxiv.org/html/2510.04399v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3c55f387684569fc84 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
