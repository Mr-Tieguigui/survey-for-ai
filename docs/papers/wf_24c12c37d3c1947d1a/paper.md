# Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies

> 实证/审计/复现 · 2026 · `wf_24c12c37d3c1947d1a`

**作者**：Ruixiao Lin, Xinhao Deng, Qingming Li, Jianan Ma, Yunhao Feng, Yuqi Qing, Zhenyuan Li, Yechao Zhang, Shiwen Cui, Changhua Meng, Tianwei Zhang, Xingjun Ma, Qi Li, Ke Xu, Shouling Ji  
**原文**：https://arxiv.org/abs/2606.23075  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
摘要以五模块×五阶段矩阵分析自演化系统攻击，并报告两框架案例；攻击持久率/放大倍数均是待核原设置数值，非普遍事实。

## 2. 论文的核心内容与贡献

### configuration:cfg_mlas_openclaw_hermes_attack_case_protocol_v1
相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

**适用版本**：v1；**原文定位**：§8 Table8/9 and runtime analysis tool L752–785；§2.5 tool L363–373；§8 methods tool L721–761。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_24c12c37d3c1947d1a`
摘要以五模块×五阶段矩阵分析自演化系统攻击，并报告两框架案例；攻击持久率/放大倍数均是待核原设置数值，非普遍事实。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议

### MLAS OpenClaw/Hermes finite comparative threat cases
`cfg_mlas_openclaw_hermes_attack_case_protocol_v1` · attack_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定5模块×5生命周期矩阵和指定framework版本下的攻击case protocol；受测agent的演化路径与研究者协议分开。 |
| 改进过程与下一轮参与 | 映射输入至mutation/selection/persistent skills，比较Hermes scanned hub-install与unscanned background-review及OpenClaw plugin path，记录CIA+privacy攻击持久与扫描覆盖。 |
| 保留的状态及时间尺度 | 目标skill/memory持久性是被测结果，研究者payload/矩阵/评分规则本身不演化。 |
| 外部固定部分 | - Hermes0.15.1/OpenClaw2026.6.2 - GPT5 backbone - 40攻击场景及重复规则 - 人工定义CIA+P/持久判据 |
| 评价与选择设置 | - **cases**：40 - **categories**：- integrity - confidentiality - availability - privacy - **repetitions per scenario**：3 - **total run count**：unresolved: Table8 160 vs path/repetition denominator; no synthesized total - **versions**：- Hermes0.15.1 - OpenClaw2026.6.2 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：明确case protocol及目标framework（状态：`supported`；定位：§8 Table8/9 and runtime analysis tool L752–785）。
- **更新由什么过程产生**：固定研究者攻击评测，非自演化改进器（状态：`contradicted`；定位：§8 Table8/9 and runtime analysis tool L752–785）。
- **状态怎样持久保留**：受测skill与snapshot跨过程持久（状态：`supported`；定位：§8 Table8/9 and runtime analysis tool L752–785）。
- **更新怎样进入后续改进**：没有攻击protocol从结果自改的训练链（状态：`contradicted`；定位：§8 Table8/9 and runtime analysis tool L752–785）。

**配置判定**：相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

来源：https://arxiv.org/html/2606.23075v1；版本：v1；定位：§8 Table8/9 and runtime analysis tool L752–785；§2.5 tool L363–373；§8 methods tool L721–761。

## 4. 实验、评价协议与结果的可解释范围


- **cases**：40
- **categories**：- integrity - confidentiality - availability - privacy
- **repetitions per scenario**：3
- **total run count**：unresolved: Table8 160 vs path/repetition denominator; no synthesized total
- **versions**：- Hermes0.15.1 - OpenClaw2026.6.2

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_24c12c37d3c1947d1a`**：摘要以五模块×五阶段矩阵分析自演化系统攻击，并报告两框架案例；攻击持久率/放大倍数均是待核原设置数值，非普遍事实。
  - 来源版本：2606.23075v1；定位：Atom entry http://arxiv.org/abs/2606.23075v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6safe_ev_cfg_mlas_openclaw_hermes_attack_case_protocol_v1`**：映射输入至mutation/selection/persistent skills，比较Hermes scanned hub-install与unscanned background-review及OpenClaw plugin path，记录CIA+privacy攻击持久与扫描覆盖。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- case study系统/路径同时有多项差异，作者用causal措辞不等于独立随机控制因果识别。
- 40/40是场景分母，3重复及Table8写160 runs的乘法口径未统一；不擅自宣称480独立攻击run。
- 100% persistence与1/40 scanner阻挡限指定payload/版本/路径，不是任意攻击普适概率或现版本安全审计。
- MLAS理论25格不代表所有格都有同等实验证据；不把概念amplification因子当任意部署测得量。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_5d77616c137a6fe2` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-evolving%22+AND+%28all%3Aagent+OR+all%3Alanguage+OR+all%3Amodel%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=200&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `r6safe_src_safety` · 已存来源 · v1
  - https://arxiv.org/html/2606.23075v1；阅读深度：`selected_original_method_and_scope_limits`。
- `r6safe_src_safety_taxonomy` · 已存来源 · v1
  - https://arxiv.org/html/2606.23075v1；阅读深度：`selected_original_method_and_scope_limits`。

**证据深度**：original_abstract, selected_original_method_and_scope_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_24c12c37d3c1947d1a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
