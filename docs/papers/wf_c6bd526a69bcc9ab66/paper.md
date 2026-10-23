# Self-evolving Agentic Customer Support System at LinkedIn

> 方法论文 · 2026 · `wf_c6bd526a69bcc9ab66`

**作者**：Chih Hui Wang, Mengdie Tu, Qianyun Zhang, Wei Wu, Lili Zhou, Mingqi Shen, Changshuai Wei  
**原文**：https://arxiv.org/abs/2608.10224  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
LinkedIn 支持系统以 RAG、演化自动提示和模块评价组成带版本及护栏的闭环，摘要报告生产随机 A/B；需分开自演化更新配置和集成系统试验，不能把整体线上提升全归因递归机制。

## 2. 论文的核心内容与贡献

### configuration:cfg_linkedin_prompt_population_evolution_v1
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2608.10224v1；**原文定位**：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18ctx_role_review_wf_c6bd526a69bcc9ab66`
LinkedIn 支持系统以 RAG、演化自动提示和模块评价组成带版本及护栏的闭环，摘要报告生产随机 A/B；需分开自演化更新配置和集成系统试验，不能把整体线上提升全归因递归机制。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### LinkedIn: constrained prompt evolution with versioned deployment
`cfg_linkedin_prompt_population_evolution_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定生产generator/judge/企业约束，进化prompt population与长期版本artifact外循环。 |
| 改进过程与下一轮参与 | LLM初始化prompt→固定fitness评估→elite选择→semantic crossover/mutation产生新prompt；保存/回滚版本，生产评分及regression供下一优化周期。 |
| 保留的状态及时间尺度 | elite、fitness cache、versioned prompts跨generation保留；runtime跨session无latent memory。 |
| 外部固定部分 | - 企业政策hard constraints - base GPT-4o-mini及GPT-4.1 evaluator - 遗传搜索算子与scoring规则 - 运行时和检索语料刷新ETL |
| 评价与选择设置 | - **cycle runtime**：hours to days - **generator**：GPT-4o-mini - **no cross session latent state**：True - **offline judge**：GPT-4.1 - **online study**：two weeks single enterprise; bundled treatment - **typical outer cadence**：weekly or refresh/regression triggered |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：prompt优化器、受测agent、evaluator和长期artifact边界明确。（状态：`supported`；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294）。
- **更新由什么过程产生**：自身运行/评分引导prompt种群更新。（状态：`supported`；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294）。
- **状态怎样持久保留**：elite/版本prompt跨generation与部署周期保留。（状态：`supported`；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294）。
- **更新怎样进入后续改进**：新elite成为后续交叉/变异的parent，新agent行为及评分进入后续优化。（状态：`supported`；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2608.10224v1；版本：2608.10224v1；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294。

## 4. 实验、评价协议与结果的可解释范围


- **cycle runtime**：hours to days
- **generator**：GPT-4o-mini
- **no cross session latent state**：True
- **offline judge**：GPT-4.1
- **online study**：two weeks single enterprise; bundled treatment
- **typical outer cadence**：weekly or refresh/regression triggered

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_c6bd526a69bcc9ab66`**：LinkedIn 支持系统以 RAG、演化自动提示和模块评价组成带版本及护栏的闭环，摘要报告生产随机 A/B；需分开自演化更新配置和集成系统试验，不能把整体线上提升全归因递归机制。
  - 来源版本：2608.10224v1；定位：Atom entry http://arxiv.org/abs/2608.10224v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_linkedin_prompt_population_evolution_v1`**：固定生产generator/judge/企业约束，进化prompt population与长期版本artifact外循环。 LLM初始化prompt→固定fitness评估→elite选择→semantic crossover/mutation产生新prompt；保存/回滚版本，生产评分及regression供下一优化周期。
  - 来源版本：2608.10224v1；定位：§2.2 Algorithm 1 tool L76–128；§2.3–§3 tool L129–157；Limitations tool L272–294；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- prompt和版本artifact演化不等于基础模型/LLM改写遗传算子或检索语料自行生长；ETL更新与自改归因分开。
- 业务约束hard filter是设计边界，非已证明安全或完全合规；生成prompt数量/代数实际运行值本次未核。
- 两周在线A/B treatment混合Auto-Prompt、agent RAG及评估迭代，不能把全部在线增益归因prompt自改。
- proprietary backend和closed models尚未端到端开源复现；受控多语测试只有英中，不推所有locale。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_linkedin` · 已存来源 · 2608.10224v1
  - https://arxiv.org/html/2608.10224v1；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18ctx_role_src_5b1dc5ef02082f5f` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-evolving%22+AND+%28all%3Aagent+OR+all%3Alanguage+OR+all%3Amodel%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c6bd526a69bcc9ab66 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
