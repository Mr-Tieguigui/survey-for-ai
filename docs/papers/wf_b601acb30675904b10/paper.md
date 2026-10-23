# RSI-Router: Evolving Subtask-Level LLM Routing and Skills for Cost-Efficient Agents

> 方法论文 · 2026 · `wf_b601acb30675904b10`

**作者**：Hao Li, Hangfan Zhang, Zhiyao Cui, Chunjiang Mu, Yiqun Zhang, Bo Zhang, Danyang Jia, Shuyue Hu  
**原文**：https://arxiv.org/abs/2609.34712  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
RSI-Router revises subtasks, model assignments and skills from training traces. Validation performance/cost selects a Pareto population; historical routers/skills guide later proposals. Bounded strategy-level feedback changes later router/skill proposals; six iterations are not six accepted gains or weight self-modification.

### 与 RSI 的具体关系

- Bounded strategy-level feedback changes later router/skill proposals; six iterations are not six accepted gains or weight self-modification.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_b601acb30675904b10
RSI-Router revises subtasks, model assignments and skills from training traces. Validation performance/cost selects a Pareto population; historical routers/skills guide later proposals.

**适用版本**：2609.34712v1；**原文定位**：Router/skill loop; PDF physical page 3, derived page-text lines 13-29 (one-based local extraction, not web-tool lines)；Data boundaries; PDF physical page 5, derived page-text lines 40-44 (one-based local extraction, not web-tool lines)；Price and cost scope; PDF physical page 6, derived page-text lines 4-10 (one-based local extraction, not web-tool lines)；Budget and scores; PDF physical page 6, derived page-text lines 1-10 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Success for four benchmarks, reward 0-1 for WebShop; test costs include routing/skill-context tokens. Train/validation guide evolution; test gives no feedback. Three repeats and learned-baseline seeds averaged.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_b601acb30675904b10`**：RSI-Router revises subtasks, model assignments and skills from training traces. Validation performance/cost selects a Pareto population; historical routers/skills guide later proposals.
  - 来源版本：2609.34712v1；定位：Router/skill loop; PDF physical page 3, derived page-text lines 13-29 (one-based local extraction, not web-tool lines)；Data boundaries; PDF physical page 5, derived page-text lines 40-44 (one-based local extraction, not web-tool lines)；Price and cost scope; PDF physical page 6, derived page-text lines 4-10 (one-based local extraction, not web-tool lines)；Budget and scores; PDF physical page 6, derived page-text lines 1-10 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Router/skill loop
**来源**：https://arxiv.org/pdf/2609.34712v1  
**实际版本**：2609.34712v1  
**精确定位**：PDF physical page 3, derived page-text lines 13-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_b601acb30675904b10`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Data boundaries
**来源**：https://arxiv.org/pdf/2609.34712v1  
**实际版本**：2609.34712v1  
**精确定位**：PDF physical page 5, derived page-text lines 40-44 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_b601acb30675904b10`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Budget and scores
**来源**：https://arxiv.org/pdf/2609.34712v1  
**实际版本**：2609.34712v1  
**精确定位**：PDF physical page 6, derived page-text lines 1-10 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_b601acb30675904b10`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Price and cost scope
**来源**：https://arxiv.org/pdf/2609.34712v1  
**实际版本**：2609.34712v1  
**精确定位**：PDF physical page 6, derived page-text lines 4-10 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_b601acb30675904b10`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Costs use fixed 1:30 small-model price estimates; inference savings omit total offline search cost. One model pair and finite splits bound generalization.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_b601acb30675904b10` · RSI-Router: Evolving Subtask-Level LLM Routing and Skills for Cost-Efficient Agents · 2609.34712v1
  - https://arxiv.org/pdf/2609.34712v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Inference savings are not total research savings; no configuration certification.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b601acb30675904b10 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
