# Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero

> 方法论文 · 2026 · `wf_62b4bbaa99be14d657`

**作者**：Zipei Yu, Yue-Jiao Gong, Zeyuan Ma, Yuncheng Jiang, Zhiguang Cao  
**原文**：https://arxiv.org/abs/2609.35328  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
HADA samples projects from an algorithm evolution tree; hyper agent can edit task-agent and its own files, then task agent edits the MetaBBO project. Training/evaluation logs and scores guide later iterations. Explicit meta-improver self-modification is allowed while projects and execution records persist. Evidence supports bounded recursive design search.

### 与 RSI 的具体关系

- Explicit meta-improver self-modification is allowed while projects and execution records persist. Evidence supports bounded recursive design search.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_62b4bbaa99be14d657
HADA samples projects from an algorithm evolution tree; hyper agent can edit task-agent and its own files, then task agent edits the MetaBBO project. Training/evaluation logs and scores guide later iterations.

**适用版本**：2609.35328v1；**原文定位**：Project and hyper-to-task archive update; PDF physical page 4, derived page-text lines 10-41 (one-based local extraction, not web-tool lines)；Execution feedback and aggregation; PDF physical page 5, derived page-text lines 32-44 (one-based local extraction, not web-tool lines)；Proxy/final scope; PDF physical page 6, derived page-text lines 17-35 (one-based local extraction, not web-tool lines)；Adaptation boundary; PDF physical page 9, derived page-text lines 34-41 (one-based local extraction, not web-tool lines)；Domain scoring; PDF physical page 6, derived page-text lines 23-34 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Instance/run gives a domain-dependent score aggregated across problems/runs. Constrained infeasibility maps to zero; multiobjective scoring uses normalized hypervolume. Proxy and final budgets differ.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_62b4bbaa99be14d657`**：HADA samples projects from an algorithm evolution tree; hyper agent can edit task-agent and its own files, then task agent edits the MetaBBO project. Training/evaluation logs and scores guide later iterations.
  - 来源版本：2609.35328v1；定位：Project and hyper-to-task archive update; PDF physical page 4, derived page-text lines 10-41 (one-based local extraction, not web-tool lines)；Execution feedback and aggregation; PDF physical page 5, derived page-text lines 32-44 (one-based local extraction, not web-tool lines)；Proxy/final scope; PDF physical page 6, derived page-text lines 17-35 (one-based local extraction, not web-tool lines)；Adaptation boundary; PDF physical page 9, derived page-text lines 34-41 (one-based local extraction, not web-tool lines)；Domain scoring; PDF physical page 6, derived page-text lines 23-34 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Project and hyper-to-task archive update
**来源**：https://arxiv.org/pdf/2609.35328v1  
**实际版本**：2609.35328v1  
**精确定位**：PDF physical page 4, derived page-text lines 10-41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_62b4bbaa99be14d657`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Execution feedback and aggregation
**来源**：https://arxiv.org/pdf/2609.35328v1  
**实际版本**：2609.35328v1  
**精确定位**：PDF physical page 5, derived page-text lines 32-44 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_62b4bbaa99be14d657`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Domain scoring
**来源**：https://arxiv.org/pdf/2609.35328v1  
**实际版本**：2609.35328v1  
**精确定位**：PDF physical page 6, derived page-text lines 23-34 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_62b4bbaa99be14d657`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Proxy/final scope
**来源**：https://arxiv.org/pdf/2609.35328v1  
**实际版本**：2609.35328v1  
**精确定位**：PDF physical page 6, derived page-text lines 17-35 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_62b4bbaa99be14d657`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Adaptation boundary
**来源**：https://arxiv.org/pdf/2609.35328v1  
**实际版本**：2609.35328v1  
**精确定位**：PDF physical page 9, derived page-text lines 34-41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_62b4bbaa99be14d657`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Study covers specified optimization domains and a 100-step horizon. Cheap five-epoch/five-run proxy evaluation differs from twenty-epoch/ten-run final evaluation; cross-domain adaptation continues evolution from an earlier optimum, not zero-shot transfer.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_62b4bbaa99be14d657` · Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero · 2609.35328v1
  - https://arxiv.org/pdf/2609.35328v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No certification of edited evaluator invariance or specific evolved projects; superiority unreplicated.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_62b4bbaa99be14d657 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
