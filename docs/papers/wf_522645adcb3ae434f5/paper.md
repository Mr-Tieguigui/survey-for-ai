# Learning to Plan and Realize Separately for Open-Ended Dialogue Systems

> 背景/相邻基础 · 2020 · `wf_522645adcb3ae434f5`

**作者**：Sashank Santhanam, Zhuo Cheng, Brodie Mather, Bonnie Dorr, Archna Bhatia, Bryanna Hebenstreit, Alan Zemel, Adam Dalton, Tomek Strzalkowski, Samira Shaikh  
**原文**：https://arxiv.org/abs/2009.12506  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The dialogue system separately trains a response planner and a surface realizer; symbolic ask/framing labels provide silver supervision and GPT-2-based models generate plans and responses. Current survey selection decision: exclude this dialogue-generation paper from technical synthesis for insufficient demonstrated RSI thematic connection; retain its method facts and bounded training feedback. Separate supervised training and fixed optimizers can provide feedback without optimizer rewriting.

### 与 RSI 的具体关系

- Current survey selection decision: exclude this dialogue-generation paper from technical synthesis for insufficient demonstrated RSI thematic connection; retain its method facts and bounded training feedback. Separate supervised training and fixed optimizers can provide feedback without optimizer rewriting.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `r3_abstract_review_wf_522645adcb3ae434f5`
把开放对话生成拆成规划与实现两阶段；生成任务流程分解不表示改进器自改。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

### 已存角色解释 · `b570_01_role_2009_12506`
The dialogue system separately trains a response planner and a surface realizer; symbolic ask/framing labels provide silver supervision and GPT-2-based models generate plans and responses.

研究类型：未单列；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r3_abstract_ev_2009_12506`**：把开放对话生成拆成规划与实现两阶段；生成任务流程分解不表示改进器自改。
  - 来源版本：2009.12506v2；定位：Atom entry http://arxiv.org/abs/2009.12506v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_01_ev_2009_12506`**：The dialogue system separately trains a response planner and a surface realizer; symbolic ask/framing labels provide silver supervision and GPT-2-based models generate plans and responses.
  - 来源版本：2009.12506v2；定位：§3.2 method: symbolic/supervised planning and realization tool L75–85；Assumptions / boundaries: §3.2 method: symbolic/supervised planning and realization tool L104–110；深度：`selected_primary_scope_exclusion_supported_by_original_body`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本轮只读官方版本摘要，未核全文方法、证明、数据或性能数值；未建立与RSI的直接机制关系。保留作角色/相关性复核和术语边界，不自动进入最终引用清单。
- Both components are trained separately for the dialogue task, with bounded training feedback; the paper notes imperfect automatic silver annotations. The selected planning/realization passages do not establish a sufficiently explicit bridge to the current RSI Survey’s recursive or system-level capability improvement questions.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_01_src_2009_12506` · Learning to Plan and Realize Separately for Open-Ended Dialogue Systems · 2009.12506v2
  - https://arxiv.org/html/2009.12506v2；阅读深度：`selected_primary_scope_exclusion_supported_by_original_body`。
- `r3_abstract_src_src_d45253343eca569f` · 已存来源 · Atom snapshot 2026-10-11 with per-entry arXiv versions
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22open-ended%22+AND+%28all%3Alearning+OR+all%3Aagent+OR+all%3Aevolution%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=200&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：selected_primary_scope_exclusion_supported_by_original_body。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_522645adcb3ae434f5 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
