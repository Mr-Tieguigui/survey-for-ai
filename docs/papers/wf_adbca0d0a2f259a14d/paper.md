# Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden?

> 实证/审计/复现 · 2026 · `wf_adbca0d0a2f259a14d`

**作者**：Haomin Luo  
**原文**：https://arxiv.org/abs/2609.35897  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
This is a causal audit of released Disco103, not a new algorithm-discovery run. Zero-pinning, timed freezing, transplantation and clamping separate recurrent history from continuing agent-parameter learning across reward scaling, streams, change and sparse exploration. Controlled seeded assays show task-dependent state support and mismatch costs; matching replay capacity reverses an apparent adaptation advantage. The paper explicitly bridges RSI to auditing a self-discovered improvement rule; retain bounded-mechanism evaluation without inventing new recursive discovery.

### 与 RSI 的具体关系

- The paper explicitly bridges RSI to auditing a self-discovered improvement rule; retain bounded-mechanism evaluation without inventing new recursive discovery.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_adbca0d0a2f259a14d
This is a causal audit of released Disco103, not a new algorithm-discovery run. Zero-pinning, timed freezing, transplantation and clamping separate recurrent history from continuing agent-parameter learning across reward scaling, streams, change and sparse exploration. Controlled seeded assays show task-dependent state support and mismatch costs; matching replay capacity reverses an apparent adaptation advantage.

**适用版本**：2609.35897v1；**原文定位**：§1–2 Audit and interface; PDF p2; derived page text lines 13–45 (one-based local extraction, not web-tool lines)；§4.1–4.2 Horizon/reward scaling; PDF p5; derived page text lines 32–60 (one-based local extraction, not web-tool lines)；§4.4 Replay confounding; PDF p7; derived page text lines 48–56 (one-based local extraction, not web-tool lines)；§5.1 Capability gates; PDF p8; derived page text lines 25–38 (one-based local extraction, not web-tool lines)；§7 Conditional conclusion; PDF p9; derived page text lines 34–41 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_adbca0d0a2f259a14d`**：This is a causal audit of released Disco103, not a new algorithm-discovery run. Zero-pinning, timed freezing, transplantation and clamping separate recurrent history from continuing agent-parameter learning across reward scaling, streams, change and sparse exploration. Controlled seeded assays show task-dependent state support and mismatch costs; matching replay capacity reverses an apparent adaptation advantage.
  - 来源版本：2609.35897v1；定位：§1–2 Audit and interface; PDF p2; derived page text lines 13–45 (one-based local extraction, not web-tool lines)；§4.1–4.2 Horizon/reward scaling; PDF p5; derived page text lines 32–60 (one-based local extraction, not web-tool lines)；§4.4 Replay confounding; PDF p7; derived page text lines 48–56 (one-based local extraction, not web-tool lines)；§5.1 Capability gates; PDF p8; derived page text lines 25–38 (one-based local extraction, not web-tool lines)；§7 Conditional conclusion; PDF p9; derived page text lines 34–41 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §1–2 Audit and interface
**来源**：https://arxiv.org/pdf/2609.35897v1  
**实际版本**：2609.35897v1  
**精确定位**：PDF p2; derived page text lines 13–45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_adbca0d0a2f259a14d`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §4.1–4.2 Horizon/reward scaling
**来源**：https://arxiv.org/pdf/2609.35897v1  
**实际版本**：2609.35897v1  
**精确定位**：PDF p5; derived page text lines 32–60 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_adbca0d0a2f259a14d`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §4.4 Replay confounding
**来源**：https://arxiv.org/pdf/2609.35897v1  
**实际版本**：2609.35897v1  
**精确定位**：PDF p7; derived page text lines 48–56 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_adbca0d0a2f259a14d`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · §5.1 Capability gates
**来源**：https://arxiv.org/pdf/2609.35897v1  
**实际版本**：2609.35897v1  
**精确定位**：PDF p8; derived page text lines 25–38 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_adbca0d0a2f259a14d`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §7 Conditional conclusion
**来源**：https://arxiv.org/pdf/2609.35897v1  
**实际版本**：2609.35897v1  
**精确定位**：PDF p9; derived page text lines 34–41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_adbca0d0a2f259a14d`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Model systems intentionally separate perceptual complexity; full-Atari Pong remains near the losing floor and requires competence diagnosis before memory attribution. State freezing still lets weights/other quantities learn. Endpoint or mastery gains do not show the learned update rule recursively rewriting itself during this audit; revision benefits remain condition-dependent.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_adbca0d0a2f259a14d` · Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden? · 2609.35897v1
  - https://arxiv.org/pdf/2609.35897v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_adbca0d0a2f259a14d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
