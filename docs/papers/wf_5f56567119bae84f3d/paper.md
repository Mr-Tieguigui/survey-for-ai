# Searching Search Spaces: Meta-evolving a Geometric Encoding for Neural Networks

> 方法论文 · 2024 · `wf_5f56567119bae84f3d`

**作者**：Tarek Kunze, Paul Templier, Dennis G Wilson  
**原文**：https://arxiv.org/abs/2403.14019  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
以 Cartesian Genetic Programming 元演化 GENE 间接编码的距离函数，使内层网络搜索空间更易优化，并讨论未见问题泛化；需核外层搜索预算和编码保留，不能当自改深度无界。

## 2. 论文的核心内容与贡献

### configuration:cfg_gene_cgp_encoding_search
任务表现与网络属性fitness筛选并更新CGP群体，保留群体参与下一代距离函数提案，四结构条件在有限meta-search边界内成立；距离函数不是CGP顶层规则，不认证更强自改。

**适用版本**：2403.14019v1；**原文定位**：v1 §III-A–E tool L117–154；v1 §IV-A/C tool L155–197；v1 §V tool L211–217。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_5f56567119bae84f3d`
以 Cartesian Genetic Programming 元演化 GENE 间接编码的距离函数，使内层网络搜索空间更易优化，并讨论未见问题泛化；需核外层搜索预算和编码保留，不能当自改深度无界。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### GENE meta-evolution: CGP learns distance-to-weight encoding
`cfg_gene_cgp_encoding_search` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 外层CGP距离函数群体，固定内层ES训练网络坐标和固定meta-fitness组合；距离函数控制genotype→policy权重。 |
| 改进过程与下一轮参与 | CGP生成距离函数，对每个函数完整训练HalfCheetah/Walker2D策略并合成任务及网络属性fitness后更新CGP群体，归档最优函数。 |
| 保留的状态及时间尺度 | CGP群体与最优函数跨代保留，最终函数在新内层策略搜索中固定复用；CGP变异/更新规则不被学习出的函数修改。 |
| 外部固定部分 | - 外层CGP搜索规则 - 内层ES算法 - 任务与网络架构 - 手设fitness属性与beta=1/3 |
| 评价与选择设置 | - **additional selection assessment**：- Hopper - Swimmer - **generations**：635 - **selected**：LD367 - **train tasks**：- HalfCheetah - Walker2D |

**配置判定**：任务表现与网络属性fitness筛选并更新CGP群体，保留群体参与下一代距离函数提案，四结构条件在有限meta-search边界内成立；距离函数不是CGP顶层规则，不认证更强自改。

来源：https://arxiv.org/html/2403.14019v1；版本：2403.14019v1；定位：v1 §III-A–E tool L117–154；v1 §IV-A/C tool L155–197；v1 §V tool L211–217。

## 4. 实验、评价协议与结果的可解释范围


- **additional selection assessment**：- Hopper - Swimmer
- **generations**：635
- **selected**：LD367
- **train tasks**：- HalfCheetah - Walker2D

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_5f56567119bae84f3d`**：以 Cartesian Genetic Programming 元演化 GENE 间接编码的距离函数，使内层网络搜索空间更易优化，并讨论未见问题泛化；需核外层搜索预算和编码保留，不能当自改深度无界。
  - 来源版本：2403.14019v1；定位：Atom entry http://arxiv.org/abs/2403.14019v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_gene_cgp_encoding_search`**：任务表现与网络属性fitness筛选并更新CGP群体，保留群体参与下一代距离函数提案，四结构条件在有限meta-search边界内成立；距离函数不是CGP顶层规则，不认证更强自改。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 元演化计算成本是主要限制，635代实验不是通用计算节约。
- top10经包括Hopper/Swimmer在内的多环境考察后选LD367，不能把最终选择所见环境称为完全未用于选择的测试。
- 内层任务/架构固定，扩大curriculum只是未来工作。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_gene_meta_encoding` · 已存来源 · 2403.14019v1
  - https://arxiv.org/html/2403.14019v1；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `s18_role_src_946b5a9844f9a97d` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28all%3A%22editable+improver%22+OR+all%3A%22meta-evolution%22+OR+all%3A%22G%C3%B6del+agent%22+OR+all%3A%22Godel+machine%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5f56567119bae84f3d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
