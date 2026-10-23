# Self-Referential Quality Diversity Through Differential Map-Elites

> 方法论文 · 2021 · `wf_b34e58fb330c465613`

**作者**：Tae Jong Choi, Julian Togelius  
**原文**：https://arxiv.org/abs/2107.04964  
**研究分支**：群体、自博弈与开放式探索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：CVT行为网格及elites档案X/P，固定DE/rand/1/bin公式、scaling F和crossover CR；具体更新过程为：从4个不同非空cell取target/donors，差分变异与交叉后按cell fitness保留elite；self-reference指当前population向量差分自定步幅；更新状态的保留与后继使用为：elite档案跨代保存参与下轮取样；没有改写DE算子、参数更新规则或meta-controller的步骤。

## 2. 论文的核心内容与贡献

### configuration:cfg_differential_map_elites_fixed_de
四结构条件限于有限QD种群反馈边界成立：目标/行为函数明确，trial来自自身archive，按cell择优保留并参与后继差分提案。self-reference仅种群差分，不证明DE顶层规则学习或更强RSI。

**适用版本**：2107.04964v1；**原文定位**：PDF v1 physical p3 §3 Algorithm1 tool L206–274；PDF v1 physical p4 Add-To-Archive and controls tool L287–402；PDF v1 physical p5 discussion tool L470–491。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_b34e58fb330c465613`
Differential MAP-Elites组合差分演化算子与CVT-MAP-Elites档案进行质量多样性优化；不因self-referential题名直接认定元改进器自改。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Differential MAP-Elites: fixed DE operators over elite archive
`cfg_differential_map_elites_fixed_de` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | CVT行为网格及elites档案X/P，固定DE/rand/1/bin公式、scaling F和crossover CR。 |
| 改进过程与下一轮参与 | 从4个不同非空cell取target/donors，差分变异与交叉后按cell fitness保留elite；self-reference指当前population向量差分自定步幅。 |
| 保留的状态及时间尺度 | elite档案跨代保存参与下轮取样；没有改写DE算子、参数更新规则或meta-controller的步骤。 |
| 外部固定部分 | - F=0.5 - CR=0.9 - CVT centroids/behavior projection - DE mutation/crossover公式及objective |
| 评价与选择设置 | - **CR**：0.9 - **F**：0.5 - **benchmarks**：25 numerical functions - **retention**：per-cell higher-fitness replacement |

**配置判定**：四结构条件限于有限QD种群反馈边界成立：目标/行为函数明确，trial来自自身archive，按cell择优保留并参与后继差分提案。self-reference仅种群差分，不证明DE顶层规则学习或更强RSI。

来源：https://arxiv.org/pdf/2107.04964v1；版本：2107.04964v1；定位：PDF v1 physical p3 §3 Algorithm1 tool L206–274；PDF v1 physical p4 Add-To-Archive and controls tool L287–402；PDF v1 physical p5 discussion tool L470–491。

## 4. 实验、评价协议与结果的可解释范围


- **CR**：0.9
- **F**：0.5
- **benchmarks**：25 numerical functions
- **retention**：per-cell higher-fitness replacement

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_b34e58fb330c465613`**：Differential MAP-Elites组合差分演化算子与CVT-MAP-Elites档案进行质量多样性优化；不因self-referential题名直接认定元改进器自改。
  - 来源版本：2107.04964v1；定位：Atom entry http://arxiv.org/abs/2107.04964v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_differential_map_elites_fixed_de`**：四结构条件限于有限QD种群反馈边界成立：目标/行为函数明确，trial来自自身archive，按cell择优保留并参与后继差分提案。self-reference仅种群差分，不证明DE顶层规则学习或更强RSI。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 与本库EVOM/AutoML-zero相同，archive参与后继生成足以支持结构C4，不能因F/CR固定就否定；该结构标签不认证优化器自身学得新规则。
- 仅CEC2005函数及线性行为投影实验；神经网络训练在讨论中是后续检验方向。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_differential_map_elites` · 已存来源 · 2107.04964v1
  - https://arxiv.org/pdf/2107.04964v1；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `r4_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b34e58fb330c465613 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
