# Voyager: An Open-Ended Embodied Agent with Large Language Models

> 方法论文 · 2023 · `wf_b71b1297191d522793`

**作者**：Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar  
**原文**：https://arxiv.org/abs/2305.16291  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Minecraft课程与执行技能库；具体更新过程为：通过验证的技能进入库，检索技能直接输入后续代码生成以组合新技能；更新状态的保留与后继使用为：跨Minecraft任务的技能积累。

### 定点原文补充：具体问题与执行过程
Minecraft 中的开放式代理，结合自动课程、可执行技能库与迭代代码生成，积累可复用行为。

1. 课程读取环境状态与成败历史提出目标；通过环境反馈、执行错误和 GPT-4 验证修订代码。
2. 验证成功后将程序及描述嵌入写入技能库；新任务检索前五个相关技能辅助组合。

**实验与选择协议**：

- 代码生成若四轮后仍卡住，改换课程任务。
- 评价包含物品发现、科技树、地图覆盖与新世界任务；使用高层 Mineflayer API，与像素输入、底层控制研究不同。

**作者报告的结果（未独立复现）**：作者在 160 次提示迭代内报告发现 63 种物品；该次数不是 160 次已接受能力改进。

**解释边界**：

- 基础语言模型与控制 API 固定；保留的是代码技能和任务经历。
- 作者重解释的文本代理基线及高层控制接口限制跨系统公平比较。

