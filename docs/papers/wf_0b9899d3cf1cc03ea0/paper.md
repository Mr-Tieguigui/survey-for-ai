# Reachability Analysis of Self Modifying Code

> 方法论文 · 2019 · `wf_0b9899d3cf1cc03ea0`

**作者**：Tayssir Touili, Xin Ye  
**原文**：https://arxiv.org/abs/1909.12626  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Defines SM-PDS configurations as control point, stack and active transition-rule phase, including rule-replacement transitions. The malware study compares malicious-entry reachability with and without self-modifying semantics on 13 modified examples. Formal RSI verification background representing changing code rules and retained stack state for bounded executable checks, without capability-gain or universal safety claims.

### 与 RSI 的具体关系

- Formal RSI verification background representing changing code rules and retained stack state for bounded executable checks, without capability-gain or universal safety claims.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_0b9899d3cf1cc03ea0
Defines SM-PDS configurations as control point, stack and active transition-rule phase, including rule-replacement transitions. The malware study compares malicious-entry reachability with and without self-modifying semantics on 13 modified examples.

**适用版本**：arXiv:1909.12626v1；**原文定位**：Rule and configuration semantics; PDF p3; derived text lines 1-46 (one-based local extraction, not web-tool lines)；Malware reachability protocol; PDF p13; derived text lines 61-84 (one-based local extraction, not web-tool lines)；Instruction-replacement restriction; PDF p5; derived text lines 3-17 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_0b9899d3cf1cc03ea0`
以可修改转移规则的 pushdown 模型表达自修改程序并计算前后向可达配置，工具用于恶意软件检测；可作受限形式验证方法基础，不能将其模型内可达性算法泛化为任意自改系统完全验证。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

SM-PDS configuration/regular set; malware experiment checks entry reachability, Y/N for 13 examples, not broad detection accuracy.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_0b9899d3cf1cc03ea0`**：以可修改转移规则的 pushdown 模型表达自修改程序并计算前后向可达配置，工具用于恶意软件检测；可作受限形式验证方法基础，不能将其模型内可达性算法泛化为任意自改系统完全验证。
  - 来源版本：1909.12626v1；定位：Atom entry http://arxiv.org/abs/1909.12626v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_06_ev_wf_0b9899d3cf1cc03ea0`**：Defines SM-PDS configurations as control point, stack and active transition-rule phase, including rule-replacement transitions. The malware study compares malicious-entry reachability with and without self-modifying semantics on 13 modified examples.
  - 来源版本：arXiv:1909.12626v1；定位：Rule and configuration semantics; PDF p3; derived text lines 1-46 (one-based local extraction, not web-tool lines)；Malware reachability protocol; PDF p13; derived text lines 61-84 (one-based local extraction, not web-tool lines)；Instruction-replacement restriction; PDF p5; derived text lines 3-17 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Rule and configuration semantics
**来源**：https://arxiv.org/pdf/1909.12626v1  
**实际版本**：arXiv:1909.12626v1  
**精确定位**：PDF p3; derived text lines 1-46 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0b9899d3cf1cc03ea0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Malware reachability protocol
**来源**：https://arxiv.org/pdf/1909.12626v1  
**实际版本**：arXiv:1909.12626v1  
**精确定位**：PDF p13; derived text lines 61-84 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0b9899d3cf1cc03ea0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Instruction-replacement restriction
**来源**：https://arxiv.org/pdf/1909.12626v1  
**实际版本**：arXiv:1909.12626v1  
**精确定位**：PDF p5; derived text lines 3-17 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0b9899d3cf1cc03ea0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Binary translation assumes an assembly/memory oracle and same-operand-count instruction replacement; the stated case affecting subsequent instructions is unsupported. Model-specific reachability is not correctness certification of arbitrary self-rewriting AI.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_0b9899d3cf1cc03ea0` · Reachability Analysis of Self Modifying Code · arXiv:1909.12626v1
  - https://arxiv.org/pdf/1909.12626v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `s18ctx_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**仍未核准的内容**：

- Unrestricted binary rewriting and AI safety specification applicability remain unestablished.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0b9899d3cf1cc03ea0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
