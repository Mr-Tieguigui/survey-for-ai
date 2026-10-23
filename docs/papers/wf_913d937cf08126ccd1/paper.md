# SrDetection: A Self-Referential Framework for Data Leakage Detection in Code Large Language Models

> 评测方法/测量科学 · 2026 · `wf_913d937cf08126ccd1`

**作者**：Shuaimin Li, Liyang Fan, Zeyang Li, Zhuoyue Wan, Yufang Lin, Shiwen Ni, Feiteng Fang, Hamid Alinejad-Rokny, Yuanfeng Song, Kun Jing, Chen Jason Zhang, Min Yang  
**原文**：https://arxiv.org/abs/2606.29815  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SrDetection evaluates a code sample relative to semantics-preserving variants, using original-sample perplexity rank in gray-box mode or output-overlap rank in black-box mode to detect possible memorization without an external reference threshold. Retained as evaluation-validity background for code-agent/RSI benchmarks: leakage detection helps bound performance evidence, not an RSI mechanism.

### 与 RSI 的具体关系

- Retained as evaluation-validity background for code-agent/RSI benchmarks: leakage detection helps bound performance evidence, not an RSI mechanism.

## 2. 论文的核心内容与贡献

### role:b570_11_role_wf_913d937cf08126ccd1
SrDetection evaluates a code sample relative to semantics-preserving variants, using original-sample perplexity rank in gray-box mode or output-overlap rank in black-box mode to detect possible memorization without an external reference threshold.

**适用版本**：arXiv:2606.29815v1；**原文定位**：Sample-level leakage objective; PDF physical page 3, derived page-text lines 127-140 (one-based local extraction, not web-tool lines)；Self-relative decision algorithm; PDF physical page 4, derived page-text lines 1-28 (one-based local extraction, not web-tool lines)；Execution-validated test variants; PDF physical page 4, derived page-text lines 47-53 (one-based local extraction, not web-tool lines)；Black-box generation-overlap score; PDF physical page 4, derived page-text lines 105-118 (one-based local extraction, not web-tool lines)；Filtered controlled leakage testbed; PDF physical page 5, derived page-text lines 23-42 (one-based local extraction, not web-tool lines)；Variant and black-box limitations; PDF physical page 9, derived page-text lines 5-16 (one-based local extraction, not web-tool lines)；Strict decision versus algorithmic equality; PDF physical page 5, derived page-text lines 3-17 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Sample-level leakage labels and accuracy/precision/recall/F1; no capability-improving successor.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_11_ev_wf_913d937cf08126ccd1`**：SrDetection evaluates a code sample relative to semantics-preserving variants, using original-sample perplexity rank in gray-box mode or output-overlap rank in black-box mode to detect possible memorization without an external reference threshold.
  - 来源版本：arXiv:2606.29815v1；定位：Sample-level leakage objective; PDF physical page 3, derived page-text lines 127-140 (one-based local extraction, not web-tool lines)；Self-relative decision algorithm; PDF physical page 4, derived page-text lines 1-28 (one-based local extraction, not web-tool lines)；Execution-validated test variants; PDF physical page 4, derived page-text lines 47-53 (one-based local extraction, not web-tool lines)；Black-box generation-overlap score; PDF physical page 4, derived page-text lines 105-118 (one-based local extraction, not web-tool lines)；Filtered controlled leakage testbed; PDF physical page 5, derived page-text lines 23-42 (one-based local extraction, not web-tool lines)；Variant and black-box limitations; PDF physical page 9, derived page-text lines 5-16 (one-based local extraction, not web-tool lines)；Strict decision versus algorithmic equality; PDF physical page 5, derived page-text lines 3-17 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Sample-level leakage objective
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 3, derived page-text lines 127-140 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Self-relative decision algorithm
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 4, derived page-text lines 1-28 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · Execution-validated test variants
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 4, derived page-text lines 47-53 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 机制 / 定义 · Black-box generation-overlap score
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 4, derived page-text lines 105-118 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 机制 / 定义 · Filtered controlled leakage testbed
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 5, derived page-text lines 23-42 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · Variant and black-box limitations
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 9, derived page-text lines 5-16 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 7 · 限制 · Strict decision versus algorithmic equality
**来源**：https://arxiv.org/pdf/2606.29815v1  
**实际版本**：arXiv:2606.29815v1  
**精确定位**：PDF physical page 5, derived page-text lines 3-17 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_913d937cf08126ccd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Detection depends on variant diversity and semantics preservation; large/instruction-tuned models may mask black-box output differences. Self-reference here is within-sample contrast, not agent self-modification. Algorithm 1 uses equality to the extremum while the figure uses strict inequalities; tie handling is not certified. Controlled testbed filters original-easiest samples before a train/test split and mixes continued pretraining; its held-out-label/reporting interpretation needs targeted review before numerical results are admitted.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_11_src_wf_913d937cf08126ccd1` · SrDetection: A Self-Referential Framework for Data Leakage Detection in Code Large Language Models · arXiv:2606.29815v1
  - https://arxiv.org/pdf/2606.29815v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Tie handling conflicts between Figure 1 strict extrema and Algorithm 1 extremum equality; numerical classification behavior pending.
- Controlled testbed reports held-out test subset after training-subset continued pretraining; numerical-label accounting needs root review.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_913d937cf08126ccd1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
