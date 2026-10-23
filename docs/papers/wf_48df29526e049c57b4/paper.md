# On the use of feature-maps and parameter control for improved quality-diversity meta-evolution

> 方法论文 · 2021 · `wf_48df29526e049c57b4`

**作者**：David M. Bossens, Danesh Tarapore  
**原文**：https://arxiv.org/abs/2105.10317  
**研究分支**：群体、自博弈与开放式探索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
QD 元演化用档案级 meta-fitness 优化行为特征映射，并动态控制变异率与内层代数；有改进搜索方法的元层线索，需区分元基因、固定目标和保留策略。

## 2. 论文的核心内容与贡献

### configuration:cfg_qd_meta_featuremap_control
共享解数据库/元分布与学得行为映射反馈进入后续档案构建和改进，四结构条件限于bounded QD state-feedback成立；CMA-ES顶层规则固定。

**适用版本**：2105.10317v1；**原文定位**：PDF v1 physical pp3–5 §3.1–3.4 Algorithm1 tool L107–328；PDF v1 physical p6 §3.5 tool L329–340；PDF v1 physical pp10–12 selected results/conclusion tool L690–737。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_48df29526e049c57b4`
QD 元演化用档案级 meta-fitness 优化行为特征映射，并动态控制变异率与内层代数；有改进搜索方法的元层线索，需区分元基因、固定目标和保留策略。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### QD meta-evolution: feature maps and parameter control
`cfg_qd_meta_featuremap_control` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | CMA-ES元分布m/C/sigma、映射W、底层MAP-Elites档案和共享k-best数据库D；用户固定base features和meta objective。 |
| 改进过程与下一轮参与 | 元分布采样W重建档案，内层MAP-Elites生成新控制解回写D，按档案meta-fitness更新元分布；动态控制可为RL/内生/annealing/static不同条件。 |
| 保留的状态及时间尺度 | D跨元代保留并填充下轮档案，m/C/sigma保留影响下轮W采样及后续解生成。 |
| 外部固定部分 | - CMA-ES与MAP-Elites更新形式 - meta-fitness和损伤集 - base features及featuremap family - 外部参数控制算法选项 |
| 评价与选择设置 | - **config boundary**：shared core loop, no particular controller performance certified - **controls**：- static - endogenous - annealing - reinforcement-learning - **domain**：DART8-joint planar robot arm - **map families**：- linear - nonlinear - feature-selection |

**配置判定**：共享解数据库/元分布与学得行为映射反馈进入后续档案构建和改进，四结构条件限于bounded QD state-feedback成立；CMA-ES顶层规则固定。

来源：https://arxiv.org/pdf/2105.10317v1；版本：2105.10317v1；定位：PDF v1 physical pp3–5 §3.1–3.4 Algorithm1 tool L107–328；PDF v1 physical p6 §3.5 tool L329–340；PDF v1 physical pp10–12 selected results/conclusion tool L690–737。

## 4. 实验、评价协议与结果的可解释范围


- **config boundary**：shared core loop, no particular controller performance certified
- **controls**：- static - endogenous - annealing - reinforcement-learning
- **domain**：DART8-joint planar robot arm
- **map families**：- linear - nonlinear - feature-selection

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_48df29526e049c57b4`**：QD 元演化用档案级 meta-fitness 优化行为特征映射，并动态控制变异率与内层代数；有改进搜索方法的元层线索，需区分元基因、固定目标和保留策略。
  - 来源版本：2105.10317v1；定位：Atom entry http://arxiv.org/abs/2105.10317v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_qd_meta_featuremap_control`**：共享解数据库/元分布与学得行为映射反馈进入后续档案构建和改进，四结构条件限于bounded QD state-feedback成立；CMA-ES顶层规则固定。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 49条件不是单一统一配置，本卡仅共同结构，RL/内生/static不得混称同时启用。
- meta-fitness提升与真实RSI计算增长不同；更强非线性映射需要更多function evaluations。
- 机器人模拟默认指令运动成功，未核实际硬件鲁棒性。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_qd_meta_featuremaps` · 已存来源 · 2105.10317v1
  - https://arxiv.org/pdf/2105.10317v1；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `s18_role_src_946b5a9844f9a97d` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28all%3A%22editable+improver%22+OR+all%3A%22meta-evolution%22+OR+all%3A%22G%C3%B6del+agent%22+OR+all%3A%22Godel+machine%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_48df29526e049c57b4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
