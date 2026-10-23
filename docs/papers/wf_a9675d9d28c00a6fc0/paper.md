# RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement

> 方法论文 · 2026 · `wf_a9675d9d28c00a6fc0`

**作者**：Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Zhiyou Heng, Zhaosong Li  
**原文**：https://arxiv.org/abs/2609.27612  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：RegenHarness: A Robot Agent Harness withEvidence-Gated Recursive Self-Improvement。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
RegenHarness binds commits to identity/version/condition evidence and defines revision with regressions, target improvement, authorization and rollback; active missions retain configuration. Explicit RSI protocol revises context, templates, routing and bounded recovery for later missions; no online weights or weakening acceptance predicates.

### 与 RSI 的具体关系

- Explicit RSI protocol revises context, templates, routing and bounded recovery for later missions; no online weights or weakening acceptance predicates.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_a9675d9d28c00a6fc0
RegenHarness binds commits to identity/version/condition evidence and defines revision with regressions, target improvement, authorization and rollback; active missions retain configuration.

**适用版本**：2609.27612v1；**原文定位**：Evidence-bound commit; PDF physical page 7, derived page-text lines 22-36 (one-based local extraction, not web-tool lines)；Cross-mission release; PDF physical page 8, derived page-text lines 19-45 (one-based local extraction, not web-tool lines)；Physical scope; PDF physical page 9, derived page-text lines 19-28 (one-based local extraction, not web-tool lines)；Comparison specification; PDF physical page 15, derived page-text lines 1-11 (one-based local extraction, not web-tool lines)；Assessment separation; PDF physical page 14, derived page-text lines 57-64 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节

### RegenHarness v1 cross-mission revision protocol with unreached empirical closure
`cfg_regenharness_cross_mission_revision_protocol_v1` · declared_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | robot runtime、mission evidence store及harness revision protocol；可写context selection、templates、routing、bounded recovery config，物理safety interlocks及acceptance predicate不由updater削弱。 |
| 改进过程与下一轮参与 | revision generator把mission failure/cost和trace转为candidate manifest；fixed regression/target metric及release authorization后才部署candidate，保留rollback。 |
| 保留的状态及时间尺度 | 协议规定mission-boundary version release、mission pinning和下批mission records进入下一revision cycle；所读实验展示mission execution，未列actual accepted revision sequence。 |
| 外部固定部分 | - model、skill provider、safety/evidence/commit contracts - candidate admission predicate、fixed regression controls和release authorization - online weights不在协议内 |
| 评价与选择设置 | - **RSI evaluation**：specified frozen-vs-accepted-candidate comparison, not quantitative revision results in inspected passages - **demonstrated**：quadruped inspection and closed-route completion cases - **implemented**：Python immutable contracts and SQLite runtime; ROS2/vendor/simulator adapters |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4.9明确harness revision对象与权限。（状态：`supported`；定位：§4.8–4.9 event history and revision protocol tool L234–257；§5–6 implementation and demonstrated missions tool L260–274；§6.8 assessment design rather than measured revision sequence tool L362–368）。
- **更新由什么过程产生**：候选生成/接受为协议声明；实际accepted revision实验未在所读§6.8报告。（状态：`unknown`；定位：§4.8–4.9 event history and revision protocol tool L234–257；§5–6 implementation and demonstrated missions tool L260–274；§6.8 assessment design rather than measured revision sequence tool L362–368）。
- **状态怎样持久保留**：协议有version和rollback；执行case有持久evidence，不足等同已完成修订部署。（状态：`unknown`；定位：§4.8–4.9 event history and revision protocol tool L234–257；§5–6 implementation and demonstrated missions tool L260–274；§6.8 assessment design rather than measured revision sequence tool L362–368）。
- **更新怎样进入后续改进**：后续mission反馈路径为协议声明；未获得实施后再次修订的实证。（状态：`unknown`；定位：§4.8–4.9 event history and revision protocol tool L234–257；§5–6 implementation and demonstrated missions tool L260–274；§6.8 assessment design rather than measured revision sequence tool L362–368）。

**配置判定**：保留已声明的harness revision protocol及其邻接相关性；实际自诱导candidate release、更新状态保留及跨mission再次改进证据unknown，配置pending，不将deployment演示升级core。

