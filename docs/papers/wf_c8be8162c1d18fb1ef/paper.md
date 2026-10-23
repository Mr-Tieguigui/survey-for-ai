# EVALOOOP: A Self-Consistency-Centered Framework for Assessing Large Language Model Robustness in Programming

> 评测方法/测量科学 · 2025 · `wf_c8be8162c1d18fb1ef`

**作者**：Sen Fang, Weiyuan Ding, Mengshi Zhang, Zihao Chen, Bowen Xu  
**原文**：https://arxiv.org/abs/2505.12185  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：EvaLoop: Assessing LLM Robustness in Programming from a Self-consistency Perspective (https://arxiv.org/html/2505.12185v1)。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
EvaLoop measures semantic robustness through generation→test→summary→new-prompt cycles or a code-translation chain, stopping at functional failure. It uses pass@1 and average sustainable loops across378 MBPP Plus tasks (max10 loops) and375 MXEVAL tasks in a Python→JavaScript→PHP→Ruby→Perl→Python chain. Optional RSI evaluation background for degradation under iterative artifacts; test-gated cycling alone is not evidence of recursive capability gain.

### 与 RSI 的具体关系

- Optional RSI evaluation background for degradation under iterative artifacts; test-gated cycling alone is not evidence of recursive capability gain.

## 2. 论文的核心内容与贡献

### role:b570_02_role_wf_c8be8162c1d18fb1ef
EvaLoop measures semantic robustness through generation→test→summary→new-prompt cycles or a code-translation chain, stopping at functional failure. It uses pass@1 and average sustainable loops across378 MBPP Plus tasks (max10 loops) and375 MXEVAL tasks in a Python→JavaScript→PHP→Ruby→Perl→Python chain.

**适用版本**：2505.12185v1；**原文定位**：§2.1 generation-summary loop and stopping rule tool L127–147；§3 actual scoring, task counts and chain tool L176–183；§3 diagnostic interpretation boundary tool L205–209。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_02_ev_wf_c8be8162c1d18fb1ef`**：EvaLoop measures semantic robustness through generation→test→summary→new-prompt cycles or a code-translation chain, stopping at functional failure. It uses pass@1 and average sustainable loops across378 MBPP Plus tasks (max10 loops) and375 MXEVAL tasks in a Python→JavaScript→PHP→Ruby→Perl→Python chain.
  - 来源版本：2505.12185v1；定位：§2.1 generation-summary loop and stopping rule tool L127–147；§3 actual scoring, task counts and chain tool L176–183；§3 diagnostic interpretation boundary tool L205–209；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2.1 generation-summary loop and stopping rule
**来源**：https://arxiv.org/html/2505.12185v1  
**实际版本**：2505.12185v1  
**精确定位**：tool L127–147  
**关联证据**：`b570_02_ev_wf_c8be8162c1d18fb1ef`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §3 actual scoring, task counts and chain
**来源**：https://arxiv.org/html/2505.12185v1  
**实际版本**：2505.12185v1  
**精确定位**：tool L176–183  
**关联证据**：`b570_02_ev_wf_c8be8162c1d18fb1ef`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · §3 diagnostic interpretation boundary
**来源**：https://arxiv.org/html/2505.12185v1  
**实际版本**：2505.12185v1  
**精确定位**：tool L205–209  
**关联证据**：`b570_02_ev_wf_c8be8162c1d18fb1ef`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The score concerns preserved task semantics over transformations, not improvement of the model or its future improvement mechanism. Results are bounded by these task suites, language chain and10-loop cap; claims about memorization/comprehension in §3 are diagnostic interpretations, not controlled causal identification.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_02_src_wf_c8be8162c1d18fb1ef` · EvaLoop: Assessing LLM Robustness in Programming from a Self-consistency Perspective (https://arxiv.org/html/2505.12185v1) · 2505.12185v1
  - https://arxiv.org/html/2505.12185v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c8be8162c1d18fb1ef --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
