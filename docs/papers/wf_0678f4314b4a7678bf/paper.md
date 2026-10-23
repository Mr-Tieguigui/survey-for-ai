# Benchmarking Zero-Shot LLM-Generated Parent Selection in Genetic Programming for Symbolic Regression

> Benchmark/数据集/任务套件 · 2026 · `wf_0678f4314b4a7678bf`

**作者**：Hengzhe Zhang, Qi Chen, Bing Xue, Wolfgang Banzhaf, Mengjie Zhang  
**原文**：https://arxiv.org/abs/2607.23505  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
评测LLM零样本合成GP父选择算子的质量：每模型10个有效算子，在12个SRBench回归问题、五个80/20划分种子上执行固定GP；区分训练搜索有效性与留出预测R²。算子生成阶段没有性能反馈或元演化，语法/功能失败重试不能当算子性能自改。

## 2. 论文的核心内容与贡献

### role:r11_role_zero_shot_gp
评测LLM零样本合成GP父选择算子的质量：每模型10个有效算子，在12个SRBench回归问题、五个80/20划分种子上执行固定GP；区分训练搜索有效性与留出预测R²。算子生成阶段没有性能反馈或元演化，语法/功能失败重试不能当算子性能自改。

**适用版本**：2607.23505v1；**原文定位**：§3.2 evolutionary framework tool L95–113；§3.3 zero-shot generation tool L115–118；§4.1–4.3 settings/datasets/protocol tool L121–140；§5.3–6 generalization/conclusion tool L282–291。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_0678f4314b4a7678bf`
在遗传规划符号回归中比较 LLM 零样本生成的父代选择算子，摘要明示没有迭代元演化反馈，其他部件和搜索预算固定；可作算子生成对照，不能当递归元演化实证。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：可作为LLM设计优化算子的零反馈对照与泛化测量参考；内层GP有种群/误差反馈，本文并未实证LLM反复改进其父选择算子。
- **leakage and information boundary**：作者称新算子合成具有抗记忆污染优势；这不是训练语料污染审计或无泄露证明。测试R²与训练R²的榜单关联不同。
- **metrics**：- 训练及测试R²；每算子跨60次运行的均值/中位数，再跨10算子聚合 - 运行时间、代码长度、生成尝试和成本是辅助分析；公开榜单秩相关仅探索性关联
- **selection and reuse**：每次仅任务说明生成代码，无参考算子、无GP收益回传；执行/数量等基本检查失败则重生成，直到10个有效算子。报告最佳算子与总体分布必须区分。
- **split and visibility**：12个聚类选定SRBench/OpenML问题，每问题80/20训练测试划分、五种子；target encoding只拟合训练集。GP适应度使用训练数据。
- **task or data unit**：评测单元为一个独立合成的父选择算子及其60次GP运行；每LLM汇总10算子、600次运行。GP种群200、100代；只有父选择算子被替换。
- **unknowns**：- 生成代码具体实现和全部开销核算未复现 - 训练语料实际污染率unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_0678f4314b4a7678bf`**：在遗传规划符号回归中比较 LLM 零样本生成的父代选择算子，摘要明示没有迭代元演化反馈，其他部件和搜索预算固定；可作算子生成对照，不能当递归元演化实证。
  - 来源版本：2607.23505v1；定位：Atom entry http://arxiv.org/abs/2607.23505v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r11_ev_zero_shot_gp`**：评测LLM零样本合成GP父选择算子的质量：每模型10个有效算子，在12个SRBench回归问题、五个80/20划分种子上执行固定GP；区分训练搜索有效性与留出预测R²。算子生成阶段没有性能反馈或元演化，语法/功能失败重试不能当算子性能自改。
  - 来源版本：2607.23505v1；定位：§3.2 evolutionary framework tool L95–113；§3.3 zero-shot generation tool L115–118；§4.1–4.3 settings/datasets/protocol tool L121–140；§5.3–6 generalization/conclusion tool L282–291；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只覆盖固定GP框架的父选择、12个问题及所列预算；不代表整个算法设计空间。
- §5.3明确榜单相关非因果，测试泛化联系不清楚；§6抗污染陈述为作者论断。
- 仅所选原文协议/边界段核查，未运行代码或独立复现数值。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 只覆盖固定GP框架的父选择、12个问题及所列预算；不代表整个算法设计空间。; §5.3明确榜单相关非因果，测试泛化联系不清楚；§6抗污染陈述为作者论断。; 仅所选原文协议/边界段核查，未运行代码或独立复现数值。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_zero_shot_gp` · Benchmarking Zero-Shot LLM-Generated Parent Selection in Genetic Programming for Symbolic Regression · 2607.23505v1
  - https://arxiv.org/html/2607.23505v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。
- `s18_role_src_946b5a9844f9a97d` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28all%3A%22editable+improver%22+OR+all%3A%22meta-evolution%22+OR+all%3A%22G%C3%B6del+agent%22+OR+all%3A%22Godel+machine%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0678f4314b4a7678bf --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
