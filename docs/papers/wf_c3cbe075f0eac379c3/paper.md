# On First-Order Meta-Learning Algorithms

> 方法论文 · 2018 · `wf_c3cbe075f0eac379c3`

**作者**：Alex Nichol, Joshua Achiam, John Schulman  
**原文**：https://arxiv.org/abs/1803.02999  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Reptile: a Scalable Metalearning Algorithm。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
Cached v1 is Reptile: sample a task, train task weights with SGD, then move a shared initialization toward them. Few-shot classification tests adaptation of the initialization to a newly sampled task. RSI foundation for outer-loop improvement of adaptation ability; distinguishes a learned initial condition from a self-modified learning algorithm.

### 与 RSI 的具体关系

- RSI foundation for outer-loop improvement of adaptation ability; distinguishes a learned initial condition from a self-modified learning algorithm.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_c3cbe075f0eac379c3
Cached v1 is Reptile: sample a task, train task weights with SGD, then move a shared initialization toward them. Few-shot classification tests adaptation of the initialization to a newly sampled task.

**适用版本**：arXiv:1803.02999v1；**原文定位**：Reptile serial update; PDF p2; derived text lines 20-39 (one-based local extraction, not web-tool lines)；Few-shot task protocol; PDF p6; derived text lines 46-55 (one-based local extraction, not web-tool lines)；Task-distribution assumption; PDF p10; derived text lines 10-22 (one-based local extraction, not web-tool lines)；Displayed update algebra sign conflict; PDF p6; derived text lines 33-45 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_c3cbe075f0eac379c3`
Reptile 与一阶 MAML 属学习可快速微调初始化的元学习方法，Reptile 采样任务训练后把初始化移向任务权重；是重要元学习邻接基础，但外层算法固定不能仅凭元学习认作递归改进器自改。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

K-shot N-way task sampled from classes with training examples and one held-out test example per class; score is held-out classification accuracy after adaptation.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_c3cbe075f0eac379c3`**：Reptile 与一阶 MAML 属学习可快速微调初始化的元学习方法，Reptile 采样任务训练后把初始化移向任务权重；是重要元学习邻接基础，但外层算法固定不能仅凭元学习认作递归改进器自改。
  - 来源版本：1803.02999v3；定位：Atom entry http://arxiv.org/abs/1803.02999v3；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_c3cbe075f0eac379c3`**：Cached v1 is Reptile: sample a task, train task weights with SGD, then move a shared initialization toward them. Few-shot classification tests adaptation of the initialization to a newly sampled task.
  - 来源版本：arXiv:1803.02999v1；定位：Reptile serial update; PDF p2; derived text lines 20-39 (one-based local extraction, not web-tool lines)；Few-shot task protocol; PDF p6; derived text lines 46-55 (one-based local extraction, not web-tool lines)；Task-distribution assumption; PDF p10; derived text lines 10-22 (one-based local extraction, not web-tool lines)；Displayed update algebra sign conflict; PDF p6; derived text lines 33-45 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Reptile serial update
**来源**：https://arxiv.org/pdf/1803.02999v1  
**实际版本**：arXiv:1803.02999v1  
**精确定位**：PDF p2; derived text lines 20-39 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_c3cbe075f0eac379c3`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Few-shot task protocol
**来源**：https://arxiv.org/pdf/1803.02999v1  
**实际版本**：arXiv:1803.02999v1  
**精确定位**：PDF p6; derived text lines 46-55 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_c3cbe075f0eac379c3`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Task-distribution assumption
**来源**：https://arxiv.org/pdf/1803.02999v1  
**实际版本**：arXiv:1803.02999v1  
**精确定位**：PDF p10; derived text lines 10-22 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_c3cbe075f0eac379c3`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 冲突 · Displayed update algebra sign conflict
**来源**：https://arxiv.org/pdf/1803.02999v1  
**实际版本**：arXiv:1803.02999v1  
**精确定位**：PDF p6; derived text lines 33-45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_c3cbe075f0eac379c3`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Assumes a training distribution of tasks. A fixed update algorithm can yield bounded meta-learning improvements; it does not demonstrate autonomous redesign of the optimizer.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

存在已存冲突或待核证据；请保留各版本和判断，不自行合并为确定结论：

- b570_06_ev_wf_c3cbe075f0eac379c3

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_c3cbe075f0eac379c3` · Reptile: a Scalable Metalearning Algorithm · arXiv:1803.02999v1
  - https://arxiv.org/pdf/1803.02999v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18ctx_role_src_36dcd0fd301066b1` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=1711.03938%2C1711.03953%2C1711.04340%2C1711.05101%2C1711.07414%2C1711.09846%2C1711.09883%2C1712.01815%2C1712.06567%2C1712.07040%2C1801.02668%2C1801.10314%2C1802.06070%2C1802.07569%2C1803.02999%2C1803.03453%2C1803.04585%2C1803.05457%2C1803.10122%2C1804.03980%2C1804.06893%2C1805.00899%2C1805.01109%2C1805.09613%2C1805.11604%2C1805.11973%2C1805.12069%2C1805.12114%2C1806.00178%2C1806.01261%2C1806.07937%2C1806.08730%2C1806.09030%2C1807.00734%2C1807.05076%2C1808.08745%2C1808.09422%2C1808.09468%2C1809.02156%2C1809.07124%2C1809.09600%2C1809.11096%2C1810.00069%2C1810.00123%2C1810.04805%2C1810.07074%2C1810.08272%2C1810.10535%2C1810.10863%2C1811.00739%2C1811.01241%2C1811.07871%2C1811.08886%2C1812.01070%2C1812.01825%2C1812.08775%2C1812.10757%2C1901.02860%2C1901.09492%2C1901.10995%2C1902.03689%2C1902.04043%2C1902.06705%2C1902.07638%2C1902.09469%2C1903.00161%2C1903.06733%2C1903.08772%2C1903.09848%2C1903.10145%2C1903.12261%2C1904.07734%2C1904.09675%2C1904.09728%2C1904.10509%2C1904.12901%2C1905.01386%2C1905.07830%2C1905.09717%2C1905.10044%2C1905.10847%2C1905.10985%2C1905.13053%2C1906.02243%2C1906.05015%2C1906.08253%2C1906.08663%2C1906.11951%2C1907.00909%2C1907.03651%2C1907.09190%2C1907.11692%2C1907.12108%2C1908.04734%2C1908.10084%2C1909.01095%2C1909.02622%2C1909.03848%2C1909.06146%2C1909.06576&max_results=100；阅读深度：`未单列`。

**仍未核准的内容**：

- PDF p6 Eq22 has a sign inconsistent with Algorithm1 and Eq23; algorithm identity is clear but that displayed algebra is pending.

**证据深度**：selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c3cbe075f0eac379c3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
