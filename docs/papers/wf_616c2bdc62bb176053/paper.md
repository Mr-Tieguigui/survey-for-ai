# The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

> 综合系统/智能体 · 2026 · `wf_616c2bdc62bb176053`

**作者**：Alex Iacob, Andrej Jovanović, William F. Shen, Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani, Niccolò Alberto Elia Venanzi, Jiayi Nie, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, Rika Antonova, Nicholas D. Lane  
**原文**：https://arxiv.org/abs/2606.26294  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已读原文系统实现、协议与评价限制；将声明协议和实做证据分开。

## 2. 论文的核心内容与贡献

### configuration:cfg_red_queen_controlled_utility_search
v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。

**适用版本**：v3；**原文定位**：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_red_queen_controlled_utility_search
`cfg_red_queen_controlled_utility_search` · implemented_structural_search_with_domain_specific_profiles

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 含任务代理、学习评价者和可编辑meta-agent的共享工作区归档，加按slot版本化的epoch评价状态。 |
| 改进过程与下一轮参与 | 父节点代码产生子工作区；CMP/Thompson选择扩展；epoch内冻结评价者，checkpoint由验证锚点评价选择替换并擦除依赖旧评价者的utility记录。 |
| 保留的状态及时间尺度 | 子工作区跨归档搜索保留并可再次生成修改；晋升评价者跨epoch保留，继续影响后续搜索。 |
| 外部固定部分 | 评分与编排harness、checkpoint规则、固定验证锚点、角色/任务平衡；基础模型权重不由该代码归档过程更新。 |
| 实验实现状态 | implemented_search_domain_profiles_not_performance_normalized |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。（状态：`supported`；定位：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1）。
- **更新由什么过程产生**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。（状态：`supported`；定位：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1）。
- **状态怎样持久保留**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。（状态：`supported`；定位：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1）。
- **更新怎样进入后续改进**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。（状态：`supported`；定位：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1）。

**配置判定**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。

来源：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3–3.1；PDF p.4 §3.2；PDF p.5 §4；PDF p.18 Appendix B.1–B.3；PDF p.19 Algorithm 1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`new_sys_ev_cfg_red_queen_controlled_utility_search`**：v3方法与Algorithm 1明确支持代码归档及评价slot的递归更新和后续搜索参与；评价者仅在checkpoint替换，epoch内评分固定。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 验证锚点属于搜索validation split；不能把它与完全不参与搜索的held-out test split混为一谈。
- 可选对抗池使评价目标包含额外压力；不认证所有角色有跨epoch可比的全局best-belief。
- paper writer/prover只具有epoch局部赢家；anchor角色才能使用所述全局选择解释。
- HGM-H是RQGM实验内组合基线：HyperAgents式工作区加HGM搜索、冻结评价者；不等于原HGM或原HyperAgents完整配置。
- 不同领域模型、角色和评分协议不同；本配置只抽取共同搜索结构，不混合性能数字。
- 连续utility的reward-design扩展需另配参数，本文配置只代表§3/Algorithm 1的二元评价结构。
- 验证锚点属于搜索validation split；不能把它与完全不参与搜索的held-out test split混为一谈。；可选对抗池使评价目标包含额外压力；不认证所有角色有跨epoch可比的全局best-belief。；paper writer/prover只具有epoch局部赢家；anchor角色才能使用所述全局选择解释。；HGM-H是RQGM实验内组合基线：HyperAgents式工作区加HGM搜索、冻结评价者；不等于原HGM或原HyperAgents完整配置。；不同领域模型、角色和评分协议不同；本配置只抽取共同搜索结构，不混合性能数字。；连续utility的reward-design扩展需另配参数，本文配置只代表§3/Algorithm 1的二元评价结构。

## 7. 与其他论文的具体关系

### [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](../r03_method/wf_title_1935c85b092513ff.md)
关系：`adapts_design_of` · `r3_red_queen_adapts_hgm_search` · 当前展示权限：`primary_supported`。
RQGM v3 §3.1与Appendix B.2明确沿用HGM的CMP/Thompson父节点采样、节点自身计数评价采样及UCB-Air扩展门控；HGM v3 §3.3原方法确认这三个组成。

**关系边界**：谱系只落在搜索调度组件；不代表完整SWE60实验配置、代码逐行复用或理论保证无条件继承。RQGM只在epoch内满足剩余假设时讨论HGM分析；跨epoch额外要求受控替换与依赖记录擦除。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3.1；PDF p.18 Appendix B.2。
- object：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p3.1；S3.SS3.SSS0.Px1.p2.1；S3.SS3.SSS0.Px1.p5.1；S3.SS3.SSS0.Px2.p1.1；S3.SS3.SSS0.Px3.p2.1。

### [Hyperagents](../r03_method/wf_17eec8a15debc212b5.md)
关系：`adapts_design_of` · `r3_red_queen_adapts_hyperagents_workspace` · 当前展示权限：`primary_supported`。
RQGM把每个归档节点设为任务角色、评价角色及meta-agent共同组成的可编辑工作区；Appendix B.1明确采用HyperAgents的角色工作区与meta编辑设定。HyperAgents原文§3确认任务代理与可自改meta程序的共同可编辑边界。

**关系边界**：继承只覆盖共享可编辑任务/meta工作区组件；RQGM替换了搜索调度并增加评价slot与utility版本处理，不等于沿用原HyperAgents主实验完整算法或parent-selection变体。HGM-H基线仍是RQGM内部组合变体。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3；PDF p.18 Appendix B.1；PDF p.5 §4 Baselines。
- object：https://arxiv.org/html/2603.19461v1；版本：v1；定位：S3.p1.1；S3.p3.1；S3.p4.1；S3.p5.1。

### [HELIX: Model-Harness Co-evolution for Recursive Self-Improvement](../r04_system/wf_123445f953408e5162.md)
关系：`contrasts_system_boundary_with` · `r3_helix_red_queen_boundary` · 当前展示权限：`primary_supported`。
HELIX实际评价配置固定模型与外部验证器，重组harness并导出模型更新数据；RQGM的代码搜索则把学习评价者纳入工作区、在固定验证锚点约束下按checkpoint替换。两者的已实施可变状态及评价边界不同。

**关系边界**：仅为策展者双端机制比较，无直接历史继承或共同基准性能主张；HELIX提出的模型–harness整环没有在该v1中实际训练完成，不能与RQGM已实施的评价slot搜索混作同一证据级实验。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2608.13951v1；版本：v1；定位：S2.SS3.p1；S3.SS3.p1；S9.SS5.p1。
- object：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3；PDF p.4 §3.2；PDF p.19 Algorithm 1。

## 8. 来源清单、复查入口与解析缺口
- `new_sys_src_red_queen` · 已存来源 · v3
  - https://arxiv.org/pdf/2606.26294v3；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_original_methods_and_limitations。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_616c2bdc62bb176053 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
