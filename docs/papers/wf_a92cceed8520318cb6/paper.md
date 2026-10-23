# DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

> 方法论文 · 2023 · `wf_a92cceed8520318cb6`

**作者**：Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts  
**原文**：https://arxiv.org/abs/2310.03714  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：混合teleprompter编译记录；具体更新过程为：teleprompter接受程序/训练集/metric并返回新程序；BootstrapFewShot以teacher或zero-shot程序收集成功轨迹；更新状态的保留与后继使用为：单次编译与潜在再编译。

## 2. 论文的核心内容与贡献

### configuration:cfg_dspy_compiled_teacher_composition
正文代码明确把首次compiled_rag传入后续teleprompter的teacher参数，以保留后的程序生成后续优化所需示例并微调新程序。只认证该组合方法的更新teacher参与，不推广到所有DSPy运行。

**适用版本**：v1；**原文定位**：S3.SS3.p7；S4.SS0.SSS0.Px2.p2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dspy_fixed_teacher_single_compile
附录E.1中teacher负责生成轨迹，新增示例写入独立compiled_program，随后返回；该单次调用未让返回后的compiled_program再次承担轨迹生成以改进后继程序。

**适用版本**：v1；**原文定位**：A5.SS1.p1；S4.SS0.SSS0.Px1.p2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dspy_harness_control_static_baseline
具体静态基线为每(model,domain)单次BootstrapFewShot后固定部署，不混入DSPy compiled-teacher两阶段组合或TextGrad的BootstrapFewShotRandomSearch。

**适用版本**：v1；**原文定位**：Harness-control S3.SS2.p1；Harness-control S3.SS4.p1；DSPy S4.SS0.SSS0.Px1.p2；DSPy A5.SS1.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dspy_textgrad_bfsr_baseline
本次指定BFSR基线为独立候选编译与选优；不混入DSPy另一种compiled-teacher组合配置。10候选/最多8示例来自TextGrad具体实验，而非DSPy原文默认参数。

**适用版本**：v1；**原文定位**：TextGrad S3.SS3.p8；DSPy A5.SS2.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_dspy
`cfg_dspy` · scope_index

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 混合teleprompter编译记录 |
| 改进过程与下一轮参与 | teleprompter接受程序/训练集/metric并返回新程序；BootstrapFewShot以teacher或zero-shot程序收集成功轨迹 |
| 保留的状态及时间尺度 | 单次编译与潜在再编译 |
| 外部固定部分 | teleprompter、metric、teacher及选择规则 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。（状态：`unknown`；定位：§3.3–4 tool L182–253）。
- **更新由什么过程产生**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。（状态：`unknown`；定位：§3.3–4 tool L182–253）。
- **状态怎样持久保留**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。（状态：`unknown`；定位：§3.3–4 tool L182–253）。
- **更新怎样进入后续改进**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。（状态：`unknown`；定位：§3.3–4 tool L182–253）。

**配置判定**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。

来源：https://arxiv.org/html/2310.03714v1；版本：2310.03714v1；定位：§3.3–4 tool L182–253。

### cfg_dspy_fixed_teacher_single_compile
`cfg_dspy_fixed_teacher_single_compile` · single_compile_pseudocode_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定teacher、BootstrapFewShot与本次生成的compiled_program；单次编译配置 |
| 保留的状态及时间尺度 | compiled program可跨查询；组合方法跨两次编译 |
| 外部固定部分 | teacher during a compile call、teleprompter、metric、LM；teacher跨组合调用可替换 |

**配置判定**：附录E.1中teacher负责生成轨迹，新增示例写入独立compiled_program，随后返回；该单次调用未让返回后的compiled_program再次承担轨迹生成以改进后继程序。

来源：https://arxiv.org/html/2310.03714v1；版本：v1；定位：A5.SS1.p1；S4.SS0.SSS0.Px1.p2。

