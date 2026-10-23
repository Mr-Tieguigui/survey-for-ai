# SelfSearch: Reward-Free Search for Self-Improving Agents

> 方法论文 · 2026 · `wf_afa4824af910b5eb66`

**作者**：Jungwoo Yang, Injin Kong, Yohan Jo  
**原文**：https://arxiv.org/abs/2609.37968  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SelfSearch revises agent repository from earlier self-improvement records/local checks. Successor code runs next episode; two lineages share records without downstream benchmark search feedback. Revised tools shape later self-modification; same repository does not imply identical model across improvement and downstream execution.

### 与 RSI 的具体关系

- Revised tools shape later self-modification; same repository does not imply identical model across improvement and downstream execution.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_afa4824af910b5eb66
SelfSearch revises agent repository from earlier self-improvement records/local checks. Successor code runs next episode; two lineages share records without downstream benchmark search feedback.

**适用版本**：2609.37968v1；**原文定位**：Successor and feedback; PDF physical page 3, derived page-text lines 22-40 (one-based local extraction, not web-tool lines)；Lineages and search boundary; PDF physical page 3, derived page-text lines 41-58 (one-based local extraction, not web-tool lines)；Costs and consistency; PDF physical page 9, derived page-text lines 24-41 (one-based local extraction, not web-tool lines)；Models and scoring; PDF physical page 4, derived page-text lines 10-29 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Two lineages, ten generations; 120 SWE-bench Verified, 60 Multilingual, 89 Terminal-Bench2.1 tasks. Population success is mean lineage rate, not union; costs include failures.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_afa4824af910b5eb66`**：SelfSearch revises agent repository from earlier self-improvement records/local checks. Successor code runs next episode; two lineages share records without downstream benchmark search feedback.
  - 来源版本：2609.37968v1；定位：Successor and feedback; PDF physical page 3, derived page-text lines 22-40 (one-based local extraction, not web-tool lines)；Lineages and search boundary; PDF physical page 3, derived page-text lines 41-58 (one-based local extraction, not web-tool lines)；Costs and consistency; PDF physical page 9, derived page-text lines 24-41 (one-based local extraction, not web-tool lines)；Models and scoring; PDF physical page 4, derived page-text lines 10-29 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Successor and feedback
**来源**：https://arxiv.org/pdf/2609.37968v1  
**实际版本**：2609.37968v1  
**精确定位**：PDF physical page 3, derived page-text lines 22-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_afa4824af910b5eb66`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Lineages and search boundary
**来源**：https://arxiv.org/pdf/2609.37968v1  
**实际版本**：2609.37968v1  
**精确定位**：PDF physical page 3, derived page-text lines 41-58 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_afa4824af910b5eb66`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Models and scoring
**来源**：https://arxiv.org/pdf/2609.37968v1  
**实际版本**：2609.37968v1  
**精确定位**：PDF physical page 4, derived page-text lines 10-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_afa4824af910b5eb66`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Costs and consistency
**来源**：https://arxiv.org/pdf/2609.37968v1  
**实际版本**：2609.37968v1  
**精确定位**：PDF physical page 9, derived page-text lines 24-41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_afa4824af910b5eb66`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Final endpoints are assessed, not score-selected. Independent-search consistency remains future work. Reward-free excludes downstream search reward, not local feedback or evaluation cost.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_afa4824af910b5eb66` · SelfSearch: Reward-Free Search for Self-Improving Agents · 2609.37968v1
  - https://arxiv.org/pdf/2609.37968v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No independent repeated-chain verification.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_afa4824af910b5eb66 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
