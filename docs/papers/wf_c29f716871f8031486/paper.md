# Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

> 方法论文 · 2025 · `wf_c29f716871f8031486`

**作者**：Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune  
**原文**：https://arxiv.org/abs/2505.22954  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：可编译、可继续编辑代码的代理归档；具体更新过程为：被修改的编码代理参与后续自修改；更新状态的保留与后继使用为：归档父代产生后继代码版本。

### 定点原文补充：具体问题与执行过程
研究编码代理能否修改自己的实现，并让保留的后继代理继续自修改；基础模型权重冻结。

1. 从档案采样父代，综合成绩与已有子代数量进行探索；父代分析日志、提出功能、改写自身代码。
2. 候选经评测后，仅能编译且仍可编辑代码的版本进入档案；档案并非只保存即时最高分。

**实验与选择协议**：

- 作者运行 80 次迭代；SWE-bench 指 Verified 子集，使用分阶段候选评测。
- Polyglot 报告 pass@1，而相应社区榜单采用可看一次真值反馈的 pass@2，二者不直接等价。

**作者报告的结果（未独立复现）**：作者报告 SWE-bench 20.0%→50.0%、Polyglot 14.2%→30.7%；这是该论文设置的作者结果，未在此复现。

**解释边界**：

- 档案维护和父代选择固定，不在代理可修改代码中。
- 编码基准改善被用作自修改能力代理指标，不足以独立证明改进器加速或无界增长。