### cfg_dspy_compiled_teacher_composition
`cfg_dspy_compiled_teacher_composition` · two_stage_method_example_not_repeated_self_improver_gain

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 首次得到的compiled_rag作为后续BootstrapFinetune的teacher，连同两次编译的程序生成流程 |
| 保留的状态及时间尺度 | compiled program可跨查询；组合方法跨两次编译 |
| 外部固定部分 | teacher during a compile call、teleprompter、metric、LM；teacher跨组合调用可替换 |

**配置判定**：正文代码明确把首次compiled_rag传入后续teleprompter的teacher参数，以保留后的程序生成后续优化所需示例并微调新程序。只认证该组合方法的更新teacher参与，不推广到所有DSPy运行。

来源：https://arxiv.org/html/2310.03714v1；版本：v1；定位：S3.SS3.p7；S4.SS0.SSS0.Px2.p2。

### cfg_dspy_textgrad_bfsr_baseline
`cfg_dspy_textgrad_bfsr_baseline` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | DSPy BootstrapFewShotRandomSearch baseline instantiated in TextGrad prompt-optimization evaluation |
| 改进过程与下一轮参与 | Bootstrap candidate few-shot demonstrations, independently generate candidate programs, evaluate candidates, return the best program. No winner-to-successor teacher recursion is asserted. |
| 保留的状态及时间尺度 | selected compiled prompt retained across held-out queries |
| 外部固定部分 | - teleprompter - metric - candidate generation rule - per-call teacher - LM backends as specified by TextGrad |
| 评价与选择设置 | - **candidate programs**：10 - **datasets**：- BBH word sorting - BBH object counting - GSM8k - **evaluation claim**：uses_as_baseline_only; no superiority claim added - **maximum few shot examples**：8 - **optimizer**：BootstrapFewShotRandomSearch |

**配置判定**：本次指定BFSR基线为独立候选编译与选优；不混入DSPy另一种compiled-teacher组合配置。10候选/最多8示例来自TextGrad具体实验，而非DSPy原文默认参数。

来源：https://arxiv.org/html/2406.07496v1；版本：v1；定位：TextGrad S3.SS3.p8；DSPy A5.SS2.p1。

### cfg_dspy_harness_control_static_baseline
`cfg_dspy_harness_control_static_baseline` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Harness-control论文的DSPy-static：每个(model,domain)单独运行一次BootstrapFewShot，随后固定配置与示例用于评价。 |
| 改进过程与下一轮参与 | 固定teacher/单次编译以domain verifier筛选成功轨迹并生成few-shot demonstrations；不进行在线配置策略更新。 |
| 保留的状态及时间尺度 | 编译后的静态配置与demonstrations跨评价episode保留。 |
| 外部固定部分 | structured prompt、when_needed tools/retrieval、brief_plan、final_check；每(model,domain)一次编译；domain verifier；底层模型。 |
| 评价与选择设置 | - **comparison scope**：Harness-control main matrix and stated follow-ups; not DSPy original benchmark configuration - **compile frequency**：once per (model, domain) - **max steps**：not_explicitly_specified_for_DSPy_static_in_selected_section - **memory policy**：not_explicitly_specified_for_DSPy_static_in_selected_section - **optimizer**：BootstrapFewShot - **planning policy**：brief_plan - **prompt style**：structured - **teacher exact backbone**：not_explicitly_specified_for_compilation_in_selected_section - **tool policy**：when_needed - **training subset**：small labeled subset; exact count not specified in the selected §3.4 - **verification policy**：final_check |

**配置判定**：具体静态基线为每(model,domain)单次BootstrapFewShot后固定部署，不混入DSPy compiled-teacher两阶段组合或TextGrad的BootstrapFewShotRandomSearch。

来源：https://arxiv.org/html/2607.25415v1；版本：v1；定位：Harness-control S3.SS2.p1；Harness-control S3.SS4.p1；DSPy S4.SS0.SSS0.Px1.p2；DSPy A5.SS1.p1。

## 4. 实验、评价协议与结果的可解释范围


