# MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory

> 方法论文 · 2026 · `wf_d045f6a3ccf0df1e41`

**作者**：Sujato Dutta, Sreekruthy Tummala, Shashank Vanga, Ayushmi Pavani  
**原文**：https://arxiv.org/abs/2610.08586v1  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
依具体更新边界裁定；不按self-evolving标题认证递归性。

## 2. 论文的核心内容与贡献

### configuration:cfg_mindset_versioned_schema_controller
core仅指有界记忆组织更新系统：保留的schema状态参与下一次更新；不额外要求控制器权重可变，也不据此认证收益或无界改进。

**适用版本**：v1；**原文定位**：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_mindset_versioned_schema_controller
`cfg_mindset_versioned_schema_controller` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定能量函数控制器维护不可变episodes与可变版本schema。 |
| 改进过程与下一轮参与 | 新episode在固定兼容性、矛盾、历史损伤与碎片化规则下reinforce/supersede/split/new；检索按schema还原原始证据。 |
| 保留的状态及时间尺度 | schema版本、异常与前后继保留；其centroid/counters/exceptions改变后续兼容、recurrence、能量比较和schema更新。 |
| 外部固定部分 | - 手工开发集校准的权重/阈值冻结 - 编码器、reranker和answer模型 - 能量及动作规则 |

**配置判定**：core仅指有界记忆组织更新系统：保留的schema状态参与下一次更新；不额外要求控制器权重可变，也不据此认证收益或无界改进。

来源：https://arxiv.org/html/2610.08586v1；版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_memory_ev_cfg_mindset_versioned_schema_controller`**：新episode在固定兼容性、矛盾、历史损伤与碎片化规则下reinforce/supersede/split/new；检索按schema还原原始证据。
  - 来源版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 无梯度训练、摄入/检索不调用生成模型。
- 最高观察F1限冻结样本和作者实现，不作跨论文优越性结论。
- 固定更新规则不抵消schema在后续更新中的作用；core结构裁定不是控制器或模型参数自改认证。
- core仅指有界记忆组织更新系统：保留的schema状态参与下一次更新；不额外要求控制器权重可变，也不据此认证收益或无界改进。

## 7. 与其他论文的具体关系

### [A-MEM: Agentic Memory for LLM Agents](../r03_method/wf_1aacba116cbe3c5bc3.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_mindset_versioned_schema_controller_cfg_amem` · 当前展示权限：`primary_supported`。
MINDSET固定能量规则管理不可变episodes的版本schema；A-MEM通过LLM重写邻近note语义和链接。两者持久组织变化均不能自动推得控制器参数或改进规则自改。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_mindset：https://arxiv.org/html/2610.08586v1；版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。
- r4_memory_src_mindset：https://arxiv.org/html/2610.08586v1；版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。

## 8. 来源清单、复查入口与解析缺口
- `r4_memory_src_mindset` · 已存来源 · v1
  - https://arxiv.org/html/2610.08586v1；阅读深度：`未单列`。

**证据深度**：selected_primary_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d045f6a3ccf0df1e41 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
