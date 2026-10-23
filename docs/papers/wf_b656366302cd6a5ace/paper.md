# What is Missing from AI Post-Training AI: An Empirical Analysis

> 实证/审计/复现 · 2026 · `wf_b656366302cd6a5ace`

**作者**：Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong, Zhong Zhang, Maosong Sun, Yankai Lin  
**原文**：https://arxiv.org/abs/2608.19072  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The paper separates strategy revision from execution changes in 1,338 released PostTrainBench trajectories; an experiment requires an executed parameter update. Observational analysis uses no reruns. Separate three-run Qwen3-1.7B interventions add journals, skills, evaluator feedback and planning guidance. The supported distinction is effective execution feedback versus weak spontaneous strategy reopening. Direct AI-post-training-AI boundary: execution loops can improve models while strategy selection fails to reopen.

### 与 RSI 的具体关系

- Direct AI-post-training-AI boundary: execution loops can improve models while strategy selection fails to reopen.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_b656366302cd6a5ace
The paper separates strategy revision from execution changes in 1,338 released PostTrainBench trajectories; an experiment requires an executed parameter update. Observational analysis uses no reruns. Separate three-run Qwen3-1.7B interventions add journals, skills, evaluator feedback and planning guidance. The supported distinction is effective execution feedback versus weak spontaneous strategy reopening.

**适用版本**：2608.19072v1；**原文定位**：§2 Definitions and annotation; PDF p3; derived page text lines 2–45 (one-based local extraction, not web-tool lines)；§4 Controlled setting; PDF p5; derived page text lines 7–16 (one-based local extraction, not web-tool lines)；§4.1 Journal/skills/evaluator; PDF p5; derived page text lines 18–47 (one-based local extraction, not web-tool lines)；§5.1 Execution/strategy distinction; PDF p9; derived page text lines 44–59 (one-based local extraction, not web-tool lines)；§2.2 Evaluation uncertainty; PDF p3; derived page text lines 33–40 (one-based local extraction, not web-tool lines)；§4.2 Guidance/uncertainty; PDF p8; derived page text lines 36–57 (one-based local extraction, not web-tool lines)；§4.3 Compute ceiling; PDF p9; derived page text lines 4–14 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_b656366302cd6a5ace`**：The paper separates strategy revision from execution changes in 1,338 released PostTrainBench trajectories; an experiment requires an executed parameter update. Observational analysis uses no reruns. Separate three-run Qwen3-1.7B interventions add journals, skills, evaluator feedback and planning guidance. The supported distinction is effective execution feedback versus weak spontaneous strategy reopening.
  - 来源版本：2608.19072v1；定位：§2 Definitions and annotation; PDF p3; derived page text lines 2–45 (one-based local extraction, not web-tool lines)；§4 Controlled setting; PDF p5; derived page text lines 7–16 (one-based local extraction, not web-tool lines)；§4.1 Journal/skills/evaluator; PDF p5; derived page text lines 18–47 (one-based local extraction, not web-tool lines)；§5.1 Execution/strategy distinction; PDF p9; derived page text lines 44–59 (one-based local extraction, not web-tool lines)；§2.2 Evaluation uncertainty; PDF p3; derived page text lines 33–40 (one-based local extraction, not web-tool lines)；§4.2 Guidance/uncertainty; PDF p8; derived page text lines 36–57 (one-based local extraction, not web-tool lines)；§4.3 Compute ceiling; PDF p9; derived page text lines 4–14 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2 Definitions and annotation
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p3; derived page text lines 2–45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §4 Controlled setting
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p5; derived page text lines 7–16 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §4.1 Journal/skills/evaluator
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p5; derived page text lines 18–47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 机制 / 定义 · §5.1 Execution/strategy distinction
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p9; derived page text lines 44–59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · §2.2 Evaluation uncertainty
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p3; derived page text lines 33–40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 6 · 限制 · §4.2 Guidance/uncertainty
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p8; derived page text lines 36–57 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 7 · 限制 · §4.3 Compute ceiling
**来源**：https://arxiv.org/pdf/2608.19072v1  
**实际版本**：2608.19072v1  
**精确定位**：PDF p9; derived page text lines 4–14 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_b656366302cd6a5ace`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- LLM trajectory labels are author-reviewed; observational and intervention hardware differ. AIME has 30 problems and pass@8 best-run differences are interpreted qualitatively within evaluation variance. Initial human guidance does not establish sustained autonomous strategy revision; extra tokens/iterations do not imply recursive acceleration or universal strategic incapacity.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_b656366302cd6a5ace` · What is Missing from AI Post-Training AI: An Empirical Analysis · 2608.19072v1
  - https://arxiv.org/pdf/2608.19072v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b656366302cd6a5ace --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
