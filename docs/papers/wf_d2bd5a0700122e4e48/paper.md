# EXTRACT: Efficient Policy Learning by Extracting Transferable Robot Skills from Offline Data

> 方法论文 · 2024 · `wf_d2bd5a0700122e4e48`

**作者**：Jesse Zhang, Minho Heo, Zuxin Liu, Erdem Biyik, Joseph J Lim, Yao Liu, Rasool Fakoor  
**原文**：https://arxiv.org/abs/2406.17768  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：EXTRACT: Efficient Policy Learning by Extracting Transferrable Robot Skills from Offline Data。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
EXTRACT learns discrete skills with continuous arguments from offline visual trajectories, freezes a low-level decoder, and learns a skill-selection/argument policy online. Transfer experiments use image observations/sparse rewards in Kitchen and LIBERO. RSI skill-library background separating frozen reusable skills from feedback-updated selection; offline library training is not recursive revision of its extractor.

### 与 RSI 的具体关系

- RSI skill-library background separating frozen reusable skills from feedback-updated selection; offline library training is not recursive revision of its extractor.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_d2bd5a0700122e4e48
EXTRACT learns discrete skills with continuous arguments from offline visual trajectories, freezes a low-level decoder, and learns a skill-selection/argument policy online. Transfer experiments use image observations/sparse rewards in Kitchen and LIBERO.

**适用版本**：arXiv:2406.17768v1；**原文定位**：Fine-tuning and online policy; PDF p5; derived text lines 47-59 (one-based local extraction, not web-tool lines)；Kitchen/LIBERO protocol; PDF p6; derived text lines 36-55 (one-based local extraction, not web-tool lines)；Data and modality limits; PDF p8; derived text lines 58-65 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_d2bd5a0700122e4e48`
EXTRACT 用预训练视觉语言模型从离线数据抽取带连续参数的语义技能，下游学习何时选技能及调参数；属于技能复用方法，不是社会影响，也未从摘要确认技能库或改进器被循环升级。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Kitchen four-subtask sequence with reward1 per completion; LIBERO four suites of ten tasks, 50 target demos/task then RL. Outcome is return/success versus interactions, not accepted generations.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_d2bd5a0700122e4e48`**：EXTRACT 用预训练视觉语言模型从离线数据抽取带连续参数的语义技能，下游学习何时选技能及调参数；属于技能复用方法，不是社会影响，也未从摘要确认技能库或改进器被循环升级。
  - 来源版本：2406.17768v3；定位：Atom entry http://arxiv.org/abs/2406.17768v3；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_d2bd5a0700122e4e48`**：EXTRACT learns discrete skills with continuous arguments from offline visual trajectories, freezes a low-level decoder, and learns a skill-selection/argument policy online. Transfer experiments use image observations/sparse rewards in Kitchen and LIBERO.
  - 来源版本：arXiv:2406.17768v1；定位：Fine-tuning and online policy; PDF p5; derived text lines 47-59 (one-based local extraction, not web-tool lines)；Kitchen/LIBERO protocol; PDF p6; derived text lines 36-55 (one-based local extraction, not web-tool lines)；Data and modality limits; PDF p8; derived text lines 58-65 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Fine-tuning and online policy
**来源**：https://arxiv.org/pdf/2406.17768v1  
**实际版本**：arXiv:2406.17768v1  
**精确定位**：PDF p5; derived text lines 47-59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d2bd5a0700122e4e48`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Kitchen/LIBERO protocol
**来源**：https://arxiv.org/pdf/2406.17768v1  
**实际版本**：arXiv:2406.17768v1  
**精确定位**：PDF p6; derived text lines 36-55 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d2bd5a0700122e4e48`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Data and modality limits
**来源**：https://arxiv.org/pdf/2406.17768v1  
**实际版本**：arXiv:2406.17768v1  
**精确定位**：PDF p8; derived text lines 58-65 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d2bd5a0700122e4e48`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Needs initial data from similar environments; cross-robot/modal transfer is limited. LIBERO additionally uses 50 target demonstrations per task before RL; this is not zero-demonstration self-improvement.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_d2bd5a0700122e4e48` · EXTRACT: Efficient Policy Learning by Extracting Transferrable Robot Skills from Offline Data · arXiv:2406.17768v1
  - https://arxiv.org/pdf/2406.17768v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18ctx_role_src_bee1778dc88c5a5a` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3Alearning+OR+ti%3Aevolution+OR+ti%3Aadaptive%29+AND+%28ti%3Amemory+OR+ti%3Askill%29+AND+%28all%3Aagent+OR+all%3ALLM%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=600&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**仍未核准的内容**：

- Cross-robot, substantially different environment and other modality transfer remain unestablished.

**证据深度**：selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d2bd5a0700122e4e48 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
