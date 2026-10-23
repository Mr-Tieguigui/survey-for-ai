# Self-Modifying Cartesian Genetic Programming

> 方法论文 · 2011 · `wf_10fce309c459ee352e`

**作者**：Simon L. Harding, Julian F. Miller, Wolfgang Banzhaf  
**原文**：https://doi.org/10.1007/978-3-642-17310-3_4  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The SMCGP chapter defines phenotype development from a genotype copy, with self-modifying instructions queued in a To-Do list and applied between iterations. Fitness is accumulated across problem-family instances; self-modification operators share the evolved function representation with computational operators. RSI-method precursor bridge: evolved code changes its future phenotype and I/O structure. Neither developmental iteration counts nor fixed outer search imply recursively improving evolutionary machinery or open-ended capability growth.

### 与 RSI 的具体关系

- RSI-method precursor bridge: evolved code changes its future phenotype and I/O structure. Neither developmental iteration counts nor fixed outer search imply recursively improving evolutionary machinery or open-ended capability growth.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_10fce309c459ee352e
The SMCGP chapter defines phenotype development from a genotype copy, with self-modifying instructions queued in a To-Do list and applied between iterations. Fitness is accumulated across problem-family instances; self-modification operators share the evolved function representation with computational operators.

**适用版本**：2011 book chapter, author-hosted copy；**原文定位**：development and fitness semantics; PDF physical page 3, derived page-text lines 5-17 (one-based local extraction, not web-tool lines)；To-Do modification execution; PDF physical page 4, derived page-text lines 12-23 (one-based local extraction, not web-tool lines)；user budget and unresolved operator set; PDF physical page 4, derived page-text lines 24-33 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Phenotype fitness increments over a sequence/family, or a configured single-phenotype evaluation for single-instance problems; no uniform benchmark score across these cases is assumed.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_10fce309c459ee352e`**：The SMCGP chapter defines phenotype development from a genotype copy, with self-modifying instructions queued in a To-Do list and applied between iterations. Fitness is accumulated across problem-family instances; self-modification operators share the evolved function representation with computational operators.
  - 来源版本：2011 book chapter, author-hosted copy；定位：development and fitness semantics; PDF physical page 3, derived page-text lines 5-17 (one-based local extraction, not web-tool lines)；To-Do modification execution; PDF physical page 4, derived page-text lines 12-23 (one-based local extraction, not web-tool lines)；user budget and unresolved operator set; PDF physical page 4, derived page-text lines 24-33 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · development and fitness semantics
**来源**：https://www.cs.mun.ca/~banzhaf/papers/SMCGP_book2011.pdf  
**实际版本**：2011 book chapter, author-hosted copy  
**精确定位**：PDF physical page 3, derived page-text lines 5-17 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_10fce309c459ee352e`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · To-Do modification execution
**来源**：https://www.cs.mun.ca/~banzhaf/papers/SMCGP_book2011.pdf  
**实际版本**：2011 book chapter, author-hosted copy  
**精确定位**：PDF physical page 4, derived page-text lines 12-23 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_10fce309c459ee352e`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · user budget and unresolved operator set
**来源**：https://www.cs.mun.ca/~banzhaf/papers/SMCGP_book2011.pdf  
**实际版本**：2011 book chapter, author-hosted copy  
**精确定位**：PDF physical page 4, derived page-text lines 24-33 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_10fce309c459ee352e`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The To-Do budget is user chosen and the minimal self-modifying function set is unresolved. Numeric activation depends on comparing inputs, while Boolean functions use an implementation-specific always-active rule. This is developmental program self-modification within fixed evolutionary machinery.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_10fce309c459ee352e` · Self-Modifying Cartesian Genetic Programming · 2011 book chapter, author-hosted copy
  - https://www.cs.mun.ca/~banzhaf/papers/SMCGP_book2011.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_10fce309c459ee352e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
