# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

> 方法论文 · 2026 · `wf_4f5bbf3318b1fe409e`

**作者**：Shengtao Zhang, Jiaqian Wang, Ruiwen Zhou, Junwei Liao, Yuchen Feng, Zhuo Li, Yujie Zheng, Weinan Zhang, Ying Wen, Zhiyu Li, Feiyu Xiong, Yutao Qi, Bo Tang, Muning Wen  
**原文**：https://arxiv.org/abs/2601.03192  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Core persistent memory configuration; improvement rule self-rewrite and unbounded recursion are not established.

## 2. 论文的核心内容与贡献

### configuration:cfg_memrl_runtime_memory
Core persistent-memory configuration; no evidence that update algorithm rewrites itself.

**适用版本**：2601.03192v2；**原文定位**：§3.1–4.4；§5.1–5.3；Appendix E Table8–9；§6；Appendix G。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_memrl_runtime_memory
`cfg_memrl_runtime_memory` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Frozen LLM, episodic triplets (intent, experience, utility), retrieval and reward update. |
| 更新状态 | Experiences and scalar utilities; not backbone weights. |
| 改进过程与下一轮参与 | Similarity recall, utility ranking, environmental reward EMA, trajectory summarization/writeback. |
| 保留的状态及时间尺度 | Cross-task runtime memory; transfer freezes the learned bank. |
| 外部固定部分 | Backbone, embedding, reward definition, retrieval/update rule, alpha/lambda and task protocol. |

**已登记超参数**：

- **Q init**：0
- **alpha**：0.3
- **benchmark order**：- BigCodeBench - Lifelong OS - Lifelong DB - ALFWorld - HLE
- **delta**：- 0.38 - 0.5 - 0.37 - 0.62 - 0.25
- **k1**：- 10 - 10 - 10 - 5 - 5
- **k2**：- 5 - 5 - 5 - 3 - 3
- **lambda value**：0.5
- **locator**：Appendix E Table8

**配置判定**：Core persistent-memory configuration; no evidence that update algorithm rewrites itself.

来源：https://arxiv.org/html/2601.03192v2；版本：2601.03192v2；定位：§3.1–4.4；§5.1–5.3；Appendix E Table8–9；§6；Appendix G。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- §4.4 stability assumes frozen inference and stationary tasks.
- §6/G: long-horizon variance, ambiguous multi-memory credit, sparse task similarity.
- Appendix E Table9 split counts and 7:3 notes need reconciliation; CSR is not held-out pass@1.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `completion_src_memrl_v2` · 已存来源 · 2601.03192v2
  - https://arxiv.org/html/2601.03192v2；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_limits_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4f5bbf3318b1fe409e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
