# HELIX: Model-Harness Co-evolution for Recursive Self-Improvement

> 综合系统/智能体 · 2026 · `wf_123445f953408e5162`

**作者**：Tianyu Fan, Chao Huang  
**原文**：https://arxiv.org/abs/2608.13951  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已读原文系统实现、协议与评价限制；将声明协议和实做证据分开。

## 2. 论文的核心内容与贡献

### configuration:cfg_helix_build_update_rebuild_protocol
形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。

**适用版本**：v1；**原文定位**：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_helix_harness_portfolio_data
实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。

**适用版本**：v1；**原文定位**：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_helix_build_update_rebuild_protocol
`cfg_helix_build_update_rebuild_protocol` · protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 模型参数与可执行harness组合库组成的跨轮状态Z_t=(M_theta_t,Phi_t)。 |
| 改进过程与下一轮参与 | 协议规定G把已验证sibling轨迹变成训练记录，U更新模型；B结合证据和新模型重建harness组合库。 |
| 保留的状态及时间尺度 | 形式协议跨build–update–rebuild轮次保留模型与harness状态。 |
| 外部固定部分 | 外部任务、目标、验证器、类型化组合约束；G/U/B为声明的接口，不是已验证的自主改写算法。 |
| 实验实现状态 | proposed_protocol_model_update_not_executed |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。（状态：`supported`；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1）。
- **更新由什么过程产生**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。（状态：`supported`；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1）。
- **状态怎样持久保留**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。（状态：`supported`；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1）。
- **更新怎样进入后续改进**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。（状态：`supported`；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1）。

**配置判定**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。

来源：https://arxiv.org/html/2608.13951v1；版本：v1；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S9.SS5.p1。

### cfg_helix_harness_portfolio_data
`cfg_helix_harness_portfolio_data` · implemented_harness_evaluation_and_data_materialization

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定模型标签下的类型化harness组合、运行证据和导出的模型更新数据。 |
| 改进过程与下一轮参与 | 枚举并检查源可追溯的组件组合，执行65候选×100任务矩阵及选定候选后续评价；将sibling结果物化为训练数据。 |
| 保留的状态及时间尺度 | 运行轨迹、recipe/lockfile、评价证据和导出数据保存；本轮未训练后继模型。 |
| 外部固定部分 | 固定模型标签MiniMax-M2.7-highspeed、预设组件空间/筛查和评价协议、外部验证器。 |
| 实验实现状态 | implemented_harness_and_export_only_no_model_update |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。（状态：`supported`；定位：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1）。
- **更新由什么过程产生**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。（状态：`unknown`；定位：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1）。
- **状态怎样持久保留**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。（状态：`supported`；定位：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1）。
- **更新怎样进入后续改进**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。（状态：`unknown`；定位：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1）。

**配置判定**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。

来源：https://arxiv.org/html/2608.13951v1；版本：v1；定位：S3.SS3.p1；S5.SS2.p1；S5.SS2.p2；S5.SS3.p1；S5.SS4.p1；S6.SS2.p1；S9.SS1.p1；S9.SS3.p1；S9.SS5.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`new_sys_ev_cfg_helix_build_update_rebuild_protocol`**：形式化协议支持模型–harness状态在声明边界内闭环返回；该判定只对应所提协议，不对应已实施模型训练或多轮整环实验。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`new_sys_ev_cfg_helix_harness_portfolio_data`**：实际研究证明harness比较和验证数据交接；所查有限候选枚举与数据导出不足以证明由已更新模型驱动下一次harness重建，保留为邻接证据配置。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- §9.5明确未训练更新后的模型；不能认证模型–harness全环实证或其递归收益。
- 四条件在formal_specification层次成立，不代表自主性、代码复用或实验复现。
- 未实施模型参数更新，不升级为模型–harness整环实证。
- 100个LCB来源AtCoder题只检查公开测试，不等于官方LiveCodeBench隐藏测试表现。
- 79/100是事后候选组合覆盖并集，不能作为单一可部署harness得分。
- 65候选主矩阵每题一次、选定LCB后续10次、SWE后续2次；不能混合排名或声称同预算因果改善。
- §9.5明确未训练更新后的模型；不能认证模型–harness全环实证或其递归收益。；四条件在formal_specification层次成立，不代表自主性、代码复用或实验复现。
- 未实施模型参数更新，不升级为模型–harness整环实证。；100个LCB来源AtCoder题只检查公开测试，不等于官方LiveCodeBench隐藏测试表现。；79/100是事后候选组合覆盖并集，不能作为单一可部署harness得分。；65候选主矩阵每题一次、选定LCB后续10次、SWE后续2次；不能混合排名或声称同预算因果改善。

## 7. 与其他论文的具体关系

### [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](../r04_system/wf_616c2bdc62bb176053.md)
关系：`contrasts_system_boundary_with` · `r3_helix_red_queen_boundary` · 当前展示权限：`primary_supported`。
HELIX实际评价配置固定模型与外部验证器，重组harness并导出模型更新数据；RQGM的代码搜索则把学习评价者纳入工作区、在固定验证锚点约束下按checkpoint替换。两者的已实施可变状态及评价边界不同。

**关系边界**：仅为策展者双端机制比较，无直接历史继承或共同基准性能主张；HELIX提出的模型–harness整环没有在该v1中实际训练完成，不能与RQGM已实施的评价slot搜索混作同一证据级实验。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2608.13951v1；版本：v1；定位：S2.SS3.p1；S3.SS3.p1；S9.SS5.p1。
- object：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3；PDF p.4 §3.2；PDF p.19 Algorithm 1。

## 8. 来源清单、复查入口与解析缺口
- `new_sys_src_helix` · 已存来源 · v1
  - https://arxiv.org/html/2608.13951v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_original_methods_and_limitations。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_123445f953408e5162 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
