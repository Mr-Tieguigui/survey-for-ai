# MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution

> 方法论文 · 2026 · `wf_825842f3cb42f01a8c`

**作者**：Junde Wu, Jiayuan Zhu, Minghao Hu, Fenglin Liu, Jiazhen Pan  
**原文**：https://arxiv.org/abs/2609.24838  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
MedRSI 将诊断失败转为工具组合与任务模型训练，以临床代价排优先级并将快速发现与跨后续患者队列的慢注册分开；有生成、验证、持久采用线索，仍需核临床任务与验证边界。

## 2. 论文的核心内容与贡献

### configuration:cfg_medrsi_stable_tool_registry_v1
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2609.24838v1；**原文定位**：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_825842f3cb42f01a8c`
MedRSI 将诊断失败转为工具组合与任务模型训练，以临床代价排优先级并将快速发现与跨后续患者队列的慢注册分开；有生成、验证、持久采用线索，仍需核临床任务与验证边界。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### MedRSI: clinically prioritized tool invention and slow registration
`cfg_medrsi_stable_tool_registry_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定GPT-4o推理/反思器、实验工具池、稳定版本工具registry和后续病例失败回流。 |
| 改进过程与下一轮参与 | 按固定临床代价rubric聚类失败，生成/组合/训练候选；发现收益为正后冻结包，经后续3个合格cohort配对评估收益及临床代价，串行注册；registry变动须重评依赖。 |
| 保留的状态及时间尺度 | 稳定代码/模型工具和依赖版本跨20轮保留；实验工具不写入稳定诊断轨迹。 |
| 外部固定部分 | - GPT-4o 2024-08-06及临床judge/rubric - 注册门槛与病例分区 - 允许的架构库、预算、OpenHands接口 |
| 评价与选择设置 | - **candidate attempt budget per round**：6 - **long horizon ablation rounds**：30 - **priority lambda**：2 - **public improvement rounds**：20 - **reasoning model**：GPT-4o 2024-08-06 - **registration margin**：0.5 balanced accuracy points or 0.01 normalized EF error - **test policy**：patient-separated locked final test; round-wise test curves retrospective - **trial cohorts K**：3 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：诊断器、反思/工具构建器和registry为整体。（状态：`supported`；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217）。
- **更新由什么过程产生**：自身病例失败引导新工具代码/模型的构建。（状态：`supported`；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217）。
- **状态怎样持久保留**：通过试验的版本工具长期进入稳定registry。（状态：`supported`；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217）。
- **更新怎样进入后续改进**：新registry改变后续诊断记录及待解决失败，进而改变下一轮工具开发。（状态：`supported`；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2609.24838v1；版本：2609.24838v1；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217。

## 4. 实验、评价协议与结果的可解释范围


- **candidate attempt budget per round**：6
- **long horizon ablation rounds**：30
- **priority lambda**：2
- **public improvement rounds**：20
- **reasoning model**：GPT-4o 2024-08-06
- **registration margin**：0.5 balanced accuracy points or 0.01 normalized EF error
- **test policy**：patient-separated locked final test; round-wise test curves retrospective
- **trial cohorts K**：3

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_825842f3cb42f01a8c`**：MedRSI 将诊断失败转为工具组合与任务模型训练，以临床代价排优先级并将快速发现与跨后续患者队列的慢注册分开；有生成、验证、持久采用线索，仍需核临床任务与验证边界。
  - 来源版本：2609.24838v1；定位：Atom entry http://arxiv.org/abs/2609.24838v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_medrsi_stable_tool_registry_v1`**：固定GPT-4o推理/反思器、实验工具池、稳定版本工具registry和后续病例失败回流。 按固定临床代价rubric聚类失败，生成/组合/训练候选；发现收益为正后冻结包，经后续3个合格cohort配对评估收益及临床代价，串行注册；registry变动须重评依赖。
  - 来源版本：2609.24838v1；定位：§2.1 tool L96–118；§2.2–2.3 tool L119–200；§3.1–3.2 tool L202–217；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- K统计合格cohort而非改进轮；固定候选与reference registry，异步试验不代表3次重新训练。
- 临床judge、严重度rubric和注册objective固定；医学应用不因领域标签自动排除，亦不等于临床安全认证。
- private cohort与原文注册流程尚未独立复现；public comparator部分沿用MedAgent-Pro报告值，不能假设全部同预算重新运行。
- 最终test在轨迹及checkpoint冻结后回顾评估；不是test反馈指导工具构建。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_medrsi` · 已存来源 · 2609.24838v1
  - https://arxiv.org/html/2609.24838v1；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_825842f3cb42f01a8c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
