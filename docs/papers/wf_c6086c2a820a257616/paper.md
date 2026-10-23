# AlgoEvolve: LLM-driven Meta-evolution of Algorithmic Trading Programs

> 方法论文 · 2026 · `wf_c6086c2a820a257616`

**作者**：Dhruv Sharma, Gautam Shroff  
**原文**：https://arxiv.org/abs/2606.26173  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：内层Python策略种群、四gene Evolver Prompt种群、固定Pro/Flash和performance report；具体更新过程为：inner注入Top2Best/Worst代码分数；outer选elite/交叉gene，Meta-LLM读report改一gene，Pnext驱动下一inner run；更新状态的保留与后继使用为：策略父本跨inner代；prompt genome跨meta-generations保留并继续生成。

## 2. 论文的核心内容与贡献

### configuration:cfg_algoevolve_prompt_genome_meta_search_v1
演化Evolver Prompt进入后续策略搜索，报告反馈推动下一prompt mutation，四结构条件在双层有限搜索内成立。

**适用版本**：2606.26173v1；**原文定位**：§3.2–4.1 tool L97–136；§4.2 Algorithm1 tool L137–218；§5.1–5.2 tool L221–240。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### AlgoEvolve: four-gene prompt meta-evolution
`cfg_algoevolve_prompt_genome_meta_search_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 内层Python策略种群、四gene Evolver Prompt种群、固定Pro/Flash和performance report。 |
| 改进过程与下一轮参与 | inner注入Top2Best/Worst代码分数；outer选elite/交叉gene，Meta-LLM读report改一gene，Pnext驱动下一inner run。 |
| 保留的状态及时间尺度 | 策略父本跨inner代；prompt genome跨meta-generations保留并继续生成。 |
| 外部固定部分 | - System Prompt/I-O约束 - curated gene选项 - Meta-LLM与外层交叉变异规则 |

**配置判定**：演化Evolver Prompt进入后续策略搜索，报告反馈推动下一prompt mutation，四结构条件在双层有限搜索内成立。

来源：https://arxiv.org/html/2606.26173v1；版本：2606.26173v1；定位：§3.2–4.1 tool L97–136；§4.2 Algorithm1 tool L137–218；§5.1–5.2 tool L221–240。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_algoevolve_prompt_genome_meta_search_v1`**：演化Evolver Prompt进入后续策略搜索，报告反馈推动下一prompt mutation，四结构条件在双层有限搜索内成立。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Algorithm1 L194用D_test给outer fitness并选父，该test是meta-selection数据，不能称全流程未见finaltest。
- 仅NUMIN匿名5分钟模拟和固定成本，不认证实盘收益或Meta-LLM因果诊断正确。
- 基础模型与顶层搜索规则固定，不是无限自改。
- - Algorithm1 L194用D_test给outer fitness并选父，该test是meta-selection数据，不能称全流程未见finaltest。 - 仅NUMIN匿名5分钟模拟和固定成本，不认证实盘收益或Meta-LLM因果诊断正确。 - 基础模型与顶层搜索规则固定，不是无限自改。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_algoevolve_v1` · 已存来源 · 2606.26173v1
  - https://arxiv.org/html/2606.26173v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c6086c2a820a257616 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
