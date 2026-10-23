# Lessons from Penetration Tests on Large-Scale Agent Systems

> 实证/审计/复现 · 2026 · `wf_d9c7b9736abd7945d4`

**作者**：Kevin Eykholt, Dhilung Kirat, Xiaokui Shu, Jiyong Jang, Frederico Araujo, Ian Molloy  
**原文**：https://arxiv.org/abs/2605.27042  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The paper reports two 2025 proprietary-agent penetration-test cases, including source/infrastructure access and an isolated pre-production replica for the first. Untrusted issue/repository input and tool/host weaknesses yield author-observed unintended execution/exposure. A separate February-2026 OpenClaw architecture analysis discusses self-accessible controls. Optional RSI governance background: agents with runtime/code access can reach controls, making sandbox and authorization premises material to persistent self-modification.

### 与 RSI 的具体关系

- Optional RSI governance background: agents with runtime/code access can reach controls, making sandbox and authorization premises material to persistent self-modification.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_d9c7b9736abd7945d4
The paper reports two 2025 proprietary-agent penetration-test cases, including source/infrastructure access and an isolated pre-production replica for the first. Untrusted issue/repository input and tool/host weaknesses yield author-observed unintended execution/exposure. A separate February-2026 OpenClaw architecture analysis discusses self-accessible controls.

**适用版本**：2605.27042v1；**原文定位**：§2.2 Test environment; PDF p2; derived page text lines 94–105 (one-based local extraction, not web-tool lines)；§2.2 Observed findings; PDF p3; derived page text lines 16–39 (one-based local extraction, not web-tool lines)；§4 Filtering/isolation; PDF p5; derived page text lines 1–29 (one-based local extraction, not web-tool lines)；§4.1 Proposed recommendations; PDF p5; derived page text lines 31–43 (one-based local extraction, not web-tool lines)；§5.3 Theoretical self-modification; PDF p6; derived page text lines 84–100 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_d9c7b9736abd7945d4`**：The paper reports two 2025 proprietary-agent penetration-test cases, including source/infrastructure access and an isolated pre-production replica for the first. Untrusted issue/repository input and tool/host weaknesses yield author-observed unintended execution/exposure. A separate February-2026 OpenClaw architecture analysis discusses self-accessible controls.
  - 来源版本：2605.27042v1；定位：§2.2 Test environment; PDF p2; derived page text lines 94–105 (one-based local extraction, not web-tool lines)；§2.2 Observed findings; PDF p3; derived page text lines 16–39 (one-based local extraction, not web-tool lines)；§4 Filtering/isolation; PDF p5; derived page text lines 1–29 (one-based local extraction, not web-tool lines)；§4.1 Proposed recommendations; PDF p5; derived page text lines 31–43 (one-based local extraction, not web-tool lines)；§5.3 Theoretical self-modification; PDF p6; derived page text lines 84–100 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2.2 Test environment
**来源**：https://arxiv.org/pdf/2605.27042v1  
**实际版本**：2605.27042v1  
**精确定位**：PDF p2; derived page text lines 94–105 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_d9c7b9736abd7945d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §2.2 Observed findings
**来源**：https://arxiv.org/pdf/2605.27042v1  
**实际版本**：2605.27042v1  
**精确定位**：PDF p3; derived page text lines 16–39 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_d9c7b9736abd7945d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §4 Filtering/isolation
**来源**：https://arxiv.org/pdf/2605.27042v1  
**实际版本**：2605.27042v1  
**精确定位**：PDF p5; derived page text lines 1–29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_d9c7b9736abd7945d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · §4.1 Proposed recommendations
**来源**：https://arxiv.org/pdf/2605.27042v1  
**实际版本**：2605.27042v1  
**精确定位**：PDF p5; derived page text lines 31–43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_d9c7b9736abd7945d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §5.3 Theoretical self-modification
**来源**：https://arxiv.org/pdf/2605.27042v1  
**实际版本**：2605.27042v1  
**精确定位**：PDF p6; derived page text lines 84–100 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_d9c7b9736abd7945d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Case studies give no representative failure rate or held-out RSI performance. Recommendations are proposed controls, not tested interventions. OpenClaw self-modification through indirect injection is explicitly theoretical and must not be merged with observed proprietary exploits or recursive capability improvement.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_d9c7b9736abd7945d4` · Lessons from Penetration Tests on Large-Scale Agent Systems · 2605.27042v1
  - https://arxiv.org/pdf/2605.27042v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d9c7b9736abd7945d4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
