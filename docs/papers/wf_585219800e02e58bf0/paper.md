# MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

> 方法论文 · 2026 · `wf_585219800e02e58bf0`

**作者**：Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang  
**原文**：https://arxiv.org/abs/2605.27366  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：技能资产及技能级经验；具体更新过程为：技能catalog进入任务system prompt，planning选择复用；技能.memory随技能加载；更新状态的保留与后继使用为：跨任务与技能使用。

## 2. 论文的核心内容与贡献

### configuration:cfg_muse_skill_lifecycle
技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。

**适用版本**：2605.27366v2；**原文定位**：§3.2–3.3 tool L211–246。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_muse_skill_lifecycle
`cfg_muse_skill_lifecycle` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 技能资产及技能级经验 |
| 改进过程与下一轮参与 | 技能catalog进入任务system prompt，planning选择复用；技能.memory随技能加载 |
| 保留的状态及时间尺度 | 跨任务与技能使用 |
| 外部固定部分 | skill_create等创建/评估程序、LLM |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。（状态：`supported`；定位：§3.2–3.3 tool L211–246）。
- **更新由什么过程产生**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。（状态：`supported`；定位：§3.2–3.3 tool L211–246）。
- **状态怎样持久保留**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。（状态：`supported`；定位：§3.2–3.3 tool L211–246）。
- **更新怎样进入后续改进**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。（状态：`supported`；定位：§3.2–3.3 tool L211–246）。

**配置判定**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。

来源：https://arxiv.org/html/2605.27366v2；版本：2605.27366v2；定位：§3.2–3.3 tool L211–246。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_muse_skill_lifecycle`**：技能包跨任务保留；失败测试/执行触发refiner修订并重检，后续加载技能时同时呈现每技能memory。由此在技能库及更新回路边界支持结构C4，不要求固定Skill Creator提示自身改写。
  - 来源版本：2605.27366v2；定位：§3.2–3.3 tool L211–246；深度：`未单列`。

- **`e2_w_muse_autoskill`**：技能创建/检验/复用，经验随技能加载；需要进一步查经验是否进入技能创建或修订算子
  - 来源版本：v2；定位：S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px1.p1；Sx1.p1；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_muse_autoskill`**：技能catalog进入任务system prompt，planning选择复用；技能.memory随技能加载
  - 来源版本：v2；定位：S3.SS1.p1；S3.SS1.SSS0.Px1.p1；S3.SS2.SSS0.Px6.p1；S3.SS3.SSS0.Px1.p1；深度：`未单列`。

- **`e4_cfg_muse_skill_lifecycle`**：技能创建检查失败会调用update_skill，运行失败导致修订；技能.memory随后使用时加载。
  - 来源版本：v2；定位：S3.SS2.SSS0.Px2.p3；S3.SS2.SSS0.Px6.p2；S3.SS3.SSS0.Px1.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 原文描述方法与运行接口，不代表本次已独立追踪每次creator调用或复现其代码。
- 有tests运行tests，无tests使用较弱sandbox/runtime反馈，不能统称每个技能都经过单元测试。
- 不认证跨代理迁移自动带走经验：Appendix C明确per-agent memory不随发布技能包迁移。
- 本
- 轮
- 确
- 认
- 长
- 期
- 技
- 能
- 资
- 产
- ，
- 条
- 件
- 4
- 仍
- 未
- 知
- ；
- 7
- 5
- /
- 9
- 可
- 运
- 行
- 子
- 集
- 单
- 轨
- 迹
- 创
- 建
- 及
- 接
- 收
- 者
- t
- r
- a
- n
- s
- f
- e
- 限
- 制
- 保
- 留
- p
- l
- i
- g
- c
- o
- 影
- 响
- 调
- 用
- 尚
- 每
- 经
- 验
- 进
- 入
- 修
- 订
- 算
- 。
- 不
- 得
- 把
- 另
- 一
- 个
- 全
- 局
- m
- y
- 边
- 界
- 自
- 动
- 套
- 到
- 该
- 配
- 置
- 失
- 败
- 反
- 馈
- 触
- 发
- 但
- 是
- 否
- 随
- 实
- 际
- 加
- 载
- 闭
- 合
- 或
- 仅
- 复
- 等
- 同
- 于
- 改
- 参
- 与

## 7. 与其他论文的具体关系

### [Voyager: An Open-Ended Embodied Agent with Large Language Models](../r03_method/wf_b71b1297191d522793.md)
关系：`structurally_similar_to` · `r2_muse_autoskill_voyager_13` · 当前展示权限：`primary_supported`。
MUSE-Autoskill和Voyager均把生成且通过可用验证的技能保存为可检索资产，供后续任务使用。MUSE保存带SKILL.md及可选脚本/资源/测试的技能包，并在加载技能时呈现技能级.memory.md；Voyager保存Minecraft可执行技能代码，把检索技能放入下一次GPT-4代码生成提示，并依据环境反馈、执行错误和成功检查迭代。

**关系边界**：相似性只覆盖生成、检查、保存、检索及后续复用链条；不能把MUSE技能级经验参与创建/修订算子的未闭合问题视为已解决，也不能把MUSE的SkillsBench转移实验当作Voyager的Minecraft结果。没有历史继承或代码复用主张。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2605.27366v2；版本：v2；定位：S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px1.p1；Sx1.p1；S3.SS2.SSS0.Px2.p3；S3.SS2.SSS0.Px6.p1。
- object：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2。
- expand_src_w_muse_autoskill：https://arxiv.org/html/2605.27366v2；版本：v2；定位：S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px2.p2；S3.SS2.SSS0.Px3.p1；S3.SS3.SSS0.Px1.p1；Sx1.p1。
- expand_src_w_voyager：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p1；S2.SS2.p2；S2.SS3.p1；S2.SS3.p2。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_muse_autoskill` · MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation · v2
  - https://arxiv.org/html/2605.27366v2；阅读深度：`未单列`。
- `r7root_src_muse_state_feedback` · 已存来源 · 2605.27366v2
  - https://arxiv.org/html/2605.27366v2；阅读深度：`未单列`。
- `src_20261013_w_muse_autoskill` · 已存来源 · v2
  - https://arxiv.org/html/2605.27366v2；阅读深度：`未单列`。
- `stage1_src_w_muse_autoskill` · 已存来源 · v2
  - https://arxiv.org/html/2605.27366v2；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_585219800e02e58bf0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
