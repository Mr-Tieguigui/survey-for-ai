# ExpeL: LLM Agents Are Experiential Learners

> 方法论文 · 2023 · `wf_984256074226b209d4`

**作者**：Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang  
**原文**：https://arxiv.org/abs/2308.10144  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Training-stage ReAct/Reflexion trajectories, a persistent experience pool, an editable natural-language insight set, and a successful-trajectory vectorstore；具体更新过程为：Reflexion retries collect successes and failures. The instruction-following model compares failed/successful trajectories and applies ADD, EDIT, UPVOTE, or DOWNVOTE to insights; the updated insight set is used in subsequent extraction. Evaluation concatenates learned insights and retrieves similar successful trajectories without parameter training；更新状态的保留与后继使用为：Trajectories and insights persist across offline collection/extraction tasks; evaluation retrieves this fixed constructed pool。

### 定点原文补充：具体问题与执行过程
在不更新语言模型参数的情况下，将跨任务经验转成可检索成功轨迹和可复用洞见。

1. 训练任务先用 ReAct 规划、Reflexion 重试，记录成功/失败轨迹。
2. 比较同题的失败与成功、不同题的成功模式；用 ADD/EDIT/UPVOTE/DOWNVOTE 维护洞见及计数，计数到零时删除。

**实验与选择协议**：

- 成功轨迹通过向量相似度检索；测试提示拼接洞见和相似成功示例。
- 主要评价协议是训练经验之后，对未见任务单次尝试；不能与允许重试的设置混算。

**解释边界**：

- 改进对象是外部经验与提示上下文，基础模型冻结。
- 成功轨迹仍可能次优；洞见计数机制不是通用事实真值保证。

