# SkillVine: Agent Skill Evolution via Branching Exploration

> 方法论文 · 2026 · `wf_78f6b1fa610432baa7`

**作者**：Kaiwei Liu, Jiqian Dong, Liran Dong, Shuai Mao, Mingming Zhao, Bufang Yang, Jie Chuai, Zhitang Chen, Guoliang Xing, Zhenyu Yan  
**原文**：https://arxiv.org/abs/2609.32731  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：技能库版本和其任务轨迹；具体更新过程为：Eq1明确更新器U接收库及该库执行所得轨迹；主干反馈控制分支粒度；更新状态的保留与后继使用为：跨技能搜索轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_skillvine_branching
更正条件4：技能自身不必包含可写的改进控制代码。更新器U、节点选择和验证规则继续作为固定接口；不认证U代码自改或元改进收益。

**适用版本**：v1；**原文定位**：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px2.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p3；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_skillvine_branching
`cfg_skillvine_branching` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 技能库版本和其任务轨迹 |
| 改进过程与下一轮参与 | Eq1明确更新器U接收库及该库执行所得轨迹；主干反馈控制分支粒度 |
| 保留的状态及时间尺度 | 跨技能搜索轮次 |
| 外部固定部分 | 更新器U、LLM、node selector及验证规则 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：技能库版本和其任务轨迹（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1）。
- **更新由什么过程产生**：Eq1明确更新器U接收库及该库执行所得轨迹；主干反馈控制分支粒度（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1）。
- **状态怎样持久保留**：跨技能搜索轮次（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1）。
- **更新怎样进入后续改进**：U接收被选技能库及由该版本执行产生的轨迹，生成技能编辑；接受版本跨训练批保留，主干和各分支继续用自己的库采集轨迹并提出下一轮更新。（状态：`supported`；定位：S3.SS1.p1；S3.SS3.SSS0.Px2.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p3）。

**配置判定**：更正条件4：技能自身不必包含可写的改进控制代码。更新器U、节点选择和验证规则继续作为固定接口；不认证U代码自改或元改进收益。

来源：https://arxiv.org/html/2609.32731v1；版本：v1；定位：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px2.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p3；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_skillvine`**：保留历史库，从节点采集轨迹生成编辑；分支粒度取决于主干接受结果
  - 来源版本：v1；定位：S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p2；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_skillvine`**：Eq1明确更新器U接收库及该库执行所得轨迹；主干反馈控制分支粒度
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS2.SSS0.Px2.p1；S3.SS3.SSS0.Px1.p1；深度：`未单列`。

- **`e4_cfg_skillvine_branching`**：U接收被选技能库及由该版本执行产生的轨迹，生成技能编辑；接受版本跨训练批保留，主干和各分支继续用自己的库采集轨迹并提出下一轮更新。
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS3.SSS0.Px2.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p3；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 确
- 认
- 分
- 支
- 技
- 能
- 演
- 化
- ；
- 库
- 是
- 否
- 直
- 接
- 改
- 变
- 进
- 执
- 行
- 机
- 制
- 而
- 非
- 被
- 外
- 部
- 程
- 序
- 编
- 辑
- 仍
- 待
- 核
- ，
- 不
- 将
- 图
- 搜
- 索
- 自
- 动
- 证
- R
- S
- I
- 任
- 务
- 产
- 生
- 诊
- 断
- 轨
- 迹
- 已
- U
- 的
- 可
- 写
- 项
- 及
- 包
- 含
- 实
- 际
- 控
- 未
- 保
- 留
- 定
- 并
- 按
- 用
- 途
- 引
- 更
- 正
- 条
- 件
- 4
- ：
- 身
- 必
- 代
- 码
- 。
- 新
- 器
- 、
- 节
- 点
- 选
- 择
- 和
- 验
- 规
- 则
- 继
- 续
- 作
- 为
- 固
- 口
- 或
- 元
- 收
- 益

## 7. 与其他论文的具体关系

### [R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution](../r03_method/wf_1b0137a9f0b0244159.md)
关系：`contrasts_system_boundary_with` · `r2_skillvine_r2flow_12` · 当前展示权限：`primary_supported`。
SkillVine在可回溯版本图中比较主干和旁支的验证准确率，并以主干结果控制旁支编辑粒度；R² Flow则把技能库、图、策略/流参数和验证计数作为阶段状态，用可靠性后验及流诊断选择技能编辑，经配对回放的多指标非劣门控后进入下一阶段重训。两者共享技能库迭代这一比较轴，具体搜索和接受机制不同。

**关系边界**：仅为策展者的双端机制比较；未取得直接继承、代码复用或同一任务同预算性能比较证据。R² Flow的固定阶段递归不能据此解释为更新算子自身代码修改。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2609.32731v1；版本：v1；定位：S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p2。
- object：https://arxiv.org/html/2609.33867v1；版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。
- expand_src_w_skillvine：https://arxiv.org/html/2609.32731v1；版本：v1；定位：S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p2。
- expand_src_w_r2flow：https://arxiv.org/html/2609.33867v1；版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_skillvine` · SkillVine: Agent Skill Evolution via Branching Exploration · v1
  - https://arxiv.org/html/2609.32731v1；阅读深度：`未单列`。
- `src_20261013_w_skillvine` · 已存来源 · v1
  - https://arxiv.org/html/2609.32731v1；阅读深度：`未单列`。
- `stage1_src_w_skillvine` · 已存来源 · v1
  - https://arxiv.org/html/2609.32731v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_78f6b1fa610432baa7 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
