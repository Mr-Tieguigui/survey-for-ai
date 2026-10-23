# Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses

> 方法论文 · 2026 · `wf_28881c2e1ce10ebb94`

**作者**：Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang  
**原文**：https://arxiv.org/abs/2608.24876  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定base LLM/tools外的memory-control M=(E,W,rho,C)为唯一可写层：经验skills、WM schema/update proposal、invocation policy及state checkers。fixed Claude-Code Meta-Agent和admission gate在外；具体更新过程为：结构trace把state、skills、action、observation和checker decisions关联；Meta-Agent做repair localization并按被诊断组件提patch；fixed gate要求修复source failure且不回退dev anchors；更新状态的保留与后继使用为：accepted M跨任务继承，后续行为生成新structured trace再触发diagnosis/patch；未通过则沿用旧M。

## 2. 论文的核心内容与贡献

### configuration:cfg_recuris_cross_task_memory_control_evolution_v1
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 结构trace把state、skills、action、observation和checker decisions关联；Meta-Agent做repair localization并按被诊断组件提patch；fixed gate要求修复source failure且不回退dev anchors。

**适用版本**：2608.24876v1；**原文定位**：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Recuris v1 cross-task memory-control evolution under fixed Meta-Agent
`cfg_recuris_cross_task_memory_control_evolution_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定base LLM/tools外的memory-control M=(E,W,rho,C)为唯一可写层：经验skills、WM schema/update proposal、invocation policy及state checkers。fixed Claude-Code Meta-Agent和admission gate在外。 |
| 改进过程与下一轮参与 | 结构trace把state、skills、action、observation和checker decisions关联；Meta-Agent做repair localization并按被诊断组件提patch；fixed gate要求修复source failure且不回退dev anchors。 |
| 保留的状态及时间尺度 | accepted M跨任务继承，后续行为生成新structured trace再触发diagnosis/patch；未通过则沿用旧M。 |
| 外部固定部分 | - base model、tools、Meta-Agent及localization/patch程序 - fixed validation gate、非memory harness - 预先固定evolve/dev/test split；test不进patch或gate |
| 评价与选择设置 | - **Meta-Agent**：Claude Code; same fixed prompts/procedure across rounds - **base**：default doubao-seed-2-0-pro frozen; same model also simulated user on tau2 - **evaluation**：tau2 Retail/Airline and SkillFlow; default k=4 independent attempts, 200-step cap; prior split evolve/dev/test |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2.1明确四component patch空间及外部fixed agent。（状态：`supported`；定位：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257）。
- **更新由什么过程产生**：fixed但LLM-based Meta-Agent由本系统执行失败trace诱导component patch。（状态：`supported`；定位：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257）。
- **状态怎样持久保留**：§2.3 admission持久替换M；其余component原样复制。（状态：`supported`；定位：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257）。
- **更新怎样进入后续改进**：新M改变未来state/skill/verification行为并生成下一轮trace。（状态：`supported`；定位：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 结构trace把state、skills、action、observation和checker decisions关联；Meta-Agent做repair localization并按被诊断组件提patch；fixed gate要求修复source failure且不回退dev anchors。

来源：https://arxiv.org/html/2608.24876v1；版本：2608.24876v1；定位：§2.1 writable memory-control boundary and trace tool L153–175；§2.3.1–3 localization, component patch and fixed gate tool L204–227；§2.3.4 retained update generates next trace tool L228–234；§2.3.5 distinct single-task adaptation tool L235–237；§3.1 actual Meta-Agent and evaluation freeze tool L246–257。

## 4. 实验、评价协议与结果的可解释范围


- **Meta-Agent**：Claude Code; same fixed prompts/procedure across rounds
- **base**：default doubao-seed-2-0-pro frozen; same model also simulated user on tau2
- **evaluation**：tau2 Retail/Airline and SkillFlow; default k=4 independent attempts, 200-step cap; prior split evolve/dev/test

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_recuris_cross_task_memory_control_evolution_v1`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 结构trace把state、skills、action、observation和checker decisions关联；Meta-Agent做repair localization并按被诊断组件提patch；fixed gate要求修复source failure且不回退dev anchors。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- localization是实用repair attribution，作者明确不宣称因果识别。
- 可变checker C是任务状态支持检查，admission gate自身固定；不能混为评价者完全自改。
- cross-task配置评价冻结memory；§2.3.5单task一bit test-time adaptation为另一模式，未并入。
- localization是实用repair attribution，作者明确不宣称因果识别。; 可变checker C是任务状态支持检查，admission gate自身固定；不能混为评价者完全自改。; cross-task配置评价冻结memory；§2.3.5单task一bit test-time adaptation为另一模式，未并入。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_recuris` · Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses · 2608.24876v1
  - https://arxiv.org/html/2608.24876v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_28881c2e1ce10ebb94 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
