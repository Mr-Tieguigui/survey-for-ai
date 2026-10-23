# Beyond Successor Accuracy: State Retention for Recursive Self-Improvement in Recommendation

> 实证/审计/复现 · 2026 · `wf_2f8e97c9feb1a46023`

**作者**：Jinfeng Xu, Zheyu Chen, Ziyue Peng, Zheng Lin, Wenhao Yuan, Jian Chen, Shujie Li, Edith Ngai  
**原文**：https://arxiv.org/abs/2610.07105  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Rec-RSI evaluates retention across generated-interaction updates using marginally matched cross- versus within-generation pairs (CGA) and label-free top-k rank separation. Four datasets, three encoders and three seeded trajectories per setting use separate checkpoint-selection, diagnosis and confirmation windows; Sports is prospective. The author reports selected-family superiority over the direct successor in 34/36 first-update held-out trajectories, with preference varying by architecture and round. Direct generated-supervision feedback into successor training; retained as bounded state-retention evidence.

### 与 RSI 的具体关系

- Direct generated-supervision feedback into successor training; retained as bounded state-retention evidence.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_2f8e97c9feb1a46023
Rec-RSI evaluates retention across generated-interaction updates using marginally matched cross- versus within-generation pairs (CGA) and label-free top-k rank separation. Four datasets, three encoders and three seeded trajectories per setting use separate checkpoint-selection, diagnosis and confirmation windows; Sports is prospective. The author reports selected-family superiority over the direct successor in 34/36 first-update held-out trajectories, with preference varying by architecture and round.

**适用版本**：2610.07105v1；**原文定位**：§2.2–3 CGA and evaluation protocol; PDF p2; derived page text lines 33–111 (one-based local extraction, not web-tool lines)；§3 Training and comparison units; PDF p3; derived page text lines 34–59 (one-based local extraction, not web-tool lines)；§4.4 Held-out and second-update evaluation; PDF p4; derived page text lines 40–71 (one-based local extraction, not web-tool lines)；§2.2 Interpretation boundary; PDF p2; derived page text lines 55–67 (one-based local extraction, not web-tool lines)；§4.3 Rank separation boundary; PDF p3; derived page text lines 121–125 (one-based local extraction, not web-tool lines)；§4.4 Storage and round dependence; PDF p4; derived page text lines 48–69 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_2f8e97c9feb1a46023`**：Rec-RSI evaluates retention across generated-interaction updates using marginally matched cross- versus within-generation pairs (CGA) and label-free top-k rank separation. Four datasets, three encoders and three seeded trajectories per setting use separate checkpoint-selection, diagnosis and confirmation windows; Sports is prospective. The author reports selected-family superiority over the direct successor in 34/36 first-update held-out trajectories, with preference varying by architecture and round.
  - 来源版本：2610.07105v1；定位：§2.2–3 CGA and evaluation protocol; PDF p2; derived page text lines 33–111 (one-based local extraction, not web-tool lines)；§3 Training and comparison units; PDF p3; derived page text lines 34–59 (one-based local extraction, not web-tool lines)；§4.4 Held-out and second-update evaluation; PDF p4; derived page text lines 40–71 (one-based local extraction, not web-tool lines)；§2.2 Interpretation boundary; PDF p2; derived page text lines 55–67 (one-based local extraction, not web-tool lines)；§4.3 Rank separation boundary; PDF p3; derived page text lines 121–125 (one-based local extraction, not web-tool lines)；§4.4 Storage and round dependence; PDF p4; derived page text lines 48–69 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2.2–3 CGA and evaluation protocol
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p2; derived page text lines 33–111 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §3 Training and comparison units
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p3; derived page text lines 34–59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §4.4 Held-out and second-update evaluation
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p4; derived page text lines 40–71 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · §2.2 Interpretation boundary
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p2; derived page text lines 55–67 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §4.3 Rank separation boundary
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p3; derived page text lines 121–125 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · §4.4 Storage and round dependence
**来源**：https://arxiv.org/pdf/2610.07105v1  
**实际版本**：2610.07105v1  
**精确定位**：PDF p4; derived page text lines 48–69 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_2f8e97c9feb1a46023`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- CGA describes update-boundary complementarity under fixed fusion, including non-genealogical pairs, rather than certifying a causal parent-child edge. Dataset–encoder settings are primary units, trajectory rates descriptive. The signal is chiefly between architectures, weak within architecture; a retained pair adds a model and forward pass. Two updates do not demonstrate unbounded RSI.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_2f8e97c9feb1a46023` · Beyond Successor Accuracy: State Retention for Recursive Self-Improvement in Recommendation · 2610.07105v1
  - https://arxiv.org/pdf/2610.07105v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2f8e97c9feb1a46023 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
