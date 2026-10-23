# Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation

> 方法论文 · 2026 · `wf_3d9bbfc26722916509`

**作者**：Rui Wang, Ruijie Wang, Bo Chen, Jiangxuan Long, Yingyu Liang  
**原文**：https://arxiv.org/abs/2609.36695  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
INFLOW couples certainty-calibrated retrieval, semantic belief-shift selection and on-policy distillation from a retrieval-conditioned EMA teacher; retained examples update the student and teacher signals are recomputed. The introduction explicitly connects internal-state diagnosis, retrieval and selective distillation to progress toward RSI (PDF p.2 lines 7-25). The supported object is a bounded model/data update mechanism.

### 与 RSI 的具体关系

- The introduction explicitly connects internal-state diagnosis, retrieval and selective distillation to progress toward RSI (PDF p.2 lines 7-25). The supported object is a bounded model/data update mechanism.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_3d9bbfc26722916509
INFLOW couples certainty-calibrated retrieval, semantic belief-shift selection and on-policy distillation from a retrieval-conditioned EMA teacher; retained examples update the student and teacher signals are recomputed.

**适用版本**：2609.36695v1；**原文定位**：Problem and three-stage iteration; PDF physical page 4, derived page-text lines 23-31 (one-based local extraction, not web-tool lines)；Selection and EMA distillation; PDF physical page 6, derived page-text lines 16-31 (one-based local extraction, not web-tool lines)；Explicit RSI bridge; PDF physical page 2, derived page-text lines 7-25 (one-based local extraction, not web-tool lines)；Conditional convergence; PDF physical page 11, derived page-text lines 1-7 (one-based local extraction, not web-tool lines)；Transfer need not repair labels; PDF physical page 11, derived page-text lines 41-47 (one-based local extraction, not web-tool lines)；Question-level metrics; PDF physical page 7, derived page-text lines 29-32 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Test question is the unit. Avg@3 is mean accuracy over three rollout indices and SD their standard deviation; Maj@3 is majority-vote answer accuracy. Runtime includes retrieval, generation, selection and updates.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_3d9bbfc26722916509`**：INFLOW couples certainty-calibrated retrieval, semantic belief-shift selection and on-policy distillation from a retrieval-conditioned EMA teacher; retained examples update the student and teacher signals are recomputed.
  - 来源版本：2609.36695v1；定位：Problem and three-stage iteration; PDF physical page 4, derived page-text lines 23-31 (one-based local extraction, not web-tool lines)；Selection and EMA distillation; PDF physical page 6, derived page-text lines 16-31 (one-based local extraction, not web-tool lines)；Explicit RSI bridge; PDF physical page 2, derived page-text lines 7-25 (one-based local extraction, not web-tool lines)；Conditional convergence; PDF physical page 11, derived page-text lines 1-7 (one-based local extraction, not web-tool lines)；Transfer need not repair labels; PDF physical page 11, derived page-text lines 41-47 (one-based local extraction, not web-tool lines)；Question-level metrics; PDF physical page 7, derived page-text lines 29-32 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Problem and three-stage iteration
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 4, derived page-text lines 23-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Selection and EMA distillation
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 6, derived page-text lines 16-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · Explicit RSI bridge
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 2, derived page-text lines 7-25 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 测量 / 结果 · Question-level metrics
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 7, derived page-text lines 29-32 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Conditional convergence
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 11, derived page-text lines 1-7 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · Transfer need not repair labels
**来源**：https://arxiv.org/pdf/2609.36695v1  
**实际版本**：2609.36695v1  
**精确定位**：PDF physical page 11, derived page-text lines 41-47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_3d9bbfc26722916509`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Information transfer does not ensure correction: belief shifts can propagate wrong answers and later training can degrade a weak starting model. Local convergence requires smoothness and a PL condition, not an unconditional RSI guarantee.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_3d9bbfc26722916509` · Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation · 2609.36695v1
  - https://arxiv.org/pdf/2609.36695v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3d9bbfc26722916509 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