来源：[2308.10144v3](https://arxiv.org/html/2308.10144v3)；定位：§4.1–4.3 ExpeL；Algorithms 1–3。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_expel
Core loop refers to experience/insight construction, not frozen-pool evaluation alone.

**适用版本**：v3；**原文定位**：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_expel_evolvelab_adapter
这是MemEvolve论文的ExpeL适配器与评价设置，不复现原论文所有任务/提示，不能把适配结果外推为ExpeL普遍失败。

**适用版本**：2512.18746v1；**原文定位**：S5.SS3.p1；S5.SS3.p2；S8.SS3.p2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_expel_faithfulness_audit
Audit-specific ExpeL implementation; not exact reproduction of original all variants.

**适用版本**：2601.22436v1；**原文定位**：Appendix C ExpeL；§3.1–3.3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_expel
`cfg_expel` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Training-stage ReAct/Reflexion trajectories, a persistent experience pool, an editable natural-language insight set, and a successful-trajectory vectorstore. |
| 改进过程与下一轮参与 | Reflexion retries collect successes and failures. The instruction-following model compares failed/successful trajectories and applies ADD, EDIT, UPVOTE, or DOWNVOTE to insights; the updated insight set is used in subsequent extraction. Evaluation concatenates learned insights and retrieves similar successful trajectories without parameter training. |
| 保留的状态及时间尺度 | Trajectories and insights persist across offline collection/extraction tasks; evaluation retrieves this fixed constructed pool. |
| 外部固定部分 | - Frozen language model weights - ReAct base planner and Reflexion retry procedure - Manually supplied examples - Insight operations and importance-count rules - Retrieval mechanism |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Training-stage ReAct/Reflexion trajectories, a persistent experience pool, an editable natural-language insight set, and a successful-trajectory vectorstore.（状态：`supported`；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。
- **更新由什么过程产生**：Reflexion retries collect successes and failures. The instruction-following model compares failed/successful trajectories and applies ADD, EDIT, UPVOTE, or DOWNVOTE to insights; the updated insight set is used in subsequent extraction. Evaluation concatenates learned insights and retrieves similar successful trajectories without parameter training.（状态：`supported`；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。
- **状态怎样持久保留**：Trajectories and insights persist across offline collection/extraction tasks; evaluation retrieves this fixed constructed pool.（状态：`supported`；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。
- **更新怎样进入后续改进**：Reflexion retries collect successes and failures. The instruction-following model compares failed/successful trajectories and applies ADD, EDIT, UPVOTE, or DOWNVOTE to insights; the updated insight set is used in subsequent extraction. Evaluation concatenates learned insights and retrieves similar successful trajectories without parameter training.（状态：`supported`；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。

**已核对的公式、算法或任务定义**：

- Insight operations: ADD/EDIT/UPVOTE/DOWNVOTE update content and importance; zero-count insights are removed.
- Evaluation context concatenates the insight list and top-k task-similar successful trajectories.

**配置判定**：Core loop refers to experience/insight construction, not frozen-pool evaluation alone.

来源：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

### cfg_expel_evolvelab_adapter
`cfg_expel_evolvelab_adapter` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | EvolveLab中ExpeLProvider重实现及Flash-Searcher评测 |
| 改进过程与下一轮参与 | 成功失败轨迹凝练insight，写入向量库并按语义检索 |
| 保留的状态及时间尺度 | 实现支持经历写入后续检索；审计任务中的完整原配置等价未认证 |
| 外部固定部分 | EvolveLab统一MemoryProvider接口、Flash-Searcher、目标任务与backbone |

**配置判定**：这是MemEvolve论文的ExpeL适配器与评价设置，不复现原论文所有任务/提示，不能把适配结果外推为ExpeL普遍失败。

来源：https://arxiv.org/html/2512.18746v1；版本：2512.18746v1；定位：S5.SS3.p1；S5.SS3.p2；S8.SS3.p2。

### cfg_expel_faithfulness_audit
`cfg_expel_faithfulness_audit` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | ExpeL implementation in the experience-faithfulness intervention study |
| 改进过程与下一轮参与 | Original ExpeL experience extraction is distinct from this audit intervention; fixed offline experience pool is retrieved during evaluation. |
| 保留的状态及时间尺度 | Offline experience pool retained across evaluation queries; no new memory updates inferred from the causal audit. |
| 外部固定部分 | - GPT-4o backbone - all-mpnet-base-v2 embeddings - Faiss retriever - offline experience pool and intervention procedure |
| 评价与选择设置 | - **backbone**：GPT-4o - **embedding**：all-mpnet-base-v2 - **maximum retries**：3 - **retrieval index**：Faiss - **task settings**：- **ALFWorld**：- **environment step limit**：20 - **retrieved experiences**：2 - **HotpotQA**：- **environment step limit**：7 - **retrieved experiences**：6 - **WebShop**：- **environment step limit**：15 - **retrieved experiences**：2 - **temperature**：0.0 |

**配置判定**：Audit-specific ExpeL implementation; not exact reproduction of original all variants.

来源：https://arxiv.org/html/2601.22436v1；版本：2601.22436v1；定位：Appendix C ExpeL；§3.1–3.3。

## 4. 实验、评价协议与结果的可解释范围


- **backbone**：GPT-4o
- **embedding**：all-mpnet-base-v2
- **maximum retries**：3
- **retrieval index**：Faiss
- **task settings**：- **ALFWorld**：- **environment step limit**：20 - **retrieved experiences**：2 - **HotpotQA**：- **environment step limit**：7 - **retrieved experiences**：6 - **WebShop**：- **environment step limit**：15 - **retrieved experiences**：2
- **temperature**：0.0

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_expel`**：提取器对既有insights做ADD/EDIT/UPVOTE/DOWNVOTE；修改后集合输入后续提取；收集阶段使用Reflexion
  - 来源版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1；深度：`AI_primary_method_passage_recheck`。

- **`oct15_training_ev_w_expel`**：ExpeL transforms training-task outcomes into persistent editable natural-language insights and retrieved successful trajectories. Evaluation uses them in context; the original configuration does not update model weights.
  - 来源版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1；深度：`AI_primary_method_passage_recheck`。

- **`r4_memory_ev_expel_existing`**：成功/失败经验经insight编辑形成持久知识，部署把insights及相似成功轨迹加入上下文。
  - 来源版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Core loop refers to experience/insight construction, not frozen-pool evaluation alone.
- The insight extractor defaults to gpt-4-0613; the complete system is not a single universally specified backbone.
- No distillation into weights is described in this original ExpeL configuration.
- Audit-specific implementation; no exact replication of every original configuration.
- Causal intervention tests actual memory use; does not establish a universal no-benefit result.
- 核
- 心
- 只
- 在
- 建
- 设
- 经
- 验
- 和
- i
- n
- s
- g
- h
- t
- 的
- 配
- 置
- ；
- 固
- 定
- 评
- 测
- 推
- 理
- 另
- 列
- a
- d
- j
- c
- e

## 7. 与其他论文的具体关系

### [Reflexion: Language Agents with Verbal Reinforcement Learning](../r03_method/wf_3fb5d6b0a837235b64.md)
关系：`adapts_design_of` · `r2_expel_reflexion_4` · 当前展示权限：`primary_supported`。
ExpeL明确在训练经验收集阶段采用Reflexion的失败轨迹反思与同任务重试：失败后累积反思文本并输入下一次ReAct试次；随后把跨任务经验用于insights提取。Reflexion原方法确认Actor、Evaluator、反思器及跨试次反思记忆循环。

**关系边界**：适配关系仅覆盖训练经验收集组件；ExpeL主部署配置单次作答，§5.5另有测试重试变体，不能把两个配置混合。Reflexion原文反思记忆通常只保留1–3条，不认证跨任务永久记忆；未检查代码复用。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S5.SS5.p1；A4.SS5.p1。
- object：https://arxiv.org/html/2303.11366v4；版本：v4；定位：S3.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。
- expand_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

### [Self-Improving Large Language Models via Progressive Experience Evolution](../r03_method/wf_99859d66d76076f2e9.md)
关系：`contrasts_system_boundary_with` · `r2_spee_expel_9` · 当前展示权限：`primary_supported`。
Both extract reusable explicit experience from successful and failed trajectories. ExpeL edits persistent natural-language insights and retrieves successful examples with frozen model weights. SPEE additionally validates experience by probe utility, distills it into policy parameters, and follows with GRPO.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2608.02139v2（v2；Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）；https://arxiv.org/html/2308.10144v3（v3；S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。

### [Self-Evolving Agent Harness](../r02_concept/wf_d774ae4f1af498b39c.md)
关系：`contrasts_system_boundary_with` · `oct15_harness_expel_interpreted_boundary` · 当前展示权限：`primary_supported`。
The harness framework distinguishes interpreted memory/insight updates from executable runtime mutation around fixed weights. Original ExpeL concretely updates natural-language insights and retrieved trajectories during construction, then uses a fixed pool at evaluation. This illustrates an interpreted-state boundary, not general executable self-rewriting.

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- oct15_intake_src_2610_18813v1_html：https://arxiv.org/html/2610.18813v1；版本：v1；定位：S2；S3。
- oct15_training_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。
- oct15_intake_src_2610_18813v1_html：https://arxiv.org/html/2610.18813v1；版本：v1；定位：S2；S3。
- oct15_training_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

### [TeleTune: Evolving Agent Skills From Offline Telemetry](../r03_method/wf_80501dd94b58c15ace.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_teletune_offline_library_optimizer_cfg_expel` · 当前展示权限：`primary_supported`。
两者保留文字知识供之后行为使用。TeleTune按固定日志的动作预测错误编辑且dev准确率门控；ExpeL比较成功/失败轨迹编辑insight并在评估检索成功轨迹。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_teletune：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
- r4_memory_src_expel_existing：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。
- r4_memory_src_teletune：https://arxiv.org/html/2610.05437v2；版本：v2；定位：§2.1–2.2, tool text L85–110；§2.3–2.4, tool text L111–118。
- r4_memory_src_expel_existing：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_faithfulness_v1` · 已存来源 · v1
  - https://arxiv.org/html/2601.22436v1；阅读深度：`未单列`。
- `completion_src_memevolve_v1` · 已存来源 · 2512.18746v1
  - https://arxiv.org/html/2512.18746v1；阅读深度：`未单列`。
- `expand_src_w_expel` · ExpeL · v3
  - https://arxiv.org/html/2308.10144v3；阅读深度：`未单列`。
- `oct15_training_src_w_expel` · 已存来源 · v3
  - https://arxiv.org/html/2308.10144v3；阅读深度：`targeted_primary_method_and_configuration_crosscheck`。
- `r4_memory_src_expel_existing` · 已存来源 · v3
  - https://arxiv.org/html/2308.10144v3；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_984256074226b209d4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
