# Scientific Opinion Summarization: Paper Meta-review Generation Dataset, Methods, and Evaluation

> Benchmark/数据集/任务套件 · 2023 · `wf_b48c5811e2821b4037`

**作者**：Qi Zeng, Mankeerat Sidhu, Ansel Blume, Hou Pong Chan, Lu Wang, Heng Ji  
**原文**：https://arxiv.org/abs/2305.14647  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ORSum/科学意见总结以同一论文的title、abstract、多个reviews和给定decision生成meta-review，评价意见faithfulness、讨论优缺点/共识争议和decision consistency。CGI²属于同一meta-review内两轮checklist self-refinement，不能当跨任务保留的RSI方法。

## 2. 论文的核心内容与贡献

### role:r14_role_opinion
ORSum/科学意见总结以同一论文的title、abstract、多个reviews和给定decision生成meta-review，评价意见faithfulness、讨论优缺点/共识争议和decision consistency。CGI²属于同一meta-review内两轮checklist self-refinement，不能当跨任务保留的RSI方法。

**适用版本**：2305.14647v1；**原文定位**：§3 dataset/split tool L82–96；§4–5 refinement and evaluation tool L114–139；§6.2 truncation/iterations tool L180–183；§8 limitations tool L196–198。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

### 已存角色解释 · `r3_abstract_review_wf_b48c5811e2821b4037`
提出scientific opinion summarization任务、ORSUM数据和checklist迭代内省方法；meta-review是论文评审汇总任务，不是领域综述论文。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：背景：可支持自动科研review生成与评测模块；同回答内self-refinement不证明自改器或跨任务学习。
- **metrics**：- ROUGE-L/BERTScore相关性、SummaC事实一致性、平均DiscoScore连贯性 - reference-free LLM-based discussion involvement/opinion faithfulness/decision consistency；不把人工meta-review视为必然高质量gold
- **selection and reuse**：方法演示用gpt-3.5-turbo、两迭代；review截断300tokens，后续轮删原review仅保留其讨论/evidence与draft。
- **split and visibility**：9890/549/550 train/validation/test；meta-review composition额外100条人标含每venue一条后随机补齐，非全部语料人工质量复核。
- **task or data unit**：OpenReview 39venues的10989条meta-review、40903条individual review；保留meta-review>20tokens并排非官方reviewer comments；单位为论文review集合→meta-review。
- **unknowns**：- 预训练污染/按论文语义去重完整审计unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r3_abstract_ev_2305_14647`**：提出scientific opinion summarization任务、ORSUM数据和checklist迭代内省方法；meta-review是论文评审汇总任务，不是领域综述论文。
  - 来源版本：2305.14647v3；定位：Atom entry http://arxiv.org/abs/2305.14647v3；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r14_ev_opinion`**：ORSum/科学意见总结以同一论文的title、abstract、多个reviews和给定decision生成meta-review，评价意见faithfulness、讨论优缺点/共识争议和decision consistency。CGI²属于同一meta-review内两轮checklist self-refinement，不能当跨任务保留的RSI方法。
  - 来源版本：2305.14647v1；定位：§3 dataset/split tool L82–96；§4–5 refinement and evaluation tool L114–139；§6.2 truncation/iterations tool L180–183；§8 limitations tool L196–198；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- OpenReview偏机器学习且accepted paper多，不外推其他领域；不输入author rebuttal。
- reference summaries质量有限，LLM评价和截断会影响结论，未独立复现。
- 官方精确v1 title为Meta-review Generation with Checklist-guided Iterative Introspection；原主表Scientific Opinion...保留为历史标题，未作新paper或跨ID合并。
- 本轮只读官方版本摘要，未核全文方法、证明、数据或性能数值；未建立与RSI的直接机制关系。保留作角色/相关性复核和术语边界，不自动进入最终引用清单。
- OpenReview偏机器学习且accepted paper多，不外推其他领域；不输入author rebuttal。; reference summaries质量有限，LLM评价和截断会影响结论，未独立复现。; 官方精确v1 title为Meta-review Generation with Checklist-guided Iterative Introspection；原主表Scientific Opinion...保留为历史标题，未作新paper或跨ID合并。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_opinion` · Scientific Opinion Summarization: Paper Meta-review Generation Dataset, Methods, and Evaluation · 2305.14647v1
  - https://arxiv.org/html/2305.14647v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。
- `r3_abstract_src_src_697aa2dbcb298ebd` · 已存来源 · Atom snapshot 2026-10-11 with per-entry arXiv versions
  - https://export.arxiv.org/api/query?id_list=2304.02554%2C2304.03277%2C2304.03279%2C2304.03442%2C2304.03512%2C2304.03516%2C2304.04370%2C2304.05128%2C2304.05302%2C2304.05332%2C2304.05376%2C2304.06767%2C2304.06975%2C2304.07327%2C2304.08244%2C2304.08354%2C2304.10149%2C2304.10592%2C2304.11116%2C2304.11477%2C2304.12244%2C2304.12998%2C2304.13007%2C2304.13343%2C2304.13712%2C2304.14979%2C2305.00833%2C2305.01210%2C2305.01498%2C2305.01582%2C2305.01937%2C2305.02412%2C2305.02499%2C2305.03047%2C2305.03111%2C2305.03453%2C2305.03653%2C2305.04087%2C2305.04091%2C2305.04533%2C2305.05176%2C2305.05183%2C2305.06161%2C2305.06474%2C2305.06590%2C2305.06983%2C2305.07759%2C2305.07796%2C2305.07922%2C2305.08144%2C2305.08291%2C2305.08698%2C2305.10250%2C2305.10355%2C2305.10403%2C2305.10425%2C2305.10601%2C2305.10626%2C2305.11206%2C2305.11554%2C2305.11792%2C2305.11854%2C2305.12524%2C2305.12707%2C2305.12744%2C2305.13048%2C2305.13068%2C2305.13172%2C2305.13304%2C2305.13455%2C2305.13534%2C2305.13660%2C2305.13685%2C2305.13735%2C2305.13829%2C2305.14002%2C2305.14045%2C2305.14196%2C2305.14233%2C2305.14259%2C2305.14279%2C2305.14314%2C2305.14322%2C2305.14325%2C2305.14333%2C2305.14387%2C2305.14449%2C2305.14647%2C2305.14688%2C2305.14739%2C2305.14752%2C2305.14788%2C2305.14908%2C2305.14992%2C2305.15186%2C2305.15294%2C2305.15324%2C2305.15334%2C2305.15486%2C2305.15717&max_results=100；阅读深度：`未单列`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b48c5811e2821b4037 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
