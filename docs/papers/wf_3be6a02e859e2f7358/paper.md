# ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement

> 方法论文 · 2026 · `wf_3be6a02e859e2f7358`

**作者**：Siwei Wu, Jincheng Ren, Yizhi Li, Haau-Sing Li, Chengran Yang, Yuxuan Zhang, Weicheng Gu, Jian Yang, Riza Batista-Navarro, Chuanyi Zhang, Xianglong Liu, Ming Zhou, Bryan Dai, Chenghua Lin  
**原文**：https://arxiv.org/abs/2609.14857  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ModularRSI 对同任务成功与失败轨迹作跨任务归因，独立演化五类 harness 模块后整合，并称演化任务与下游 benchmark 分离；应核作用对象、模块合并和泛化协议，不能仅据摘要认证无泄漏。

## 2. 论文的核心内容与贡献

### configuration:cfg_modularrsi_function_library_evolution
代码层函数库及其历史在后续自修改循环中保留并生效，四项结构条件在此harness边界内满足；未认证基础模型或固定gate自行改进。

**适用版本**：2609.14857v1；**原文定位**：v1 §3.1–3.7 tool L130–181；v1 §4–5.3 tool L182–208；v1 §6.4 tool L260–271；v1 §7 tool L294–298。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_3be6a02e859e2f7358`
ModularRSI 对同任务成功与失败轨迹作跨任务归因，独立演化五类 harness 模块后整合，并称演化任务与下游 benchmark 分离；应核作用对象、模块合并和泛化协议，不能仅据摘要认证无泄漏。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### ModularRSI: independently evolved harness modules with integration
`cfg_modularrsi_function_library_evolution` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定基础模型和代码修改提示内，五类harness行为函数库、历史轨迹memory、每函数演化history；基础通信和sandbox初始化不属演化目标。 |
| 改进过程与下一轮参与 | 正在演化的agent承担分析与Code-Modify角色；同任务成功/失败对照、跨任务票数定位函数后改写，校验通过的模块函数用于后续rollout/分析和跨模块整合。 |
| 保留的状态及时间尺度 | 每轮保留验证函数、轨迹和演化history，五模块独立演化后额外整合；最终库冻结但评价时仍按任务选择激活函数。 |
| 外部固定部分 | - 基础LLM权重 - Code-Modify/分析和gate提示模板 - 任务评价器 - 固定五模块接口及可编辑范围 - benchmark留出协议 |
| 评价与选择设置 | - **backbones**：- DeepSeek-V4-Flash-Preview - DeepSeek-V4-Flash-0731 - **batch size**：10 - **comparison control**：§6.4 AHE/Meta-Harness 16 epochs to match aggregate evolution rounds; not certified identical token or dollar expenditure; web search disabled in this comparison - **curated resource size**：2000 - **downstream**：- TerminalBench2.0 - SWE-Bench Verified - **evolution epochs per module**：3 - **evolution instances per domain**：120 - **seed harness**：Terminus-2 / Harbor |

**配置判定**：代码层函数库及其历史在后续自修改循环中保留并生效，四项结构条件在此harness边界内满足；未认证基础模型或固定gate自行改进。

来源：https://arxiv.org/html/2609.14857v1；版本：2609.14857v1；定位：v1 §3.1–3.7 tool L130–181；v1 §4–5.3 tool L182–208；v1 §6.4 tool L260–271；v1 §7 tool L294–298。

## 4. 实验、评价协议与结果的可解释范围


- **backbones**：- DeepSeek-V4-Flash-Preview - DeepSeek-V4-Flash-0731
- **batch size**：10
- **comparison control**：§6.4 AHE/Meta-Harness 16 epochs to match aggregate evolution rounds; not certified identical token or dollar expenditure; web search disabled in this comparison
- **curated resource size**：2000
- **downstream**：- TerminalBench2.0 - SWE-Bench Verified
- **evolution epochs per module**：3
- **evolution instances per domain**：120
- **seed harness**：Terminus-2 / Harbor

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_3be6a02e859e2f7358`**：ModularRSI 对同任务成功与失败轨迹作跨任务归因，独立演化五类 harness 模块后整合，并称演化任务与下游 benchmark 分离；应核作用对象、模块合并和泛化协议，不能仅据摘要认证无泄漏。
  - 来源版本：2609.14857v1；定位：Atom entry http://arxiv.org/abs/2609.14857v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5agent_ev_cfg_modularrsi_function_library_evolution`**：代码层函数库及其历史在后续自修改循环中保留并生效，四项结构条件在此harness边界内满足；未认证基础模型或固定gate自行改进。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 静态检查、同agent的diff审查及随机2任务执行验证主要排运行/协议错误，不是跨任务性能显著性或独立安全保证。
- 作者明确未做单独隔离contrastive分析贡献的消融；不能把集成收益全部归因对照机制。
- 策展bench-disjoint是作者构建和筛选协议声明；下游benchmark高层领域标签用于检索引导，不等于从未参考benchmark领域。
- 原始2000任务中实验仅每域120；不同表使用的Flash-Preview/Flash-0731及对照协议不能混同。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 有限任务配置的结构核查，不是全文逐段审核、独立复现或单调收益认证。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5agent_src_w_modularrsi` · 已存来源 · 2609.14857v1
  - https://arxiv.org/html/2609.14857v1；阅读深度：`targeted_primary_method_controls_and_limits`。
- `s18_role_src_cf0403161b25df87` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-improving%22+AND+%28all%3Aagent+OR+all%3Alanguage%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_controls_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3be6a02e859e2f7358 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
