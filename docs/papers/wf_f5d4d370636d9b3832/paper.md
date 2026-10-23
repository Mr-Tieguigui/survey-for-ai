# A Self-Improving Coding Agent

> 方法论文 · 2025 · `wf_f5d4d370636d9b3832`

**作者**：Maxime Robeyns, Martin Szummer, Laurence Aitchison  
**原文**：https://arxiv.org/abs/2504.15228  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：代理版本及成绩归档；具体更新过程为：被选代理执行后继代码修改；更新状态的保留与后继使用为：下一轮选择归档最优代理作meta-agent。

### 定点原文补充：具体问题与执行过程
将编码代理本身作为改进任务，下一轮由档案中效用最高的代理担任元代理，允许改动完整 Python 代码库。

1. 初始系统有文件与命令工具、编码/问题求解/推理子代理，以及周期检查偏离行为的 overseer。
2. 保留代理和评测成绩；档案选中的代理查阅历史、提出改进并实现后继版本。

**实验与选择协议**：

- 效用综合任务得分、美元成本与墙钟时间，权重为 0.5/0.25/0.25；成本与时间归一化上限为 $10 和 300 秒。
- 超时后效用再乘 0.5；这一分数用于选择后继元代理，不用于参数梯度更新。

**解释边界**：

- 成本、时间和超时会影响选择，不能把其效用等同于单一准确率。
- 作者指出持续提出新颖、可实现修改的困难；固定效用和评测设置不认证强 RSI。

来源：[2504.15228v2](https://arxiv.org/html/2504.15228v2)；定位：§3 Methods, Eq. (1)–(2), Algorithm 1；§3.1 Initial agent；§5.1 Limitations。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_sica
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v2；**原文定位**：Sections 3-4。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_sica_hgm_comparison
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v3；**原文定位**：S2.p1；S2.p3；S4.SS1.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_sica
`cfg_sica` · method_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 代理版本及成绩归档。 |
| 改进过程与下一轮参与 | 被选代理执行后继代码修改。 |
| 保留的状态及时间尺度 | 下一轮选择归档最优代理作meta-agent。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2504.15228v2；版本：v2；定位：Sections 3-4。

### cfg_sica_hgm_comparison
`cfg_sica_hgm_comparison` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | SICA baseline implementation in HGM SWE-Verified-60 and Polyglot comparison |
| 改进过程与下一轮参与 | 被选代理执行后继代码修改。 |
| 保留的状态及时间尺度 | 下一轮选择归档最优代理作meta-agent。 |

**配置判定**：HGM研究的基线重实现与搜索树分析配置，非原论文全套实验协议；具体代码/预算等价未认证。

来源：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_sica`**：SICA从档案选最优代理作为下一轮元代理；无模型权重更新。
  - 来源版本：v2；定位：S3.p1；S3.p3；深度：`AI_rechecked_primary_text_author_report`。

- **`e_sica_eval`**：所查实验采用固定50题SWE子集；成本与短超时影响收益解释。
  - 来源版本：v2；定位：S4.p1；S5.SS1.p2；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 外部基准与效用固定
- 不能与其他论文不同设置直接按百分比排名

## 7. 与其他论文的具体关系

### [Automated Design of Agentic Systems](../r04_system/wf_c9890d5668d1c1b33e.md)
关系：`adapts_design_of` · `r_sica_adas` · 当前展示权限：`primary_supported`。
SICA作者明确将其主循环与ADAS档案循环对照：保留代理档案与评测结果，但从档案选择最佳代理充当下一轮元代理，并允许编辑完整Python代码库；ADAS原配置是固定元代理生成目标代理forward函数。

**关系边界**：支持作者明确说明的循环改造，不认证源码复用；ADAS不修改元代理这一结论限于所核Meta Agent Search配置，不将作者对self-improving的术语立场当统一范围协议。

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2504.15228v2（v2；S3.p1.1；S2.p5.1）；https://arxiv.org/html/2408.08435v2（v2；S3.p1.1；S3.p2.1）。

### [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../r03_method/wf_c29f716871f8031486.md)
关系：`alternative_mechanism_to` · `r_dgm_sica` · 当前展示权限：`primary_supported`。
SICA按当前最佳得分选择下一轮元代理；DGM保留多分支档案并按表现与子代探索程度采样父代。

**关系边界**：作者明确同期工作；仅比较选择机制，不画继承边，也不接受任务表现必然等于改进能力的推论。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p3；S3.p3。
- object：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p3。

### [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](../r03_method/wf_title_1935c85b092513ff.md)
关系：`evaluates_configuration` · `r_hgm_sica` · 当前展示权限：`primary_supported`。
HGM在其SWE-Verified-60/Polyglot算法比较中分析SICA的任务得分选择准则与后代clade实证生产力。

**关系边界**：只认证HGM研究中的SICA式算法实例与选择分析，不把结果推广到全部SICA版本或任务；相关性不是因果能力保证。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- object：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。
- recheck_src_w_hgm：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- recheck_src_w_sica：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_sica` · 已存来源 · v2
  - https://arxiv.org/html/2504.15228v2；阅读深度：`未单列`。
- `root_crosscheck_src_w_hgm` · 已存来源 · v3
  - https://arxiv.org/html/2510.21614v3；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f5d4d370636d9b3832 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
