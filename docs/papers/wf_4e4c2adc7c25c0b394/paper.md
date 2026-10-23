# Towards Strategy-Level RSI for Skill-Augmented Agents: Learning When to Reuse Skills from Execution Feedback

> 方法论文 · 2026 · `wf_4e4c2adc7c25c0b394`

**作者**：Shuang Guo, Xiaobo Sui, Fei Jiang, Ruixin Li, Manxiang Li, Rong Li, Ziyang Ou  
**原文**：https://arxiv.org/abs/2609.26863  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：SkillApt: Learning When to Activate Agent Skills from Counterfactual Evidence。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
SkillApt holds skill content fixed and accumulates matched WITH/WITHOUT evidence to revise a state-conditioned LOAD/ABSTAIN boundary. Frozen v1 scoring uses correctness changes and maps correctness ties to 0.5. Bounded strategy-level RSI changes later activation boundaries from execution evidence while procedures/models stay fixed. Cohort title differs from cached v1 heading; both are retained with matching arXiv identity.

### 与 RSI 的具体关系

- Bounded strategy-level RSI changes later activation boundaries from execution evidence while procedures/models stay fixed. Cohort title differs from cached v1 heading; both are retained with matching arXiv identity.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_4e4c2adc7c25c0b394
SkillApt holds skill content fixed and accumulates matched WITH/WITHOUT evidence to revise a state-conditioned LOAD/ABSTAIN boundary. Frozen v1 scoring uses correctness changes and maps correctness ties to 0.5.

**适用版本**：2609.26863v1；**原文定位**：Controller and utility; PDF physical page 2, derived page-text lines 54-86 (one-based local extraction, not web-tool lines)；Matched evidence and cost distinction; PDF physical page 2, derived page-text lines 93-120 (one-based local extraction, not web-tool lines)；Retrieval, transfer and split limits; PDF physical page 7, derived page-text lines 59-90 (one-based local extraction, not web-tool lines)；v1 scoring interpretation; PDF physical page 3, derived page-text lines 21-59 (one-based local extraction, not web-tool lines)；Metrics and censoring; PDF physical page 5, derived page-text lines 4-24 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Matched skill/state execution pair changes target-skill availability alone. Official correctness precedes tie costs, but v1 collapses both cost-tie classes. Main confirmatory SRA analysis has 111 complete states after two censored failures; measures accuracy, activation/avoidance and costs.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_4e4c2adc7c25c0b394`**：SkillApt holds skill content fixed and accumulates matched WITH/WITHOUT evidence to revise a state-conditioned LOAD/ABSTAIN boundary. Frozen v1 scoring uses correctness changes and maps correctness ties to 0.5.
  - 来源版本：2609.26863v1；定位：Controller and utility; PDF physical page 2, derived page-text lines 54-86 (one-based local extraction, not web-tool lines)；Matched evidence and cost distinction; PDF physical page 2, derived page-text lines 93-120 (one-based local extraction, not web-tool lines)；Retrieval, transfer and split limits; PDF physical page 7, derived page-text lines 59-90 (one-based local extraction, not web-tool lines)；v1 scoring interpretation; PDF physical page 3, derived page-text lines 21-59 (one-based local extraction, not web-tool lines)；Metrics and censoring; PDF physical page 5, derived page-text lines 4-24 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Controller and utility
**来源**：https://arxiv.org/pdf/2609.26863v1  
**实际版本**：2609.26863v1  
**精确定位**：PDF physical page 2, derived page-text lines 54-86 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4e4c2adc7c25c0b394`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Matched evidence and cost distinction
**来源**：https://arxiv.org/pdf/2609.26863v1  
**实际版本**：2609.26863v1  
**精确定位**：PDF physical page 2, derived page-text lines 93-120 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4e4c2adc7c25c0b394`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · v1 scoring interpretation
**来源**：https://arxiv.org/pdf/2609.26863v1  
**实际版本**：2609.26863v1  
**精确定位**：PDF physical page 3, derived page-text lines 21-59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4e4c2adc7c25c0b394`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 测量 / 结果 · Metrics and censoring
**来源**：https://arxiv.org/pdf/2609.26863v1  
**实际版本**：2609.26863v1  
**精确定位**：PDF physical page 5, derived page-text lines 4-24 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4e4c2adc7c25c0b394`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Retrieval, transfer and split limits
**来源**：https://arxiv.org/pdf/2609.26863v1  
**实际版本**：2609.26863v1  
**精确定位**：PDF physical page 7, derived page-text lines 59-90 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4e4c2adc7c25c0b394`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Final skill identities are not held out; evidence is sparse, two domains/external validation remain blocked, and cost-tie effects are absent from the v1 estimator. The activation score is not a calibrated causal effect; separately fitted spreadsheet diagnostics do not establish policy transfer.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_4e4c2adc7c25c0b394` · SkillApt: Learning When to Activate Agent Skills from Counterfactual Evidence · 2609.26863v1
  - https://arxiv.org/pdf/2609.26863v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Preserve title variant; do not infer a separate work or latest version.
- No causal calibration or configuration certification.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4e4c2adc7c25c0b394 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
