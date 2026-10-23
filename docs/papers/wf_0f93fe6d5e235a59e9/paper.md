# Cura 1T: Healthcare Foundation Model via Recursive Self-Improvement

> 方法论文 · 2026 · `wf_0f93fe6d5e235a59e9`

**作者**：Haolin Chen, Leon Qi, Steve Brown, Deon Metelski, Tao Xia, Joonyul Lee, Qixuan Wang, Kevin Riley, Frank Wang, Weiran Yao  
**原文**：https://arxiv.org/abs/2607.15314  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：training-agent、保留adapter/checkpoint、data mixture、graded trajectories和human plan/keep/revert gates；具体更新过程为：agent诊断失败用skills修data；SFT筛→RL→SDFT训练评价，human review若keep则成下一continuation并积累validated recipe；更新状态的保留与后继使用为：kept round和mixture入下一轮；reverted只留历史不作训练parent。

## 2. 论文的核心内容与贡献

### configuration:cfg_cura_human_gated_data_recipe_adapter_loop_v1
agent数据修订、accepted model continuation回流下一失败诊断，四条件在带人工gate的有限post-training系统成立，不称全自动。

**适用版本**：2607.15314v1；**原文定位**：§3.1–3.2 tool L110–150；§6 limits tool L243–250。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Cura 1T: human-gated data-recipe and adapter continuation
`cfg_cura_human_gated_data_recipe_adapter_loop_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | training-agent、保留adapter/checkpoint、data mixture、graded trajectories和human plan/keep/revert gates。 |
| 改进过程与下一轮参与 | agent诊断失败用skills修data；SFT筛→RL→SDFT训练评价，human review若keep则成下一continuation并积累validated recipe。 |
| 保留的状态及时间尺度 | kept round和mixture入下一轮；reverted只留历史不作训练parent。 |
| 外部固定部分 | - 训练agent - human plan/review gates - 训练栈/benchmark harness/row validation |

**配置判定**：agent数据修订、accepted model continuation回流下一失败诊断，四条件在带人工gate的有限post-training系统成立，不称全自动。

来源：https://arxiv.org/html/2607.15314v1；版本：2607.15314v1；定位：§3.1–3.2 tool L110–150；§6 limits tool L243–250。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_cura_human_gated_data_recipe_adapter_loop_v1`**：agent数据修订、accepted model continuation回流下一失败诊断，四条件在带人工gate的有限post-training系统成立，不称全自动。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- v1题名Specialized Model for Agentic Healthcare，规范主表其他标题非本版原文。
- LoRA adapter非全参数训练；plan和keep/revert/deploy均有human review。
- 报告benchmark不证真实临床安全，不能写成部署医疗有效性。
- SDFT privileged-context额外信息是外部输入，不称纯无监督自举。
- - v1题名Specialized Model for Agentic Healthcare，规范主表其他标题非本版原文。 - LoRA adapter非全参数训练；plan和keep/revert/deploy均有human review。 - 报告benchmark不证真实临床安全，不能写成部署医疗有效性。 - SDFT privileged-context额外信息是外部输入，不称纯无监督自举。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_cura_1t_v1` · 已存来源 · 2607.15314v1
  - https://arxiv.org/html/2607.15314v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0f93fe6d5e235a59e9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
