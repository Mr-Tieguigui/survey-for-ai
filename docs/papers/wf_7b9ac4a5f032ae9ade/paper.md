# BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics

> 方法论文 · 2026 · `wf_7b9ac4a5f032ae9ade`

**作者**：Junqi Liu, Yufan He, Yexiao He, Pengfei Guo, Dong Yang, Andriy Myronenko, Can Zhao, Hanrong Ye, Tianhao Qi, Yuyin Zhou, Daguang Xu, Yucheng Tang  
**原文**：https://arxiv.org/abs/2608.16211  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
BaT 的 Stage Bank 在策略更新环外合成状态，BiCuRL 按固定留出评价选择课程、rubric 验证 rollout 并用 GRPO 更新策略后回评；有明确闭环线索，应优先核配置而非因医疗场景排除。

## 2. 论文的核心内容与贡献

### configuration:cfg_bat_bicurl_policy_curriculum_v1
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2608.16211v1；**原文定位**：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_7b9ac4a5f032ae9ade`
BaT 的 Stage Bank 在策略更新环外合成状态，BiCuRL 按固定留出评价选择课程、rubric 验证 rollout 并用 GRPO 更新策略后回评；有明确闭环线索，应优先核配置而非因医疗场景排除。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### BaT BiCuRL: benchmark-guided retained policy training
`cfg_bat_bicurl_policy_curriculum_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前策略、固定阶段库、聚合诊断路由及保留/回退checkpoint组成训练系统。 |
| 改进过程与下一轮参与 | 聚合阶段分数选薄弱阶段；当前policy在三池混合沙箱采样并GRPO更新；评估后保留候选或回退最佳checkpoint，下一轮重诊断和采样。 |
| 保留的状态及时间尺度 | 跨训练轮保留policy参数及最佳checkpoint；不是单个研究任务的临时上下文。 |
| 外部固定部分 | - 公共阶段rubric、固定评估器和环境 - StageBank在policy更新循环外异步构建 - GRPO、路由、回退规则 - 固定OpenHands及公开skills执行层 |
| 评价与选择设置 | - **KL reference prompts**：256 - **controller final content**：same seven tracks; disjoint runs - **evaluation tracks**：7 - **fallback KL threshold**：0.1 - **fallback patience score drops**：3 - **models**：- Qwen3.5-4B - Qwen3.5-9B - **pool proportions**：- 0.5 - 0.25 - 0.25 - **repeated executions per track**：10 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：policy/课程/诊断边界明确。（状态：`supported`；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235）。
- **更新由什么过程产生**：自己的执行轨迹和失败诊断触发参数更新与下轮课程。（状态：`supported`；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235）。
- **状态怎样持久保留**：保留checkpoint供后续轮使用。（状态：`supported`；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235）。
- **更新怎样进入后续改进**：更新policy产生下轮rollout和聚合阶段诊断，再决定训练分布。（状态：`supported`；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2608.16211v1；版本：2608.16211v1；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235。

## 4. 实验、评价协议与结果的可解释范围


- **KL reference prompts**：256
- **controller final content**：same seven tracks; disjoint runs
- **evaluation tracks**：7
- **fallback KL threshold**：0.1
- **fallback patience score drops**：3
- **models**：- Qwen3.5-4B - Qwen3.5-9B
- **pool proportions**：- 0.5 - 0.25 - 0.25
- **repeated executions per track**：10

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_7b9ac4a5f032ae9ade`**：BaT 的 Stage Bank 在策略更新环外合成状态，BiCuRL 按固定留出评价选择课程、rubric 验证 rollout 并用 GRPO 更新策略后回评；有明确闭环线索，应优先核配置而非因医疗场景排除。
  - 来源版本：2608.16211v1；定位：Atom entry http://arxiv.org/abs/2608.16211v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_bat_bicurl_policy_curriculum_v1`**：当前策略、固定阶段库、聚合诊断路由及保留/回退checkpoint组成训练系统。 聚合阶段分数选薄弱阶段；当前policy在三池混合沙箱采样并GRPO更新；评估后保留候选或回退最佳checkpoint，下一轮重诊断和采样。
  - 来源版本：2608.16211v1；定位：§2.1–2.2 tool L107–184；Appendix A.2–A.4 tool L309–359；Appendix A.6 tool L396–411；§4.6 tool L222–235；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- StageBank生成不是当前policy在线改写自身训练数据生成器；rubric及执行层不自改。
- 训练controller和最终评估共享七任务内容、只运行分离；不能称完全独立held-out任务泛化。统计单位为7轨道，非70独立样本。
- 9B同默认runner policy分数53.4与完整BaT Agent79.6属于不同系统边界，不能混用增益。
- 4B在列举8个外部测试均退步，9B亦有保留损失；不能由医学任务收益推普遍增益。
- 本次未复核全部训练日志/泄漏扫描或跨seed复现，不认证模型参数以外的改进算子升级。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_bat` · 已存来源 · 2608.16211v1
  - https://arxiv.org/html/2608.16211v1；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_5b1dc5ef02082f5f` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-evolving%22+AND+%28all%3Aagent+OR+all%3Alanguage+OR+all%3Amodel%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7b9ac4a5f032ae9ade --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
