# KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

> 方法论文 · 2026 · `wf_ba19f0a17f5460757e`

**作者**：Yunxin Li, Jinchao Li, Shibo Su, Zhenran Xu, Chenrui Zhao, Tongshu Bian, Xiaoman Liang, Meishan Zhang, Baotian Hu, Min Zhang  
**原文**：https://arxiv.org/abs/2607.12625  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Host与GUI executor及持久经验/技能store构成边界；短期blackboard另存跨应用值。配置限于§4的轨迹诱导、检索和失败技能修复；具体更新过程为：Reflect从运行轨迹诱导经验项/声明式技能；复用技能失败时优先原位修复，引用原技能、失败步骤、屏幕证据和先前反馈；合格记录经检查后入库；更新状态的保留与后继使用为：经验、技能、可靠性计数跨任务保留；后续检索改变路由和执行，产生的新失败再驱动修复。非权重更新。

## 2. 论文的核心内容与贡献

### configuration:cfg_knowact_guiclaw_memory_skill_repair_v1
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 Reflect从运行轨迹诱导经验项/声明式技能；复用技能失败时优先原位修复，引用原技能、失败步骤、屏幕证据和先前反馈；合格记录经检查后入库。

**适用版本**：2607.12625v1；**原文定位**：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### KnowAct-GUIClaw v1 trajectory-derived memory and guarded skill repair
`cfg_knowact_guiclaw_memory_skill_repair_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Host与GUI executor及持久经验/技能store构成边界；短期blackboard另存跨应用值。配置限于§4的轨迹诱导、检索和失败技能修复。 |
| 改进过程与下一轮参与 | Reflect从运行轨迹诱导经验项/声明式技能；复用技能失败时优先原位修复，引用原技能、失败步骤、屏幕证据和先前反馈；合格记录经检查后入库。 |
| 保留的状态及时间尺度 | 经验、技能、可靠性计数跨任务保留；后续检索改变路由和执行，产生的新失败再驱动修复。非权重更新。 |
| 外部固定部分 | - host/executor模型配置及action normalization接口 - 当前指令优先、实时GUI状态契约、skill extraction/repair外层提示与过滤规则 |
| 评价与选择设置 | - **AndroidDaily**：LLM judge for GUI-only; two human experts for answer tasks - **MobileWorld**：117 GUI-Only tasks, native deterministic evaluator, 50-step cap; pass@1 primary - **models**：default Qwen3.5-397B host / Qwen3.5-35B executor; Kimi-K2.6 separate configuration |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4.1区分host–executor接口及两个持久store。（状态：`supported`；定位：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253）。
- **更新由什么过程产生**：§4.5系统自己由轨迹诱导经验并修复失败的复用技能。（状态：`supported`；定位：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253）。
- **状态怎样持久保留**：技能/经验入长期store，保留计数及先前反馈。（状态：`supported`；定位：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253）。
- **更新怎样进入后续改进**：更新后技能/经验条件化未来路由执行；未来复用失败携原技能和反馈再修复。（状态：`supported`；定位：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 Reflect从运行轨迹诱导经验项/声明式技能；复用技能失败时优先原位修复，引用原技能、失败步骤、屏幕证据和先前反馈；合格记录经检查后入库。

来源：https://arxiv.org/html/2607.12625v1；版本：2607.12625v1；定位：§4.1–4.2 boundary and memory retrieval tool L150–163；§4.4–4.5 retained skill repair and experience feedback tool L187–203；§5.1 evaluation interfaces tool L205–211；§5.3 compound ablation boundary tool L251–253。

## 4. 实验、评价协议与结果的可解释范围


- **AndroidDaily**：LLM judge for GUI-only; two human experts for answer tasks
- **MobileWorld**：117 GUI-Only tasks, native deterministic evaluator, 50-step cap; pass@1 primary
- **models**：default Qwen3.5-397B host / Qwen3.5-35B executor; Kimi-K2.6 separate configuration

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_knowact_guiclaw_memory_skill_repair_v1`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 Reflect从运行轨迹诱导经验项/声明式技能；复用技能失败时优先原位修复，引用原技能、失败步骤、屏幕证据和先前反馈；合格记录经检查后入库。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只承认外部memory/skill层有限闭环，不推断backbone或外层改进器自改。
- 主表与消融同时改变host、router、memory或skills；不能把全部收益单独归因于递归修复。
- 所读§5.1未建立记忆构建任务与最终117-task评价的严格隔离；不宣称未见任务泛化。
- 只承认外部memory/skill层有限闭环，不推断backbone或外层改进器自改。; 主表与消融同时改变host、router、memory或skills；不能把全部收益单独归因于递归修复。; 所读§5.1未建立记忆构建任务与最终117-task评价的严格隔离；不宣称未见任务泛化。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_knowact` · KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill · 2607.12625v1
  - https://arxiv.org/html/2607.12625v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ba19f0a17f5460757e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
