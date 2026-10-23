# Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks

> 方法论文 · 2022 · `wf_b19cf261a8c2db070b`

**作者**：Wenhu Chen, Xueguang Ma, Xinyi Wang, William W. Cohen  
**原文**：https://arxiv.org/abs/2211.12588  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Program of Thoughts binds quantities and composes multi-step Python programs, then uses an interpreter/SymPy for computation; compares few-shot, zero-shot and self-consistency variants on numerical/financial QA. RSI harness background for executable computation/checking; a component useful in research/evaluation loops, but an individual PoT answer is not an RSI iteration.

### 与 RSI 的具体关系

- RSI harness background for executable computation/checking; a component useful in research/evaluation loops, but an individual PoT answer is not an RSI iteration.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_b19cf261a8c2db070b
Program of Thoughts binds quantities and composes multi-step Python programs, then uses an interpreter/SymPy for computation; compares few-shot, zero-shot and self-consistency variants on numerical/financial QA.

**适用版本**：arXiv:2211.12588v1；**原文定位**：Program binding and execution; PDF p3; derived text lines 48-99 (one-based local extraction, not web-tool lines)；Evaluation variants and scores; PDF p6; derived text lines 1-30 (one-based local extraction, not web-tool lines)；Grounding and logic errors; PDF p7; derived text lines 93-112 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_b19cf261a8c2db070b`
Program of Thoughts 把语言模型推理表达为程序并交给外部计算器执行，另结合自一致采样；主要是推理/工具接口基础，未体现改进器或跨任务持久状态更新。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

QA problem and final-answer score per dataset, with separate greedy, self-consistency and zero-shot protocols; program-loop iterations are computation, not self-improvement rounds.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_b19cf261a8c2db070b`**：Program of Thoughts 把语言模型推理表达为程序并交给外部计算器执行，另结合自一致采样；主要是推理/工具接口基础，未体现改进器或跨任务持久状态更新。
  - 来源版本：2211.12588v4；定位：Atom entry http://arxiv.org/abs/2211.12588v4；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_b19cf261a8c2db070b`**：Program of Thoughts binds quantities and composes multi-step Python programs, then uses an interpreter/SymPy for computation; compares few-shot, zero-shot and self-consistency variants on numerical/financial QA.
  - 来源版本：arXiv:2211.12588v1；定位：Program binding and execution; PDF p3; derived text lines 48-99 (one-based local extraction, not web-tool lines)；Evaluation variants and scores; PDF p6; derived text lines 1-30 (one-based local extraction, not web-tool lines)；Grounding and logic errors; PDF p7; derived text lines 93-112 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Program binding and execution
**来源**：https://arxiv.org/pdf/2211.12588v1  
**实际版本**：arXiv:2211.12588v1  
**精确定位**：PDF p3; derived text lines 48-99 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_b19cf261a8c2db070b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Evaluation variants and scores
**来源**：https://arxiv.org/pdf/2211.12588v1  
**实际版本**：arXiv:2211.12588v1  
**精确定位**：PDF p6; derived text lines 1-30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_b19cf261a8c2db070b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Grounding and logic errors
**来源**：https://arxiv.org/pdf/2211.12588v1  
**实际版本**：arXiv:2211.12588v1  
**精确定位**：PDF p7; derived text lines 93-112 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_b19cf261a8c2db070b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Correct execution cannot ensure correct grounding or generated logic; error analysis separates these failure modes. This is inference prompting rather than a recursive system update.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_b19cf261a8c2db070b` · Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks · arXiv:2211.12588v1
  - https://arxiv.org/pdf/2211.12588v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18ctx_role_src_160e7395c4b0e6d6` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2211.11501%2C2211.11890%2C2211.12588%2C2211.12701%2C2211.14275%2C2211.15451%2C2211.15533%2C2211.15914%2C2212.01326%2C2212.03221%2C2212.03533%2C2212.06355%2C2212.07597%2C2212.07769%2C2212.07919%2C2212.08073%2C2212.09251%2C2212.09561%2C2212.09689%2C2212.10001%2C2212.10403%2C2212.10509%2C2212.10947%2C2212.11279%2C2212.13465%2C2212.14024%2C2301.00234%2C2301.02010%2C2301.03740%2C2301.03988%2C2301.04104%2C2301.04589%2C2301.05327%2C2301.08028%2C2301.08727%2C2301.09785%2C2301.12652%2C2302.00083%2C2302.00288%2C2302.00618%2C2302.00785%2C2302.00923%2C2302.01318%2C2302.01560%2C2302.02216%2C2302.02676%2C2302.04166%2C2302.04580%2C2302.04761%2C2302.05446%2C2302.06590%2C2302.06784%2C2302.07842%2C2302.07867%2C2302.08468%2C2302.09248%2C2302.10149%2C2302.12170%2C2302.12173%2C2302.12246%2C2302.12433%2C2302.12813%2C2302.12927%2C2302.13439%2C2302.13971%2C2302.14502%2C2303.03004%2C2303.03885%2C2303.04132%2C2303.04360%2C2303.04671%2C2303.04910%2C2303.06532%2C2303.07678%2C2303.08774%2C2303.08896%2C2303.09014%2C2303.10130%2C2303.10512%2C2303.11366%2C2303.11381%2C2303.12712%2C2303.13217%2C2303.13375%2C2303.13548%2C2303.14070%2C2303.14524%2C2303.14623%2C2303.15056%2C2303.16634%2C2303.17071%2C2303.17491%2C2303.17564%2C2303.17580%2C2303.17760%2C2303.18223%2C2304.00385%2C2304.00612%2C2304.01097%2C2304.01904&max_results=100；阅读深度：`未单列`。

**仍未核准的内容**：

- General autonomous improvement and causal benefits inside RSI are not demonstrated.

**证据深度**：selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b19cf261a8c2db070b --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
