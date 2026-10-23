# ReVision3D: Attribution-Guided Recursive Self-Improvement for 3D Medical Perception

> 方法论文 · 2026 · `wf_434c1e20d5f35240df`

**作者**：Ho Hin Lee, Yuyin Zhou, Yannan Yu, Shi Gu, Yifan Wu  
**原文**：https://arxiv.org/abs/2609.32984  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：人工编排的冻结LLM designer、当前3D reader系统Sigma和跨修订playbook；不含未经执行的自动level scheduler；具体更新过程为：回放归因当前漏检→designer改采集/感知配置/训练recipe/推理程序→固定J和接受规则检验→保留Sigma及成败playbook，再归因剩余失败指导后续候选；更新状态的保留与后继使用为：reader参数、adapter/程序及playbook跨实际修订保留；允许四种预定义干预层。

## 2. 论文的核心内容与贡献

### configuration:cfg_revision3d_orchestrated_retained_system_v2
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2609.32984v2；**原文定位**：§3 tool L124–186；Appendix H tool L523–536。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_434c1e20d5f35240df`
ReVision3D 用冻结设计 LLM 提出采集、感知、训练或推理修订，固定验证器和系统目标，以空间标注回放定位瓶颈并保留超过种子噪声的变更；有可核闭环候选，需逐层拆配置。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### ReVision3D: bounded designer revisions under fixed verifier
`cfg_revision3d_orchestrated_retained_system_v2` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 人工编排的冻结LLM designer、当前3D reader系统Sigma和跨修订playbook；不含未经执行的自动level scheduler。 |
| 改进过程与下一轮参与 | 回放归因当前漏检→designer改采集/感知配置/训练recipe/推理程序→固定J和接受规则检验→保留Sigma及成败playbook，再归因剩余失败指导后续候选。 |
| 保留的状态及时间尺度 | reader参数、adapter/程序及playbook跨实际修订保留；允许四种预定义干预层。 |
| 外部固定部分 | - reference masks及5mm空间verifier - 固定promotion J与接受规则 - 冻结designer及预定义动作空间 - 固定外部annotated volumes |
| 评价与选择设置 | - **designer**：frozen Claude Opus 5 - **inference acceptance**：paired bootstrap P(deltaJ>0)>=0.9 - **promotion FP budgets**：- 0.25 - 0.5 - 1 - 2 - **reader**：Qwen3-VL-4B-Instruct - **spatial tolerance mm**：5 - **training acceptance**：positive every matched seed and mean deltaJ exceeds incumbent seed range - **training reward**：hits - bounded duplicate/falsefinding penalties + correct silence 0.5 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：实际designer/reader/retained artifact和人工编排边界明确。（状态：`supported`；定位：§3 tool L124–186；Appendix H tool L523–536）。
- **更新由什么过程产生**：当前reader失败归因与designer代码/配置修改触发更新。（状态：`supported`；定位：§3 tool L124–186；Appendix H tool L523–536）。
- **状态怎样持久保留**：通过检验的Sigma和经验playbook被保留。（状态：`supported`；定位：§3 tool L124–186；Appendix H tool L523–536）。
- **更新怎样进入后续改进**：接受更新后重新归因剩余失败，并将成功/失败假设写playbook供后续设计；不要求Eq5实际自动执行。（状态：`supported`；定位：§3 tool L124–186；Appendix H tool L523–536）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2609.32984v2；版本：2609.32984v2；定位：§3 tool L124–186；Appendix H tool L523–536。

## 4. 实验、评价协议与结果的可解释范围


- **designer**：frozen Claude Opus 5
- **inference acceptance**：paired bootstrap P(deltaJ>0)>=0.9
- **promotion FP budgets**：- 0.25 - 0.5 - 1 - 2
- **reader**：Qwen3-VL-4B-Instruct
- **spatial tolerance mm**：5
- **training acceptance**：positive every matched seed and mean deltaJ exceeds incumbent seed range
- **training reward**：hits - bounded duplicate/falsefinding penalties + correct silence 0.5

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_434c1e20d5f35240df`**：ReVision3D 用冻结设计 LLM 提出采集、感知、训练或推理修订，固定验证器和系统目标，以空间标注回放定位瓶颈并保留超过种子噪声的变更；有可核闭环候选，需逐层拆配置。
  - 来源版本：2609.32984v2；定位：Atom entry http://arxiv.org/abs/2609.32984v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_revision3d_orchestrated_retained_system_v2`**：人工编排的冻结LLM designer、当前3D reader系统Sigma和跨修订playbook；不含未经执行的自动level scheduler。 回放归因当前漏检→designer改采集/感知配置/训练recipe/推理程序→固定J和接受规则检验→保留Sigma及成败playbook，再归因剩余失败指导后续候选。
  - 来源版本：2609.32984v2；定位：§3 tool L124–186；Appendix H tool L523–536；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Equation 5 的level路由是回顾性表述，未调度实验；本core是实际有人编排的修订反馈系统，不认证端到端自主scheduler。
- replay仅几何/渲染精确；未见view的reader输出须实际运行。有限G采样归因不提供因果保证或证明不可检测。
- 最终multi-organ测试在决策冻结后进行，但更早component-study test cohort存在重叠，不能统一称全部实验test完全未用于探索。
- mask verifier只认证定位，不能推病理、恶性、临床推理或安全；四种干预外的新backbone/模态并未自主引入。
- training reward可调权重不等于promotion J可编辑；本次未运行代码/重新训练。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_revision` · 已存来源 · 2609.32984v2
  - https://arxiv.org/html/2609.32984v2；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_434c1e20d5f35240df --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
