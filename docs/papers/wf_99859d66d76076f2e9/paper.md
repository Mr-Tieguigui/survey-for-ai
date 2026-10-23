# Self-Improving Large Language Models via Progressive Experience Evolution

> 方法论文 · 2026 · `wf_99859d66d76076f2e9`

**作者**：Shijie Ren, Xiting Wang, Meng Li, Yujie Guo, Yunhang Yao, Ziheng Peng, Xunlong Wang, Yuetan Chen, Haoyang Zhou, Yunlong Liang, Fandong Meng  
**原文**：https://arxiv.org/abs/2608.02139  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：The current mathematical reasoning policy, its global explicit experience pool, experience-conditioned detached teacher branch, student branch, and subsequent GRPO training stage；具体更新过程为：The current policy extracts experiences from successful and failed trajectories, consolidates them, and filters candidates by held-out probe marginal utility. An experience-conditioned teacher rescoring branch supplies reverse-KL on-policy self-distillation targets; the resulting student is further optimized by GRPO；更新状态的保留与后继使用为：The experience pool persists across its evolution rounds; distilled policy parameters persist through the training stages. Full repeated end-to-end training loops remain a future empirical question in v2。

## 2. 论文的核心内容与贡献

### configuration:cfg_spee
The v2 conclusion says the framework supports closed-loop iteration and leaves multiple full rounds for future work.

**适用版本**：v2；**原文定位**：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_spee
`cfg_spee` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | The current mathematical reasoning policy, its global explicit experience pool, experience-conditioned detached teacher branch, student branch, and subsequent GRPO training stage. |
| 改进过程与下一轮参与 | The current policy extracts experiences from successful and failed trajectories, consolidates them, and filters candidates by held-out probe marginal utility. An experience-conditioned teacher rescoring branch supplies reverse-KL on-policy self-distillation targets; the resulting student is further optimized by GRPO. |
| 保留的状态及时间尺度 | The experience pool persists across its evolution rounds; distilled policy parameters persist through the training stages. Full repeated end-to-end training loops remain a future empirical question in v2. |
| 外部固定部分 | - DAPO-math-17k task data - Binary reward mechanism - Probe set and positive-utility filter - OPSD reverse-KL update - GRPO optimizer - Experience available to teacher only during training |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：The current mathematical reasoning policy, its global explicit experience pool, experience-conditioned detached teacher branch, student branch, and subsequent GRPO training stage.（状态：`supported`；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）。
- **更新由什么过程产生**：The current policy extracts experiences from successful and failed trajectories, consolidates them, and filters candidates by held-out probe marginal utility. An experience-conditioned teacher rescoring branch supplies reverse-KL on-policy self-distillation targets; the resulting student is further optimized by GRPO.（状态：`supported`；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）。
- **状态怎样持久保留**：The experience pool persists across its evolution rounds; distilled policy parameters persist through the training stages. Full repeated end-to-end training loops remain a future empirical question in v2.（状态：`supported`；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）。
- **更新怎样进入后续改进**：The current policy extracts experiences from successful and failed trajectories, consolidates them, and filters candidates by held-out probe marginal utility. An experience-conditioned teacher rescoring branch supplies reverse-KL on-policy self-distillation targets; the resulting student is further optimized by GRPO.（状态：`supported`；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）。

**已核对的公式、算法或任务定义**：

- Eqs. 6-8: current-policy extraction and consolidation form candidate experiences.
- Eqs. 9-11: probe marginal reward improvement filters and updates the experience pool.
- Eq. 15: reverse KL matches student to the detached experience-conditioned teacher.

**配置判定**：The v2 conclusion says the framework supports closed-loop iteration and leaves multiple full rounds for future work.

来源：https://arxiv.org/html/2608.02139v2；版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_spee`**：当前模型提取/合并经验，probe筛选；经验用于OPSD，随后GRPO；方法支持闭环
  - 来源版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx5.p1；深度：`AI_primary_method_passage_recheck`。

- **`oct15_training_ev_w_spee`**：SPEE evolves explicit experiences using the current policy and probe utility, internalizes them through experience-conditioned on-policy self-distillation, and applies GRPO. The v2 evidence supports the stages and experience evolution, not an already measured multi-cycle end-to-end recursion.
  - 来源版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- The v2 conclusion says the framework supports closed-loop iteration and leaves multiple full rounds for future work.
- Experiments span Qwen3 1.7B, 4B, and 8B mathematical reasoning; no universal domain extension is established.
- ExpeL is a curator comparison here; no direct head-to-head benchmark or certified code reuse is established.
- v
- 2
- 已
- 重
- 读
- ，
- 不
- 能
- 把
- 方
- 法
- 支
- 持
- 闭
- 环
- 说
- 成
- 整
- 个
- 两
- 阶
- 段
- 管
- 线
- 多
- 次
- 循
- 实
- 验
- 证
- ；
- 结
- 论
- 将
- 轮
- 列
- 未
- 来
- 研
- 究

## 7. 与其他论文的具体关系

### [ExpeL: LLM Agents Are Experiential Learners](../r03_method/wf_984256074226b209d4.md)
关系：`contrasts_system_boundary_with` · `r2_spee_expel_9` · 当前展示权限：`primary_supported`。
Both extract reusable explicit experience from successful and failed trajectories. ExpeL edits persistent natural-language insights and retrieves successful examples with frozen model weights. SPEE additionally validates experience by probe utility, distills it into policy parameters, and follows with GRPO.

**关系边界**：未单列

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2608.02139v2（v2；Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1）；https://arxiv.org/html/2308.10144v3（v3；S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1）。

### [SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection](../r03_method/wf_5038de512c3639adcd.md)
关系：`contrasts_system_boundary_with` · `oct15_skillscaffold_spee_training_boundary` · 当前展示权限：`primary_supported`。
Both use current-policy-generated explicit guidance to improve future parameterized behavior. SkillScaffold selects query-specific skills using likelihood changes on fixed verified Scouts and jointly applies GRPO without a separate distillation stage. SPEE filters a persistent experience pool by probe reward improvement and explicitly distills it before further GRPO.

**关系边界**：未单列

**已存关系来源与定位（保留原记录端点语义）**：
- oct15_intake_src_2610_18807v1_html：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
- oct15_training_src_w_spee：https://arxiv.org/html/2608.02139v2；版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。
- oct15_intake_src_2610_18807v1_html：https://arxiv.org/html/2610.18807v1；版本：v1；定位：S4.SS1；S4.SS2；S4.SS3；S4.SS4；S4.SS5；A1.SS2；A1.SS3。
- oct15_training_src_w_spee：https://arxiv.org/html/2608.02139v2；版本：v2；定位：Sx2.SSx2.p2；Sx2.SSx2.p3；Sx2.SSx2.p4；Sx2.SSx2.SSS0.Px1.p1；Sx2.SSx3.p1；Sx3.SSx1；Sx5.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_spee` · Self-Improving Large Language Models via Progressive Experience Evolution · v2
  - https://arxiv.org/html/2608.02139v2；阅读深度：`未单列`。
- `oct15_training_src_w_spee` · 已存来源 · v2
  - https://arxiv.org/html/2608.02139v2；阅读深度：`targeted_primary_method_and_configuration_crosscheck`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_99859d66d76076f2e9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
