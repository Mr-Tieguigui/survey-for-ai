# One Prompt Does Not Fit All: Self-Meta-Evolve for Personalized Information Extraction

> 方法论文 · 2026 · `wf_8ba3a2cc19ed0ecb23`

**作者**：Hongliang Li, Lu Wang, Yong Xu, Hanyang Chen, Zhitao Hou, Xiaoting Qin, Song Ge, Qingwei Lin, Dongmei Zhang  
**原文**：https://arxiv.org/abs/2609.21626  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Self-Meta-Evolve edits structured user prompts from AI-User feedback and buffers successful traces; a meta-optimizer rewrites editing strategy for future persona adaptation. Inner edits change the meta-prompt guiding later edits, a bounded recursive strategy update.

### 与 RSI 的具体关系

- Inner edits change the meta-prompt guiding later edits, a bounded recursive strategy update.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_8ba3a2cc19ed0ecb23
Self-Meta-Evolve edits structured user prompts from AI-User feedback and buffers successful traces; a meta-optimizer rewrites editing strategy for future persona adaptation.

**适用版本**：2609.21626v1；**原文定位**：Inner editing; PDF physical page 5, derived page-text lines 57-86 (one-based local extraction, not web-tool lines)；Meta-prompt evolution; PDF physical page 6, derived page-text lines 5-22 (one-based local extraction, not web-tool lines)；AI-user and coverage limits; PDF physical page 9, derived page-text lines 35-64 (one-based local extraction, not web-tool lines)；Success threshold; PDF physical page 4, derived page-text lines 46-53 (one-based local extraction, not web-tool lines)；Splits; PDF physical page 6, derived page-text lines 32-35 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Persona/document extraction loss; success threshold 0.75 calibrated on development personas. Main 292-persona split 60/20/20 plus disjoint STEM/Humanities tests; SR@t measures adaptation efficiency.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_8ba3a2cc19ed0ecb23`**：Self-Meta-Evolve edits structured user prompts from AI-User feedback and buffers successful traces; a meta-optimizer rewrites editing strategy for future persona adaptation.
  - 来源版本：2609.21626v1；定位：Inner editing; PDF physical page 5, derived page-text lines 57-86 (one-based local extraction, not web-tool lines)；Meta-prompt evolution; PDF physical page 6, derived page-text lines 5-22 (one-based local extraction, not web-tool lines)；AI-user and coverage limits; PDF physical page 9, derived page-text lines 35-64 (one-based local extraction, not web-tool lines)；Success threshold; PDF physical page 4, derived page-text lines 46-53 (one-based local extraction, not web-tool lines)；Splits; PDF physical page 6, derived page-text lines 32-35 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Inner editing
**来源**：https://arxiv.org/pdf/2609.21626v1  
**实际版本**：2609.21626v1  
**精确定位**：PDF physical page 5, derived page-text lines 57-86 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_8ba3a2cc19ed0ecb23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Meta-prompt evolution
**来源**：https://arxiv.org/pdf/2609.21626v1  
**实际版本**：2609.21626v1  
**精确定位**：PDF physical page 6, derived page-text lines 5-22 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_8ba3a2cc19ed0ecb23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Success threshold
**来源**：https://arxiv.org/pdf/2609.21626v1  
**实际版本**：2609.21626v1  
**精确定位**：PDF physical page 4, derived page-text lines 46-53 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_8ba3a2cc19ed0ecb23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 测量 / 结果 · Splits
**来源**：https://arxiv.org/pdf/2609.21626v1  
**实际版本**：2609.21626v1  
**精确定位**：PDF physical page 6, derived page-text lines 32-35 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_8ba3a2cc19ed0ecb23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · AI-user and coverage limits
**来源**：https://arxiv.org/pdf/2609.21626v1  
**实际版本**：2609.21626v1  
**精确定位**：PDF physical page 9, derived page-text lines 35-64 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_8ba3a2cc19ed0ecb23`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- LLM-user feedback may favor judge-assessable patterns. Personas mainly cover English US enterprise occupations; prompts cannot supply missing model knowledge.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_8ba3a2cc19ed0ecb23` · One Prompt Does Not Fit All: Self-Meta-Evolve for Personalized Information Extraction · 2609.21626v1
  - https://arxiv.org/pdf/2609.21626v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Preference and performance effects unreplicated.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8ba3a2cc19ed0ecb23 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
