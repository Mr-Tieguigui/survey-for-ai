# Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning

> 方法论文 · 2026 · `wf_e0ffbcca2ade456f55`

**作者**：Shujin Wu, Cheng Qian, Xiusi Chen, Heng Ji  
**原文**：https://arxiv.org/abs/2607.21971  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
METAEVOLVE synthesizes histories from static program pools, trains with GRPO on execution-score gain and uses the trained proposer in the same OpenEvolve search as comparison. Bounded RSI contribution learns a later feedback-guided proposer; search controller stays fixed.

### 与 RSI 的具体关系

- Bounded RSI contribution learns a later feedback-guided proposer; search controller stays fixed.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_e0ffbcca2ade456f55
METAEVOLVE synthesizes histories from static program pools, trains with GRPO on execution-score gain and uses the trained proposer in the same OpenEvolve search as comparison.

**适用版本**：2607.21971v1；**原文定位**：Context and fitness; PDF physical page 4, derived page-text lines 11-31 (one-based local extraction, not web-tool lines)；Synthetic histories and reward; PDF physical page 4, derived page-text lines 32-52 (one-based local extraction, not web-tool lines)；Finite scope; PDF physical page 5, derived page-text lines 15-27 (one-based local extraction, not web-tool lines)；Same controller; PDF physical page 5, derived page-text lines 43-46 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Fitness multiplies all-tests correctness and capped inverse runtime. Reward -1 without strict gain, otherwise score difference. Seven datasets (50 cases each), eight open-ended tasks; same search isolates proposer.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_e0ffbcca2ade456f55`**：METAEVOLVE synthesizes histories from static program pools, trains with GRPO on execution-score gain and uses the trained proposer in the same OpenEvolve search as comparison.
  - 来源版本：2607.21971v1；定位：Context and fitness; PDF physical page 4, derived page-text lines 11-31 (one-based local extraction, not web-tool lines)；Synthetic histories and reward; PDF physical page 4, derived page-text lines 32-52 (one-based local extraction, not web-tool lines)；Finite scope; PDF physical page 5, derived page-text lines 15-27 (one-based local extraction, not web-tool lines)；Same controller; PDF physical page 5, derived page-text lines 43-46 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Context and fitness
**来源**：https://arxiv.org/pdf/2607.21971v1  
**实际版本**：2607.21971v1  
**精确定位**：PDF physical page 4, derived page-text lines 11-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_e0ffbcca2ade456f55`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Synthetic histories and reward
**来源**：https://arxiv.org/pdf/2607.21971v1  
**实际版本**：2607.21971v1  
**精确定位**：PDF physical page 4, derived page-text lines 32-52 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_e0ffbcca2ade456f55`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Same controller
**来源**：https://arxiv.org/pdf/2607.21971v1  
**实际版本**：2607.21971v1  
**精确定位**：PDF physical page 5, derived page-text lines 43-46 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_e0ffbcca2ade456f55`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Finite scope
**来源**：https://arxiv.org/pdf/2607.21971v1  
**实际版本**：2607.21971v1  
**精确定位**：PDF physical page 5, derived page-text lines 15-27 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_e0ffbcca2ade456f55`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Sorted synthetic histories are not observed online chains. Finite coding/open-ended evaluation does not establish unrestricted meta-improver self-modification.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_e0ffbcca2ade456f55` · Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning · 2607.21971v1
  - https://arxiv.org/pdf/2607.21971v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Synthetic histories are not executed RSI rounds; results remain author reports.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e0ffbcca2ade456f55 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
