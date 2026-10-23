# LTL Model Checking of Concurrent Self Modifying Code

> 背景/相邻基础 · 2025 · `wf_e89fb495d022538fd1`

**作者**：Tayssir Touili, Olzhas Zhangeldinov  
**原文**：https://doi.org/10.1007/978-3-032-00828-2_17  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The actual author-hosted manuscript studies LTL analysis of concurrent self-modifying programs using SM-DPNs. Its Python experiments compare direct analysis with translation to DPNs, and its application is malware detection. Runtime code mutation is the research object; the reviewed work supplies no capability-improving agent succession protocol. Background bridge: the SM-DPN abstraction and single-indexed LTL protocol provide a formal-verification reference for code that an RSI system may rewrite. Use only with this explicit bridge and the stated abstraction boundaries; this is not empirical evidence of agent capability improvement.

### 与 RSI 的具体关系

- Background bridge: the SM-DPN abstraction and single-indexed LTL protocol provide a formal-verification reference for code that an RSI system may rewrite. Use only with this explicit bridge and the stated abstraction boundaries; this is not empirical evidence of agent capability improvement.

## 2. 论文的核心内容与贡献

### role:b570_04_role_wf_e89fb495d022538fd1
The actual author-hosted manuscript studies LTL analysis of concurrent self-modifying programs using SM-DPNs. Its Python experiments compare direct analysis with translation to DPNs, and its application is malware detection. Runtime code mutation is the research object; the reviewed work supplies no capability-improving agent succession protocol.

**适用版本**：author-hosted unversioned manuscript, retrieved 2026-10-19；**原文定位**：Abstract: SM-DPN and single-indexed LTL; PDF p1; derived text lines 9-18 (one-based local extraction, not web-tool lines)；4.1 Experimental comparison and units; PDF p17; derived text lines 3-15 (one-based local extraction, not web-tool lines)；5 Conclusion: actual scope; PDF p19; derived text lines 18-29 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_04_ev_wf_e89fb495d022538fd1`**：The actual author-hosted manuscript studies LTL analysis of concurrent self-modifying programs using SM-DPNs. Its Python experiments compare direct analysis with translation to DPNs, and its application is malware detection. Runtime code mutation is the research object; the reviewed work supplies no capability-improving agent succession protocol.
  - 来源版本：author-hosted unversioned manuscript, retrieved 2026-10-19；定位：Abstract: SM-DPN and single-indexed LTL; PDF p1; derived text lines 9-18 (one-based local extraction, not web-tool lines)；4.1 Experimental comparison and units; PDF p17; derived text lines 3-15 (one-based local extraction, not web-tool lines)；5 Conclusion: actual scope; PDF p19; derived text lines 18-29 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Abstract: SM-DPN and single-indexed LTL
**来源**：https://www.irif.fr/~zhangeldinov/papers/ltl_mc_smdpn.pdf  
**实际版本**：author-hosted unversioned manuscript, retrieved 2026-10-19  
**精确定位**：PDF p1; derived text lines 9-18 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_e89fb495d022538fd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · 4.1 Experimental comparison and units
**来源**：https://www.irif.fr/~zhangeldinov/papers/ltl_mc_smdpn.pdf  
**实际版本**：author-hosted unversioned manuscript, retrieved 2026-10-19  
**精确定位**：PDF p17; derived text lines 3-15 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_e89fb495d022538fd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · 5 Conclusion: actual scope
**来源**：https://www.irif.fr/~zhangeldinov/papers/ltl_mc_smdpn.pdf  
**实际版本**：author-hosted unversioned manuscript, retrieved 2026-10-19  
**精确定位**：PDF p19; derived text lines 18-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_04_ev_wf_e89fb495d022538fd1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Single-indexed LTL formulas and the declared SM-DPN abstraction delimit the verification problem. Program mutation and malware detection do not alone establish recursive capability improvement. The cached 26-page author manuscript is not asserted to be byte-identical to the Springer chapter or a later journal version.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_04_src_wf_e89fb495d022538fd1` · LTL Model Checking of Concurrent Self Modifying Code · author-hosted unversioned manuscript, retrieved 2026-10-19
  - https://www.irif.fr/~zhangeldinov/papers/ltl_mc_smdpn.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e89fb495d022538fd1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
