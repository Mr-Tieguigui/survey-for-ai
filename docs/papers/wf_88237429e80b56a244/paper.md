# Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses

> 方法论文 · 2026 · `wf_88237429e80b56a244`

**作者**：Tailin Zhou  
**原文**：https://arxiv.org/abs/2608.08466  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：单一冻结DeepSeek-V4-Flash分别承担task-harness H、evolver strategy Σ和meta-evolver；三scope独立历史，固定using_harness注入接口及外部评价；具体更新过程为：根据执行reward、祖先版本图与BOOTSTRAP lessons选择seed并写H；candidate执行反馈影响后续编辑，commit pool保留多方向；meta层改Σ的seed/evolution/commit/export策略，meta自身执行逻辑不可写；更新状态的保留与后继使用为：committed harness snapshots、reward/semantic edges、BOOTSTRAP.md及Σ跨外层迭代保留；最终按validation导出，非LLM权重更新。

## 2. 论文的核心内容与贡献

### configuration:cfg_hsi_task_harness_and_evolver_v1
在有限harness+evolver状态闭环上四条件支持；不要求最外层规则自改，不把5轮有限任务改善解释为强RSI或无界加速。

**适用版本**：2608.08466v1；**原文定位**：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### HSI v1 task-specific harness/evolver with frozen outer anchor
`cfg_hsi_task_harness_and_evolver_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单一冻结DeepSeek-V4-Flash分别承担task-harness H、evolver strategy Σ和meta-evolver；三scope独立历史，固定using_harness注入接口及外部评价。 |
| 改进过程与下一轮参与 | 根据执行reward、祖先版本图与BOOTSTRAP lessons选择seed并写H；candidate执行反馈影响后续编辑，commit pool保留多方向；meta层改Σ的seed/evolution/commit/export策略，meta自身执行逻辑不可写。 |
| 保留的状态及时间尺度 | committed harness snapshots、reward/semantic edges、BOOTSTRAP.md及Σ跨外层迭代保留；最终按validation导出，非LLM权重更新。 |
| 外部固定部分 | - 冻结LLM与外层initialization template - 任务注入接口及外部评分/数据split - 任务执行thinking-off，evolution/meta thinking-on的固定配置 |
| 评价与选择设置 | - **backbone**：DeepSeek-V4-Flash preview API - **evaluation**：BALROG %Progress; evolutionLCB mu−0.5sigma; Setup A resampled seeds vs BabaIsAI family-heldout Setup B - **iterations**：5 - **react steps per iteration max**：80 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.1–3.2明确三层独立可写边界和固定outer anchor。（状态：`supported`；定位：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326）。
- **更新由什么过程产生**：同冻结模型根据任务反馈实际提出harness/Σ修改。（状态：`supported`；定位：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326）。
- **状态怎样持久保留**：版本图、commit pool和BOOTSTRAP及Σ跨迭代保存。（状态：`supported`；定位：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326）。
- **更新怎样进入后续改进**：后继seed/编辑读取reward/lessons，改后Σ决定后续搜索和选择。（状态：`supported`；定位：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326）。

**配置判定**：在有限harness+evolver状态闭环上四条件支持；不要求最外层规则自改，不把5轮有限任务改善解释为强RSI或无界加速。

来源：https://arxiv.org/html/2608.08466v1；版本：2608.08466v1；定位：§3.1–3.2 boundary/state tool L142–165；§3.3 seed/commit/meta/export tool L172–202；§4.1 setup/splits tool L220–230；§4.4–5.1 nonmonotonicity/limits tool L290–326。

## 4. 实验、评价协议与结果的可解释范围


- **backbone**：DeepSeek-V4-Flash preview API
- **evaluation**：BALROG %Progress; evolutionLCB mu−0.5sigma; Setup A resampled seeds vs BabaIsAI family-heldout Setup B
- **iterations**：5
- **react steps per iteration max**：80

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_hsi_task_harness_and_evolver_v1`**：在有限harness+evolver状态闭环上四条件支持；不要求最外层规则自改，不把5轮有限任务改善解释为强RSI或无界加速。 根据执行reward、祖先版本图与BOOTSTRAP lessons选择seed并写H；candidate执行反馈影响后续编辑，commit pool保留多方向；meta层改Σ的seed/evolution/commit/export策略，meta自身执行逻辑不可写。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- T=5、每迭代最多80react步骤，单seed演化；个别后期修改退化，非单调改进。
- Setup A同任务集新seed重采样，不能称未见任务测试；BabaIsAI另设dev/val/test且test隔离。
- 公开leaderboard含不同模型/推理预算，不是受控同设置优越性证明；反馈和backbone能力界为实证范围而非普遍不可能性定理。
- T=5、每迭代最多80react步骤，单seed演化；个别后期修改退化，非单调改进。; Setup A同任务集新seed重采样，不能称未见任务测试；BabaIsAI另设dev/val/test且test隔离。; 公开leaderboard含不同模型/推理预算，不是受控同设置优越性证明；反馈和backbone能力界为实证范围而非普遍不可能性定理。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_hier` · Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses · 2608.08466v1
  - https://arxiv.org/html/2608.08466v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_88237429e80b56a244 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
