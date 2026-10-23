# MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution

> 综合系统/智能体 · 2026 · `wf_a6652285d15eac3e23`

**作者**：Prithwish Jana, Mononito Goswami, Hao Liu, Xinyu Li, Langlin Huang, Zhehui Huang, Zhishen Huang, Patrick Blöbaum, Anoop Deoras, Purak Jain, Nikos Kanakaris, Sahika Genc  
**原文**：https://arxiv.org/abs/2609.38349  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
MILO evolves executable harnesses and a search configuration through island lineage memory, coding-agent mutators and a stall-triggered orchestrator. The append-only memory retains admitted and rejected children, while orchestration changes island structure, mutator assignment or task curriculum. Direct RSI bridge: persistent harness rewrites affect subsequent task solving, and orchestration adapts the search strategy used to generate later rewrites. No unrestricted model-weight or optimizer-code self-redesign is inferred.

### 与 RSI 的具体关系

- Direct RSI bridge: persistent harness rewrites affect subsequent task solving, and orchestration adapts the search strategy used to generate later rewrites. No unrestricted model-weight or optimizer-code self-redesign is inferred.

## 2. 论文的核心内容与贡献

### role:b570_10_role_wf_a6652285d15eac3e23
MILO evolves executable harnesses and a search configuration through island lineage memory, coding-agent mutators and a stall-triggered orchestrator. The append-only memory retains admitted and rejected children, while orchestration changes island structure, mutator assignment or task curriculum.

**适用版本**：arXiv:2609.38349v1；**原文定位**：append-only lineages and orchestration actions; PDF physical page 7, derived page-text lines 31-44 (one-based local extraction, not web-tool lines)；adaptive search configuration and stall diagnosis; PDF physical page 8, derived page-text lines 19-30 (one-based local extraction, not web-tool lines)；admission versus adaptive validation monitoring/selection; PDF physical page 9, derived page-text lines 17-31 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 系统架构、组件与更新过程
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Search-set accuracy/cost frontier and declared hypervolume/non-dominance admission; Bval tracks progress/stalls and selects a final frontier harness. Transfer and scientific-discovery numerics remain pending.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_10_ev_wf_a6652285d15eac3e23`**：MILO evolves executable harnesses and a search configuration through island lineage memory, coding-agent mutators and a stall-triggered orchestrator. The append-only memory retains admitted and rejected children, while orchestration changes island structure, mutator assignment or task curriculum.
  - 来源版本：arXiv:2609.38349v1；定位：append-only lineages and orchestration actions; PDF physical page 7, derived page-text lines 31-44 (one-based local extraction, not web-tool lines)；adaptive search configuration and stall diagnosis; PDF physical page 8, derived page-text lines 19-30 (one-based local extraction, not web-tool lines)；admission versus adaptive validation monitoring/selection; PDF physical page 9, derived page-text lines 17-31 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · append-only lineages and orchestration actions
**来源**：https://arxiv.org/pdf/2609.38349v1  
**实际版本**：arXiv:2609.38349v1  
**精确定位**：PDF physical page 7, derived page-text lines 31-44 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_a6652285d15eac3e23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · adaptive search configuration and stall diagnosis
**来源**：https://arxiv.org/pdf/2609.38349v1  
**实际版本**：arXiv:2609.38349v1  
**精确定位**：PDF physical page 8, derived page-text lines 19-30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_a6652285d15eac3e23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · admission versus adaptive validation monitoring/selection
**来源**：https://arxiv.org/pdf/2609.38349v1  
**实际版本**：arXiv:2609.38349v1  
**精确定位**：PDF physical page 9, derived page-text lines 17-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_a6652285d15eac3e23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- A round/child is not necessarily an admitted harness. Search-set frontier admission is distinct from Bval monitoring: Bval gains reset stall counters and Bval selects the returned harness, so that split is an adaptive monitoring/selection resource rather than an untouched final test. Fixed models and a finite budget bound the procedure.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_10_src_wf_a6652285d15eac3e23` · MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution · arXiv:2609.38349v1
  - https://arxiv.org/pdf/2609.38349v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- MILO prior oversized HTML held is superseded only for this actual v1 PDF role review; no claim that every evolutionary round is an accepted revision.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a6652285d15eac3e23 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