来源：[2505.22954v3](https://arxiv.org/html/2505.22954v3)；定位：§3 Darwin Gödel Machine；§4.1–4.4 Experiments；Appendix C.2–C.4。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_dgm
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v3；**原文定位**：Section 3; Appendix C.4。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dgm_hgm_comparison
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v3；**原文定位**：S2.p1；S2.p3；S4.SS1.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dgm_polyglot
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v3；**原文定位**：Sections 3-4.2; Appendix E.3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_dgm
`cfg_dgm` · main_experiment

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 可编译、可继续编辑代码的代理归档。 |
| 改进过程与下一轮参与 | 被修改的编码代理参与后续自修改。 |
| 保留的状态及时间尺度 | 归档父代产生后继代码版本。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2505.22954v3；版本：v3；定位：Section 3; Appendix C.4。

### cfg_dgm_polyglot
`cfg_dgm_polyglot` · domain_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 可编译、可继续编辑代码的代理归档。 |
| 改进过程与下一轮参与 | 被修改的编码代理参与后续自修改。 |
| 保留的状态及时间尺度 | 归档父代产生后继代码版本。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2505.22954v3；版本：v3；定位：Sections 3-4.2; Appendix E.3。

### cfg_dgm_hgm_comparison
`cfg_dgm_hgm_comparison` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | DGM baseline implementation in HGM SWE-Verified-60 and Polyglot comparison |
| 改进过程与下一轮参与 | 被修改的编码代理参与后续自修改。 |
| 保留的状态及时间尺度 | 归档父代产生后继代码版本。 |

**配置判定**：HGM研究的基线重实现与搜索树分析配置，非原论文全套实验协议；具体代码/预算等价未认证。

来源：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_dgm`**：代理代码可自修改并保留有效候选；外层档案/父选择固定。
  - 来源版本：v3；定位：S3.p2；S3.p3；深度：`AI_rechecked_primary_text_author_report`。

- **`e_dgm_theory`**：DGM以经验评价替代原理论的证明要求。
  - 来源版本：v3；定位：S3.p1；深度：`AI_rechecked_primary_text_author_report`。

- **`e_dgm_adas`**：作者以固定元代理的ADAS范式作机制对照及基线。
  - 来源版本：v3；定位：S2.p2；S4.SS3.p1；深度：`AI_rechecked_primary_text_author_report`。

- **`e_dgm_sica`**：作者把SICA描述为并行、相近的工作，区分开放式档案探索。
  - 来源版本：v3；定位：S2.p3；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只保留编译及编辑能力合格候选；冻结FM
- 不是Gödel最优性保证或源码继承
- 未证明两篇代码复用或实验完全等价
- 不是SICA→DGM技术继承证据

## 7. 与其他论文的具体关系

### [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../r02_concept/wf_0e73b118b5b1559785.md)
关系：`alternative_mechanism_to` · `r_dgm_godel` · 当前展示权限：`primary_supported`。
Gödel Machine用形式证明触发可包含证明搜索器的代码重写；DGM将接受依据改为实验反馈，采用档案式开放探索。

**关系边界**：思想启发与证据机制替代；DGM不继承Gödel Machine在一致公理和可证明性条件下的最优性保证，不证明无界增长。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p1。
- object：https://arxiv.org/html/cs/0309048v5；版本：v5；定位：S2.SS2.p1；S4.SS1.p1。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p1。
- recheck_src_w_godel：https://arxiv.org/html/cs/0309048v5；版本：v5；定位：S2.SS2.p1；S4.SS1.p1。

### [Hyperagents](../r03_method/wf_17eec8a15debc212b5.md)
关系：`extends_configuration_of` · `r_hyper_dgm` · 当前展示权限：`primary_supported`。
DGM-H作者明确基于DGM保留开放式档案探索，并将任务代理与可编辑元代理结合为同一程序，使生成后续改进的元级机制可被编辑。DGM原方法将开放探索与档案/父代选择排除在代理可修改代码之外。

**关系边界**：主实验的父代选择仍手工固定；父代选择修改为附加探测配置，不将其结果混入主配置；仅作者方法继承核查，不证明任意任务无界加速。

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2603.19461v1（v1；S3.p1.1；S3.p3.1；S3.p4.1；S3.p5.1）；https://arxiv.org/html/2505.22954v3（v3；S3.p2.1；S3.p3.1）。

### [Automated Design of Agentic Systems](../r04_system/wf_c9890d5668d1c1b33e.md)
关系：`contrasts_system_boundary_with` · `r_dgm_adas` · 当前展示权限：`primary_supported`。
DGM由可演化代理修改自身代码，ADAS核查配置由固定元代理生成目标代理函数；DGM另实现固定元代理消融模拟ADAS式设计。

**关系边界**：DGM消融是该论文的重实现，不能称原ADAS代码或整个原实验被完全复现；档案、选择与评价仍有固定部分。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p2；S3.p2；S4.SS3.p1。
- object：https://arxiv.org/html/2408.08435v2；版本：v2；定位：S3.p1；S3.p2。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p2；S4.SS3.p1。

### [A Self-Improving Coding Agent](../r03_method/wf_f5d4d370636d9b3832.md)
关系：`alternative_mechanism_to` · `r_dgm_sica` · 当前展示权限：`primary_supported`。
SICA按当前最佳得分选择下一轮元代理；DGM保留多分支档案并按表现与子代探索程度采样父代。

**关系边界**：作者明确同期工作；仅比较选择机制，不画继承边，也不接受任务表现必然等于改进能力的推论。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p3；S3.p3。
- object：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p3。

### [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](../r03_method/wf_title_1935c85b092513ff.md)
关系：`evaluates_configuration` · `r_hgm_dgm` · 当前展示权限：`primary_supported`。
HGM在SWE-Verified-60/Polyglot运行树上分析DGM选择指标与后代clade实证生产力的关系。

**关系边界**：配置限于该研究的算法实例和离线树分析，原DGM完整任务集/预算不等同；经验后代最大值是有界估计，不是内在改进能力的普遍测量。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- object：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p2；S3.p3。
- recheck_src_w_hgm：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p2；S3.p3。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_dgm` · 已存来源 · v3
  - https://arxiv.org/html/2505.22954v3；阅读深度：`未单列`。
- `root_crosscheck_src_w_hgm` · 已存来源 · v3
  - https://arxiv.org/html/2510.21614v3；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline, original_abstract, registry_abstract。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c29f716871f8031486 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
