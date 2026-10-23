# SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection

> 方法论文 · 2026 · `wf_5038de512c3639adcd`

**作者**：Wenlin Zhong, Hao Wang, Kun Yuan, Fan Yang, Jinluan Yang, Dian Jin, Xu Tan, Yiquan Wu, Kun Kuang  
**原文**：https://arxiv.org/abs/2610.18807v1  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Training-time joint Generator/Executor parameter learning is core; skill-free deployed policy alone is adjacent.

## 2. 论文的核心内容与贡献

### configuration:cfg_skillscaffold_anchor_rl
Core training configuration; anchor variant must not be conflated with the balanced signed group-based utility.

**适用版本**：v1；**原文定位**：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_skillscaffold_group_rl
Core applies to the jointly updated training system. Utility is a policy-relative scoring surrogate; deployed skill-free inference is a separate configuration.

**适用版本**：v1；**原文定位**：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_skillscaffold_skillfree_deployment
A product of training self-improvement; inference alone does not establish ongoing RSI.

**适用版本**：v1；**原文定位**：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_skillscaffold_group_rl
`cfg_skillscaffold_group_rl` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Training-time shared Generator/Executor policy and per-update candidate skills, using success/failure Scout groups. ALFWorld, ScienceWorld and tau2-Bench instantiate separate domain training runs. |
| 改进过程与下一轮参与 | Collect four skill-free Scouts, generate four candidate skills from outcome-labeled evidence, rank by signed outcome-aware likelihood difference, inject only a positive-utility maximum, collect four post-Scouts, and jointly update shared policy parameters with role-specific GRPO rewards. |
| 保留的状态及时间尺度 | Parameters persist across training updates and affect both subsequent skill generation and execution; no persistent external skill library is assumed. |
| 外部固定部分 | - Environment outcome verifier and tools - GRPO optimization and role reward normalization - Likelihood utility equation and U > 0 injection gate - Task dataset and format constraints |
| 评价与选择设置 | - **base model**：Qwen3-8B - **candidates**：4 - **deployment external skill**：None - **initialization note**：tau2-Bench uses a domain-adapted SFT checkpoint; other listed group variants start from base Qwen3-8B. - **post scouts**：4 - **scouts**：4 - **training steps**：- **ALFWorld**：100 - **ScienceWorld**：160 - **tau2-Bench**：200 |
| 实验实现状态 | reported_training_runs_not_independently_replicated |

**配置判定**：Core applies to the jointly updated training system. Utility is a policy-relative scoring surrogate; deployed skill-free inference is a separate configuration.

来源：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。

### cfg_skillscaffold_anchor_rl
`cfg_skillscaffold_anchor_rl` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | WebShop training-time shared Generator/Executor policy with one verified successful Scout as generation and scoring anchor. |
| 改进过程与下一轮参与 | Use the first successful Scout as anchor. If none succeeds, skip skill generation. Rank candidates by anchor likelihood difference, gate on positive utility, and jointly train shared parameters with clipped nonnegative Generator utility and environment Executor rewards. |
| 保留的状态及时间尺度 | Shared policy weights persist across WebShop training updates and change subsequent Generator and Executor behavior. |
| 外部固定部分 | - Environment outcome verifier and tools - GRPO optimization and role reward normalization - Likelihood utility equation and U > 0 injection gate - Task dataset and format constraints - First-success anchor rule and zero-clipped Generator reward |
| 评价与选择设置 | - **base model**：Qwen3-8B - **benchmark**：WebShop - **candidates**：4 - **maximum interaction steps**：15 - **post scouts**：4 - **scouts**：4 - **training steps**：200 |

**配置判定**：Core training configuration; anchor variant must not be conflated with the balanced signed group-based utility.

来源：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。

### cfg_skillscaffold_skillfree_deployment
`cfg_skillscaffold_skillfree_deployment` · inference_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | A frozen trained Executor with the external skill pathway disabled at deployment. |
| 改进过程与下一轮参与 | Run the trained policy without Scout collection, generated skill injection, or further parameter updates. |
| 保留的状态及时间尺度 | Training-produced weights persist, but this inference configuration has no admitted update loop. |
| 外部固定部分 | - Trained weights - Environment tools - Skill pathway disabled |

