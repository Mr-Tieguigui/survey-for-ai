# Meta$^n$: Recursive Self-Improvement through Emergent Depth

> 方法论文 · 2026 · `wf_518f6f6cde2093479a`

**作者**：Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa, Dongyeop Kang  
**原文**：https://arxiv.org/abs/2608.24735  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：代码层栈及候选链归档；具体更新过程为：递归进入累积代码与轨迹，而非驱动操作自修改；更新状态的保留与后继使用为：固定Omega读取前层产物；不改写Omega。

## 2. 论文的核心内容与贡献

### configuration:cfg_meta_n
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v1；**原文定位**：Sections 2.2-2.4。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_meta_n_agentic
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v1；**原文定位**：Sections 2.2-2.4; Appendix J。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_meta_n
`cfg_meta_n` · main_experiment

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 代码层栈及候选链归档。 |
| 改进过程与下一轮参与 | 递归进入累积代码与轨迹，而非驱动操作自修改。 |
| 保留的状态及时间尺度 | 固定Omega读取前层产物；不改写Omega。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2608.24735v1；版本：v1；定位：Sections 2.2-2.4。

### cfg_meta_n_agentic
`cfg_meta_n_agentic` · domain_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 代码层栈及候选链归档。 |
| 改进过程与下一轮参与 | 递归进入累积代码与轨迹，而非驱动操作自修改。 |
| 保留的状态及时间尺度 | 固定Omega读取前层产物；不改写Omega。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2608.24735v1；版本：v1；定位：Sections 2.2-2.4; Appendix J。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_meta_n`**：固定Ω以累积代码和轨迹作输入产生下一层，递归输入与操作更新分开。
  - 来源版本：v1；定位：S2.SS1.p5；S2.SS2.SSS0.Px1.p1；S2.SS2.SSS0.Px1.p3；深度：`AI_rechecked_primary_text_author_report`。

- **`e_meta_n_contrast`**：作者把HyperAgents等作为保留固定驱动的自指路线进行对照。
  - 来源版本：v1；定位：S2.SS1.p3；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 固定Ω本身没有发生改写
- 其元深度数值划分是作者框架，未独立认证

## 7. 与其他论文的具体关系

### [Hyperagents](../r03_method/wf_17eec8a15debc212b5.md)
关系：`contrasts_system_boundary_with` · `r_meta_n_hyper` · 当前展示权限：`primary_supported`。
Meta-n固定Ω并增深其输入代码/轨迹栈；HyperAgents将任务与元修改代码放入可编辑程序，但主实验父代选择仍固定。

**关系边界**：不沿用Meta-n作者自定的2.5层深度作为领域标准；输入层级增长不同于外算子自改，主实验与父代选择附加探测分开。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2608.24735v1；版本：v1；定位：S2.SS1.p5；S2.SS2.SSS0.Px1.p1；S2.SS2.SSS0.Px1.p3。
- object：https://arxiv.org/html/2603.19461v1；版本：v1；定位：S3.p1；S3.p3；S3.p5。
- recheck_src_w_meta_n：https://arxiv.org/html/2608.24735v1；版本：v1；定位：S2.SS1.p3。
- recheck_src_w_meta_n：https://arxiv.org/html/2608.24735v1；版本：v1；定位：S2.SS1.p5；S2.SS2.SSS0.Px1.p1；S2.SS2.SSS0.Px1.p3。
- recheck_src_w_hyperagents：https://arxiv.org/html/2603.19461v1；版本：v1；定位：S3.p5；S4.p1。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_meta_n` · 已存来源 · v1
  - https://arxiv.org/html/2608.24735v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_518f6f6cde2093479a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
