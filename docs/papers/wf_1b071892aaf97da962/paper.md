# Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks

> 实证/审计/复现 · 2026 · `wf_1b071892aaf97da962`

**作者**：Franziska Roesner, Tadayoshi Kohno  
**原文**：https://arxiv.org/abs/2609.17817  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
以受污染 benchmark 诱导 DGM、SICA、Hyperagents 自修改并在干净任务表现出漏洞，摘要注明 DGM 实验有修改且污染可在后续干净演化中持续；应核攻击、框架版本与迁移条件。

## 2. 论文的核心内容与贡献

### configuration:cfg_trusting_trust_modified_dgm_poison_protocol_v1
邻接的受控协议/外部提案学习或攻击实验；不可把受测程序更新和固定协议本身的自改混为一谈。

**适用版本**：v1；**原文定位**：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239；§3.2 Table1 tool L230–253。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_1b071892aaf97da962`
以受污染 benchmark 诱导 DGM、SICA、Hyperagents 自修改并在干净任务表现出漏洞，摘要注明 DGM 实验有修改且污染可在后续干净演化中持续；应核攻击、框架版本与迁移条件。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议

### Trusting Trust modified-DGM benchmark-poisoning study
`cfg_trusting_trust_modified_dgm_poison_protocol_v1` · attack_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 研究者固定的poisoned/clean benchmark与中性heldout评测协议；DGM adapter的模型与诊断prompt被实验修改，受测程序演化与攻击协议分开。 |
| 改进过程与下一轮参与 | 比较poisoned vs clean演化，再对携带所演化组件的最高分代理做10中性任务×3次安全输出检查；本卡只记录授权实验范围与污染转移测量。 |
| 保留的状态及时间尺度 | 受测代码组件跨12代左右保留并影响中性解题；固定攻击评测协议不在测试中自改。 |
| 外部固定部分 | - 研究者构造benchmark/任务条件 - 修改diagnosis prompt及选定模型 - 中性heldout任务与vulnerability判读 |
| 评价与选择设置 | - **DGM prompt**：substantially modified diagnosis prompt; outside attacker threat model - **focus**：CertCheck controlled modified-DGM case - **heldout tasks**：10 - **repeats per task**：3 - **reporting**：highest-accuracy agent that carries evolved component, may differ from tip - **upstream DGM commit**：a565fd2 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：固定攻击adapter与被测演化代理分别定义（状态：`supported`；定位：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239）。
- **更新由什么过程产生**：本卡是研究者提供poisoning和测试，非自演化攻击器（状态：`contradicted`；定位：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239）。
- **状态怎样持久保留**：目标组件保留至heldout评价（状态：`supported`；定位：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239）。
- **更新怎样进入后续改进**：无证据显示攻击评价协议自己产生后继协议或学习攻击算法（状态：`contradicted`；定位：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239）。

**配置判定**：邻接的受控协议/外部提案学习或攻击实验；不可把受测程序更新和固定协议本身的自改混为一谈。

来源：https://arxiv.org/html/2609.17817v1；版本：v1；定位：§3.1–3.2 tool L141–190；§3.2.1–3.2.2 tool L218–239；§3.2 Table1 tool L230–253。

## 4. 实验、评价协议与结果的可解释范围


- **DGM prompt**：substantially modified diagnosis prompt; outside attacker threat model
- **focus**：CertCheck controlled modified-DGM case
- **heldout tasks**：10
- **repeats per task**：3
- **reporting**：highest-accuracy agent that carries evolved component, may differ from tip
- **upstream DGM commit**：a565fd2

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_1b071892aaf97da962`**：以受污染 benchmark 诱导 DGM、SICA、Hyperagents 自修改并在干净任务表现出漏洞，摘要注明 DGM 实验有修改且污染可在后续干净演化中持续；应核攻击、框架版本与迁移条件。
  - 来源版本：2609.17817v1；定位：Atom entry http://arxiv.org/abs/2609.17817v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5safe_ev_cfg_trusting_trust_modified_dgm_poison_protocol_v1`**：比较poisoned vs clean演化，再对携带所演化组件的最高分代理做10中性任务×3次安全输出检查；本卡只记录授权实验范围与污染转移测量。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- DGM诊断prompt鼓励可复用code-emitter的改动是substantial且超出文中仅benchmark控制威胁模型；不能写成stock DGM被同攻击攻破。
- Qwen3.5-397B成功与gpt-oss/ Sonnet不同，不能把个别60solutions当总体成功率或所有模型普遍漏洞。
- 选择最高分且携带组件的代理可不是实际tip；作者的组件选择与完整部署政策安全需分开。
- 10中性任务重复3次是受测解题数，非30独立演化run；2 poison演化不构成跨seed风险估计。
- SICA/Hyperagents有单独stock-prompt实验，本卡不借用这些结果到modified DGM。
- 本卡是安全审计证据，不提供攻击代码或部署动作；不把benchmark得分提高当作真实安全/能力改善。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5safe_src_trusting_trust` · 已存来源 · v1
  - https://arxiv.org/html/2609.17817v1；阅读深度：`selected_primary_methods_version_changes_assumptions_and_limits`。
- `r5safe_src_trusting_trust_results` · 已存来源 · v1
  - https://arxiv.org/html/2609.17817v1；阅读深度：`selected_primary_methods_version_changes_assumptions_and_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_methods_version_changes_assumptions_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1b071892aaf97da962 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
