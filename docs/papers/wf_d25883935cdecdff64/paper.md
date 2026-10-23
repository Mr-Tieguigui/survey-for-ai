# Self-Navigated Residual Mamba for Universal Industrial Anomaly Detection

> 方法论文 · 2025 · `wf_d25883935cdecdff64`

**作者**：Hanxi Li, Jingqi Wu, Lin Yuanbo Wu, Mingliang Li, Deyin Liu, Jialie Shen, Chunhua Shen  
**原文**：https://arxiv.org/abs/2508.01591  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SNARM selects presumed-normal patches within a test image to refine residual references and uses guided Mamba scans/multi-view decoding; evaluated for industrial anomaly detection/localization. Excluded after primary scope review: self-navigation/reference denotes patch selection and residual matching inside anomaly inference; no RSI improvement mechanism is identified.

### 与 RSI 的具体关系

- Excluded after primary scope review: self-navigation/reference denotes patch selection and residual matching inside anomaly inference; no RSI improvement mechanism is identified.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `b570_06_role_wf_d25883935cdecdff64`
SNARM selects presumed-normal patches within a test image to refine residual references and uses guided Mamba scans/multi-view decoding; evaluated for industrial anomaly detection/localization.

研究类型：Anomaly localization with self-referenced patch matching；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Image/pixel anomaly predictions on MVTec-AD/MVTec-3D/VisA; I-AUROC, P-AUROC, PRO and P-AP are detection/localization metrics.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_06_ev_wf_d25883935cdecdff64`**：SNARM selects presumed-normal patches within a test image to refine residual references and uses guided Mamba scans/multi-view decoding; evaluated for industrial anomaly detection/localization.
  - 来源版本：arXiv:2508.01591v1；定位：Residual navigator and self-reference; PDF p4; derived text lines 4-32 (one-based local extraction, not web-tool lines)；Benchmark and metrics; PDF p5; derived text lines 104-115 (one-based local extraction, not web-tool lines)；Patch normality assumption; PDF p4; derived text lines 33-48 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Residual navigator and self-reference
**来源**：https://arxiv.org/pdf/2508.01591v1  
**实际版本**：arXiv:2508.01591v1  
**精确定位**：PDF p4; derived text lines 4-32 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d25883935cdecdff64`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Benchmark and metrics
**来源**：https://arxiv.org/pdf/2508.01591v1  
**实际版本**：arXiv:2508.01591v1  
**精确定位**：PDF p5; derived text lines 104-115 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d25883935cdecdff64`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · Patch normality assumption
**来源**：https://arxiv.org/pdf/2508.01591v1  
**实际版本**：arXiv:2508.01591v1  
**精确定位**：PDF p4; derived text lines 33-48 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_d25883935cdecdff64`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Intra-image matching assumes low-waypoint-score patches are normal. This task-specific reference assumption is not autonomous validation of an improved system or recursive detector modification.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_d25883935cdecdff64` · Self-Navigated Residual Mamba for Universal Industrial Anomaly Detection · arXiv:2508.01591v1
  - https://arxiv.org/pdf/2508.01591v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d25883935cdecdff64 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
