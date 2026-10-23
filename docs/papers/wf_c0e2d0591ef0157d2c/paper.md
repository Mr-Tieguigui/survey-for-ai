# Recursive Optimization with Controlled Language Models: Inference-Time Control, Tokenization Co-Evolution, and the Fourth Loop

> 方法论文 · 2026 · `wf_c0e2d0591ef0157d2c`

**作者**：Logan Matthew Napolitano  
**原文**：https://doi.org/10.5281/zenodo.18361798  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Recursive Optimization with Controlled Language Models combines repetition-risk probing and decode-time control with bounded self-generated-data micro-training and checkpoint rollback. Its fourth loop proposes vocabulary merges, embedding resizing/initialization and targeted adaptation that actually exercises the new tokens. Direct bounded RSI bridge: generated data changes weights and tokenization/embeddings for later generation. A successful iteration is distinct from a proven net capability gain or an improved optimizer.

### 与 RSI 的具体关系

- Direct bounded RSI bridge: generated data changes weights and tokenization/embeddings for later generation. A successful iteration is distinct from a proven net capability gain or an improved optimizer.

## 2. 论文的核心内容与贡献

### role:b570_09_role_wf_c0e2d0591ef0157d2c
Recursive Optimization with Controlled Language Models combines repetition-risk probing and decode-time control with bounded self-generated-data micro-training and checkpoint rollback. Its fourth loop proposes vocabulary merges, embedding resizing/initialization and targeted adaptation that actually exercises the new tokens.

**适用版本**：Zenodo 18361799；**原文定位**：micro-training commit/rollback and stopping safeguards; PDF physical page 11, derived page-text lines 3-27 (one-based local extraction, not web-tool lines)；token/embedding growth and targeted adaptation; PDF physical page 16, derived page-text lines 3-24 (one-based local extraction, not web-tool lines)；checkpoint invalidation after misconfiguration; PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Judge-relative quality retention, canary forgetting and consecutive-rollback limits bound micro-training; entropy/attention boundary stress proposes tokenizer changes. No cross-task aggregate score is certified.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_09_ev_wf_c0e2d0591ef0157d2c`**：Recursive Optimization with Controlled Language Models combines repetition-risk probing and decode-time control with bounded self-generated-data micro-training and checkpoint rollback. Its fourth loop proposes vocabulary merges, embedding resizing/initialization and targeted adaptation that actually exercises the new tokens.
  - 来源版本：Zenodo 18361799；定位：micro-training commit/rollback and stopping safeguards; PDF physical page 11, derived page-text lines 3-27 (one-based local extraction, not web-tool lines)；token/embedding growth and targeted adaptation; PDF physical page 16, derived page-text lines 3-24 (one-based local extraction, not web-tool lines)；checkpoint invalidation after misconfiguration; PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · micro-training commit/rollback and stopping safeguards
**来源**：https://zenodo.org/api/records/18361799/files/recursive_optimization_book.pdf/content  
**实际版本**：Zenodo 18361799  
**精确定位**：PDF physical page 11, derived page-text lines 3-27 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c0e2d0591ef0157d2c`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · token/embedding growth and targeted adaptation
**来源**：https://zenodo.org/api/records/18361799/files/recursive_optimization_book.pdf/content  
**实际版本**：Zenodo 18361799  
**精确定位**：PDF physical page 16, derived page-text lines 3-24 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c0e2d0591ef0157d2c`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · checkpoint invalidation after misconfiguration
**来源**：https://zenodo.org/api/records/18361799/files/recursive_optimization_book.pdf/content  
**实际版本**：Zenodo 18361799  
**精确定位**：PDF physical page 10, derived page-text lines 14-21 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c0e2d0591ef0157d2c`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The stated fixed judge and threshold are guard mechanisms, not a proof against Goodhart effects. The report explicitly invalidates a later dense-training checkpoint after threshold misconfiguration; claimed ceiling-breaking, density ratios and sustained improvement are not independently verified or certified as configurations.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_09_src_wf_c0e2d0591ef0157d2c` · Recursive Optimization with Controlled Language Models: Inference-Time Control, Tokenization Co-Evolution, and the Fourth Loop · Zenodo 18361799
  - https://zenodo.org/api/records/18361799/files/recursive_optimization_book.pdf/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Report's assertion that frozen judging prevents Goodhart is treated as design intent, not a guarantee.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c0e2d0591ef0157d2c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
