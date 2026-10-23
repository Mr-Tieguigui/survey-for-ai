# Adaptive Recursive Cognition (ARC): A Reproducible Architecture for Multi-Loop Stabilization, Self-Improvement, and Token-Level Control in Language Models

> 综合系统/智能体 · 2026 · `wf_414fa04971bca883fd`

**作者**：Logan Matthew Napolitano  
**原文**：https://doi.org/10.5281/zenodo.18342791  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Adaptive Recursive Cognition: A Reproducible Architecture for Multi-Loop Language Model Self-Stabilization。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
This ARC technical reference defines reversible micro-training from self-generated, frozen-judge-scored responses, with quality/canary rollback checks. A fourth loop diagnoses tokenization stress, proposes deltas, re-encodes data, micro-trains and admits only deltas improving specified stability/efficiency criteria. Direct bounded RSI bridge: feedback updates weights and tokenizer state used for future generation, with rollback and fixed measurement rules. It does not certify unbounded improvement or autonomous redesign of the entire learning process.

### 与 RSI 的具体关系

- Direct bounded RSI bridge: feedback updates weights and tokenizer state used for future generation, with rollback and fixed measurement rules. It does not certify unbounded improvement or autonomous redesign of the entire learning process.

## 2. 论文的核心内容与贡献

### role:b570_10_role_wf_414fa04971bca883fd
This ARC technical reference defines reversible micro-training from self-generated, frozen-judge-scored responses, with quality/canary rollback checks. A fourth loop diagnoses tokenization stress, proposes deltas, re-encodes data, micro-trains and admits only deltas improving specified stability/efficiency criteria.

**适用版本**：Zenodo 18342792；**原文定位**：micro-training commit/rollback protocol; PDF physical page 14, derived page-text lines 4-15 (one-based local extraction, not web-tool lines)；tokenizer delta loop and criteria; PDF physical page 19, derived page-text lines 4-23 (one-based local extraction, not web-tool lines)；scale/domain and automation limits; PDF physical page 26, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 系统架构、组件与更新过程
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Weighted quality/canary metrics plus tokenizer stability/efficiency; documented hardware/defaults are not promoted to verified experimental configurations.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_10_ev_wf_414fa04971bca883fd`**：This ARC technical reference defines reversible micro-training from self-generated, frozen-judge-scored responses, with quality/canary rollback checks. A fourth loop diagnoses tokenization stress, proposes deltas, re-encodes data, micro-trains and admits only deltas improving specified stability/efficiency criteria.
  - 来源版本：Zenodo 18342792；定位：micro-training commit/rollback protocol; PDF physical page 14, derived page-text lines 4-15 (one-based local extraction, not web-tool lines)；tokenizer delta loop and criteria; PDF physical page 19, derived page-text lines 4-23 (one-based local extraction, not web-tool lines)；scale/domain and automation limits; PDF physical page 26, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · micro-training commit/rollback protocol
**来源**：https://zenodo.org/api/records/18342792/files/ARC_Technical_Specification_v1%20(1).pdf/content  
**实际版本**：Zenodo 18342792  
**精确定位**：PDF physical page 14, derived page-text lines 4-15 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_414fa04971bca883fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · tokenizer delta loop and criteria
**来源**：https://zenodo.org/api/records/18342792/files/ARC_Technical_Specification_v1%20(1).pdf/content  
**实际版本**：Zenodo 18342792  
**精确定位**：PDF physical page 19, derived page-text lines 4-23 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_414fa04971bca883fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · scale/domain and automation limits
**来源**：https://zenodo.org/api/records/18342792/files/ARC_Technical_Specification_v1%20(1).pdf/content  
**实际版本**：Zenodo 18342792  
**精确定位**：PDF physical page 26, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_414fa04971bca883fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The documented domain is 8B English technical/reasoning tasks; scaling, multimodal behavior and full tokenizer-loop automation remain open. The micro-training commit inequality allows a declared nondegradation tolerance, so a commit is not necessarily a strict capability gain.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_10_src_wf_414fa04971bca883fd` · Adaptive Recursive Cognition: A Reproducible Architecture for Multi-Loop Language Model Self-Stabilization · Zenodo 18342792
  - https://zenodo.org/api/records/18342792/files/ARC_Technical_Specification_v1%20(1).pdf/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_414fa04971bca883fd --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
