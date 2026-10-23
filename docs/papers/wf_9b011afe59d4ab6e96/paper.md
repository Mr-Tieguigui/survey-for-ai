# Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification

> 方法论文 · 2026 · `wf_9b011afe59d4ab6e96`

**作者**：Jie Feng, Xiaoyang Wang, Xin Chen, Yuanyuan Shi  
**原文**：https://arxiv.org/abs/2609.14260  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
LLM edits typed structures from parents and evaluator records. Validity checks and per-operating-point fitting yield NRMSE rewards; reported implementation activates archive feedback and proposer RL. Context and weight RSI channels operate within fixed grammar/evaluator.

### 与 RSI 的具体关系

- Context and weight RSI channels operate within fixed grammar/evaluator.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_9b011afe59d4ab6e96
LLM edits typed structures from parents and evaluator records. Validity checks and per-operating-point fitting yield NRMSE rewards; reported implementation activates archive feedback and proposer RL.

**适用版本**：2609.14260v1；**原文定位**：Structure-fit-reward loop; PDF physical page 3, derived page-text lines 39-44 (one-based local extraction, not web-tool lines)；Active channels; PDF physical page 8, derived page-text lines 83-98 (one-based local extraction, not web-tool lines)；Simulation and identifiability; PDF physical page 10, derived page-text lines 13-39 (one-based local extraction, not web-tool lines)；NRMSE evaluation; PDF physical page 7, derived page-text lines 43-52 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Structure fitted per operating point; mean NRMSE gives reward -log NRMSE, with unchanged-edit penalty. 512 candidates per policy batch; good fit does not establish physical identity.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_9b011afe59d4ab6e96`**：LLM edits typed structures from parents and evaluator records. Validity checks and per-operating-point fitting yield NRMSE rewards; reported implementation activates archive feedback and proposer RL.
  - 来源版本：2609.14260v1；定位：Structure-fit-reward loop; PDF physical page 3, derived page-text lines 39-44 (one-based local extraction, not web-tool lines)；Active channels; PDF physical page 8, derived page-text lines 83-98 (one-based local extraction, not web-tool lines)；Simulation and identifiability; PDF physical page 10, derived page-text lines 13-39 (one-based local extraction, not web-tool lines)；NRMSE evaluation; PDF physical page 7, derived page-text lines 43-52 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Structure-fit-reward loop
**来源**：https://arxiv.org/pdf/2609.14260v1  
**实际版本**：2609.14260v1  
**精确定位**：PDF physical page 3, derived page-text lines 39-44 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_9b011afe59d4ab6e96`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Active channels
**来源**：https://arxiv.org/pdf/2609.14260v1  
**实际版本**：2609.14260v1  
**精确定位**：PDF physical page 8, derived page-text lines 83-98 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_9b011afe59d4ab6e96`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · NRMSE evaluation
**来源**：https://arxiv.org/pdf/2609.14260v1  
**实际版本**：2609.14260v1  
**精确定位**：PDF physical page 7, derived page-text lines 43-52 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_9b011afe59d4ab6e96`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Simulation and identifiability
**来源**：https://arxiv.org/pdf/2609.14260v1  
**实际版本**：2609.14260v1  
**精确定位**：PDF physical page 10, derived page-text lines 13-39 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_9b011afe59d4ab6e96`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- One simulated inverter, clean data, two operating points. Independent parameter fits can favor physically wrong structures; terminal measurements do not uniquely identify internals, and stability/passivity constraints are absent.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_9b011afe59d4ab6e96` · Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification · 2609.14260v1
  - https://arxiv.org/pdf/2609.14260v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Recovery and exact parameters uncertified.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_9b011afe59d4ab6e96 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