来源：https://arxiv.org/html/2609.27612v1；版本：2609.27612v1；定位：§4.8–4.9 event history and revision protocol tool L234–257；§5–6 implementation and demonstrated missions tool L260–274；§6.8 assessment design rather than measured revision sequence tool L362–368。

## 4. 实验、评价协议与结果的可解释范围

Proposed frozen/candidate comparison fixes model/provider, uses held-out tasks and measures success, false completion, duplicate dispatch, recovery, regressions and release overhead. Physical cases are separate.


- **RSI evaluation**：specified frozen-vs-accepted-candidate comparison, not quantitative revision results in inspected passages
- **demonstrated**：quadruped inspection and closed-route completion cases
- **implemented**：Python immutable contracts and SQLite runtime; ROS2/vendor/simulator adapters

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_regenharness_cross_mission_revision_protocol_v1`**：保留已声明的harness revision protocol及其邻接相关性；实际自诱导candidate release、更新状态保留及跨mission再次改进证据unknown，配置pending，不将deployment演示升级core。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

- **`b570_07_ev_wf_a9675d9d28c00a6fc0`**：RegenHarness binds commits to identity/version/condition evidence and defines revision with regressions, target improvement, authorization and rollback; active missions retain configuration.
  - 来源版本：2609.27612v1；定位：Evidence-bound commit; PDF physical page 7, derived page-text lines 22-36 (one-based local extraction, not web-tool lines)；Cross-mission release; PDF physical page 8, derived page-text lines 19-45 (one-based local extraction, not web-tool lines)；Physical scope; PDF physical page 9, derived page-text lines 19-28 (one-based local extraction, not web-tool lines)；Comparison specification; PDF physical page 15, derived page-text lines 1-11 (one-based local extraction, not web-tool lines)；Assessment separation; PDF physical page 14, derived page-text lines 57-64 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Evidence-bound commit
**来源**：https://arxiv.org/pdf/2609.27612v1  
**实际版本**：2609.27612v1  
**精确定位**：PDF physical page 7, derived page-text lines 22-36 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a9675d9d28c00a6fc0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Cross-mission release
**来源**：https://arxiv.org/pdf/2609.27612v1  
**实际版本**：2609.27612v1  
**精确定位**：PDF physical page 8, derived page-text lines 19-45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a9675d9d28c00a6fc0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Assessment separation
**来源**：https://arxiv.org/pdf/2609.27612v1  
**实际版本**：2609.27612v1  
**精确定位**：PDF physical page 14, derived page-text lines 57-64 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a9675d9d28c00a6fc0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Physical scope
**来源**：https://arxiv.org/pdf/2609.27612v1  
**实际版本**：2609.27612v1  
**精确定位**：PDF physical page 9, derived page-text lines 19-28 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a9675d9d28c00a6fc0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Comparison specification
**来源**：https://arxiv.org/pdf/2609.27612v1  
**实际版本**：2609.27612v1  
**精确定位**：PDF physical page 15, derived page-text lines 1-11 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a9675d9d28c00a6fc0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Warehouse/circuit cases show execution and history-dependent completion. Section 6.8 comparison/RSI criteria specify a protocol, not an executed paired benchmark or accepted revision sequence.
- 不能把warehouse任务成功、ROS日志或history-dependent completion当作cross-mission RSI gain。
- §6.8给assessment protocol和held-out要求，未报告revision cohort、accept/reject数据或before/after收益。
- 本配置保留protocol/context事实；自诱导更新、更新状态保留、后继改进参与的实验状态unknown，配置pending而非排除结果。
- 不能把warehouse任务成功、ROS日志或history-dependent completion当作cross-mission RSI gain。; §6.8给assessment protocol和held-out要求，未报告revision cohort、accept/reject数据或before/after收益。; 本配置保留protocol/context事实；自诱导更新、更新状态保留、后继改进参与的实验状态unknown，配置pending而非排除结果。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_regen` · RegenHarness: A Robot Agent Harness withEvidence-Gated Recursive Self-Improvement · 2609.27612v1
  - https://arxiv.org/html/2609.27612v1；阅读深度：`未单列`。
- `b570_07_src_wf_a9675d9d28c00a6fc0` · RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement · 2609.27612v1
  - https://arxiv.org/pdf/2609.27612v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Existing configuration ID unchanged; no new accepted configuration or executed RSI benchmark certified.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`pending_scope_only_no_configuration_claim_admission`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a9675d9d28c00a6fc0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
