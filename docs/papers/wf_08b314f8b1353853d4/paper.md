# Universal Behavioral Manifold 2 (UBM2): A Lie-Algebraic Framework for Activation-Space Geometry and Cross-Architecture Steering in Large Language Models

> 方法论文 · 2026 · `wf_08b314f8b1353853d4`

**作者**：Logan Matthew Napolitano  
**原文**：https://doi.org/10.5281/zenodo.20214773  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
UBM2 describes a frozen-model activation-hook loop in which the steered model generates and evaluates candidate responses and updates a small steering matrix. Candidate geometry/step sizes pass an internally defined behavioral gate; reported accepted iterations are distinct from attempted iterations. Direct bounded RSI bridge: current steering modifies the system producing/evaluating updates to later steering. Frozen backbone weights do not negate that feedback, but this does not establish global convergence or an indefinitely improving learner.

### 与 RSI 的具体关系

- Direct bounded RSI bridge: current steering modifies the system producing/evaluating updates to later steering. Frozen backbone weights do not negate that feedback, but this does not establish global convergence or an indefinitely improving learner.

## 2. 论文的核心内容与贡献

### role:b570_10_role_wf_08b314f8b1353853d4
UBM2 describes a frozen-model activation-hook loop in which the steered model generates and evaluates candidate responses and updates a small steering matrix. Candidate geometry/step sizes pass an internally defined behavioral gate; reported accepted iterations are distinct from attempted iterations.

**适用版本**：Zenodo 20214774；**原文定位**：activation-geometry target with frozen weights; PDF physical page 26, derived page-text lines 30-40 (one-based local extraction, not web-tool lines)；steered model updates steering; PDF physical page 27, derived page-text lines 10-13 (one-based local extraction, not web-tool lines)；two accepted steps and internal-metric boundary; PDF physical page 28, derived page-text lines 19-31 (one-based local extraction, not web-tool lines)；p-value/percentile equivalence assertion; PDF physical page 27, derived page-text lines 14-18 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Internal C/composite behavioral scores and a percentile admission rule on prompts; a percentile rule is not independently certified as a statistical significance test.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_10_ev_wf_08b314f8b1353853d4`**：UBM2 describes a frozen-model activation-hook loop in which the steered model generates and evaluates candidate responses and updates a small steering matrix. Candidate geometry/step sizes pass an internally defined behavioral gate; reported accepted iterations are distinct from attempted iterations.
  - 来源版本：Zenodo 20214774；定位：activation-geometry target with frozen weights; PDF physical page 26, derived page-text lines 30-40 (one-based local extraction, not web-tool lines)；steered model updates steering; PDF physical page 27, derived page-text lines 10-13 (one-based local extraction, not web-tool lines)；two accepted steps and internal-metric boundary; PDF physical page 28, derived page-text lines 19-31 (one-based local extraction, not web-tool lines)；p-value/percentile equivalence assertion; PDF physical page 27, derived page-text lines 14-18 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · activation-geometry target with frozen weights
**来源**：https://zenodo.org/api/records/20214774/files/CYGNUS_UBM2_PAPER.pdf/content  
**实际版本**：Zenodo 20214774  
**精确定位**：PDF physical page 26, derived page-text lines 30-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_08b314f8b1353853d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · steered model updates steering
**来源**：https://zenodo.org/api/records/20214774/files/CYGNUS_UBM2_PAPER.pdf/content  
**实际版本**：Zenodo 20214774  
**精确定位**：PDF physical page 27, derived page-text lines 10-13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_08b314f8b1353853d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · two accepted steps and internal-metric boundary
**来源**：https://zenodo.org/api/records/20214774/files/CYGNUS_UBM2_PAPER.pdf/content  
**实际版本**：Zenodo 20214774  
**精确定位**：PDF physical page 28, derived page-text lines 19-31 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_08b314f8b1353853d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 冲突 · p-value/percentile equivalence assertion
**来源**：https://zenodo.org/api/records/20214774/files/CYGNUS_UBM2_PAPER.pdf/content  
**实际版本**：Zenodo 20214774  
**精确定位**：PDF physical page 27, derived page-text lines 14-18 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_10_ev_wf_08b314f8b1353853d4`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The paper reports only two accepted changes in seven trials and uses internal behavioral metrics rather than downstream benchmarks. Its statement equating p<0.05 with an 85th-percentile threshold lacks a supplied calibration establishing that equivalence; significance, performance magnitudes and portable Lie-algebraic guarantees remain pending.

存在已存冲突或待核证据；请保留各版本和判断，不自行合并为确定结论：

- b570_10_ev_wf_08b314f8b1353853d4

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_10_src_wf_08b314f8b1353853d4` · Universal Behavioral Manifold 2 (UBM2): A Lie-Algebraic Framework for Activation-Space Geometry and Cross-Architecture Steering in Large Language Models · Zenodo 20214774
  - https://zenodo.org/api/records/20214774/files/CYGNUS_UBM2_PAPER.pdf/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Gate statistical calibration and claimed gains remain unresolved; embedded old DOI 18471775 is retained as an artifact identifier, not substituted for resolved Zenodo record.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_08b314f8b1353853d4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
