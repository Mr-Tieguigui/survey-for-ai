# Self-Modifying Morphology Experiments with DyRET: Dynamic Robot for Embodied Testing

> 方法论文 · 2018 · `wf_9f2516ddeb83a94d17`

**作者**：Tønnes F. Nygaard, Charles P. Martin, Jim Torresen, Kyrre Glette  
**原文**：https://arxiv.org/abs/1803.05629  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
DyRET exposes interchangeable ROS modules and adjustable legs. Experiments compare two morphologies with manually designed controllers under voltage/environment changes, using physical walking speed as outcome. Embodied RSI background separating substrate/morphology changes from learner/improvement-policy changes; supports morphology-control attribution.

### 与 RSI 的具体关系

- Embodied RSI background separating substrate/morphology changes from learner/improvement-policy changes; supports morphology-control attribution.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_9f2516ddeb83a94d17
DyRET exposes interchangeable ROS modules and adjustable legs. Experiments compare two morphologies with manually designed controllers under voltage/environment changes, using physical walking speed as outcome.

**适用版本**：arXiv:1803.05629v1；**原文定位**：Manual gait and morphology design; PDF p4; derived text lines 69-98 (one-based local extraction, not web-tool lines)；Lab trial unit; PDF p5; derived text lines 26-35 (one-based local extraction, not web-tool lines)；Field-testing limits; PDF p6; derived text lines 41-50 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_9f2516ddeb83a94d17`
DyRET 是可调整腿长的实体四足机器人，摘要比较控制器与形态组合在供电和环境变化下的表现；身体重构不能直接等同改进算法自改，需明确其具身相邻用途。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Gait-morphology pair: 1.5m forward/backward walking repeated 10 times at two voltages; 30s field trials with only two garage/three outdoor replicates. Speed unit m/min.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_9f2516ddeb83a94d17`**：DyRET 是可调整腿长的实体四足机器人，摘要比较控制器与形态组合在供电和环境变化下的表现；身体重构不能直接等同改进算法自改，需明确其具身相邻用途。
  - 来源版本：1803.05629v4；定位：Atom entry http://arxiv.org/abs/1803.05629v4；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_9f2516ddeb83a94d17`**：DyRET exposes interchangeable ROS modules and adjustable legs. Experiments compare two morphologies with manually designed controllers under voltage/environment changes, using physical walking speed as outcome.
  - 来源版本：arXiv:1803.05629v1；定位：Manual gait and morphology design; PDF p4; derived text lines 69-98 (one-based local extraction, not web-tool lines)；Lab trial unit; PDF p5; derived text lines 26-35 (one-based local extraction, not web-tool lines)；Field-testing limits; PDF p6; derived text lines 41-50 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Manual gait and morphology design
**来源**：https://arxiv.org/pdf/1803.05629v1  
**实际版本**：arXiv:1803.05629v1  
**精确定位**：PDF p4; derived text lines 69-98 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_9f2516ddeb83a94d17`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Lab trial unit
**来源**：https://arxiv.org/pdf/1803.05629v1  
**实际版本**：arXiv:1803.05629v1  
**精确定位**：PDF p5; derived text lines 26-35 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_9f2516ddeb83a94d17`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Field-testing limits
**来源**：https://arxiv.org/pdf/1803.05629v1  
**实际版本**：arXiv:1803.05629v1  
**精确定位**：PDF p6; derived text lines 41-50 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_9f2516ddeb83a94d17`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Field tests are preliminary and the authors request more environments/evaluations. Hand-designed gaits and reconfigurable mechanics do not establish an autonomous optimizer rewriting its improvement procedure.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_9f2516ddeb83a94d17` · Self-Modifying Morphology Experiments with DyRET: Dynamic Robot for Embodied Testing · arXiv:1803.05629v1
  - https://arxiv.org/pdf/1803.05629v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**仍未核准的内容**：

- Autonomous morphology-selection learning and recursive selector update are not demonstrated.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_9f2516ddeb83a94d17 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
