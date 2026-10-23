# Personality Editing for Language Models through Adjusting Self-Referential Queries

> 方法论文 · 2025 · `wf_8154bda2f6d3efd7c9`

**作者**：Seojin Hwang, Yumin Kim, Byeongjeong Kim, Donghoon Shin, Hwanhee Lee  
**原文**：https://arxiv.org/abs/2502.11789  
**研究分支**：其他应用与相邻接口  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Personality Editing for Language Models through Relevant Knowledge Editing。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
PALETTE constructs MBTI adjustment queries and applies r-ROME rank-one weight changes to shift trait responses; evaluates alignment and trait ratios with model/human comparisons. Excluded after primary scope review: externally specified opposite personality traits and self-referential I/me statements do not provide an RSI technical bridge.

### 与 RSI 的具体关系

- Excluded after primary scope review: externally specified opposite personality traits and self-referential I/me statements do not provide an RSI technical bridge.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `s18_role_review_wf_8154bda2f6d3efd7c9`
PALETTE 将心理学自指陈述当作可编辑知识以控制语言模型人格；所编辑的是人格响应，摘要没有评价反馈驱动的递归自改链，不能仅按 self-referential 纳入核心方法。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

### 已存角色解释 · `b570_06_role_wf_8154bda2f6d3efd7c9`
PALETTE constructs MBTI adjustment queries and applies r-ROME rank-one weight changes to shift trait responses; evaluates alignment and trait ratios with model/human comparisons.

研究类型：Externally targeted personality editing with r-ROME；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Trait query/response; pairwise alignment and T/F response proportions, with GPT-4o and human agreement checks. Trait-ratio change is not a general improvement score.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_8154bda2f6d3efd7c9`**：PALETTE 将心理学自指陈述当作可编辑知识以控制语言模型人格；所编辑的是人格响应，摘要没有评价反馈驱动的递归自改链，不能仅按 self-referential 纳入核心方法。
  - 来源版本：2502.11789v4；定位：Atom entry http://arxiv.org/abs/2502.11789v4；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_8154bda2f6d3efd7c9`**：PALETTE constructs MBTI adjustment queries and applies r-ROME rank-one weight changes to shift trait responses; evaluates alignment and trait ratios with model/human comparisons.
  - 来源版本：arXiv:2502.11789v1；定位：Rank-one trait editing; PDF p2; derived text lines 28-71 (one-based local extraction, not web-tool lines)；Query and personality evaluation protocol; PDF p3; derived text lines 61-96 (one-based local extraction, not web-tool lines)；Computation limitation; PDF p5; derived text lines 1-13 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Rank-one trait editing
**来源**：https://arxiv.org/pdf/2502.11789v1  
**实际版本**：arXiv:2502.11789v1  
**精确定位**：PDF p2; derived text lines 28-71 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_8154bda2f6d3efd7c9`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Query and personality evaluation protocol
**来源**：https://arxiv.org/pdf/2502.11789v1  
**实际版本**：arXiv:2502.11789v1  
**精确定位**：PDF p3; derived text lines 61-96 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_8154bda2f6d3efd7c9`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Computation limitation
**来源**：https://arxiv.org/pdf/2502.11789v1  
**实际版本**：arXiv:2502.11789v1  
**精确定位**：PDF p5; derived text lines 1-13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_8154bda2f6d3efd7c9`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- Query construction/internal representation edits add computation. Desired trait control does not demonstrate improved general capability or a feedback loop redesigning its updater.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_8154bda2f6d3efd7c9` · Personality Editing for Language Models through Relevant Knowledge Editing · arXiv:2502.11789v1
  - https://arxiv.org/pdf/2502.11789v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8154bda2f6d3efd7c9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
