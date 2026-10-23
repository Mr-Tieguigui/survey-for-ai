# ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents

> 方法论文 · 2026 · `wf_e315e47d10c491f100`

**作者**：Shuhan Xue, Jianyuan Zhong, Ziyuan Nan, Wenbin Li, Zhaochen Yu, Jinchao Ding, Qiang Gao, Pengyu Zhan, Yuntong Zhang, Tian Cheng, Zhenfei Yin, Yingcheng Wu, Ling Yang  
**原文**：https://arxiv.org/abs/2609.17523  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ScienceBuddy couples bounded, feedback-guided harness revision with outer rubric-supervised model learning. A fixed auxiliary model diagnoses traces and proposes scoped procedural edits; matched development evaluation admits only valid positive-score candidates. Selected harnesses generate new policy-training trajectories, and model updates are reevaluated with the harness before further interaction. Direct RSI bridge: accepted harness changes persist, and updated policy weights return to later harness-adaptation cycles. Inner proposal rounds are distinct from accepted children.

### 与 RSI 的具体关系

- Direct RSI bridge: accepted harness changes persist, and updated policy weights return to later harness-adaptation cycles. Inner proposal rounds are distinct from accepted children.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_e315e47d10c491f100
ScienceBuddy couples bounded, feedback-guided harness revision with outer rubric-supervised model learning. A fixed auxiliary model diagnoses traces and proposes scoped procedural edits; matched development evaluation admits only valid positive-score candidates. Selected harnesses generate new policy-training trajectories, and model updates are reevaluated with the harness before further interaction.

**适用版本**：2609.17523v1；**原文定位**：fixed-model diagnosis; PDF physical page 8, derived page-text lines 25-30 (one-based local extraction, not web-tool lines)；outer rubric/GRPO protocol; PDF physical page 9, derived page-text lines 31-34 (one-based local extraction, not web-tool lines)；model-to-harness feedback; PDF physical page 9, derived page-text lines 51-55 (one-based local extraction, not web-tool lines)；bounded edit scope and fixed components; PDF physical page 8, derived page-text lines 34-38 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Paired parent/candidate mean normalized rubric score on matched development tasks, seeds and execution budgets; outer reward is a fixed weighted task-rubric aggregate. Final held-out tasks do not guide edits.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_e315e47d10c491f100`**：ScienceBuddy couples bounded, feedback-guided harness revision with outer rubric-supervised model learning. A fixed auxiliary model diagnoses traces and proposes scoped procedural edits; matched development evaluation admits only valid positive-score candidates. Selected harnesses generate new policy-training trajectories, and model updates are reevaluated with the harness before further interaction.
  - 来源版本：2609.17523v1；定位：fixed-model diagnosis; PDF physical page 8, derived page-text lines 25-30 (one-based local extraction, not web-tool lines)；outer rubric/GRPO protocol; PDF physical page 9, derived page-text lines 31-34 (one-based local extraction, not web-tool lines)；model-to-harness feedback; PDF physical page 9, derived page-text lines 51-55 (one-based local extraction, not web-tool lines)；bounded edit scope and fixed components; PDF physical page 8, derived page-text lines 34-38 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · fixed-model diagnosis
**来源**：https://arxiv.org/pdf/2609.17523v1  
**实际版本**：2609.17523v1  
**精确定位**：PDF physical page 8, derived page-text lines 25-30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e315e47d10c491f100`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · outer rubric/GRPO protocol
**来源**：https://arxiv.org/pdf/2609.17523v1  
**实际版本**：2609.17523v1  
**精确定位**：PDF physical page 9, derived page-text lines 31-34 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e315e47d10c491f100`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · model-to-harness feedback
**来源**：https://arxiv.org/pdf/2609.17523v1  
**实际版本**：2609.17523v1  
**精确定位**：PDF physical page 9, derived page-text lines 51-55 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e315e47d10c491f100`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · bounded edit scope and fixed components
**来源**：https://arxiv.org/pdf/2609.17523v1  
**实际版本**：2609.17523v1  
**精确定位**：PDF physical page 8, derived page-text lines 34-38 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e315e47d10c491f100`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Inner-loop task and editor models, tools, execution infrastructure, rubrics and evaluators stay fixed; this still permits persistent harness feedback and selection. Historical answers or researcher approval are not scientific ground truth. Selected evidence establishes the proposed protocol, not sustained acceleration or an unrestricted autonomous scientist.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_e315e47d10c491f100` · ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents · 2609.17523v1
  - https://arxiv.org/pdf/2609.17523v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Long-term coupled-cycle gains and full experimental configuration remain pending.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e315e47d10c491f100 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
