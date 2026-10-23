# Self Improvement via Fast Tree-search

> 方法论文 · 2026 · `wf_47bcd5ede204b7a80f`

**作者**：Xinghong Fu, Aravinth Kulanthaivelu, Yutaro Yamada  
**原文**：https://arxiv.org/abs/2609.19526  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SIFT maintains candidate harnesses, aggregates pairwise judge preferences into regularized Bradley-Terry strengths, and samples/queues candidates using judge rank, benchmark accuracy rank and visit count. Harness changes alter later agent execution and modification. Cheap judge signal guides bounded search rather than itself certifying improvement.

### 与 RSI 的具体关系

- Harness changes alter later agent execution and modification. Cheap judge signal guides bounded search rather than itself certifying improvement.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_47bcd5ede204b7a80f
SIFT maintains candidate harnesses, aggregates pairwise judge preferences into regularized Bradley-Terry strengths, and samples/queues candidates using judge rank, benchmark accuracy rank and visit count.

**适用版本**：2609.19526v1；**原文定位**：Recursive roles and archive search; PDF physical page 3, derived page-text lines 20-40 (one-based local extraction, not web-tool lines)；Judge inputs and comparisons; PDF physical page 4, derived page-text lines 4-17 (one-based local extraction, not web-tool lines)；Judge, ranking and integrity limits; PDF physical page 11, derived page-text lines 10-28 (one-based local extraction, not web-tool lines)；Search and final evaluation; PDF physical page 6, derived page-text lines 12-20 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Candidate implementation is the search unit. Pairwise wins/losses produce BT rank; a four-task gate and 50-task subset guide search, with full 225-task Polyglot final evaluation. Full set includes the search subset, so it is not task-disjoint generalization.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_47bcd5ede204b7a80f`**：SIFT maintains candidate harnesses, aggregates pairwise judge preferences into regularized Bradley-Terry strengths, and samples/queues candidates using judge rank, benchmark accuracy rank and visit count.
  - 来源版本：2609.19526v1；定位：Recursive roles and archive search; PDF physical page 3, derived page-text lines 20-40 (one-based local extraction, not web-tool lines)；Judge inputs and comparisons; PDF physical page 4, derived page-text lines 4-17 (one-based local extraction, not web-tool lines)；Judge, ranking and integrity limits; PDF physical page 11, derived page-text lines 10-28 (one-based local extraction, not web-tool lines)；Search and final evaluation; PDF physical page 6, derived page-text lines 12-20 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Recursive roles and archive search
**来源**：https://arxiv.org/pdf/2609.19526v1  
**实际版本**：2609.19526v1  
**精确定位**：PDF physical page 3, derived page-text lines 20-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_47bcd5ede204b7a80f`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Judge inputs and comparisons
**来源**：https://arxiv.org/pdf/2609.19526v1  
**实际版本**：2609.19526v1  
**精确定位**：PDF physical page 4, derived page-text lines 4-17 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_47bcd5ede204b7a80f`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Search and final evaluation
**来源**：https://arxiv.org/pdf/2609.19526v1  
**实际版本**：2609.19526v1  
**精确定位**：PDF physical page 6, derived page-text lines 12-20 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_47bcd5ede204b7a80f`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Judge, ranking and integrity limits
**来源**：https://arxiv.org/pdf/2609.19526v1  
**实际版本**：2609.19526v1  
**精确定位**：PDF physical page 11, derived page-text lines 10-28 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_47bcd5ede204b7a80f`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The strongest judge exceeds the coding backbone; downstream execution still validates gains. Scalar BT strength hides task trade-offs and editable candidates introduce evaluation-integrity risks.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_47bcd5ede204b7a80f` · Self Improvement via Fast Tree-search · 2609.19526v1
  - https://arxiv.org/pdf/2609.19526v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Runtime/cost/accuracy gains unreplicated.
- Do not equate expansion steps, accepted changes and recursive acceleration.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_47bcd5ede204b7a80f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