- **candidate programs**：10
- **datasets**：- BBH word sorting - BBH object counting - GSM8k
- **evaluation claim**：uses_as_baseline_only; no superiority claim added
- **maximum few shot examples**：8
- **optimizer**：BootstrapFewShotRandomSearch


- **comparison scope**：Harness-control main matrix and stated follow-ups; not DSPy original benchmark configuration
- **compile frequency**：once per (model, domain)
- **max steps**：not_explicitly_specified_for_DSPy_static_in_selected_section
- **memory policy**：not_explicitly_specified_for_DSPy_static_in_selected_section
- **optimizer**：BootstrapFewShot
- **planning policy**：brief_plan
- **prompt style**：structured
- **teacher exact backbone**：not_explicitly_specified_for_compilation_in_selected_section
- **tool policy**：when_needed
- **training subset**：small labeled subset; exact count not specified in the selected §3.4
- **verification policy**：final_check

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_dspy`**：父记录是DSPy框架下多种编译方法的索引，已拆为固定teacher单次编译与compiled-teacher组合；不再把混合单位当成一项待核实验或单一核心认证。
  - 来源版本：2310.03714v1；定位：§3.3–4 tool L182–253；深度：`未单列`。

- **`e2_w_dspy`**：BootstrapFewShot收集通过指标的轨迹，外部teleprompter选择参数或集成
  - 来源版本：v1；定位：S4.p1；S4.SS0.SSS0.Px1.p2；S4.SS0.SSS0.Px2.p1；S4.SS0.SSS0.Px3.p1；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_dspy`**：teleprompter接受程序/训练集/metric并返回新程序；BootstrapFewShot以teacher或zero-shot程序收集成功轨迹
  - 来源版本：v1；定位：S3.SS3.p1；S3.SS3.p2；S4.SS0.SSS0.Px1.p2；S4.SS0.SSS0.Px2.p1；深度：`未单列`。

- **`e4_cfg_dspy`**：单次BootstrapFewShot伪代码使用teacher生成轨迹并向compiled_program添加示例；另有compiled_rag作为后续BootstrapFinetune的teacher的组合示例。
  - 来源版本：v1；定位：S3.SS3.p1；S3.SS3.p7；S4.SS0.SSS0.Px1.p2；S4.SS0.SSS0.Px1.p3；A5.SS1.p1；深度：`未单列`。

- **`e4_cfg_dspy_fixed_teacher_single_compile`**：附录E.1中teacher负责生成轨迹，新增示例写入独立compiled_program，随后返回；该单次调用未让返回后的compiled_program再次承担轨迹生成以改进后继程序。
  - 来源版本：v1；定位：S4.SS0.SSS0.Px1.p2；A5.SS1.p1；深度：`未单列`。

- **`e4_cfg_dspy_compiled_teacher_composition`**：正文代码明确把首次compiled_rag传入后续teleprompter的teacher参数，以保留后的程序生成后续优化所需示例并微调新程序。只认证该组合方法的更新teacher参与，不推广到所有DSPy运行。
  - 来源版本：v1；定位：S3.SS3.p7；S4.SS0.SSS0.Px2.p2；深度：`未单列`。

