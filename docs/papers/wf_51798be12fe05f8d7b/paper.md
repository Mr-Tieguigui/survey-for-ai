# Reinforcement Learning with Self-Modifying Policies

> 方法论文 · 1998 · `wf_51798be12fe05f8d7b`

**作者**：Jürgen Schmidhuber, Jieyu Zhao, Nicol N. Schraudolph  
**原文**：https://doi.org/10.1007/978-1-4615-5529-2_12  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The paper defines self-modifying policies whose learning procedure is itself mutable; SSA evaluates long-term reward-rate effects, retains successful policy changes, and backtracks changes that fail its success-story criterion.

### 与 RSI 的具体关系

- Core historical precursor: it implements evaluated and retained self-modification of the learning policy, while its guarantees and experiment remain bounded and do not establish unbounded RSI or acceleration.

## 2. 论文的核心内容与贡献

### role:b570_11_role_wf_51798be12fe05f8d7b
The paper defines self-modifying policies whose learning procedure is itself mutable; SSA evaluates long-term reward-rate effects, retains successful policy changes, and backtracks changes that fail its success-story criterion.

**适用版本**：captured source; no latest-version assertion；**原文定位**：Derived document section page_2, lines 17-22 (one-based local extraction, not web-tool lines)；Derived document section page_2, lines 36-40 (one-based local extraction, not web-tool lines)；Derived document section page_3, lines 69-79 (one-based local extraction, not web-tool lines)；Derived document section page_4, lines 16-24 (one-based local extraction, not web-tool lines)；Derived document section page_6, lines 4-10 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_11_ev_wf_51798be12fe05f8d7b`**：The paper defines self-modifying policies whose learning procedure is itself mutable; SSA evaluates long-term reward-rate effects, retains successful policy changes, and backtracks changes that fail its success-story criterion.
  - 来源版本：captured source; no latest-version assertion；定位：Derived document section page_2, lines 17-22 (one-based local extraction, not web-tool lines)；Derived document section page_2, lines 36-40 (one-based local extraction, not web-tool lines)；Derived document section page_3, lines 69-79 (one-based local extraction, not web-tool lines)；Derived document section page_4, lines 16-24 (one-based local extraction, not web-tool lines)；Derived document section page_6, lines 4-10 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：Derived document section page_2, lines 17-22 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_51798be12fe05f8d7b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：Derived document section page_2, lines 36-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_51798be12fe05f8d7b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：Derived document section page_3, lines 69-79 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_51798be12fe05f8d7b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · selected material-limit or boundary passage
**来源**：https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：Derived document section page_4, lines 16-24 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_51798be12fe05f8d7b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · selected material-limit or boundary passage
**来源**：https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：Derived document section page_6, lines 4-10 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_51798be12fe05f8d7b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The method cannot guarantee optimal policies in general environments, improvement speed depends on the environment and agent, and the reported experiment is a bounded partially observable task rather than open-ended recursive capability growth.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_11_src_wf_51798be12fe05f8d7b` · Reinforcement Learning with Self-Modifying Policies · captured source; no latest-version assertion
  - https://aris.supsi.ch/bitstreams/32ded130-ca51-44bc-9378-d39b0895997d/download；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Numerical, configuration and relationship claims require separate evidence review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_role_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_51798be12fe05f8d7b --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
