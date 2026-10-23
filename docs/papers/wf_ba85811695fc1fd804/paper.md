# Innate Motivation for Robot Swarms by Minimizing Surprise: From Simple Simulations to Real-World Experiments

> 方法论文 · 2024 · `wf_ba85811695fc1fd804`

**作者**：Tanja Katharina Kaiser, Heiko Hamann  
**原文**：https://arxiv.org/abs/2405.02579  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Co-evolves fixed-topology actor/predictor ANN weights using sensor prediction accuracy rather than task-specific fitness. Physical experiments use a centralized onboard evolutionary master and online (1+1) selection under bounded evaluation budgets. RSI background for intrinsic feedback, joint behavior/world-model adaptation and evaluator gaming. Fixed topology/GA bounds the loop without erasing online weight evolution.

### 与 RSI 的具体关系

- RSI background for intrinsic feedback, joint behavior/world-model adaptation and evaluator gaming. Fixed topology/GA bounds the loop without erasing online weight evolution.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_ba85811695fc1fd804
Co-evolves fixed-topology actor/predictor ANN weights using sensor prediction accuracy rather than task-specific fitness. Physical experiments use a centralized onboard evolutionary master and online (1+1) selection under bounded evaluation budgets.

**适用版本**：arXiv:2405.02579v1 (official HTML route)；**原文定位**：Actor-predictor fitness evolution; Official HTML derived paragraphs 21-24 (one-based local extraction)；Onboard online protocol; Official HTML derived paragraphs 99-100 (one-based local extraction)；Physical exclusion and trivial behaviors; Official HTML derived paragraphs 122-122 (one-based local extraction)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_ba85811695fc1fd804`
机器人群体以最小化预测惊讶作内在动机并用神经演化训练，self-referential 指机器人构成彼此环境的反馈；摘要没有优化器自改，需明确开放式具身背景用途。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Genome is actor/predictor weights shared by swarm members; prediction fitness theoretical maximum 1. Physical evaluation lasts 10s, stops at 350 evaluations; five runs attempted/four retained.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_ba85811695fc1fd804`**：机器人群体以最小化预测惊讶作内在动机并用神经演化训练，self-referential 指机器人构成彼此环境的反馈；摘要没有优化器自改，需明确开放式具身背景用途。
  - 来源版本：2405.02579v1；定位：Atom entry http://arxiv.org/abs/2405.02579v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_ba85811695fc1fd804`**：Co-evolves fixed-topology actor/predictor ANN weights using sensor prediction accuracy rather than task-specific fitness. Physical experiments use a centralized onboard evolutionary master and online (1+1) selection under bounded evaluation budgets.
  - 来源版本：arXiv:2405.02579v1 (official HTML route)；定位：Actor-predictor fitness evolution; Official HTML derived paragraphs 21-24 (one-based local extraction)；Onboard online protocol; Official HTML derived paragraphs 99-100 (one-based local extraction)；Physical exclusion and trivial behaviors; Official HTML derived paragraphs 122-122 (one-based local extraction)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Actor-predictor fitness evolution
**来源**：https://arxiv.org/html/2405.02579v1  
**实际版本**：arXiv:2405.02579v1 (official HTML route)  
**精确定位**：Official HTML derived paragraphs 21-24 (one-based local extraction)  
**关联证据**：`b570_06_ev_wf_ba85811695fc1fd804`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Onboard online protocol
**来源**：https://arxiv.org/html/2405.02579v1  
**实际版本**：arXiv:2405.02579v1 (official HTML route)  
**精确定位**：Official HTML derived paragraphs 99-100 (one-based local extraction)  
**关联证据**：`b570_06_ev_wf_ba85811695fc1fd804`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Physical exclusion and trivial behaviors
**来源**：https://arxiv.org/html/2405.02579v1  
**实际版本**：arXiv:2405.02579v1 (official HTML route)  
**精确定位**：Official HTML derived paragraphs 122-122 (one-based local extraction)  
**关联证据**：`b570_06_ev_wf_ba85811695fc1fd804`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- One of five physical runs was excluded for connection failure; most surviving runs produced circling and easy predictions rather than object pushing. Prediction fitness is not automatically task usefulness or open-ended sophistication.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_ba85811695fc1fd804` · Innate Motivation for Robot Swarms by Minimizing Surprise: From Simple Simulations to Real-World Experiments · arXiv:2405.02579v1 (official HTML route)
  - https://arxiv.org/html/2405.02579v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18_role_src_075816ef1c8f29e4` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2404.14662%2C2404.14851%2C2404.15100%2C2404.15155%2C2404.15574%2C2404.15794%2C2404.15923%2C2404.16071%2C2404.16130%2C2404.16789%2C2404.18021%2C2404.18231%2C2404.18922%2C2404.18930%2C2405.00461%2C2405.00823%2C2405.00972%2C2405.01535%2C2405.01674%2C2405.01930%2C2405.02579%2C2405.02750%2C2405.02766%2C2405.02957%2C2405.03162%2C2405.03256%2C2405.03279%2C2405.03547%2C2405.03553%2C2405.03710%2C2405.06563%2C2405.06682%2C2405.06683%2C2405.06686%2C2405.07551%2C2405.07960%2C2405.08550%2C2405.08807%2C2405.09783%2C2405.09939%2C2405.10202%2C2405.10295%2C2405.11094%2C2405.11106%2C2405.11143%2C2405.11165%2C2405.11403%2C2405.11874%2C2405.12472%2C2405.12819%2C2405.13576%2C2405.14093%2C2405.14205%2C2405.14314%2C2405.14333%2C2405.14414%2C2405.14486%2C2405.14573%2C2405.14739%2C2405.14767%2C2405.14768%2C2405.15143%2C2405.15329%2C2405.15568%2C2405.15793%2C2405.16089%2C2405.16205%2C2405.16455%2C2405.16579%2C2405.16751%2C2405.16821%2C2405.16908%2C2405.17044%2C2405.17051%2C2405.17220%2C2405.17244%2C2405.17631%2C2405.17633%2C2405.18649%2C2405.18711%2C2405.19425%2C2405.19686%2C2405.20139%2C2405.20267%2C2405.20770%2C2405.20859%2C2406.00079%2C2406.00888%2C2406.01304%2C2406.01309%2C2406.01495%2C2406.01574%2C2406.01587%2C2406.02120%2C2406.02470%2C2406.02523%2C2406.02543%2C2406.02746%2C2406.02900%2C2406.03807&max_results=100；阅读深度：`未单列`。

**仍未核准的内容**：

- Open-ended adaptation potential is not demonstrated indefinite improvement or optimizer modification.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ba85811695fc1fd804 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
