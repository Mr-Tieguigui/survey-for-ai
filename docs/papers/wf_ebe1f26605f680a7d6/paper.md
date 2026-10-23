# Label-Free Reinforcement Learning via Cross-Model Entropy

> 方法论文 · 2026 · `wf_ebe1f26605f680a7d6`

**作者**：Matt Gorbett, Hossein Shirazi  
**原文**：https://arxiv.org/abs/2605.29009  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Cross-Model Entropy replaces GRPO rewards with the negative surprisal of generated response tokens under a frozen verifier from a different family. Character-overlap alignment maps verifier probabilities to generator tokens; per-position group-normalized advantages update the generator while unmatched positions are masked. RSI-component bridge: generated trajectories supply machine-computed feedback for persistent policy-weight improvement. This is a bounded self-generated training signal with a fixed external verifier, not evidence that the verifier or improvement algorithm recursively improves.

### 与 RSI 的具体关系

- RSI-component bridge: generated trajectories supply machine-computed feedback for persistent policy-weight improvement. This is a bounded self-generated training signal with a fixed external verifier, not evidence that the verifier or improvement algorithm recursively improves.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_ebe1f26605f680a7d6
Cross-Model Entropy replaces GRPO rewards with the negative surprisal of generated response tokens under a frozen verifier from a different family. Character-overlap alignment maps verifier probabilities to generator tokens; per-position group-normalized advantages update the generator while unmatched positions are masked.

**适用版本**：2605.29009v1；**原文定位**：cross-family verifier reward definition; PDF physical page 2, derived page-text lines 77-83 (one-based local extraction, not web-tool lines)；token reward normalization and masking; PDF physical page 2, derived page-text lines 98-106 (one-based local extraction, not web-tool lines)；reward proxy, overhead and scope limits; PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Tie-adjusted pairwise win rate on 805 AlpacaEval 2.0 prompts, averaged across two LLM judges; the reference is changed to a small instruction model, so these are not default leaderboard scores.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_ebe1f26605f680a7d6`**：Cross-Model Entropy replaces GRPO rewards with the negative surprisal of generated response tokens under a frozen verifier from a different family. Character-overlap alignment maps verifier probabilities to generator tokens; per-position group-normalized advantages update the generator while unmatched positions are masked.
  - 来源版本：2605.29009v1；定位：cross-family verifier reward definition; PDF physical page 2, derived page-text lines 77-83 (one-based local extraction, not web-tool lines)；token reward normalization and masking; PDF physical page 2, derived page-text lines 98-106 (one-based local extraction, not web-tool lines)；reward proxy, overhead and scope limits; PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · cross-family verifier reward definition
**来源**：https://arxiv.org/pdf/2605.29009v1  
**实际版本**：2605.29009v1  
**精确定位**：PDF physical page 2, derived page-text lines 77-83 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_ebe1f26605f680a7d6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · token reward normalization and masking
**来源**：https://arxiv.org/pdf/2605.29009v1  
**实际版本**：2605.29009v1  
**精确定位**：PDF physical page 2, derived page-text lines 98-106 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_ebe1f26605f680a7d6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · reward proxy, overhead and scope limits
**来源**：https://arxiv.org/pdf/2605.29009v1  
**实际版本**：2605.29009v1  
**精确定位**：PDF physical page 5, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_ebe1f26605f680a7d6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The verifier adds compute and memory cost and rewards low verifier surprise rather than correctness. Verifier-style drift or collapse and long-horizon behavior are not excluded; experiments cover small English-language generators and LLM-judge evaluation.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_ebe1f26605f680a7d6` · Label-Free Reinforcement Learning via Cross-Model Entropy · 2605.29009v1
  - https://arxiv.org/pdf/2605.29009v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ebe1f26605f680a7d6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
