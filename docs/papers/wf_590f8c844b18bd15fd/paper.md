# The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

> 实证/审计/复现 · 2026 · `wf_590f8c844b18bd15fd`

**作者**：Seth Dobrin, Łukasz Chmiel  
**原文**：https://arxiv.org/abs/2606.26057  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The Unfireable Safety Kernel mediates actions outside an untrusted runtime using process separation, pre-action enforcement, fail-closed behavior and signed evidence. The body reports deterministic Python/Rust equivalence fixtures, adversarial authorization tests, Z3 model and production gate-decision Kani harnesses, and containment tests on one self-modifying application replica. These are kernel-specific author tests/proofs. Direct governance bridge: persistent self-modification requires action authorization; containment differs from capability improvement.

### 与 RSI 的具体关系

- Direct governance bridge: persistent self-modification requires action authorization; containment differs from capability improvement.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_590f8c844b18bd15fd
The Unfireable Safety Kernel mediates actions outside an untrusted runtime using process separation, pre-action enforcement, fail-closed behavior and signed evidence. The body reports deterministic Python/Rust equivalence fixtures, adversarial authorization tests, Z3 model and production gate-decision Kani harnesses, and containment tests on one self-modifying application replica. These are kernel-specific author tests/proofs.

**适用版本**：2606.26057v1；**原文定位**：Contributions and threat model; PDF p3; derived page text lines 2–37 (one-based local extraction, not web-tool lines)；§6.1 Migration equivalence; PDF p9; derived page text lines 12–43 (one-based local extraction, not web-tool lines)；§6.4 Machine-checked invariant; PDF p12; derived page text lines 19–47 (one-based local extraction, not web-tool lines)；§6.5 Containment; PDF p13; derived page text lines 6–30 (one-based local extraction, not web-tool lines)；§8.3 Partial formal verification; PDF p21; derived page text lines 24–27 (one-based local extraction, not web-tool lines)；§8.3 Limitations and future work; PDF p22; derived page text lines 1–31 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_590f8c844b18bd15fd`**：The Unfireable Safety Kernel mediates actions outside an untrusted runtime using process separation, pre-action enforcement, fail-closed behavior and signed evidence. The body reports deterministic Python/Rust equivalence fixtures, adversarial authorization tests, Z3 model and production gate-decision Kani harnesses, and containment tests on one self-modifying application replica. These are kernel-specific author tests/proofs.
  - 来源版本：2606.26057v1；定位：Contributions and threat model; PDF p3; derived page text lines 2–37 (one-based local extraction, not web-tool lines)；§6.1 Migration equivalence; PDF p9; derived page text lines 12–43 (one-based local extraction, not web-tool lines)；§6.4 Machine-checked invariant; PDF p12; derived page text lines 19–47 (one-based local extraction, not web-tool lines)；§6.5 Containment; PDF p13; derived page text lines 6–30 (one-based local extraction, not web-tool lines)；§8.3 Partial formal verification; PDF p21; derived page text lines 24–27 (one-based local extraction, not web-tool lines)；§8.3 Limitations and future work; PDF p22; derived page text lines 1–31 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Contributions and threat model
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p3; derived page text lines 2–37 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §6.1 Migration equivalence
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p9; derived page text lines 12–43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §6.4 Machine-checked invariant
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p12; derived page text lines 19–47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 机制 / 定义 · §6.5 Containment
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p13; derived page text lines 6–30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §8.3 Partial formal verification
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p21; derived page text lines 24–27 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · §8.3 Limitations and future work
**来源**：https://arxiv.org/pdf/2606.26057v1  
**实际版本**：2606.26057v1  
**精确定位**：PDF p22; derived page text lines 1–31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_590f8c844b18bd15fd`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Fail-closed decision verification does not cover signing, Merkle-log or policy surfaces. Signing-key secrecy and policy environment integrity are untested assumptions. No external red team; saturation behavior and a formal policy deciding which modifications are permitted remain open. One loop/application does not establish semantic alignment or capability improvement.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_590f8c844b18bd15fd` · The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems · 2606.26057v1
  - https://arxiv.org/pdf/2606.26057v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_590f8c844b18bd15fd --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
