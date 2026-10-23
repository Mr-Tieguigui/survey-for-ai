# SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

> 方法论文 · 2026 · `wf_4de5ba4f0fe41d3822`

**作者**：Yuyao Ge, Yiwei Wang, Yuchen He, Baolong Bi, Lingrui Mei, Jiayu Yao, Lizhe Chen, Shenghua Liu  
**原文**：https://arxiv.org/abs/2610.09832v2  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
依具体更新边界裁定；不按self-evolving标题认证递归性。

## 2. 论文的核心内容与贡献

### configuration:cfg_skillforge_skill_policy_training
core限包含教师服务的完整训练循环；不认证策略自生成教师或元优化规则。

**适用版本**：v2；**原文定位**：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_skillforge_skill_policy_training
`cfg_skillforge_skill_policy_training` · training_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定GRPO/教师服务下的可变策略与持久技能库。 |
| 改进过程与下一轮参与 | 依据自身rollout累计成功率运行试用、激活、稳定、退休生命周期；固定外部教师依据失败轨迹变异技能，GRPO更新策略。 |
| 保留的状态及时间尺度 | 策略和库共同跨训练迭代保留，改变后续rollout及技能适应度。 |
| 外部固定部分 | - 教师权重及变异模板 - 二值环境奖励、GRPO - 生命周期阈值、预算和库容量 |

**配置判定**：core限包含教师服务的完整训练循环；不认证策略自生成教师或元优化规则。

来源：https://arxiv.org/html/2610.09832v2；版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_memory_ev_cfg_skillforge_skill_policy_training`**：依据自身rollout累计成功率运行试用、激活、稳定、退休生命周期；固定外部教师依据失败轨迹变异技能，GRPO更新策略。
  - 来源版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 教师与受训策略为不同模型族，不能写成同策略Generator。
- 一个episode的全部检索技能共享奖励，非已识别独立因果贡献。
- 本批未核实际代码或复现实验。
- core限包含教师服务的完整训练循环；不认证策略自生成教师或元优化规则。

## 7. 与其他论文的具体关系

### [SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection](../r03_method/wf_5038de512c3639adcd.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_skillforge_skill_policy_training_cfg_skillscaffold_group_rl` · 当前展示权限：`primary_supported`。
SkillForge以固定外部教师变异持久技能库并同步GRPO训练；SkillScaffold让共享受训策略生成当前query技能并联合训练，部署移除技能路径。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_skillforge：https://arxiv.org/html/2610.09832v2；版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。
- r4_memory_src_skillscaffold_existing：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.p1；S4.SS3.p1；S4.SS5.SSS0.Px1.p2；S4.SS5.SSS0.Px2.p1。
- r4_memory_src_skillforge：https://arxiv.org/html/2610.09832v2；版本：v2；定位：§4.1–4.3, tool text L129–187；§4.4 Algorithm 1/Eq.12, tool text L188–240。
- r4_memory_src_skillscaffold_existing：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.p1；S4.SS3.p1；S4.SS5.SSS0.Px1.p2；S4.SS5.SSS0.Px2.p1。

## 8. 来源清单、复查入口与解析缺口
- `r4_memory_src_skillforge` · 已存来源 · v2
  - https://arxiv.org/html/2610.09832v2；阅读深度：`未单列`。

**证据深度**：selected_primary_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4de5ba4f0fe41d3822 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
