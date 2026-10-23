# Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

> 方法论文 · 2026 · `wf_2144cdc921ff7eb4a5`

**作者**：Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang  
**原文**：https://arxiv.org/abs/2610.11794  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：冻结LLM、自然语言rulebook ψ、可执行world model θ、交互历史H、replay verifier及planner，面向未知deterministic POMDP。θ指程序不是神经网络参数；具体更新过程为：预测与环境observation不符触发retain/revise_rulebook/repair_code；冻结LLM修规则及编译代码。所有历史exact replay加LLM语义fidelity审核后接受，reconstructed state用于下一次planning和exploration，取得新证据再改模型；更新状态的保留与后继使用为：Z=(H,ψ,θ)及replayed internal state跨同一环境的动作/尝试保留；更改θ后回放旧轨迹重构状态，未认证跨不同game长期共享。

## 2. 论文的核心内容与贡献

### configuration:cfg_memento3_single_rulebook_executable_model_v1
单环境外部world-model状态反馈满足四条件；不因冻结LLM或固定更新算子否定C4。模型选择近似不是完整Bayesian后验认证。

**适用版本**：2610.11794v1；**原文定位**：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Memento3 v1 single persistent rulebook/executable model for interactive planning
`cfg_memento3_single_rulebook_executable_model_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LLM、自然语言rulebook ψ、可执行world model θ、交互历史H、replay verifier及planner，面向未知deterministic POMDP。θ指程序不是神经网络参数。 |
| 改进过程与下一轮参与 | 预测与环境observation不符触发retain/revise_rulebook/repair_code；冻结LLM修规则及编译代码。所有历史exact replay加LLM语义fidelity审核后接受，reconstructed state用于下一次planning和exploration，取得新证据再改模型。 |
| 保留的状态及时间尺度 | Z=(H,ψ,θ)及replayed internal state跨同一环境的动作/尝试保留；更改θ后回放旧轨迹重构状态，未认证跨不同game长期共享。 |
| 外部固定部分 | - frozen LLM及反射/编译/验证/规划接口 - 实际环境转移和completion反馈 - ARC-AGI-3 action budget/score |
| 评价与选择设置 | - **backbone**：Claude Opus5 / Claude Code extra-high - **benchmark**：25 public ARC-AGI-3 games - **objective**：goal completion probability then conditional action cost; RHAE for ARC - **verification**：exact observation replay + frozen LLM semantic fidelity |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2.1区分真实环境和外部学习state Z。（状态：`supported`；定位：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504）。
- **更新由什么过程产生**：代理依交互错误自主修ψ/θ。（状态：`supported`；定位：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504）。
- **状态怎样持久保留**：pair与历史超出单次输出持续，改代码后仍回放此前证据。（状态：`supported`；定位：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504）。
- **更新怎样进入后续改进**：已接受模型指导下次行动/探索，影响后续数据和下一次模型修订。（状态：`supported`；定位：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504）。

**配置判定**：单环境外部world-model状态反馈满足四条件；不因冻结LLM或固定更新算子否定C4。模型选择近似不是完整Bayesian后验认证。

来源：https://arxiv.org/html/2610.11794v1；版本：2610.11794v1；定位：§2.1 persistent hypothesis/feedback tool L118–135；§2.2–2.3 verification/selection tool L226–248；§3.1 scoring cost boundary tool L305–316；§6–7 public set/limits tool L495–504。

## 4. 实验、评价协议与结果的可解释范围


- **backbone**：Claude Opus5 / Claude Code extra-high
- **benchmark**：25 public ARC-AGI-3 games
- **objective**：goal completion probability then conditional action cost; RHAE for ARC
- **verification**：exact observation replay + frozen LLM semantic fidelity

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_memento3_single_rulebook_executable_model_v1`**：单环境外部world-model状态反馈满足四条件；不因冻结LLM或固定更新算子否定C4。模型选择近似不是完整Bayesian后验认证。 预测与环境observation不符触发retain/revise_rulebook/repair_code；冻结LLM修规则及编译代码。所有历史exact replay加LLM语义fidelity审核后接受，reconstructed state用于下一次planning和exploration，取得新证据再改模型。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- exact replay只认证已观测轨迹的预测；rulebook fidelity由LLM审，不是对未见状态或语义正确的形式证明。
- 25个公开ARC游戏饱和不能独立归因架构；作者要求考虑模型/推理预算、重复稳定性及heldout评价。
- real action数不含模型构建、simulation和replay成本，不能把action efficiency当总算力效率。
- 本配置仅single-model，不把population或Pong controller视为同一实证边界。
- exact replay只认证已观测轨迹的预测；rulebook fidelity由LLM审，不是对未见状态或语义正确的形式证明。; 25个公开ARC游戏饱和不能独立归因架构；作者要求考虑模型/推理预算、重复稳定性及heldout评价。; real action数不含模型构建、simulation和replay成本，不能把action efficiency当总算力效率。; 本配置仅single-model，不把population或Pong controller视为同一实证边界。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_memento` · Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks · 2610.11794v1
  - https://arxiv.org/html/2610.11794v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2144cdc921ff7eb4a5 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
