# Language Models as AI Research World Models

> 方法论文 · 2026 · `wf_227a69c0cf0910a3b1`

**作者**：Zijun Wang, Zewen Liu, Minhua Lin, Zhaotian Weng, Zhan Shi, Bing He, Yisi Sang, Dakuo Wang, Benoit Dumoulin, Wei Jin, Yuyin Zhou, Cihang Xie, Hanqing Lu  
**原文**：https://arxiv.org/abs/2610.12235  
**研究分支**：科研代理、实验与发现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
RWM keeps LLM parameters fixed and conditions forecasts on serialized experiment histories. Fixed-reference environments supply intervention gains; matched multi-round Autoresearch compares selection under identical candidate arrivals/budgets. Direct AI4AI foundation using retained experimental evidence for subsequent selection. History changes context while reference models and LLM weights stay fixed; rounds are not accepted inherited self-modifications.

### 与 RSI 的具体关系

- Direct AI4AI foundation using retained experimental evidence for subsequent selection. History changes context while reference models and LLM weights stay fixed; rounds are not accepted inherited self-modifications.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_227a69c0cf0910a3b1
RWM keeps LLM parameters fixed and conditions forecasts on serialized experiment histories. Fixed-reference environments supply intervention gains; matched multi-round Autoresearch compares selection under identical candidate arrivals/budgets.

**适用版本**：arXiv:2610.12235v1；**原文定位**：Fixed-weight in-context experience; PDF p4; derived text lines 1-38 (one-based local extraction, not web-tool lines)；Matched multi-round protocol; PDF p7; derived text lines 29-45 (one-based local extraction, not web-tool lines)；Transfer/total-cost limits; PDF p9; derived text lines 33-44 (one-based local extraction, not web-tool lines)；Fixed-reference gain units; PDF p3; derived text lines 24-50 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Intervention/outcome record with BPB, accuracy-pp or tokens/s gain; five runs/eight rounds, 16 new candidates/round, three selections/round (24 total). Final best gain and oracle-normalized AULC.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_06_ev_wf_227a69c0cf0910a3b1`**：RWM keeps LLM parameters fixed and conditions forecasts on serialized experiment histories. Fixed-reference environments supply intervention gains; matched multi-round Autoresearch compares selection under identical candidate arrivals/budgets.
  - 来源版本：arXiv:2610.12235v1；定位：Fixed-weight in-context experience; PDF p4; derived text lines 1-38 (one-based local extraction, not web-tool lines)；Matched multi-round protocol; PDF p7; derived text lines 29-45 (one-based local extraction, not web-tool lines)；Transfer/total-cost limits; PDF p9; derived text lines 33-44 (one-based local extraction, not web-tool lines)；Fixed-reference gain units; PDF p3; derived text lines 24-50 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Fixed-weight in-context experience
**来源**：https://arxiv.org/pdf/2610.12235v1  
**实际版本**：arXiv:2610.12235v1  
**精确定位**：PDF p4; derived text lines 1-38 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_227a69c0cf0910a3b1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Matched multi-round protocol
**来源**：https://arxiv.org/pdf/2610.12235v1  
**实际版本**：arXiv:2610.12235v1  
**精确定位**：PDF p7; derived text lines 29-45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_227a69c0cf0910a3b1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Fixed-reference gain units
**来源**：https://arxiv.org/pdf/2610.12235v1  
**实际版本**：arXiv:2610.12235v1  
**精确定位**：PDF p3; derived text lines 24-50 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_227a69c0cf0910a3b1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Transfer/total-cost limits
**来源**：https://arxiv.org/pdf/2610.12235v1  
**实际版本**：arXiv:2610.12235v1  
**精确定位**：PDF p9; derived text lines 33-44 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_227a69c0cf0910a3b1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Cross-environment evidence is limited to autoregressive pretraining. Better forecasts alone do not guarantee better research; sustained use needs total acquisition/inference/execution cost and unseen-environment tests.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_06_src_wf_227a69c0cf0910a3b1` · Language Models as AI Research World Models · arXiv:2610.12235v1
  - https://arxiv.org/pdf/2610.12235v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Forecast/selection tests do not establish autonomous research closure or recursive RWM redesign.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_227a69c0cf0910a3b1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
