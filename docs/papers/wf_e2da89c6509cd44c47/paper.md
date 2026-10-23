# ARC: Decode-Time Behavioral Control and Guarded Self-Optimization in Large Language Models

> 方法论文 · 2026 · `wf_e2da89c6509cd44c47`

**作者**：Logan Matthew Napolitano  
**原文**：https://doi.org/10.5281/zenodo.18321444  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：ARC: Adaptive Recursive Cognition - Stable Self-Optimization of Language Models via Contrastive Hidden-State Control and Dense Response Training。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
ARC v2 describes bounded behavioral optimization using hidden-state repetition control, SFT/DPO/RL dense-response training and continuous checkpointing. Its guarded loop compares updated checkpoints on several heuristic quality metrics and rolls back unacceptable changes. Direct bounded model-update bridge: outputs and evaluation feedback control later weight/checkpoint state. Fixed metrics/training procedure constrain rather than erase the self-improvement loop.

### 与 RSI 的具体关系

- Direct bounded model-update bridge: outputs and evaluation feedback control later weight/checkpoint state. Fixed metrics/training procedure constrain rather than erase the self-improvement loop.

## 2. 论文的核心内容与贡献

### role:b570_09_role_wf_e2da89c6509cd44c47
ARC v2 describes bounded behavioral optimization using hidden-state repetition control, SFT/DPO/RL dense-response training and continuous checkpointing. Its guarded loop compares updated checkpoints on several heuristic quality metrics and rolls back unacceptable changes.

**适用版本**：Zenodo 18321445；**原文定位**：staged dense-response training; PDF physical page 7, derived page-text lines 11-19 (one-based local extraction, not web-tool lines)；paired checkpoint keep/rollback protocol; PDF physical page 8, derived page-text lines 38-43 (one-based local extraction, not web-tool lines)；scale/language/iteration and fixed-procedure boundary; PDF physical page 12, derived page-text lines 15-30 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Density/coherence/helpfulness/penalty scores and checkpoint-relative evaluation; iteration count and proxy quality are not sustained optimizer acceleration.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_09_ev_wf_e2da89c6509cd44c47`**：ARC v2 describes bounded behavioral optimization using hidden-state repetition control, SFT/DPO/RL dense-response training and continuous checkpointing. Its guarded loop compares updated checkpoints on several heuristic quality metrics and rolls back unacceptable changes.
  - 来源版本：Zenodo 18321445；定位：staged dense-response training; PDF physical page 7, derived page-text lines 11-19 (one-based local extraction, not web-tool lines)；paired checkpoint keep/rollback protocol; PDF physical page 8, derived page-text lines 38-43 (one-based local extraction, not web-tool lines)；scale/language/iteration and fixed-procedure boundary; PDF physical page 12, derived page-text lines 15-30 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · staged dense-response training
**来源**：https://zenodo.org/api/records/18321445/files/ARC_Technical_Report_Zenodo-2.pdf/content  
**实际版本**：Zenodo 18321445  
**精确定位**：PDF physical page 7, derived page-text lines 11-19 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_e2da89c6509cd44c47`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · paired checkpoint keep/rollback protocol
**来源**：https://zenodo.org/api/records/18321445/files/ARC_Technical_Report_Zenodo-2.pdf/content  
**实际版本**：Zenodo 18321445  
**精确定位**：PDF physical page 8, derived page-text lines 38-43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_e2da89c6509cd44c47`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · scale/language/iteration and fixed-procedure boundary
**来源**：https://zenodo.org/api/records/18321445/files/ARC_Technical_Report_Zenodo-2.pdf/content  
**实际版本**：Zenodo 18321445  
**精确定位**：PDF physical page 12, derived page-text lines 15-30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_e2da89c6509cd44c47`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Tested scope is 8B English models and a few stable iterations, with heuristic metrics and no human evaluation study. The author explicitly excludes architectural/training-process self-improvement and open-ended capability acquisition. Multi-metric evaluation is not accepted as a theorem eliminating reward hacking.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_09_src_wf_e2da89c6509cd44c47` · ARC: Adaptive Recursive Cognition - Stable Self-Optimization of Language Models via Contrastive Hidden-State Control and Dense Response Training · Zenodo 18321445
  - https://zenodo.org/api/records/18321445/files/ARC_Technical_Report_Zenodo-2.pdf/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Attachment header says Technical Report Version 2.0 / January 2025; retained as source text, not silently normalized to cohort date/title.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e2da89c6509cd44c47 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
