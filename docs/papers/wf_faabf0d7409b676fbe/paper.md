# Exploring the Limits of End-to-End Feature-Affinity Propagation for Single-Point Supervised Infrared Small Target Detection

> 背景/相邻基础 · 2026 · `wf_faabf0d7409b676fbe`

**作者**：Qiancheng Zhou, Wenhua Zhang  
**原文**：https://arxiv.org/abs/2605.00722  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
GSACP studies bounded self-coupled supervision: current features produce affinity targets training the same representation, with propagation drift via feature distortion. SIRST3/MSDA single-variable audits span 116 logged variants; a code-execution LLM is bookkeeping auditor. Cross-dataset tests use source checkpoints without target fine-tuning and are zero-shot transfer. Optional RSI mechanism background: self-produced target/representation co-adaptation illustrates evaluator/target feedback drift (Eq.7–8). Explicit analogy, not recursive meta-improvement evidence.

### 与 RSI 的具体关系

- Optional RSI mechanism background: self-produced target/representation co-adaptation illustrates evaluator/target feedback drift (Eq.7–8). Explicit analogy, not recursive meta-improvement evidence.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_faabf0d7409b676fbe
GSACP studies bounded self-coupled supervision: current features produce affinity targets training the same representation, with propagation drift via feature distortion. SIRST3/MSDA single-variable audits span 116 logged variants; a code-execution LLM is bookkeeping auditor. Cross-dataset tests use source checkpoints without target fine-tuning and are zero-shot transfer.

**适用版本**：2605.00722v1；**原文定位**：§3.3 Propagation drift; PDF p3; derived page text lines 13–47 (one-based local extraction, not web-tool lines)；§5.1 Ablation protocol; PDF p4; derived page text lines 14–26 (one-based local extraction, not web-tool lines)；§5.4 Transfer protocol; PDF p9; derived page text lines 1–18 (one-based local extraction, not web-tool lines)；§5.1 Checkpoint boundary; PDF p4; derived page text lines 7–13 (one-based local extraction, not web-tool lines)；§6 Scope/limits; PDF p9; derived page text lines 34–51 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_faabf0d7409b676fbe`**：GSACP studies bounded self-coupled supervision: current features produce affinity targets training the same representation, with propagation drift via feature distortion. SIRST3/MSDA single-variable audits span 116 logged variants; a code-execution LLM is bookkeeping auditor. Cross-dataset tests use source checkpoints without target fine-tuning and are zero-shot transfer.
  - 来源版本：2605.00722v1；定位：§3.3 Propagation drift; PDF p3; derived page text lines 13–47 (one-based local extraction, not web-tool lines)；§5.1 Ablation protocol; PDF p4; derived page text lines 14–26 (one-based local extraction, not web-tool lines)；§5.4 Transfer protocol; PDF p9; derived page text lines 1–18 (one-based local extraction, not web-tool lines)；§5.1 Checkpoint boundary; PDF p4; derived page text lines 7–13 (one-based local extraction, not web-tool lines)；§6 Scope/limits; PDF p9; derived page text lines 34–51 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §3.3 Propagation drift
**来源**：https://arxiv.org/pdf/2605.00722v1  
**实际版本**：2605.00722v1  
**精确定位**：PDF p3; derived page text lines 13–47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_faabf0d7409b676fbe`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §5.1 Ablation protocol
**来源**：https://arxiv.org/pdf/2605.00722v1  
**实际版本**：2605.00722v1  
**精确定位**：PDF p4; derived page text lines 14–26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_faabf0d7409b676fbe`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §5.4 Transfer protocol
**来源**：https://arxiv.org/pdf/2605.00722v1  
**实际版本**：2605.00722v1  
**精确定位**：PDF p9; derived page text lines 1–18 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_faabf0d7409b676fbe`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · §5.1 Checkpoint boundary
**来源**：https://arxiv.org/pdf/2605.00722v1  
**实际版本**：2605.00722v1  
**精确定位**：PDF p4; derived page text lines 7–13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_faabf0d7409b676fbe`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §6 Scope/limits
**来源**：https://arxiv.org/pdf/2605.00722v1  
**实际版本**：2605.00722v1  
**精确定位**：PDF p9; derived page text lines 34–51 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_faabf0d7409b676fbe`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- This is infrared detector supervision, not an agent evolving its improvement operator. The ledger auditor leaves architecture, protocol and metrics fixed. Late-plateau reporting differs from peak selection; mask overlap trades against false alarms. Bounded feedback is real and is not denied because of a fixed optimizer.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_faabf0d7409b676fbe` · Exploring the Limits of End-to-End Feature-Affinity Propagation for Single-Point Supervised Infrared Small Target Detection · 2605.00722v1
  - https://arxiv.org/pdf/2605.00722v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_faabf0d7409b676fbe --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
