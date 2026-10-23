# Advancing Subsurface Discovery and Geothermal Monitoring with an Agentic Artificial Intelligence Framework

> 方法论文 · 2025 · `wf_bf8bce7bd3a1e07f0f`

**作者**：Randy Harsuko, Zhengfa Bi, Guodong Chen, Nori Nakata  
**原文**：https://arxiv.org/abs/2511.03852  
**研究分支**：其他应用与相邻接口  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Gemma3主代理、Jina/LanceDB文献RAG、预置DT工具和任务上下文；具体更新过程为：CoT/ReAct逐步执行检查工具并回答当前请求；CodeGemma生成可视化代码；更新状态的保留与后继使用为：任务/对话状态保存，未定义经评价保留改进库或后继改进提案。

## 2. 论文的核心内容与贡献

### configuration:cfg_gaia_v1_rag_tool_orchestration
v1只有任务编排和动态tool use；self-evolving multi-agent为未来计划，不据此认证持久改进闭环。

**适用版本**：2511.03852v1；**原文定位**：v1 §2.1–2.3 tool L60–108；v1 §4 tool L165–183。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_gaia_v2_rag_openevolve_prompt_program_loop
v2保留last best程序供下一轮算法变异评价，四结构条件在有限inverse-program系统成立；实际没有优化evaluator。

**适用版本**：2511.03852v2；**原文定位**：v2 §3.1 Eqs10–13 tool L157–198；v2 experiment tool L199–224。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### GAIA v1: fixed RAG and geoscience tool execution
`cfg_gaia_v1_rag_tool_orchestration` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Gemma3主代理、Jina/LanceDB文献RAG、预置DT工具和任务上下文。 |
| 改进过程与下一轮参与 | CoT/ReAct逐步执行检查工具并回答当前请求；CodeGemma生成可视化代码。 |
| 保留的状态及时间尺度 | 任务/对话状态保存，未定义经评价保留改进库或后继改进提案。 |
| 外部固定部分 | - 基础模型 - RAG库/预置tools - 用户参数选择 |

**配置判定**：v1只有任务编排和动态tool use；self-evolving multi-agent为未来计划，不据此认证持久改进闭环。

来源：https://arxiv.org/html/2511.03852v1；版本：2511.03852v1；定位：v1 §2.1–2.3 tool L60–108；v1 §4 tool L165–183。

### GAIA v2: RAG-guided OpenEvolve inverse-program loop
`cfg_gaia_v2_rag_openevolve_prompt_program_loop` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | GAIA检索domain priors、OpenEvolve程序搜索和接受的inverse code；简化温度到fracture参数任务。 |
| 改进过程与下一轮参与 | GAIA调整system prompt，OpenEvolve变异评价选择算法；last best算法作为下一轮基础，最多10迭代。 |
| 保留的状态及时间尺度 | best算法跨迭代传递；prompt引入domain知识；evaluator实验没有更新。 |
| 外部固定部分 | - 简化forward model/合成数据 - 基础LM - OpenEvolve搜索程序 |
| 评价与选择设置 | - **baseline**：10 independent fixed-context runs - **carry**：last best algorithm - **max iterations**：10 |

**配置判定**：v2保留last best程序供下一轮算法变异评价，四结构条件在有限inverse-program系统成立；实际没有优化evaluator。

来源：https://arxiv.org/html/2511.03852v2；版本：2511.03852v2；定位：v2 §3.1 Eqs10–13 tool L157–198；v2 experiment tool L199–224。

## 4. 实验、评价协议与结果的可解释范围


- **baseline**：10 independent fixed-context runs
- **carry**：last best algorithm
- **max iterations**：10

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_gaia_v1_rag_tool_orchestration`**：v1只有任务编排和动态tool use；self-evolving multi-agent为未来计划，不据此认证持久改进闭环。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`r8a_ev_cfg_gaia_v2_rag_openevolve_prompt_program_loop`**：v2保留last best程序供下一轮算法变异评价，四结构条件在有限inverse-program系统成立；实际没有优化evaluator。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- v1题名GAIA与主表现标题不同，按同arXiv家族保留版本。
- v2新增实验不能回填2025v1；此邻接结论不否认v2机制。
- L222明确evaluator未优化，不能把允许双对象优化的目标式当已完成实验。
- 使用OpenEvolve开源实现，非DeepMind私有AlphaEvolve完整复现。
- Table1初始combined0.6142与等权三分量均值约0.48577冲突，未认证数值比较。
- 只有简化合成inverse任务，不外推真实reservoir或一般科学发现。
- - v1题名GAIA与主表现标题不同，按同arXiv家族保留版本。 - v2新增实验不能回填2025v1；此邻接结论不否认v2机制。
- - L222明确evaluator未优化，不能把允许双对象优化的目标式当已完成实验。 - 使用OpenEvolve开源实现，非DeepMind私有AlphaEvolve完整复现。 - Table1初始combined0.6142与等权三分量均值约0.48577冲突，未认证数值比较。 - 只有简化合成inverse任务，不外推真实reservoir或一般科学发现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_gaia_geothermal_v1` · 已存来源 · 2511.03852v1
  - https://arxiv.org/html/2511.03852v1；阅读深度：`targeted_primary_method_state_feedback_limits`。
- `r8a_src_w_gaia_geothermal_v2` · 已存来源 · 2511.03852v2
  - https://arxiv.org/html/2511.03852v2；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bf8bce7bd3a1e07f0f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
