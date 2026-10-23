# TeleTune: Evolving Agent Skills From Offline Telemetry

> 方法论文 · 2026 · `wf_80501dd94b58c15ace`

**作者**：Justin Chih-Yao Chen, Elias Stengel-Eskin, Yan Chen, Pol Llado, Scott Counts, Mohit Bansal, Benjamin Van Durme, Harsh Jhamtani, Gaurav Verma  
**原文**：https://arxiv.org/abs/2610.05437v2  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
依具体更新边界裁定；不按self-evolving标题认证递归性。

## 2. 论文的核心内容与贡献

### configuration:cfg_teletune_fixed_library_deployment
固定部署不能借用离线优化的递归核心身份。

**适用版本**：v2；**原文定位**：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_teletune_offline_library_optimizer
core仅完整离线自反馈编辑系统；固定人类/专家日志是外部监督，不是在线探索。

**适用版本**：v2；**原文定位**：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_teletune_offline_library_optimizer
`cfg_teletune_offline_library_optimizer` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LM预测器/优化器、固定成功日志及可编辑工作流/技能库。 |
| 改进过程与下一轮参与 | 以当前库预测固定日志，首错驱动局部编辑；dev动作预测准确率提升才替换库，随后再用新库预测和编辑。 |
| 保留的状态及时间尺度 | 接受库跨优化步checkpoint并影响下一轮自生预测错误。 |
| 外部固定部分 | - 固定日志与teacher forcing - train/dev划分、预测匹配规则 - 同骨干冻结权重及停止预算 |

**配置判定**：core仅完整离线自反馈编辑系统；固定人类/专家日志是外部监督，不是在线探索。

来源：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。

### cfg_teletune_fixed_library_deployment
`cfg_teletune_fixed_library_deployment` · inference_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结模型与优化后库；新任务只组装示例并执行。 |
| 改进过程与下一轮参与 | 按工作流覆盖检索示例，执行期间库和示例固定。 |
| 保留的状态及时间尺度 | 训练产物跨任务复用；此部署配置没有继续编辑。 |
| 外部固定部分 | - 模型、全局库 - 每任务开始确定的示例 |

**配置判定**：固定部署不能借用离线优化的递归核心身份。

来源：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_memory_ev_cfg_teletune_offline_library_optimizer`**：以当前库预测固定日志，首错驱动局部编辑；dev动作预测准确率提升才替换库，随后再用新库预测和编辑。
  - 来源版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118；深度：`未单列`。

- **`r4_memory_ev_cfg_teletune_fixed_library_deployment`**：按工作流覆盖检索示例，执行期间库和示例固定。
  - 来源版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 任务goal在测试期可用；训练日志未记录goal时另行推断。
- 优化目标是动作预测代理指标，非每项编辑在线任务成功验证。
- 反复使用同dev集并不证明对任意未来任务泛化。
- core仅完整离线自反馈编辑系统；固定人类/专家日志是外部监督，不是在线探索。
- 固定部署不能借用离线优化的递归核心身份。

## 7. 与其他论文的具体关系

### [ExpeL: LLM Agents Are Experiential Learners](../r03_method/wf_984256074226b209d4.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_teletune_offline_library_optimizer_cfg_expel` · 当前展示权限：`primary_supported`。
两者保留文字知识供之后行为使用。TeleTune按固定日志的动作预测错误编辑且dev准确率门控；ExpeL比较成功/失败轨迹编辑insight并在评估检索成功轨迹。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_teletune：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
- r4_memory_src_expel_existing：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。
- r4_memory_src_teletune：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
- r4_memory_src_expel_existing：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

## 8. 来源清单、复查入口与解析缺口
- `r4_memory_src_teletune` · 已存来源 · v2
  - https://arxiv.org/html/2610.05437v2；阅读深度：`未单列`。

**证据深度**：selected_primary_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_80501dd94b58c15ace --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
