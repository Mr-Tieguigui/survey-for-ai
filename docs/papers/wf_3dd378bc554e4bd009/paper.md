# The Provably Aligned AI Core: A Deterministic Safety Wrapper for Self-Improving Agents

> 实证/审计/复现 · 2026 · `wf_3dd378bc554e4bd009`

**作者**：Shashank Kumar  
**原文**：https://doi.org/10.5281/zenodo.20847331  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：PAAC v8.0: Bounded Model Checking as a Safety Wrapper for Self-Modifying Agents, and Two Decomposition Attacks Against It。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
The actual v8.0 paper specifies bounded-model-checking acceptance for proposed SIL code replacements and reports that its own earlier safety claims were defeated by a vacuous-precondition bypass. A satisfiability precheck closes that bypass, while two hand-written decomposition schemas still produce accepted unsafe compositions because callers and callee obligations are not jointly reverified. This is a bounded wrapper audit, not proof of aligned RSI. Direct empirical counterexample/audit of self-modification verification; no safe-RSI guarantee or autonomous capability improvement admitted.

### 与 RSI 的具体关系

- Direct empirical counterexample/audit of self-modification verification; no safe-RSI guarantee or autonomous capability improvement admitted.

## 2. 论文的核心内容与贡献

### role:b570_04_role_wf_3dd378bc554e4bd009
The actual v8.0 paper specifies bounded-model-checking acceptance for proposed SIL code replacements and reports that its own earlier safety claims were defeated by a vacuous-precondition bypass. A satisfiability precheck closes that bypass, while two hand-written decomposition schemas still produce accepted unsafe compositions because callers and callee obligations are not jointly reverified. This is a bounded wrapper audit, not proof of aligned RSI.

**适用版本**：10.5281/zenodo.22728775；**原文定位**：3.4 Bounded verification query and decision; PDF p4; derived text lines 40-54 (one-based local extraction, not web-tool lines)；5 Vacuous bypass and limited fix; PDF p6; derived text lines 12-26 (one-based local extraction, not web-tool lines)；6.4 Bounds of decomposition evidence; PDF p8; derived text lines 1-26 (one-based local extraction, not web-tool lines)；9.1 Unguarded composition; PDF p11; derived text lines 86-92 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_04_ev_wf_3dd378bc554e4bd009`**：The actual v8.0 paper specifies bounded-model-checking acceptance for proposed SIL code replacements and reports that its own earlier safety claims were defeated by a vacuous-precondition bypass. A satisfiability precheck closes that bypass, while two hand-written decomposition schemas still produce accepted unsafe compositions because callers and callee obligations are not jointly reverified. This is a bounded wrapper audit, not proof of aligned RSI.
  - 来源版本：10.5281/zenodo.22728775；定位：3.4 Bounded verification query and decision; PDF p4; derived text lines 40-54 (one-based local extraction, not web-tool lines)；5 Vacuous bypass and limited fix; PDF p6; derived text lines 12-26 (one-based local extraction, not web-tool lines)；6.4 Bounds of decomposition evidence; PDF p8; derived text lines 1-26 (one-based local extraction, not web-tool lines)；9.1 Unguarded composition; PDF p11; derived text lines 86-92 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · 3.4 Bounded verification query and decision
**来源**：https://zenodo.org/api/records/22728775/files/paac-v8.pdf/content  
**实际版本**：10.5281/zenodo.22728775  
**精确定位**：PDF p4; derived text lines 40-54 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_3dd378bc554e4bd009`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · 5 Vacuous bypass and limited fix
**来源**：https://zenodo.org/api/records/22728775/files/paac-v8.pdf/content  
**实际版本**：10.5281/zenodo.22728775  
**精确定位**：PDF p6; derived text lines 12-26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_3dd378bc554e4bd009`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · 6.4 Bounds of decomposition evidence
**来源**：https://zenodo.org/api/records/22728775/files/paac-v8.pdf/content  
**实际版本**：10.5281/zenodo.22728775  
**精确定位**：PDF p8; derived text lines 1-26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_3dd378bc554e4bd009`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · 9.1 Unguarded composition
**来源**：https://zenodo.org/api/records/22728775/files/paac-v8.pdf/content  
**实际版本**：10.5281/zenodo.22728775  
**精确定位**：PDF p11; derived text lines 86-92 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_3dd378bc554e4bd009`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Two witnesses from three selected schemas are not an attack-surface estimate. SIL excludes real-code features, bounds are declared, preconditions remain agent-supplied, compiler gaps remain and the proof-carrying checker lacks differential comparison. The title change and v8.0 findings supersede any blanket “provably aligned” reading of the cohort title.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_04_src_wf_3dd378bc554e4bd009` · PAAC v8.0: Bounded Model Checking as a Safety Wrapper for Self-Modifying Agents, and Two Decomposition Attacks Against It · 10.5281/zenodo.22728775
  - https://zenodo.org/api/records/22728775/files/paac-v8.pdf/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No external replay of witnesses or independent soundness certification; remaining wrapper safety not established.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3dd378bc554e4bd009 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