**配置判定**：A product of training self-improvement; inference alone does not establish ongoing RSI.

来源：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。

## 4. 实验、评价协议与结果的可解释范围


- **base model**：Qwen3-8B
- **candidates**：4
- **deployment external skill**：None
- **initialization note**：tau2-Bench uses a domain-adapted SFT checkpoint; other listed group variants start from base Qwen3-8B.
- **post scouts**：4
- **scouts**：4
- **training steps**：- **ALFWorld**：100 - **ScienceWorld**：160 - **tau2-Bench**：200


- **base model**：Qwen3-8B
- **benchmark**：WebShop
- **candidates**：4
- **maximum interaction steps**：15
- **post scouts**：4
- **scouts**：4
- **training steps**：200

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`oct15_intake_ev_skillscaffold_method`**：Outcome-verified skill-free trajectories generate textual skills. Paired likelihood differences rank skills; positive gating may abstain. Shared Generator/Executor parameters receive separate GRPO signals, and later training uses the updated policy. Deployment disables skills.
  - 来源版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3；深度：`未单列`。

- **`r4_memory_ev_skillscaffold_existing`**：共享Generator/Executor参数联合GRPO，效用基于固定Scouts似然差，部署禁用技能。
  - 来源版本：v1；定位：S4.p1；S4.SS3.p1；S4.SS5.SSS0.Px1.p2；S4.SS5.SSS0.Px2.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Likelihood utility is a surrogate, not execution truth for a candidate skill.
- Candidate-specific utility scoring avoids fresh rollouts; selected post-scout execution still collects fresh rollouts.
- Generator/Executor share parameters within each domain checkpoint; separately trained benchmarks are not a single cross-domain run.

## 7. 与其他论文的具体关系

### [Self-Improving Large Language Models via Progressive Experience Evolution](../r03_method/wf_99859d66d76076f2e9.md)
关系：`contrasts_system_boundary_with` · `oct15_skillscaffold_spee_training_boundary` · 当前展示权限：`primary_supported`。
Both use current-policy-generated explicit guidance to improve future parameterized behavior. SkillScaffold selects query-specific skills using likelihood changes on fixed verified Scouts and jointly applies GRPO without a separate distillation stage. SPEE filters a persistent experience pool by probe reward improvement and explicitly distills it before further GRPO.

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- oct15_intake_src_2610_18807v1_html：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
- oct15_training_src_w_spee：https://arxiv.org/html/2608.02139v2；版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。
- oct15_intake_src_2610_18807v1_html：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
- oct15_training_src_w_spee：https://arxiv.org/html/2608.02139v2；版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。

### [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](../r03_method/wf_4de5ba4f0fe41d3822.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_skillforge_skill_policy_training_cfg_skillscaffold_group_rl` · 当前展示权限：`primary_supported`。
SkillForge以固定外部教师变异持久技能库并同步GRPO训练；SkillScaffold让共享受训策略生成当前query技能并联合训练，部署移除技能路径。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_skillforge：https://arxiv.org/html/2610.09832v2；版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。
- r4_memory_src_skillscaffold_existing：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.p1；S4.SS3.p1；S4.SS5.SSS0.Px1.p2；S4.SS5.SSS0.Px2.p1。
- r4_memory_src_skillforge：https://arxiv.org/html/2610.09832v2；版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。
- r4_memory_src_skillscaffold_existing：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.p1；S4.SS3.p1；S4.SS5.SSS0.Px1.p2；S4.SS5.SSS0.Px2.p1。

## 8. 来源清单、复查入口与解析缺口
- `oct15_intake_src_2610_18807v1_html` · 已存来源 · v1
  - https://arxiv.org/html/2610.18807v1；阅读深度：`未单列`。
- `r4_memory_src_skillscaffold_existing` · 已存来源 · v1
  - https://arxiv.org/html/2610.18807v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_fulltext_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5038de512c3639adcd --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
