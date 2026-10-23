# Deep Collective Learning: Learning Optimal Inputs and Weights Jointly in Deep Neural Networks

> 背景/相邻基础 · 2020 · `wf_75ecf36c956baffb0e`

**作者**：Xiang Deng,  Zhongfei,  Zhang  
**原文**：https://arxiv.org/abs/2009.07988  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Lookup-VNets jointly train DNN weights W and color lookup-table parameters T through gradient descent on a task loss, with parameters combined as Theta=[W,T]. Current survey selection decision: exclude this Lookup-VNet training paper from technical synthesis for insufficient demonstrated RSI thematic connection; preserve its joint update facts and bounded feedback. Ordinary supervised training with a fixed optimizer can provide feedback; rewriting the optimizer is not required.

### 与 RSI 的具体关系

- Current survey selection decision: exclude this Lookup-VNet training paper from technical synthesis for insufficient demonstrated RSI thematic connection; preserve its joint update facts and bounded feedback. Ordinary supervised training with a fixed optimizer can provide feedback; rewriting the optimizer is not required.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `r3_abstract_review_wf_75ecf36c956baffb0e`
共同学习输入表示与神经网络权重的Lookup-VNet；联合优化不等于系统更新自身改进规则。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

### 已存角色解释 · `b570_01_role_2009_07988`
Lookup-VNets jointly train DNN weights W and color lookup-table parameters T through gradient descent on a task loss, with parameters combined as Theta=[W,T].

研究类型：未单列；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r3_abstract_ev_2009_07988`**：共同学习输入表示与神经网络权重的Lookup-VNet；联合优化不等于系统更新自身改进规则。
  - 来源版本：2009.07988v1；定位：Atom entry http://arxiv.org/abs/2009.07988v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_01_ev_2009_07988`**：Lookup-VNets jointly train DNN weights W and color lookup-table parameters T through gradient descent on a task loss, with parameters combined as Theta=[W,T].
  - 来源版本：unversioned official PDF, revision not identifiable from inspected document；定位：§III learning lookup tables, equation 5 tool L311–330；Assumptions / boundaries: §III learning lookup tables, equation 5 tool L182–191；深度：`selected_primary_scope_exclusion_supported_by_original_body`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本轮只读官方版本摘要，未核全文方法、证明、数据或性能数值；未建立与RSI的直接机制关系。保留作角色/相关性复核和术语边界，不自动进入最终引用清单。
- The inputs are parameterized color embeddings. Joint gradient-based updates of representations and weights provide bounded training feedback, and the paper also studies sharing tables across networks/tasks. The selected evidence does not establish a sufficiently explicit bridge to the current RSI Survey’s recursive or system-level capability improvement questions.
- Actual observed URL is unversioned; no revision stamp was identifiable in the selected PDF. The official identity page shows the paper and sole v1 submission, but this review does not silently substitute the PDF into an earlier exact-version claim or assert latest-version equivalence.
- The inputs are parameterized color embeddings. Joint gradient-based updates of representations and weights provide bounded training feedback, and the paper also studies sharing tables across networks/tasks. The selected evidence does not establish a sufficiently explicit bridge to the current RSI Survey’s recursive or system-level capability improvement questions.; Actual observed URL is unversioned; no revision stamp was identifiable in the selected PDF. The official identity page shows the paper and sole v1 submission, but this review does not silently substitute the PDF into an earlier exact-version claim or assert latest-version equivalence.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_01_src_2009_07988` · Deep Collective Learning: Learning Optimal Inputs and Weights Jointly in Deep Neural Networks · unversioned official PDF, revision not identifiable from inspected document
  - https://arxiv.org/pdf/2009.07988；阅读深度：`selected_primary_scope_exclusion_supported_by_original_body`。
- `r3_abstract_src_src_7a001528abaea2f3` · 已存来源 · Atom snapshot 2026-10-11 with per-entry arXiv versions
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22learned+optimizer%22+OR+ti%3A%22learning+to+learn%22+OR+ti%3A%22learning+to+optimize%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=1000&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：selected_primary_scope_exclusion_supported_by_original_body。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_75ecf36c956baffb0e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
