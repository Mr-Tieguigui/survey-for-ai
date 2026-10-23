# Authorization for Self-Modifying AI Agent Populations: Conserving Authority across Replacement, Forking, and Rollback

> 方法论文 · 2026 · `wf_a84b529a4123526f5c`

**作者**：Genliang Zhu, Chu Wang  
**原文**：https://arxiv.org/abs/2610.00347  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
提出自修改代理替换、分叉和回滚时的授权继承协议，以人口前沿守恒和外部中介约束权限；摘要同时给形式假设与可执行回放，不能把有限保护效果的授权保证外推为全面行为安全。

## 2. 论文的核心内容与贡献

### configuration:cfg_population_authorization_succession_protocol_v1
相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

**适用版本**：v1；**原文定位**：§1.4 and §3.2–3.6 tool L155–157,L222–277；§8.3–8.5 tool L763–795。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_a84b529a4123526f5c`
提出自修改代理替换、分叉和回滚时的授权继承协议，以人口前沿守恒和外部中介约束权限；摘要同时给形式假设与可执行回放，不能把有限保护效果的授权保证外推为全面行为安全。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### External population authority-conservation protocol
`cfg_population_authorization_succession_protocol_v1` · external_authorization_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 位于可变agent外部的registry/ledger/effect broker与单parent授权generation forest；控制替换/分叉/rollback的authority分配。 |
| 改进过程与下一轮参与 | 候选隔离，独立证据与预算reservation，原子fence旧代/激活后代；每protected effect检查当前完整谱系与额度，rollback新建generation不恢复已耗authority。 |
| 保留的状态及时间尺度 | 持久ledger、撤销cut、预算和序列跨agent替换/重启保留；协议本身固定。 |
| 外部固定部分 | - 注册effect profile及normalizer - trusted broker与atomic ledger - A1–A10可信前提 - 独立evidence-root规则 |
| 评价与选择设置 | - **DGM evolution executed**：False - **core cases**：32 - **logical mappings**：2 - **source native adapters**：- OurArk retained descendant - DGM one deterministic EditTool mutation |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：外部protocol与可变candidate分离（状态：`supported`；定位：§1.4 and §3.2–3.6 tool L155–157,L222–277）。
- **更新由什么过程产生**：ledger规则不由agent自改（状态：`contradicted`；定位：§1.4 and §3.2–3.6 tool L155–157,L222–277）。
- **状态怎样持久保留**：monotone状态持久（状态：`supported`；定位：§1.4 and §3.2–3.6 tool L155–157,L222–277）。
- **更新怎样进入后续改进**：只执行预定授权transition，不改自身改进器（状态：`contradicted`；定位：§1.4 and §3.2–3.6 tool L155–157,L222–277）。

**配置判定**：相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

来源：https://arxiv.org/html/2610.00347v1；版本：v1；定位：§1.4 and §3.2–3.6 tool L155–157,L222–277；§8.3–8.5 tool L763–795。

## 4. 实验、评价协议与结果的可解释范围


- **DGM evolution executed**：False
- **core cases**：32
- **logical mappings**：2
- **source native adapters**：- OurArk retained descendant - DGM one deterministic EditTool mutation

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_a84b529a4123526f5c`**：提出自修改代理替换、分叉和回滚时的授权继承协议，以人口前沿守恒和外部中介约束权限；摘要同时给形式假设与可执行回放，不能把有限保护效果的授权保证外推为全面行为安全。
  - 来源版本：2610.00347v1；定位：Atom entry http://arxiv.org/abs/2610.00347v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6safe_ev_cfg_population_authorization_succession_protocol_v1`**：候选隔离，独立证据与预算reservation，原子fence旧代/激活后代；每protected effect检查当前完整谱系与额度，rollback新建generation不恢复已耗authority。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 形式结论依赖完整mediation、认证、lineage accounting及atomic durable状态，不保证被broker遗漏行为。
- 参考实现仅declared-control-root/digest binding，无真正caller authentication、key possession或public-key signatures。
- DGM仅一次adapter-authored EditTool mutation与fresh process，未跑完整open-ended evolution；32重放不是32独立演化。
- 只single-parent无merge；整数budget和opaque single-holder atoms，不实现一般效应格；不是上游生产集成或作者背书。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6safe_src_auth` · 已存来源 · v1
  - https://arxiv.org/html/2610.00347v1；阅读深度：`selected_original_method_and_scope_limits`。
- `r6safe_src_auth_adapter` · 已存来源 · v1
  - https://arxiv.org/html/2610.00347v1；阅读深度：`selected_original_method_and_scope_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_original_method_and_scope_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a84b529a4123526f5c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
