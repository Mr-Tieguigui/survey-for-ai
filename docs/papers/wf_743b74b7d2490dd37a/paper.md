# Self-Evolving Agents with Anytime-Valid Certificates

> 实证/审计/复现 · 2026 · `wf_743b74b7d2490dd37a`

**作者**：Biswa Sengupta  
**原文**：https://arxiv.org/abs/2607.00871  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SEA confines evolution to directive steering and a mutable harness around frozen L0, with self-authored reproduction-oracle search. The executed study uses a seeded 52-instance SWE-bench Verified subset and official fail-to-pass/pass-to-pass terminal grading; gold tests are reserved for terminal evaluation. No-op controls isolate reported +5 resolved on GPT and +4 on GLM. Full-stack ALG4 is disabled; its isolated 36 score accepted zero edits. Direct bounded self-evolution: separate directive learning and debugging from accepted harness edits and unimplemented slow-weight training.

### 与 RSI 的具体关系

- Direct bounded self-evolution: separate directive learning and debugging from accepted harness edits and unimplemented slow-weight training.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_743b74b7d2490dd37a
SEA confines evolution to directive steering and a mutable harness around frozen L0, with self-authored reproduction-oracle search. The executed study uses a seeded 52-instance SWE-bench Verified subset and official fail-to-pass/pass-to-pass terminal grading; gold tests are reserved for terminal evaluation. No-op controls isolate reported +5 resolved on GPT and +4 on GLM. Full-stack ALG4 is disabled; its isolated 36 score accepted zero edits.

**适用版本**：2607.00871v1；**原文定位**：§7 Actor; PDF p16; derived page text lines 9–19 (one-based local extraction, not web-tool lines)；§8 Benchmark and grading; PDF p16; derived page text lines 46–54 (one-based local extraction, not web-tool lines)；§8–9 Executed protocol; PDF p17; derived page text lines 13–49 (one-based local extraction, not web-tool lines)；§9.1–9.2 Ablation and events; PDF p19; derived page text lines 17–41 (one-based local extraction, not web-tool lines)；§10 Limitations; PDF p19; derived page text lines 42–49 (one-based local extraction, not web-tool lines)；§10 Limitations continued; PDF p20; derived page text lines 1–22 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_743b74b7d2490dd37a`**：SEA confines evolution to directive steering and a mutable harness around frozen L0, with self-authored reproduction-oracle search. The executed study uses a seeded 52-instance SWE-bench Verified subset and official fail-to-pass/pass-to-pass terminal grading; gold tests are reserved for terminal evaluation. No-op controls isolate reported +5 resolved on GPT and +4 on GLM. Full-stack ALG4 is disabled; its isolated 36 score accepted zero edits.
  - 来源版本：2607.00871v1；定位：§7 Actor; PDF p16; derived page text lines 9–19 (one-based local extraction, not web-tool lines)；§8 Benchmark and grading; PDF p16; derived page text lines 46–54 (one-based local extraction, not web-tool lines)；§8–9 Executed protocol; PDF p17; derived page text lines 13–49 (one-based local extraction, not web-tool lines)；§9.1–9.2 Ablation and events; PDF p19; derived page text lines 17–41 (one-based local extraction, not web-tool lines)；§10 Limitations; PDF p19; derived page text lines 42–49 (one-based local extraction, not web-tool lines)；§10 Limitations continued; PDF p20; derived page text lines 1–22 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §7 Actor
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p16; derived page text lines 9–19 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §8 Benchmark and grading
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p16; derived page text lines 46–54 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §8–9 Executed protocol
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p17; derived page text lines 13–49 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 机制 / 定义 · §9.1–9.2 Ablation and events
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p19; derived page text lines 17–41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §10 Limitations
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p19; derived page text lines 42–49 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · §10 Limitations continued
**来源**：https://arxiv.org/pdf/2607.00871v1  
**实际版本**：2607.00871v1  
**精确定位**：PDF p20; derived page text lines 1–22 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_743b74b7d2490dd37a`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Each expensive cell is a single run, so differences are not significance. Endogenous controller compositions remain conjectural and assumptions may erode; self-oracles can false-green, terminal grading authoritative. Slow-loop distillation is designed but untrained. Controller firing and rounds are not accepted persistent edits: ALG4 accepted none.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_743b74b7d2490dd37a` · Self-Evolving Agents with Anytime-Valid Certificates · 2607.00871v1
  - https://arxiv.org/pdf/2607.00871v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_743b74b7d2490dd37a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
