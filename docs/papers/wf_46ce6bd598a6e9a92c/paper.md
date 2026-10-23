# Generative-Evaluative Agreement: A Necessary Validity Criterion for LLM-Enabled Adaptive Assessment

> 评测方法/测量科学 · 2026 · `wf_46ce6bd598a6e9a92c`

**作者**：Grandee Lee, Yue Wang, Che Yee Lye, Luke Peh  
**原文**：https://arxiv.org/abs/2605.19529  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
GEA测量同一LLM按指定技能水平生成代码后，其评分是否恢复该指定水平：Pearson r与signed bias区分排序保真和偏移。所用水平是合成profile指令锚，不是真实学生独立能力真值；这种内部一致性诊断不能单独认证外部有效性，更不能当RSI能力增益。

## 2. 论文的核心内容与贡献

### role:r11_role_gea
GEA测量同一LLM按指定技能水平生成代码后，其评分是否恢复该指定水平：Pearson r与signed bias区分排序保真和偏移。所用水平是合成profile指令锚，不是真实学生独立能力真值；这种内部一致性诊断不能单独认证外部有效性，更不能当RSI能力增益。

**适用版本**：2605.19529v1；**原文定位**：§1.1 definition tool L92–98；§3.1 simulation tool L120–139；§4 findings tool L142–149；Limitations tool L302–305；§6 model scaling tool L289–298。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_46ce6bd598a6e9a92c`
GEA 检查同一 LLM 生成测题、模拟学生及评分时能否恢复预设技能水平，重点是教育测量效度与自评偏差；可供评价回路讨论，但未展示模型自身跨轮训练改进。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：策展者类比：可支撑自生成数据+自评闭环的测量偏差讨论；研究对象本身是教育adaptive assessment，未证明任何RSI训练循环。
- **leakage and information boundary**：同模型生成/评估共享误概念可隐藏偏差；profile条件不是外部人类gold。论文要求真实学生pilot补外部锚，不可把模拟标注称独立实测能力。
- **metrics**：- pooled skill-level Pearson r、signed bias、ordinal proficiency match；record-level聚合r须另列 - pooled r=0.698不应与跨技能均值后的record-level r=0.92互换；后者粒度不同
- **selection and reuse**：profile来自10archetype及Gaussian noise；不适用技能输出-1并排除。Haiku对比复用相同profiles/rubric；没有同任务rubric粒度或scorer identity干预消融。
- **split and visibility**：不是训练/留出测试拆分；对给定profile×slot生成响应，再由同模型、相同rubric评分。所有profile尝试全部slot以避免routing导致覆盖偏差。
- **task or data unit**：150个24维合成学生profile，六个Python OOP作业slot全覆盖、绕过adaptive routing；同Claude Sonnet4.6分两次调用生成/评分。正文报告862条结果、7788对技能观测，覆盖23/24技能。
- **unknowns**：- 900名义attempt与862记录的对账unknown - profile设定与真实学生能力之间的外部效度unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_46ce6bd598a6e9a92c`**：GEA 检查同一 LLM 生成测题、模拟学生及评分时能否恢复预设技能水平，重点是教育测量效度与自评偏差；可供评价回路讨论，但未展示模型自身跨轮训练改进。
  - 来源版本：2605.19529v1；定位：Atom entry http://arxiv.org/abs/2605.19529v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r11_ev_gea`**：GEA测量同一LLM按指定技能水平生成代码后，其评分是否恢复该指定水平：Pearson r与signed bias区分排序保真和偏移。所用水平是合成profile指令锚，不是真实学生独立能力真值；这种内部一致性诊断不能单独认证外部有效性，更不能当RSI能力增益。
  - 来源版本：2605.19529v1；定位：§1.1 definition tool L92–98；§3.1 simulation tool L120–139；§4 findings tool L142–149；Limitations tool L302–305；§6 model scaling tool L289–298；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 150profiles均合成；只测两Claude模型和Python OOP，不外推主观领域或其他模型family。
- 未直接消融rubric granularity或same-vs-cross-model scoring；不能将建议当已验证机制。
- 150×6名义为900，但报告862记录；本次所读段未解释差额，原因unknown，不自行填为失败/过滤。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 150profiles均合成；只测两Claude模型和Python OOP，不外推主观领域或其他模型family。; 未直接消融rubric granularity或same-vs-cross-model scoring；不能将建议当已验证机制。; 150×6名义为900，但报告862记录；本次所读段未解释差额，原因unknown，不自行填为失败/过滤。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_gea` · Generative-Evaluative Agreement: A Necessary Validity Criterion for LLM-Enabled Adaptive Assessment · 2605.19529v1
  - https://arxiv.org/html/2605.19529v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。
- `s18_role_src_9299d35dbd10f451` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2605.15215%2C2605.15218%2C2605.15221%2C2605.15224%2C2605.15239%2C2605.15308%2C2605.15309%2C2605.15334%2C2605.15417%2C2605.15461%2C2605.15573%2C2605.15581%2C2605.15604%2C2605.15706%2C2605.15759%2C2605.16205%2C2605.16309%2C2605.16325%2C2605.16363%2C2605.16430%2C2605.16481%2C2605.16508%2C2605.16626%2C2605.16679%2C2605.16689%2C2605.16865%2C2605.16867%2C2605.16962%2C2605.17046%2C2605.17172%2C2605.17291%2C2605.17342%2C2605.17444%2C2605.17526%2C2605.17625%2C2605.17626%2C2605.17734%2C2605.17873%2C2605.18048%2C2605.18073%2C2605.18141%2C2605.18181%2C2605.18299%2C2605.18407%2C2605.18476%2C2605.18529%2C2605.18661%2C2605.18747%2C2605.18851%2C2605.19156%2C2605.19196%2C2605.19317%2C2605.19436%2C2605.19529%2C2605.19943%2C2605.19952%2C2605.20086%2C2605.20312%2C2605.20425%2C2605.20477%2C2605.20548%2C2605.20690%2C2605.20833%2C2605.21082%2C2605.21308%2C2605.21392%2C2605.21516%2C2605.21606%2C2605.21792%2C2605.21821%2C2605.21825%2C2605.21997%2C2605.22137%2C2605.22144%2C2605.22148%2C2605.22166%2C2605.22240%2C2605.22263%2C2605.22478%2C2605.22535%2C2605.22566%2C2605.22613%2C2605.22620%2C2605.22642%2C2605.22662%2C2605.22675%2C2605.22698%2C2605.22781%2C2605.22794%2C2605.22817%2C2605.23055%2C2605.23078%2C2605.23204%2C2605.23243%2C2605.23382%2C2605.23435%2C2605.23454%2C2605.23493%2C2605.23899%2C2605.23908&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_46ce6bd598a6e9a92c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