- **`harness_final_ev_r2_harness_control_dspy_7`**：Harness-control明确把DSPy-static作为非自适应比较基线：与在线控制器共用DSPy Signature/Module上下文组装器，但以每(model,domain)一次BootstrapFewShot产生固定demonstrations。DSPy原文方法和Appendix E.1确认BootstrapFewShot执行teacher并按metric筛选轨迹，写入独立compiled_program后返回。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_explicit_plus_two_endpoint_primary_method_check`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 原文§3.4未给出全部静态六旋钮、teacher精确实例或训练子集数量，不自行填值。
- 基线是静态少样本优化而非多轮在线自改；比较不认证改进器收益。
- 所查研究报告静态基线在其有限预算下匹配或超过在线控制器，不能画成在线控制全面胜出。
- DSPy original pseudocode has its own default trials; TextGrad specifies a different instantiation.
- Code-version equivalence and independent replication not checked.
- 此索引不可承载四条件认证；请引用下列指定子配置及原文。
- 子配置范围不同，不能以组合编译认证所有DSPy运行。
- 支
- 持
- 编
- 译
- 产
- 物
- 改
- 善
- ；
- 本
- 轮
- 选
- 段
- 未
- 证
- 明
- 保
- 留
- 执
- 行
- 或
- 条
- 件
- 化
- 下
- 一
- 次
- 进
- 不
- 从
- r
- e
- c
- u
- s
- i
- v
- l
- y
- 遍
- 历
- 模
- 块
- 推
- 出
- R
- S
- I
- 固
- 定
- t
- a
- h
- 单
- 与
- 可
- 迭
- 代
- b
- o
- p
- n
- g
- 必
- 须
- 拆
- 分
- 当
- 前
- 整
- 篇
- 混
- 合
- 记
- 录
- 直
- 接
- 认
- 完
- 递
- 归
- 父
- 了
- 、
- 组
- 和
- ，
- 给
- 核
- 心
- 。
- 另
- 建
- 两
- 个
- 确
- 配
- 置
- 文
- 字
- 称
- 等
- 于
- 主
- 实
- 验
- 已
- 多
- 再
- m
- 底
- 层
- L
- M
- 无
- 限
- 器
- 收
- 益
- 例
- 全
- 部
- 关系是uses_as_baseline，不是从DSPy多轮递归机制继承而来。目标端是本研究实例化的DSPy-static单次编译基线，不能替换为混合cfg_dspy、compiled-teacher组合或TextGrad的BFSR。共享组装器是实现组件使用事实，不额外认证代码逐行复用、版本等价、保证继承或在线性能优势。

## 7. 与其他论文的具体关系

### [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](../r04_system/wf_52ede7e4f56bedfa00.md)
关系：`uses_as_baseline` · `r2_harness_control_dspy_7` · 当前展示权限：`primary_supported`。
Harness-control明确把DSPy-static作为非自适应比较基线：与在线控制器共用DSPy Signature/Module上下文组装器，但以每(model,domain)一次BootstrapFewShot产生固定demonstrations。DSPy原文方法和Appendix E.1确认BootstrapFewShot执行teacher并按metric筛选轨迹，写入独立compiled_program后返回。

**关系边界**：关系是uses_as_baseline，不是从DSPy多轮递归机制继承而来。目标端是本研究实例化的DSPy-static单次编译基线，不能替换为混合cfg_dspy、compiled-teacher组合或TextGrad的BFSR。共享组装器是实现组件使用事实，不额外认证代码逐行复用、版本等价、保证继承或在线性能优势。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2607.25415v1；版本：v1；定位：S3.SS1.p1；S3.SS2.p1；S3.SS4.p1；S5.SS1.p2.1；S5.SS2.p1；S7.p1。
- object：https://arxiv.org/html/2310.03714v1；版本：v1；定位：S3.SS3.p1；S4.SS0.SSS0.Px1.p1；S4.SS0.SSS0.Px1.p2；A5.SS1.p1。
- expand_src_w_harness_control：https://arxiv.org/html/2607.25415v1；版本：v1；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1；S3.SS2.p1。

## 8. 来源清单、复查入口与解析缺口
- `completion_agent_src_w_textgrad` · 已存来源 · v1
  - https://arxiv.org/html/2406.07496v1；阅读深度：`selected_primary_method_passages`。
- `expand_src_w_dspy` · DSPy · v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。
- `harness_final_src_w_dspy` · 已存来源 · v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。
- `harness_final_src_w_harness_control` · 已存来源 · v1
  - https://arxiv.org/html/2607.25415v1；阅读深度：`未单列`。
- `r7root_src_dspy_scope` · 已存来源 · 2310.03714v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。
- `src_20261013_w_dspy` · 已存来源 · v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。
- `stage1_src_w_dspy` · 已存来源 · v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a92cceed8520318cb6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
