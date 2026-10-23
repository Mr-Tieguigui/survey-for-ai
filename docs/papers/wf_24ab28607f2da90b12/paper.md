# Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

> 方法论文 · 2026 · `wf_24ab28607f2da90b12`

**作者**：Qifan Zhang, Dongyang Ma, Tianqing Fang, Jia Li, Jing Tang, Nuo Chen, Haitao Mi, Yan Wang  
**原文**：https://arxiv.org/abs/2604.18131  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Trains agents to explore a website and create Markdown world knowledge for future task context. Training selects trajectories with labeled-task success gain; inference exploration is task/reward free under the learned policy without weight updates. Direct bounded external-memory adaptation. Two training rejection-sampling iterations are not two accepted inference-time generations or acceleration evidence.

### 与 RSI 的具体关系

- Direct bounded external-memory adaptation. Two training rejection-sampling iterations are not two accepted inference-time generations or acceleration evidence.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_24ab28607f2da90b12
Trains agents to explore a website and create Markdown world knowledge for future task context. Training selects trajectories with labeled-task success gain; inference exploration is task/reward free under the learned policy without weight updates.

**适用版本**：arXiv:2604.18131v1；**原文定位**：Knowledge state and inference phases; PDF p3; derived text lines 25-43 (one-based local extraction, not web-tool lines)；Training reward and labels; PDF p4; derived text lines 43-59 (one-based local extraction, not web-tool lines)；Inference-only reward-free boundary; PDF p5; derived text lines 9-13 (one-based local extraction, not web-tool lines)；Environment/budgets/subset protocol; PDF p6; derived text lines 20-43 (one-based local extraction, not web-tool lines)；Model judge/graph preprocessing; PDF p7; derived text lines 19-39 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Website knowledge artifact/downstream QA trajectory; reward is labeled-task accuracy with knowledge minus baseline. Evaluation uses 1427 filtered queries/model judges; exploration/task budgets differ.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_06_ev_wf_24ab28607f2da90b12`**：Trains agents to explore a website and create Markdown world knowledge for future task context. Training selects trajectories with labeled-task success gain; inference exploration is task/reward free under the learned policy without weight updates.
  - 来源版本：arXiv:2604.18131v1；定位：Knowledge state and inference phases; PDF p3; derived text lines 25-43 (one-based local extraction, not web-tool lines)；Training reward and labels; PDF p4; derived text lines 43-59 (one-based local extraction, not web-tool lines)；Inference-only reward-free boundary; PDF p5; derived text lines 9-13 (one-based local extraction, not web-tool lines)；Environment/budgets/subset protocol; PDF p6; derived text lines 20-43 (one-based local extraction, not web-tool lines)；Model judge/graph preprocessing; PDF p7; derived text lines 19-39 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Knowledge state and inference phases
**来源**：https://arxiv.org/pdf/2604.18131v1  
**实际版本**：arXiv:2604.18131v1  
**精确定位**：PDF p3; derived text lines 25-43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_24ab28607f2da90b12`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Training reward and labels
**来源**：https://arxiv.org/pdf/2604.18131v1  
**实际版本**：arXiv:2604.18131v1  
**精确定位**：PDF p4; derived text lines 43-59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_24ab28607f2da90b12`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Environment/budgets/subset protocol
**来源**：https://arxiv.org/pdf/2604.18131v1  
**实际版本**：arXiv:2604.18131v1  
**精确定位**：PDF p6; derived text lines 20-43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_24ab28607f2da90b12`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 测量 / 结果 · Model judge/graph preprocessing
**来源**：https://arxiv.org/pdf/2604.18131v1  
**实际版本**：arXiv:2604.18131v1  
**精确定位**：PDF p7; derived text lines 19-39 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_24ab28607f2da90b12`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Inference-only reward-free boundary
**来源**：https://arxiv.org/pdf/2604.18131v1  
**实际版本**：arXiv:2604.18131v1  
**精确定位**：PDF p5; derived text lines 9-13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_24ab28607f2da90b12`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Reward-free applies at inference; training uses labels, teacher trajectories and rejection sampling. Website graph/clustering and substantial exploration budgets are engineered inputs; web-subset evidence is not general workflow-free recursion.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_24ab28607f2da90b12` · Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration · arXiv:2604.18131v1
  - https://arxiv.org/pdf/2604.18131v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Unqualified workflow-free/no-human-guidance framing is bounded by teacher, graph preprocessing and labels; unrestricted autonomy is not admitted.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_24ab28607f2da90b12 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
