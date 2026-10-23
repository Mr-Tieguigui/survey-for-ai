# Learning by Surprise: Adaptive Mitigation of Model Collapse in Large Language Models

> 失败/限制/风险 · 2024 · `wf_e876365fc2a5627991`

**作者**：Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo  
**原文**：https://arxiv.org/abs/2410.12341  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
摘要报告以next-token分布和常识任务观察合成数据退化，提出高perplexity样本过滤缓解；模型、数据和训练条件待全文配置化。

## 2. 论文的核心内容与贡献

### configuration:cfg_surprise_adaptive_perplexity_selection_v4
声明生成器—后代训练数据回流内的结构core，可承载退化负结果；不等于能力改善、加速或optimizer自改。

**适用版本**：v4；**原文定位**：§3–4 Algorithm1 tool L112–208；§8 tool L395–425。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_e876365fc2a5627991`
摘要报告以next-token分布和常识任务观察合成数据退化，提出高perplexity样本过滤缓解；模型、数据和训练条件待全文配置化。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议

### Learning by Surprise: adaptive high-perplexity autophagy
`cfg_surprise_adaptive_perplexity_selection_v4` · implemented_self_training_and_selection

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 连续M_j、累积初始真人/合成数据池、由当前M_j计算的训练样本排序；固定人类prompt及fine-tuning规则。 |
| 改进过程与下一轮参与 | 当前M_j续写固定prompt，加入数据池，以当前模型perplexity选最高1000文档再fine-tune为M_j+1；更新模型改变下一次生成及排序。 |
| 保留的状态及时间尺度 | 模型参数、累积文本池及其数据谱系跨10步保留，后代直接参与后续生成/选样。 |
| 外部固定部分 | - 固定prompt和原真人数据池 - 训练更新规则 - top1000筛选规则 - 诊断指标 |
| 评价与选择设置 | - **datasets**：- Wikitext - XL-Sum - SciAbs - **example models**：- Llama2-7B - Llama3-8B - Mistral-7B - Qwen3-0.6B - **filter top documents**：1000 - **horizon**：10 - **prompts**：fixed human-authored prefixes |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4声明连续模型/累积池边界（状态：`supported`；定位：§3–4 Algorithm1 tool L112–208）。
- **更新由什么过程产生**：模型自己生成后代训练数据并据当前预测选样（状态：`supported`；定位：§3–4 Algorithm1 tool L112–208）。
- **状态怎样持久保留**：M_j fine-tune为M_j+1且池累积（状态：`supported`；定位：§3–4 Algorithm1 tool L112–208）。
- **更新怎样进入后续改进**：M_j+1再生成及计算perplexity，影响后续训练（状态：`supported`；定位：§3–4 Algorithm1 tool L112–208）。

**配置判定**：声明生成器—后代训练数据回流内的结构core，可承载退化负结果；不等于能力改善、加速或optimizer自改。

来源：https://arxiv.org/html/2410.12341v4；版本：v4；定位：§3–4 Algorithm1 tool L112–208；§8 tool L395–425。

## 4. 实验、评价协议与结果的可解释范围


- **datasets**：- Wikitext - XL-Sum - SciAbs
- **example models**：- Llama2-7B - Llama3-8B - Mistral-7B - Qwen3-0.6B
- **filter top documents**：1000
- **horizon**：10
- **prompts**：fixed human-authored prefixes

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_e876365fc2a5627991`**：摘要报告以next-token分布和常识任务观察合成数据退化，提出高perplexity样本过滤缓解；模型、数据和训练条件待全文配置化。
  - 来源版本：2410.12341v4；定位：Atom entry http://arxiv.org/abs/2410.12341v4；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6safe_ev_cfg_surprise_adaptive_perplexity_selection_v4`**：当前M_j续写固定prompt，加入数据池，以当前模型perplexity选最高1000文档再fine-tune为M_j+1；更新模型改变下一次生成及排序。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 10步受控实验不能推所有规模/训练分布永久免collapse；失败维度和任务能力须分开。
- 筛选不需human/AI标签，不代表无需真人语料；原文§8几乎所有选中文档为真人。
- 高perplexity不是事实正确/高质量保证，随机噪声和极端分布外文本需另控。
- §4 AI段有M_j+1生成数据的文字下标笔误，按Algorithm1与邻近描述使用M_j。
- 不把header的XXXX DOI/JACM模板元数据当作已发表期刊身份。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_cedf125a16a07099` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22model+collapse%22+OR+ti%3A%22reward+hacking%22+OR+ti%3A%22reward+overoptimization%22+OR+ti%3A%22evaluator+drift%22+OR+ti%3A%22misevolution%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `r6safe_src_surprise` · 已存来源 · v4
  - https://arxiv.org/html/2410.12341v4；阅读深度：`selected_original_method_and_scope_limits`。
- `r6safe_src_surprise_filter` · 已存来源 · v4
  - https://arxiv.org/html/2410.12341v4；阅读深度：`selected_original_method_and_scope_limits`。

**证据深度**：selected_original_method_and_scope_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e876365fc2a5627991 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
