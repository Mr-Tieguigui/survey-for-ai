# Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer

> 方法论文 · 2026 · `wf_4f46d826ea654423af`

**作者**：Qiankai Xu  
**原文**：https://arxiv.org/abs/2609.38372  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The frozen model uses the same harness for solving and proposing code/notes changes; raw trajectories, scores and prior update records guide revision. Acceptance checks engineering validity including a mock task run rather than guaranteed score gain. Direct harness-level RSI: the updated harness runs both later task solving and later modification sessions. Fixed weights do not eliminate persistent feedback through code/notes.

### 与 RSI 的具体关系

- Direct harness-level RSI: the updated harness runs both later task solving and later modification sessions. Fixed weights do not eliminate persistent feedback through code/notes.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_4f46d826ea654423af
The frozen model uses the same harness for solving and proposing code/notes changes; raw trajectories, scores and prior update records guide revision. Acceptance checks engineering validity including a mock task run rather than guaranteed score gain.

**适用版本**：2609.38372v1；**原文定位**：Harness state and grader; PDF physical page 5, derived page-text lines 46-56 (one-based local extraction, not web-tool lines)；Same agent and engineering checks; PDF physical page 6, derived page-text lines 3-39 (one-based local extraction, not web-tool lines)；Single-model and stochastic-chain limits; PDF physical page 12, derived page-text lines 39-46 (one-based local extraction, not web-tool lines)；Multi-task batching; PDF physical page 6, derived page-text lines 40-45 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Task runs yield benchmark-specific score and grader output. Stage-one batches draw 12 unused tasks from each of five training sets with disjoint held-out sets. Engineering acceptance differs from downstream capability improvement.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_4f46d826ea654423af`**：The frozen model uses the same harness for solving and proposing code/notes changes; raw trajectories, scores and prior update records guide revision. Acceptance checks engineering validity including a mock task run rather than guaranteed score gain.
  - 来源版本：2609.38372v1；定位：Harness state and grader; PDF physical page 5, derived page-text lines 46-56 (one-based local extraction, not web-tool lines)；Same agent and engineering checks; PDF physical page 6, derived page-text lines 3-39 (one-based local extraction, not web-tool lines)；Single-model and stochastic-chain limits; PDF physical page 12, derived page-text lines 39-46 (one-based local extraction, not web-tool lines)；Multi-task batching; PDF physical page 6, derived page-text lines 40-45 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Harness state and grader
**来源**：https://arxiv.org/pdf/2609.38372v1  
**实际版本**：2609.38372v1  
**精确定位**：PDF physical page 5, derived page-text lines 46-56 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4f46d826ea654423af`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Same agent and engineering checks
**来源**：https://arxiv.org/pdf/2609.38372v1  
**实际版本**：2609.38372v1  
**精确定位**：PDF physical page 6, derived page-text lines 3-39 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4f46d826ea654423af`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Multi-task batching
**来源**：https://arxiv.org/pdf/2609.38372v1  
**实际版本**：2609.38372v1  
**精确定位**：PDF physical page 6, derived page-text lines 40-45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4f46d826ea654423af`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Single-model and stochastic-chain limits
**来源**：https://arxiv.org/pdf/2609.38372v1  
**实际版本**：2609.38372v1  
**精确定位**：PDF physical page 12, derived page-text lines 39-46 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_4f46d826ea654423af`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Only one strong model and one new continual-training domain are studied. Independent evolution-chain variation remains unestimated; repeated task evaluations do not replace search-chain replication.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_4f46d826ea654423af` · Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer · 2609.38372v1
  - https://arxiv.org/pdf/2609.38372v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No claim that each iteration improves score or certifies a capability gain.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4f46d826ea654423af --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
