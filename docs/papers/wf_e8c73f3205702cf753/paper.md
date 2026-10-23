# Multi-agent harness built for recursive self-improvement that orchestrates built-in and third-party agents as task DAGs; an experimental Curator rewrites each agent's Memory, Planning, Capability, and Action strategy modules and installs only verified changes

> 综合系统/智能体 · 年份待核 · `wf_e8c73f3205702cf753`

**作者**：未登记，待核  
**原文**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Raven: The Harness of Harnesses for Composable Agentic Intelligence。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
Raven exposes Memory, Planning, Capability and Action strategies around a frozen Task Agent. An Evolver diagnoses failures and proposes restricted patches; screened survivors receive training evaluation and archive competition, and the training-selected harness is frozen before sealed testing. Retained as bounded persistent harness adaptation and composition; fixed model/evaluator do not eliminate the feedback loop and do not establish stronger recursive improvers.

### 与 RSI 的具体关系

- Retained as bounded persistent harness adaptation and composition; fixed model/evaluator do not eliminate the feedback loop and do not establish stronger recursive improvers.

## 2. 论文的核心内容与贡献

### role:b570_11_role_wf_e8c73f3205702cf753
Raven exposes Memory, Planning, Capability and Action strategies around a frozen Task Agent. An Evolver diagnoses failures and proposes restricted patches; screened survivors receive training evaluation and archive competition, and the training-selected harness is frozen before sealed testing.

**适用版本**：GitHub Raven release tech-report-v1 / technical-report.pdf；**原文定位**：Frozen-model harness loop; PDF physical page 24, derived page-text lines 3-11 (one-based local extraction, not web-tool lines)；Editable policy and survivor selection; PDF physical page 24, derived page-text lines 47-66 (one-based local extraction, not web-tool lines)；Immutable kernel and cumulative patch boundary; PDF physical page 25, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)；Training/test measurement contract; PDF physical page 25, derived page-text lines 43-48 (one-based local extraction, not web-tool lines)；Finite utility and evaluation reuse limits; PDF physical page 26, derived page-text lines 1-17 (one-based local extraction, not web-tool lines)；No weight update and cost boundary; PDF physical page 26, derived page-text lines 24-36 (one-based local extraction, not web-tool lines)；Reported external experiments; PDF physical page 45, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 系统架构、组件与更新过程
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Per-task mean of K scored attempts, then equal task average; mean per-attempt success is not probability of at least one success.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_11_ev_wf_e8c73f3205702cf753`**：Raven exposes Memory, Planning, Capability and Action strategies around a frozen Task Agent. An Evolver diagnoses failures and proposes restricted patches; screened survivors receive training evaluation and archive competition, and the training-selected harness is frozen before sealed testing.
  - 来源版本：GitHub Raven release tech-report-v1 / technical-report.pdf；定位：Frozen-model harness loop; PDF physical page 24, derived page-text lines 3-11 (one-based local extraction, not web-tool lines)；Editable policy and survivor selection; PDF physical page 24, derived page-text lines 47-66 (one-based local extraction, not web-tool lines)；Immutable kernel and cumulative patch boundary; PDF physical page 25, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)；Training/test measurement contract; PDF physical page 25, derived page-text lines 43-48 (one-based local extraction, not web-tool lines)；Finite utility and evaluation reuse limits; PDF physical page 26, derived page-text lines 1-17 (one-based local extraction, not web-tool lines)；No weight update and cost boundary; PDF physical page 26, derived page-text lines 24-36 (one-based local extraction, not web-tool lines)；Reported external experiments; PDF physical page 45, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Frozen-model harness loop
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 24, derived page-text lines 3-11 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Editable policy and survivor selection
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 24, derived page-text lines 47-66 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · Immutable kernel and cumulative patch boundary
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 25, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 机制 / 定义 · Training/test measurement contract
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 25, derived page-text lines 43-48 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Finite utility and evaluation reuse limits
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 26, derived page-text lines 1-17 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · No weight update and cost boundary
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 26, derived page-text lines 24-36 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 7 · 限制 · Reported external experiments
**来源**：https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf  
**实际版本**：GitHub Raven release tech-report-v1 / technical-report.pdf  
**精确定位**：PDF physical page 45, derived page-text lines 26-42 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_e8c73f3205702cf753`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The evaluator, bookkeeping and required interfaces remain protected; weights do not change. Archive utility reuses designated full-training logs only in a stable environment; environment changes require common reevaluation. Finite search provides no global optimum. Section 7.2 reports published HarnessBank experiments rather than an independently replicated Raven end-to-end evolution result.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_11_src_wf_e8c73f3205702cf753` · Raven: The Harness of Harnesses for Composable Agentic Intelligence · GitHub Raven release tech-report-v1 / technical-report.pdf
  - https://github.com/EverMind-AI/Raven/releases/download/tech-report-v1/technical-report.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- authors
- year
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e8c73f3205702cf753 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
