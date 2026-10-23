# A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain

> 综合系统/智能体 · 2026 · `wf_52ede7e4f56bedfa00`

**作者**：Debjyoti Paul  
**原文**：https://arxiv.org/abs/2607.25415  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：冻结LM与选择harness配置的在线策略；具体更新过程为：bandit/REINFORCE参数更新影响后续配置选择和收集到的奖励；更新状态的保留与后继使用为：跨在线episode。

## 2. 论文的核心内容与贡献

### configuration:cfg_harness_control_online
结构核心限定在线控制状态；无代码自改；作者报告静态DSPy基线在该预算下更好，不画成全面性能进步

**适用版本**：v1；**原文定位**：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1；S3.SS2.p1；S5.SS1.p2.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_harness_control_online
`cfg_harness_control_online` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LM与选择harness配置的在线策略 |
| 改进过程与下一轮参与 | bandit/REINFORCE参数更新影响后续配置选择和收集到的奖励 |
| 保留的状态及时间尺度 | 跨在线episode |
| 外部固定部分 | 729行动空间、LM、奖励及bandit/REINFORCE公式 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：冻结LM与选择harness配置的在线策略（状态：`supported`；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1）。
- **更新由什么过程产生**：bandit/REINFORCE参数更新影响后续配置选择和收集到的奖励（状态：`supported`；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1）。
- **状态怎样持久保留**：跨在线episode（状态：`supported`；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1）。
- **更新怎样进入后续改进**：bandit/REINFORCE参数更新影响后续配置选择和收集到的奖励（状态：`supported`；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1）。

**配置判定**：结构核心限定在线控制状态；无代码自改；作者报告静态DSPy基线在该预算下更好，不画成全面性能进步

来源：https://arxiv.org/html/2607.25415v1；版本：v1；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1；S3.SS2.p1；S5.SS1.p2.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_harness_control`**：bandit/REINFORCE参数更新影响后续配置选择和收集到的奖励
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1；S3.SS2.p1；深度：`AI_primary_method_passage_recheck`。

- **`harness_final_ev_r2_harness_control_dspy_7`**：Harness-control明确把DSPy-static作为非自适应比较基线：与在线控制器共用DSPy Signature/Module上下文组装器，但以每(model,domain)一次BootstrapFewShot产生固定demonstrations。DSPy原文方法和Appendix E.1确认BootstrapFewShot执行teacher并按metric筛选轨迹，写入独立compiled_program后返回。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_explicit_plus_two_endpoint_primary_method_check`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 共享DSPy上下文组装器不意味着在线控制器采用BootstrapFewShot作为在线更新规则。
- 729配置的固定离散行动空间和bandit/REINFORCE更新公式保持外部固定；未证明代码自改。
- DSPy-static基线的具体实验设置应查cfg_dspy_harness_control_static_baseline，不套用DSPy其他编译组合。
- 结
- 构
- 核
- 心
- 限
- 定
- 在
- 线
- 控
- 制
- 状
- 态
- ；
- 无
- 代
- 码
- 自
- 改
- 作
- 者
- 报
- 告
- 静
- D
- S
- P
- y
- 基
- 该
- 预
- 算
- 下
- 更
- 好
- ，
- 不
- 画
- 成
- 全
- 面
- 性
- 能
- 进
- 步
- 关系是uses_as_baseline，不是从DSPy多轮递归机制继承而来。目标端是本研究实例化的DSPy-static单次编译基线，不能替换为混合cfg_dspy、compiled-teacher组合或TextGrad的BFSR。共享组装器是实现组件使用事实，不额外认证代码逐行复用、版本等价、保证继承或在线性能优势。

## 7. 与其他论文的具体关系

### [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](../r03_method/wf_a92cceed8520318cb6.md)
关系：`uses_as_baseline` · `r2_harness_control_dspy_7` · 当前展示权限：`primary_supported`。
Harness-control明确把DSPy-static作为非自适应比较基线：与在线控制器共用DSPy Signature/Module上下文组装器，但以每(model,domain)一次BootstrapFewShot产生固定demonstrations。DSPy原文方法和Appendix E.1确认BootstrapFewShot执行teacher并按metric筛选轨迹，写入独立compiled_program后返回。

**关系边界**：关系是uses_as_baseline，不是从DSPy多轮递归机制继承而来。目标端是本研究实例化的DSPy-static单次编译基线，不能替换为混合cfg_dspy、compiled-teacher组合或TextGrad的BFSR。共享组装器是实现组件使用事实，不额外认证代码逐行复用、版本等价、保证继承或在线性能优势。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2607.25415v1；版本：v1；定位：S3.SS1.p1；S3.SS2.p1；S3.SS4.p1；S5.SS1.p2.1；S5.SS2.p1；S7.p1。
- object：https://arxiv.org/html/2310.03714v1；版本：v1；定位：S3.SS3.p1；S4.SS0.SSS0.Px1.p1；S4.SS0.SSS0.Px1.p2；A5.SS1.p1。
- expand_src_w_harness_control：https://arxiv.org/html/2607.25415v1；版本：v1；定位：S3.SS1.p1；S3.SS4.p1；S5.SS2.p1；S7.p1；S3.SS2.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_harness_control` · A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain · v1
  - https://arxiv.org/html/2607.25415v1；阅读深度：`未单列`。
- `harness_final_src_w_dspy` · 已存来源 · v1
  - https://arxiv.org/html/2310.03714v1；阅读深度：`未单列`。
- `harness_final_src_w_harness_control` · 已存来源 · v1
  - https://arxiv.org/html/2607.25415v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_52ede7e4f56bedfa00 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