来源：[2305.16291v2](https://arxiv.org/html/2305.16291v2)；定位：§2.1–2.3 Method；§3.1–3.3 Experiments。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_voyager
技能库条件化下一次技能获取；未证明GPT-4权重或整套课程算法自改

**适用版本**：v2；**原文定位**：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_voyager
`cfg_voyager` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Minecraft课程与执行技能库 |
| 改进过程与下一轮参与 | 通过验证的技能进入库，检索技能直接输入后续代码生成以组合新技能 |
| 保留的状态及时间尺度 | 跨Minecraft任务的技能积累 |
| 外部固定部分 | GPT-4、控制API、验证与最多4轮生成限制 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Minecraft课程与执行技能库（状态：`supported`；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2）。
- **更新由什么过程产生**：通过验证的技能进入库，检索技能直接输入后续代码生成以组合新技能（状态：`supported`；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2）。
- **状态怎样持久保留**：跨Minecraft任务的技能积累（状态：`supported`；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2）。
- **更新怎样进入后续改进**：通过验证的技能进入库，检索技能直接输入后续代码生成以组合新技能（状态：`supported`；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2）。

**配置判定**：技能库条件化下一次技能获取；未证明GPT-4权重或整套课程算法自改

来源：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_voyager`**：通过验证的技能进入库，检索技能直接输入后续代码生成以组合新技能
  - 来源版本：v2；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2；深度：`AI_primary_method_passage_recheck`。

- **`r3_memory_ev_voyager_skills`**：执行、错误及成功反馈修订代码，通过成功验证后存入可检索技能库供后续程序使用。
  - 来源版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2；深度：`未单列`。

- **`oct15_agents_ev_r2_voyager_reflexion_5`**：Voyager将环境状态成功判断与失败批评组合为自验证，并在成功后把可执行程序加入跨任务技能库；Reflexion原配置已有独立Evaluator，反思器读取奖励、轨迹和既有记忆，为后续完整试次生成反思记忆。两者应按反馈组合与保留对象对照，不能称Reflexion没有成功评价。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_local_comparison_plus_curator_two_endpoint_boundary_correction`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 自验证同时输出成功判断与失败批评；不能把作者对反思的比较改写成Reflexion原文没有评价器。
- Voyager评测的Reflexion是另加执行错误和Voyager自验证的Minecraft适配器，不等同原Reflexion配置。
- 技
- 能
- 库
- 条
- 件
- 化
- 下
- 一
- 次
- 获
- 取
- ；
- 未
- 证
- 明
- G
- P
- T
- -
- 4
- 权
- 重
- 或
- 整
- 套
- 课
- 程
- 算
- 法
- 自
- 改
- 不据此断言技能库全部既有条目均被追溯修改。
- Voyager§2.3将其自验证称为比自反思更全面是作者局部表述，不表示原Reflexion框架缺Evaluator。Voyager§3.2明确为其Minecraft Reflexion基线添加执行错误与Voyager自验证；该适配基线不能等同原Reflexion完整配置。技能库与反思记忆的机制比较不认证代码继承、统一性能优势或跨任务永久记忆。

## 7. 与其他论文的具体关系

### [Reflexion: Language Agents with Verbal Reinforcement Learning](../r03_method/wf_3fb5d6b0a837235b64.md)
关系：`contrasts_system_boundary_with` · `r2_voyager_reflexion_5` · 当前展示权限：`primary_supported`。
Voyager将环境状态成功判断与失败批评组合为自验证，并在成功后把可执行程序加入跨任务技能库；Reflexion原配置已有独立Evaluator，反思器读取奖励、轨迹和既有记忆，为后续完整试次生成反思记忆。两者应按反馈组合与保留对象对照，不能称Reflexion没有成功评价。

**关系边界**：Voyager§2.3将其自验证称为比自反思更全面是作者局部表述，不表示原Reflexion框架缺Evaluator。Voyager§3.2明确为其Minecraft Reflexion基线添加执行错误与Voyager自验证；该适配基线不能等同原Reflexion完整配置。技能库与反思记忆的机制比较不认证代码继承、统一性能优势或跨任务永久记忆。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2；S3.SS2.p1；S3.SS2.p3。
- object：https://arxiv.org/html/2303.11366v4；版本：v4；定位：S3.p1；S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。

### [MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](../r03_method/wf_585219800e02e58bf0.md)
关系：`structurally_similar_to` · `r2_muse_autoskill_voyager_13` · 当前展示权限：`primary_supported`。
MUSE-Autoskill和Voyager均把生成且通过可用验证的技能保存为可检索资产，供后续任务使用。MUSE保存带SKILL.md及可选脚本/资源/测试的技能包，并在加载技能时呈现技能级.memory.md；Voyager保存Minecraft可执行技能代码，把检索技能放入下一次GPT-4代码生成提示，并依据环境反馈、执行错误和成功检查迭代。

**关系边界**：相似性只覆盖生成、检查、保存、检索及后续复用链条；不能把MUSE技能级经验参与创建/修订算子的未闭合问题视为已解决，也不能把MUSE的SkillsBench转移实验当作Voyager的Minecraft结果。没有历史继承或代码复用主张。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2605.27366v2；版本：v2；定位：S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px1.p1；Sx1.p1；S3.SS2.SSS0.Px2.p3；S3.SS2.SSS0.Px6.p1。
- object：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2。
- expand_src_w_muse_autoskill：https://arxiv.org/html/2605.27366v2；版本：v2；定位：S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px1.p1；Sx1.p1。
- expand_src_w_voyager：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2。

### [StateSkill-Agent: An Effective and Efficient Embodied Agent via State-conditioned Skill](../r03_method/wf_61559e687099cb99a5.md)
关系：`contrasts_system_boundary_with` · `r3_stateskill_voyager_representation_boundary` · 当前展示权限：`primary_supported`。
两者保留技能用于后续执行：StateSkill-Evolve离线修订有限状态结构并比较验证成功率；Voyager执行修订代码，经任务成功判断后加入可检索代码库。

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- r3_memory_src_stateskill_v1：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
- r3_memory_src_voyager_v2：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。
- r3_memory_src_stateskill_v1：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
- r3_memory_src_voyager_v2：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_voyager` · Voyager · v2
  - https://arxiv.org/html/2305.16291v2；阅读深度：`未单列`。
- `oct15_agents_src_w_reflexion` · 已存来源 · v4
  - https://arxiv.org/html/2303.11366v4；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `oct15_agents_src_w_voyager` · 已存来源 · v2
  - https://arxiv.org/html/2305.16291v2；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `r3_memory_src_voyager_v2` · 已存来源 · v2
  - https://arxiv.org/html/2305.16291v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b71b1297191d522793 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
