# Here Comes The AI Worm: Unleashing Zero-click Worms that Target GenAI-Powered Applications

> 实证/审计/复现 · 2024 · `wf_db2ab7f6a8568f9e8e`

**作者**：Stav Cohen, Ron Bitton, Ben Nassi  
**原文**：https://arxiv.org/abs/2403.02817  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Here Comes The AI Worm: Unleashing Zero-click Worms that Target GenAI-Powered Applications (https://arxiv.org/html/2403.02817v2)。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
Morris-II evaluates self-replicating prompt propagation and extraction in a Gemini Flash1.5 RAG email client. The unit is2,000 emails from20 Enron employees; replication requires exact string reproduction, and reported metrics distinguish retrieval, replication, payload and their combination. Optional RSI safety adjacency for memory/input contamination and propagation; do not equate replication with improvement.

### 与 RSI 的具体关系

- Optional RSI safety adjacency for memory/input contamination and propagation; do not equate replication with improvement.

## 2. 论文的核心内容与贡献

### role:b570_02_role_wf_db2ab7f6a8568f9e8e
Morris-II evaluates self-replicating prompt propagation and extraction in a Gemini Flash1.5 RAG email client. The unit is2,000 emails from20 Enron employees; replication requires exact string reproduction, and reported metrics distinguish retrieval, replication, payload and their combination.

**适用版本**：2403.02817v2；**原文定位**：§IV-A/B actual setup and metric definitions tool L176–199；§VI limitations tool L512–517。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_db2ab7f6a8568f9e8e`
Morris-II 在 RAG 应用通信中用自复制提示传播间接注入，并评价防传播 guardrail；自复制攻击链不同于能力递归改进，可作记忆/信息污染安全邻接案例但不能嫁接未测试 RSI 框架。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_db2ab7f6a8568f9e8e`**：Morris-II 在 RAG 应用通信中用自复制提示传播间接注入，并评价防传播 guardrail；自复制攻击链不同于能力递归改进，可作记忆/信息污染安全邻接案例但不能嫁接未测试 RSI 框架。
  - 来源版本：2403.02817v2；定位：Atom entry http://arxiv.org/abs/2403.02817v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_02_ev_wf_db2ab7f6a8568f9e8e`**：Morris-II evaluates self-replicating prompt propagation and extraction in a Gemini Flash1.5 RAG email client. The unit is2,000 emails from20 Enron employees; replication requires exact string reproduction, and reported metrics distinguish retrieval, replication, payload and their combination.
  - 来源版本：2403.02817v2；定位：§IV-A/B actual setup and metric definitions tool L176–199；§VI limitations tool L512–517；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §IV-A/B actual setup and metric definitions
**来源**：https://arxiv.org/html/2403.02817v2  
**实际版本**：2403.02817v2  
**精确定位**：tool L176–199  
**关联证据**：`b570_02_ev_wf_db2ab7f6a8568f9e8e`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 限制 · §VI limitations
**来源**：https://arxiv.org/html/2403.02817v2  
**实际版本**：2403.02817v2  
**精确定位**：tool L512–517  
**关联证据**：`b570_02_ev_wf_db2ab7f6a8568f9e8e`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Exact-string replication is a lower bound because modified prompts can also work. §VI notes visible prompts/payloads and does not test the Virtual Donkey mitigation against adaptive attacks. Self-propagating content is not measured recursive capability improvement.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_02_src_wf_db2ab7f6a8568f9e8e` · Here Comes The AI Worm: Unleashing Zero-click Worms that Target GenAI-Powered Applications (https://arxiv.org/html/2403.02817v2) · 2403.02817v2
  - https://arxiv.org/html/2403.02817v2；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18ctx_role_src_20fe003e28646d5b` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2402.08957%2C2402.09015%2C2402.09269%2C2402.09283%2C2402.09727%2C2402.09742%2C2402.09748%2C2402.10110%2C2402.10176%2C2402.10196%2C2402.10200%2C2402.10663%2C2402.10770%2C2402.10890%2C2402.10963%2C2402.10980%2C2402.10987%2C2402.11190%2C2402.11218%2C2402.11359%2C2402.11411%2C2402.11451%2C2402.11550%2C2402.11633%2C2402.11827%2C2402.11975%2C2402.12048%2C2402.12185%2C2402.12255%2C2402.12317%2C2402.12348%2C2402.12391%2C2402.12431%2C2402.12451%2C2402.12545%2C2402.12914%2C2402.12959%2C2402.13210%2C2402.13212%2C2402.13296%2C2402.13426%2C2402.13542%2C2402.13598%2C2402.13669%2C2402.13717%2C2402.14034%2C2402.14083%2C2402.14207%2C2402.14268%2C2402.14382%2C2402.15057%2C2402.15116%2C2402.15391%2C2402.15538%2C2402.15589%2C2402.15809%2C2402.15810%2C2402.16288%2C2402.16313%2C2402.16499%2C2402.16696%2C2402.16767%2C2402.16823%2C2402.16837%2C2402.16906%2C2402.16965%2C2402.17168%2C2402.17453%2C2402.17505%2C2402.17574%2C2402.17613%2C2402.17753%2C2402.18005%2C2402.18060%2C2402.18361%2C2402.18381%2C2402.18485%2C2402.19085%2C2402.19173%2C2402.19446%2C2402.19473%2C2403.00198%2C2403.00690%2C2403.00833%2C2403.00839%2C2403.01197%2C2403.01244%2C2403.01248%2C2403.01528%2C2403.02164%2C2403.02502%2C2403.02691%2C2403.02817%2C2403.02985%2C2403.03101%2C2403.03129%2C2403.03186%2C2403.03218%2C2403.03768%2C2403.03883&max_results=100；阅读深度：`未单列`。

**证据深度**：selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_db2ab7f6a8568f9e8e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
