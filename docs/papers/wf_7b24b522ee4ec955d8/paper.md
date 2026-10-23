# MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis

> 方法论文 · 2026 · `wf_7b24b522ee4ec955d8`

**作者**：Lei Liu, Zhaokang Liang, Qingcheng Zeng, Chenda Duan, Lu Mi, Zhen Tan, Tianyu Liu  
**原文**：https://arxiv.org/abs/2609.36235  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
MERID preserves subject-target alignment through a checked adapter, searches whole recipe/predictor pipelines, and verifies incumbent replacement with development evidence and uncertainty margins; failed candidates can inform subsequent proposals. Persistent components, incumbent and revision history guide later pipeline proposals. Memory learning is a distinct optional channel, not a property of all reported runs.

### 与 RSI 的具体关系

- Persistent components, incumbent and revision history guide later pipeline proposals. Memory learning is a distinct optional channel, not a property of all reported runs.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_7b24b522ee4ec955d8
MERID preserves subject-target alignment through a checked adapter, searches whole recipe/predictor pipelines, and verifies incumbent replacement with development evidence and uncertainty margins; failed candidates can inform subsequent proposals.

**适用版本**：2609.36235v1；**原文定位**：Pipeline and alignment; PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)；Persistent update and unchanged incumbent; PDF physical page 7, derived page-text lines 21-31 (one-based local extraction, not web-tool lines)；Clinical limits; PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)；Optional versus main memory settings; PDF physical page 52, derived page-text lines 20-29 (one-based local extraction, not web-tool lines)；Task protocol and final ensemble; PDF physical page 7, derived page-text lines 34-48 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Candidate pipeline under fixed task adapter/splits/metrics with subject-preserving bootstrap. Metrics include MPDD track score, Macro-F1 and PHQ CCC; final test prediction can ensemble up to five candidates, distinct from in-loop selection.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_7b24b522ee4ec955d8`**：MERID preserves subject-target alignment through a checked adapter, searches whole recipe/predictor pipelines, and verifies incumbent replacement with development evidence and uncertainty margins; failed candidates can inform subsequent proposals.
  - 来源版本：2609.36235v1；定位：Pipeline and alignment; PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)；Persistent update and unchanged incumbent; PDF physical page 7, derived page-text lines 21-31 (one-based local extraction, not web-tool lines)；Clinical limits; PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)；Optional versus main memory settings; PDF physical page 52, derived page-text lines 20-29 (one-based local extraction, not web-tool lines)；Task protocol and final ensemble; PDF physical page 7, derived page-text lines 34-48 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Pipeline and alignment
**来源**：https://arxiv.org/pdf/2609.36235v1  
**实际版本**：2609.36235v1  
**精确定位**：PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7b24b522ee4ec955d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Persistent update and unchanged incumbent
**来源**：https://arxiv.org/pdf/2609.36235v1  
**实际版本**：2609.36235v1  
**精确定位**：PDF physical page 7, derived page-text lines 21-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7b24b522ee4ec955d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Task protocol and final ensemble
**来源**：https://arxiv.org/pdf/2609.36235v1  
**实际版本**：2609.36235v1  
**精确定位**：PDF physical page 7, derived page-text lines 34-48 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7b24b522ee4ec955d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Clinical limits
**来源**：https://arxiv.org/pdf/2609.36235v1  
**实际版本**：2609.36235v1  
**精确定位**：PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7b24b522ee4ec955d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Optional versus main memory settings
**来源**：https://arxiv.org/pdf/2609.36235v1  
**实际版本**：2609.36235v1  
**精确定位**：PDF physical page 52, derived page-text lines 20-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7b24b522ee4ec955d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Acted-emotion tasks do not establish clinical diagnostic validity. Optional evolving research memory is disabled in the five-seed main benchmark/module ablations and is not integrated in the separate MPDD-2026 path.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_7b24b522ee4ec955d8` · MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis · 2609.36235v1
  - https://arxiv.org/pdf/2609.36235v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Review rounds are not accepted replacements; main results do not certify optional-memory behavior.
- All clinical/benchmark effects remain author reports.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7b24b522ee4ec955d8 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
