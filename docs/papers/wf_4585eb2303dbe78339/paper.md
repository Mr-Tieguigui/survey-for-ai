# Machine-generated text detection prevents language model collapse

> 失败/限制/风险 · 2025 · `wf_4585eb2303dbe78339`

**作者**：George Drayson, Emine Yilmaz, Vasileios Lampos  
**原文**：https://arxiv.org/abs/2502.15654  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：前代生成数据D_S、外部真人数据混合池、每代从原预训练p_theta重训的后代模型；固定detector及resampling规则；具体更新过程为：用上一代模型生成训练池，固定machine-text detector给human倾向权重并有放回1.5倍resample，再从原基模fine-tune后生成下一代数据；更新状态的保留与后继使用为：主要继承生成数据而非逐代连续θ；后代模型作为下一轮数据生成器。

## 2. 论文的核心内容与贡献

### configuration:cfg_detector_importance_resampling_recursive_v6
声明生成器—后代训练数据回流内的结构core，可承载退化负结果；不等于能力改善、加速或optimizer自改。

**适用版本**：v6；**原文定位**：§4.1 Algorithm1 tool L100–118；§6.2–6.3 tool L217–240。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_4585eb2303dbe78339`
摘要研究解码策略与未知来源数据下的模型坍塌，以生成文本检测器进行重要性重采样；只保留候选负结果/缓解方法。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议

### Detector-guided resampling across recursive training generations
`cfg_detector_importance_resampling_recursive_v6` · implemented_recursive_data_resampling

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 前代生成数据D_S、外部真人数据混合池、每代从原预训练p_theta重训的后代模型；固定detector及resampling规则。 |
| 改进过程与下一轮参与 | 用上一代模型生成训练池，固定machine-text detector给human倾向权重并有放回1.5倍resample，再从原基模fine-tune后生成下一代数据。 |
| 保留的状态及时间尺度 | 主要继承生成数据而非逐代连续θ；后代模型作为下一轮数据生成器。 |
| 外部固定部分 | - 原pretrained初始化 - 固定text detector - 混合系数及解码方案 - 重采样权重公式 |
| 评价与选择设置 | - **detector**：ModernBERT externally trained on MAGE; not coevolved - **generations**：10 - **models**：- GPT2 - SmolLM2 - **parameter initialization**：original pretrained model reset each generation - **sampling**：1.5n with replacement; w proportional to (1-q)^b |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4.1明示原基模及各代输出数据（状态：`supported`；定位：§4.1 Algorithm1 tool L100–118）。
- **更新由什么过程产生**：每代模型自产后代训练文本（状态：`supported`；定位：§4.1 Algorithm1 tool L100–118）。
- **状态怎样持久保留**：D_S传到后代，model p^i产生下一代输出（状态：`supported`；定位：§4.1 Algorithm1 tool L100–118）。
- **更新怎样进入后续改进**：新p^i改变下一轮训练数据；无需optimizer或detector规则自改（状态：`supported`；定位：§4.1 Algorithm1 tool L100–118）。

**配置判定**：声明生成器—后代训练数据回流内的结构core，可承载退化负结果；不等于能力改善、加速或optimizer自改。

来源：https://arxiv.org/html/2502.15654v6；版本：v6；定位：§4.1 Algorithm1 tool L100–118；§6.2–6.3 tool L217–240。

## 4. 实验、评价协议与结果的可解释范围


- **detector**：ModernBERT externally trained on MAGE; not coevolved
- **generations**：10
- **models**：- GPT2 - SmolLM2
- **parameter initialization**：original pretrained model reset each generation
- **sampling**：1.5n with replacement; w proportional to (1-q)^b

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_4585eb2303dbe78339`**：摘要研究解码策略与未知来源数据下的模型坍塌，以生成文本检测器进行重要性重采样；只保留候选负结果/缓解方法。
  - 来源版本：2502.15654v6；定位：Atom entry http://arxiv.org/abs/2502.15654v6；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6safe_ev_cfg_detector_importance_resampling_recursive_v6`**：用上一代模型生成训练池，固定machine-text detector给human倾向权重并有放回1.5倍resample，再从原基模fine-tune后生成下一代数据。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 原文每代fine-tune原p_theta，不能写成连续权重训练；结构保留通过数据链。
- 需要混合池中存在真人信息；detector不是创造真人分布的oracle。
- 权重近似density ratio，检测器AUC不等于在所有后代/新域中校准；固定训练域外可失效。
- 正文Diversity公式与Higher-is-better说明存在方向疑点，不能原封不动据此作指标总排名。
- 10代、小中模型、open-ended text、fine-tuning设置；不外推pretraining、代码任务或所有指标同步改善。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_cedf125a16a07099` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22model+collapse%22+OR+ti%3A%22reward+hacking%22+OR+ti%3A%22reward+overoptimization%22+OR+ti%3A%22evaluator+drift%22+OR+ti%3A%22misevolution%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `r6safe_src_detector` · 已存来源 · v6
  - https://arxiv.org/html/2502.15654v6；阅读深度：`selected_original_method_and_scope_limits`。
- `r6safe_src_detector_filter` · 已存来源 · v6
  - https://arxiv.org/html/2502.15654v6；阅读深度：`selected_original_method_and_scope_limits`。

**证据深度**：selected_original_method_and_scope_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4585eb2303dbe78339 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
