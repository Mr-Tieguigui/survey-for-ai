# R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution

> 方法论文 · 2026 · `wf_1b0137a9f0b0244159`

**作者**：Mingda Zhang, Qiang Huang, Yanjin Li, Zijia Wang, Qika Lin, Xiaoying Tang, Tiesunlong Shen  
**原文**：https://arxiv.org/abs/2609.33867  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：版本技能库、图、flow策略和验证计数；具体更新过程为：技能编辑改变下一阶段边集合，重训flow并重新计算诊断；独立验证门控接受；更新状态的保留与后继使用为：跨学习phase。

## 2. 论文的核心内容与贡献

### configuration:cfg_r2flow
流程递归可固定；独立verifier指论文系统的验证渠道，不是本项目独立复现

**适用版本**：v1；**原文定位**：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_r2flow
`cfg_r2flow` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 版本技能库、图、flow策略和验证计数 |
| 改进过程与下一轮参与 | 技能编辑改变下一阶段边集合，重训flow并重新计算诊断；独立验证门控接受 |
| 保留的状态及时间尺度 | 跨学习phase |
| 外部固定部分 | executor、固定相位更新和verifier规则 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：版本技能库、图、flow策略和验证计数（状态：`supported`；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5）。
- **更新由什么过程产生**：技能编辑改变下一阶段边集合，重训flow并重新计算诊断；独立验证门控接受（状态：`supported`；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5）。
- **状态怎样持久保留**：跨学习phase（状态：`supported`；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5）。
- **更新怎样进入后续改进**：技能编辑改变下一阶段边集合，重训flow并重新计算诊断；独立验证门控接受（状态：`supported`；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5）。

**配置判定**：流程递归可固定；独立verifier指论文系统的验证渠道，不是本项目独立复现

来源：https://arxiv.org/html/2609.33867v1；版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_r2flow`**：技能编辑改变下一阶段边集合，重训flow并重新计算诊断；独立验证门控接受
  - 来源版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 流
- 程
- 递
- 归
- 可
- 固
- 定
- ；
- 独
- 立
- v
- e
- r
- i
- f
- 指
- 论
- 文
- 系
- 统
- 的
- 验
- 证
- 渠
- 道
- ，
- 不
- 是
- 本
- 项
- 目
- 复
- 现

## 7. 与其他论文的具体关系

### [SkillVine: Agent Skill Evolution via Branching Exploration](../r03_method/wf_78f6b1fa610432baa7.md)
关系：`contrasts_system_boundary_with` · `r2_skillvine_r2flow_12` · 当前展示权限：`primary_supported`。
SkillVine在可回溯版本图中比较主干和旁支的验证准确率，并以主干结果控制旁支编辑粒度；R² Flow则把技能库、图、策略/流参数和验证计数作为阶段状态，用可靠性后验及流诊断选择技能编辑，经配对回放的多指标非劣门控后进入下一阶段重训。两者共享技能库迭代这一比较轴，具体搜索和接受机制不同。

**关系边界**：仅为策展者的双端机制比较；未取得直接继承、代码复用或同一任务同预算性能比较证据。R² Flow的固定阶段递归不能据此解释为更新算子自身代码修改。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2609.32731v1；版本：v1；定位：S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p2。
- object：https://arxiv.org/html/2609.33867v1；版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。
- expand_src_w_skillvine：https://arxiv.org/html/2609.32731v1；版本：v1；定位：S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px3.p1；S3.SS3.SSS0.Px4.p1；S3.SS3.SSS0.Px5.p1；S3.SS3.SSS0.Px5.p2。
- expand_src_w_r2flow：https://arxiv.org/html/2609.33867v1；版本：v1；定位：S4.SS3.p2；S4.SS3.p3；S4.SS3.p4；S4.SS3.p5。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_r2flow` · R² Flow · v1
  - https://arxiv.org/html/2609.33867v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1b0137a9f0b0244159 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
