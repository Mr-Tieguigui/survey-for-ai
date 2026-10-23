# SPECTRUM: Proximal Spectral Modulation for Looped Self-Distillation

> 方法论文 · 2026 · `wf_ccb22c274c5969aedf`

**作者**：Yunbo Long, WenJie Chen, Jiaquan Zhang, Guangya Hao, Zihang Zeng, Pengze Li, Xi Chen  
**原文**：https://arxiv.org/abs/2610.07237  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SPECTRUM recalibrates K/V geometry from fixed anchors, temporarily modulates generation, restores native weights and trains on all raw completions; merged student starts next round. Looped distillation carries weights into later data generation under fixed information budget, supporting bounded retention analysis.

### 与 RSI 的具体关系

- Looped distillation carries weights into later data generation under fixed information budget, supporting bounded retention analysis.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_ccb22c274c5969aedf
SPECTRUM recalibrates K/V geometry from fixed anchors, temporarily modulates generation, restores native weights and trains on all raw completions; merged student starts next round.

**适用版本**：2610.07237v1；**原文定位**：Fixed-anchor geometry; PDF physical page 3, derived page-text lines 48-58 (one-based local extraction, not web-tool lines)；Student succession; PDF physical page 4, derived page-text lines 1-24 (one-based local extraction, not web-tool lines)；AST and finite-check limits; PDF physical page 9, derived page-text lines 21-29 (one-based local extraction, not web-tool lines)；Single-run scope; PDF physical page 5, derived page-text lines 48-59 (one-based local extraction, not web-tool lines)；Round protocol; PDF physical page 5, derived page-text lines 48-59 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

MBPP tasks/completions with disjoint synthesis/calibration/validation/evaluation sets. 16 samples each round and separate final 64 pools; pass@k, richness Ck and Db contrasts differ.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_ccb22c274c5969aedf`**：SPECTRUM recalibrates K/V geometry from fixed anchors, temporarily modulates generation, restores native weights and trains on all raw completions; merged student starts next round.
  - 来源版本：2610.07237v1；定位：Fixed-anchor geometry; PDF physical page 3, derived page-text lines 48-58 (one-based local extraction, not web-tool lines)；Student succession; PDF physical page 4, derived page-text lines 1-24 (one-based local extraction, not web-tool lines)；AST and finite-check limits; PDF physical page 9, derived page-text lines 21-29 (one-based local extraction, not web-tool lines)；Single-run scope; PDF physical page 5, derived page-text lines 48-59 (one-based local extraction, not web-tool lines)；Round protocol; PDF physical page 5, derived page-text lines 48-59 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Fixed-anchor geometry
**来源**：https://arxiv.org/pdf/2610.07237v1  
**实际版本**：2610.07237v1  
**精确定位**：PDF physical page 3, derived page-text lines 48-58 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_ccb22c274c5969aedf`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Student succession
**来源**：https://arxiv.org/pdf/2610.07237v1  
**实际版本**：2610.07237v1  
**精确定位**：PDF physical page 4, derived page-text lines 1-24 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_ccb22c274c5969aedf`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Round protocol
**来源**：https://arxiv.org/pdf/2610.07237v1  
**实际版本**：2610.07237v1  
**精确定位**：PDF physical page 5, derived page-text lines 48-59 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_ccb22c274c5969aedf`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · AST and finite-check limits
**来源**：https://arxiv.org/pdf/2610.07237v1  
**实际版本**：2610.07237v1  
**精确定位**：PDF physical page 9, derived page-text lines 21-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_ccb22c274c5969aedf`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Five-round MBPP study has one training run; task bootstraps do not measure training variation. AST richness is not semantic algorithm identity; finite tests/samples miss invalid/rare behavior.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_ccb22c274c5969aedf` · SPECTRUM: Proximal Spectral Modulation for Looped Self-Distillation · 2610.07237v1
  - https://arxiv.org/pdf/2610.07237v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No independent training-repeat or semantic-diversity certification.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ccb22c274c5969aedf --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
