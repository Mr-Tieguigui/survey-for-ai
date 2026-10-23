# Policy-Level Recursive Self-Improvement for Embodied AI with a Criticality World Model

> 方法论文 · 2026 · `wf_7905f8e027df374c1a`

**作者**：Linxuan He, Yuying Tian, Lingxiang Fan, Jiaqi Pi, Yinqiao Lu, Shang Su, Mengkai Shi, Shuo Feng  
**原文**：https://arxiv.org/abs/2607.28251  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
执行结果训练 criticality world model，再按风险分数采集场景以训练 specialist，并以重采样校正频率偏移、门控组合 specialist 与冻结 nominal 策略；实际更新是策略与采样反馈，非社会影响论文。

## 2. 论文的核心内容与贡献

### configuration:cfg_policy_cwm_multiround_specialist_v2
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2607.28251v2；**原文定位**：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_policy_cwm_single_bc_gate_v2
按原文保留有界相邻或待定配置，不从训练或验证名称推断递归闭合。

**适用版本**：2607.28251v2；**原文定位**：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18ctx_role_review_wf_7905f8e027df374c1a`
执行结果训练 criticality world model，再按风险分数采集场景以训练 specialist，并以重采样校正频率偏移、门控组合 specialist 与冻结 nominal 策略；实际更新是策略与采样反馈，非社会影响论文。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Criticality world model: multi-round RL specialist collection
`cfg_policy_cwm_multiround_specialist_v2` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结nominal policy、可训specialist、按当前policy失败训练的风险MLP及有限场景采样器。 |
| 改进过程与下一轮参与 | 当前policy rollout标注失败→BCE更新risk score→混合proposal富集场景并记录P/q→有限buffer重采样更新specialist→新rollout重训风险模型。 |
| 保留的状态及时间尺度 | Go2保留6轮、ManiSkill17轮specialist与场景历史；nominal policy保持固定。 |
| 外部固定部分 | - 场景候选池与外部失败判据 - 固定MLP/BCE及domain-specific policy更新规则 - 固定nominal fallback - validation选择后固定test gate |
| 评价与选择设置 | - **Go2 gate**：validation final tau=0.5; trend tau=0.8 - **ManiSkill gate tau**：0 - **other domains**：one specialist update - **proposal**：positive-support mixture; finite scenario probabilities - **risk model**：lightweight MLP ranking proxy, not calibrated generative dynamics - **rounds**：- **Go2**：6 - **ManiSkill**：17 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：policy、risk predictor和采集更新整体。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **更新由什么过程产生**：当前policy自身失败决定risk学习与新经验采集。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **状态怎样持久保留**：specialist跨轮参数与历史buffer保留。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **更新怎样进入后续改进**：每次specialist更新后的新rollout提供下一轮风险标签，改变未来采样与学习。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2607.28251v2；版本：2607.28251v2；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245。

### Criticality-guided one-update BC and frozen deployment gate
`cfg_policy_cwm_single_bc_gate_v2` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | LIBERO、RoboTwin及真实机器人一次specialist BC更新，固定nominal与criticality gate部署。 |
| 改进过程与下一轮参与 | 当前policy失败训练ranking；选择专家示教并按P/q重采样一次BC；validation定gate，test仅路由两固定policy。 |
| 保留的状态及时间尺度 | 一次BC后参数保存，但test gate不更新模型/采样器。 |
| 外部固定部分 | - 专家动作标签 - 固定test gate和两policy - 一次BC训练objective |
| 评价与选择设置 | - **BC loss**：unweighted; P/q affects batch frequency not action likelihood - **domains**：- LIBERO - RoboTwin - real robot - **gate state**：LIBERO 92D / RoboTwin 437D simulator state; real robot 8 RGB-derived coordinates - **specialist updates**：1 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：单次BC与部署边界明确。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **更新由什么过程产生**：policy失败参与数据选择并有一次参数更新。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **状态怎样持久保留**：训练后模型与gate保留。（状态：`supported`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。
- **更新怎样进入后续改进**：未在这三个实验中执行更新specialist→再采失败→再更新链；部署路由没有持续学习。（状态：`unknown`；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245）。

**配置判定**：按原文保留有界相邻或待定配置，不从训练或验证名称推断递归闭合。

来源：https://arxiv.org/html/2607.28251v2；版本：2607.28251v2；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245。

## 4. 实验、评价协议与结果的可解释范围


- **Go2 gate**：validation final tau=0.5; trend tau=0.8
- **ManiSkill gate tau**：0
- **other domains**：one specialist update
- **proposal**：positive-support mixture; finite scenario probabilities
- **risk model**：lightweight MLP ranking proxy, not calibrated generative dynamics
- **rounds**：- **Go2**：6 - **ManiSkill**：17


- **BC loss**：unweighted; P/q affects batch frequency not action likelihood
- **domains**：- LIBERO - RoboTwin - real robot
- **gate state**：LIBERO 92D / RoboTwin 437D simulator state; real robot 8 RGB-derived coordinates
- **specialist updates**：1

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_7905f8e027df374c1a`**：执行结果训练 criticality world model，再按风险分数采集场景以训练 specialist，并以重采样校正频率偏移、门控组合 specialist 与冻结 nominal 策略；实际更新是策略与采样反馈，非社会影响论文。
  - 来源版本：2607.28251v2；定位：Atom entry http://arxiv.org/abs/2607.28251v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_policy_cwm_multiround_specialist_v2`**：冻结nominal policy、可训specialist、按当前policy失败训练的风险MLP及有限场景采样器。 当前policy rollout标注失败→BCE更新risk score→混合proposal富集场景并记录P/q→有限buffer重采样更新specialist→新rollout重训风险模型。
  - 来源版本：2607.28251v2；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245；深度：`未单列`。

- **`r6app_ev_cfg_policy_cwm_single_bc_gate_v2`**：LIBERO、RoboTwin及真实机器人一次specialist BC更新，固定nominal与criticality gate部署。 当前policy失败训练ranking；选择专家示教并按P/q重采样一次BC；validation定gate，test仅路由两固定policy。
  - 来源版本：2607.28251v2；定位：§3.2–3.3 tool L150–180；§4 tool L182–214；§5 tool L215–245；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- CWM为失败ranking proxy，非生成式动力学预测器；risk不等于真实梯度范数或校准失败概率。
- 归一化P/q在已实现有限buffer中近似修正；不能补回未采场景，不能消除筛选、advantage或regularization偏差，不能称无偏failure-risk梯度。
- RL两组终止轮数/数据/Go2超参不同；同轮预算不是同compute，最终gate校准改善不是新增policy更新。
- gate只在路由到nominal的上下文保留其行为；tau=0 ManiSkill总用specialist。专家示教和外部环境仍固定。
- 不把三项单次BC更新实验写成6/17轮闭环，也不认证跨训练seed稳定提升。
- 只对已读的三个实验保留adjacent；不否认多轮RL版本core。
- 不能将额外simulator state隐去后声称纯视觉无特权输入比较；训练nominal的全部行为亦未由gate全局保留。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_cwm` · 已存来源 · 2607.28251v2
  - https://arxiv.org/html/2607.28251v2；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18ctx_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7905f8e027df374c1a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
