# Developments in Cartesian Genetic Programming: self-modifying CGP

> 方法论文 · 2010 · `wf_2445ad9884e44b4148`

**作者**：Simon Harding, Julian F. Miller, Wolfgang Banzhaf  
**原文**：https://doi.org/10.1007/s10710-010-9114-1  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SMCGP separates evolutionary genotype search from a developmental process that copies the genotype, executes self-modification operators on phenotypes, accumulates fitness increments, and stops at an iteration bound or inactive self-modification. Relative node addressing enables moving/duplicating/deleting graph fragments and special I/O functions permit variable problem sizes. RSI-method precursor bridge: programs encode operators that change their subsequent executable phenotype, allowing repeated endogenous structural changes. Outer fitness selection and developer-chosen operators remain distinct from autonomous improvement of the optimizer.

### 与 RSI 的具体关系

- RSI-method precursor bridge: programs encode operators that change their subsequent executable phenotype, allowing repeated endogenous structural changes. Outer fitness selection and developer-chosen operators remain distinct from autonomous improvement of the optimizer.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_2445ad9884e44b4148
SMCGP separates evolutionary genotype search from a developmental process that copies the genotype, executes self-modification operators on phenotypes, accumulates fitness increments, and stops at an iteration bound or inactive self-modification. Relative node addressing enables moving/duplicating/deleting graph fragments and special I/O functions permit variable problem sizes.

**适用版本**：2010 publisher article, author-hosted copy；**原文定位**：bounded phenotype development; PDF physical page 7, derived page-text lines 3-12 (one-based local extraction, not web-tool lines)；relative addressing and dynamic I/O; PDF physical page 9, derived page-text lines 10-25 (one-based local extraction, not web-tool lines)；post-hoc proof versus theorem-prover fitness; PDF physical page 40, derived page-text lines 12-18 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Fitness aggregates increments across developed phenotypes for specified circuit, sequence and mathematical problem families. Generality proofs and reported evolutionary efficiency require separate result-level review.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_2445ad9884e44b4148`**：SMCGP separates evolutionary genotype search from a developmental process that copies the genotype, executes self-modification operators on phenotypes, accumulates fitness increments, and stops at an iteration bound or inactive self-modification. Relative node addressing enables moving/duplicating/deleting graph fragments and special I/O functions permit variable problem sizes.
  - 来源版本：2010 publisher article, author-hosted copy；定位：bounded phenotype development; PDF physical page 7, derived page-text lines 3-12 (one-based local extraction, not web-tool lines)；relative addressing and dynamic I/O; PDF physical page 9, derived page-text lines 10-25 (one-based local extraction, not web-tool lines)；post-hoc proof versus theorem-prover fitness; PDF physical page 40, derived page-text lines 12-18 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · bounded phenotype development
**来源**：https://www.cs.mun.ca/~banzhaf/papers/GPEM-SMCGP2010.pdf  
**实际版本**：2010 publisher article, author-hosted copy  
**精确定位**：PDF physical page 7, derived page-text lines 3-12 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_2445ad9884e44b4148`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · relative addressing and dynamic I/O
**来源**：https://www.cs.mun.ca/~banzhaf/papers/GPEM-SMCGP2010.pdf  
**实际版本**：2010 publisher article, author-hosted copy  
**精确定位**：PDF physical page 9, derived page-text lines 10-25 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_2445ad9884e44b4148`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · post-hoc proof versus theorem-prover fitness
**来源**：https://www.cs.mun.ca/~banzhaf/papers/GPEM-SMCGP2010.pdf  
**实际版本**：2010 publisher article, author-hosted copy  
**精确定位**：PDF physical page 40, derived page-text lines 12-18 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_2445ad9884e44b4148`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The developmental loop is bounded by configured iterations or inactivity; phenotype self-modification does not demonstrate self-improvement of the outer evolutionary algorithm. Activation mechanisms remain under investigation, and mathematical proofs are post-hoc rather than an in-loop theorem-prover fitness guarantee.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_2445ad9884e44b4148` · Developments in Cartesian Genetic Programming: self-modifying CGP · 2010 publisher article, author-hosted copy
  - https://www.cs.mun.ca/~banzhaf/papers/GPEM-SMCGP2010.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2445ad9884e44b4148 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
