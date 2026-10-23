# StateSkill-Agent: An Effective and Efficient Embodied Agent via State-conditioned Skill

> 方法论文 · 2026 · `wf_61559e687099cb99a5`

**作者**：Changxu Wei, Jingyi Zhang, Zhiyu Zheng, Tianyi Lin, Yixian Zhang, Yunpeng Qing, Jingyuan Liu, Zhi Hou, Jiaxing Huang  
**原文**：https://arxiv.org/abs/2610.14601v1  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
将固定技能推理、离线技能修订和技能—模型交替训练分别裁定。

## 2. 论文的核心内容与贡献

### configuration:cfg_stateskill_evolve
core限完整技能修订系统；离线调度不自动构成排除条件，不声称推理期间在线修订。

**适用版本**：v1；**原文定位**：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_stateskill_fixed_fsm_inference
运行时状态转移不等同于持续方法改进。

**适用版本**：v1；**原文定位**：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_stateskill_stategrpo_coevolution
训练闭环；不外推GPT-5.5参数训练或真实机器人在线自改。

**适用版本**：v1；**原文定位**：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_stateskill_fixed_fsm_inference
`cfg_stateskill_fixed_fsm_inference` · inference_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定技能与模型的具身执行。 |
| 改进过程与下一轮参与 | 有限状态门控按观察推进当前技能，不修订技能。 |
| 保留的状态及时间尺度 | 运行状态保留于当前任务；技能先验来自先前构建。 |
| 外部固定部分 | - 模型、技能库、低层执行器、动作接口 |

**配置判定**：运行时状态转移不等同于持续方法改进。

来源：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。

### cfg_stateskill_evolve
`cfg_stateskill_evolve` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 包含离线LLM修订器、持久技能库和固定执行模型的完整循环。 |
| 改进过程与下一轮参与 | 新成功/失败轨迹驱动状态图、指导、门控及动作先验修订；同实例验证提升才保留。 |
| 保留的状态及时间尺度 | 更新技能用于后续轨迹采集和再次修订。 |
| 外部固定部分 | - 执行模型与低层控制器 - 验证成功指标、接口和准入规则 |

**配置判定**：core限完整技能修订系统；离线调度不自动构成排除条件，不声称推理期间在线修订。

来源：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。

### cfg_stateskill_stategrpo_coevolution
`cfg_stateskill_stategrpo_coevolution` · training_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | StateSkill-Evolve与Qwen3.5-9B高层模型交替训练。 |
| 改进过程与下一轮参与 | 固定当前技能执行状态条件GRPO，再收集新轨迹修订技能。 |
| 保留的状态及时间尺度 | 模型与技能跨轮保留。 |
| 外部固定部分 | - 低层VLA冻结 - 状态效率奖励、GRPO及验证规则 |

**配置判定**：训练闭环；不外推GPT-5.5参数训练或真实机器人在线自改。

来源：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r3_memory_ev_stateskill_method`**：§3.2固定FSM执行；§3.3依据新轨迹修订且验证成功率提升才保留；§3.4交替优化高层模型；§4.1低层执行器冻结。
  - 来源版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 局部技能结束不等于任务成功；最终评测种子独立。
- 原文方法与报告结果已选段核查，未独立复现。

## 7. 与其他论文的具体关系

### [Voyager: An Open-Ended Embodied Agent with Large Language Models](../r03_method/wf_b71b1297191d522793.md)
关系：`contrasts_system_boundary_with` · `r3_stateskill_voyager_representation_boundary` · 当前展示权限：`primary_supported`。
两者保留技能用于后续执行：StateSkill-Evolve离线修订有限状态结构并比较验证成功率；Voyager执行修订代码，经任务成功判断后加入可检索代码库。

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- r3_memory_src_stateskill_v1：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
- r3_memory_src_voyager_v2：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。
- r3_memory_src_stateskill_v1：https://arxiv.org/html/2610.14601v1；版本：v1；定位：S3.SS2.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS3.p1；S3.SS3.p2；S3.SS3.p3；S3.SS4.p1；S3.SS4.p5；S3.SS4.p6；S4.SS1.p1；S4.SS4.SSS0.Px1.p1。
- r3_memory_src_voyager_v2：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2。

## 8. 来源清单、复查入口与解析缺口
- `r3_memory_src_stateskill_v1` · 已存来源 · v1
  - https://arxiv.org/html/2610.14601v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_fulltext_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_61559e687099cb99a5 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
