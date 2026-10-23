# Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

> 方法论文 · 2026 · `wf_e47daf7dae3d9497d8`

**作者**：Bingjun Luo, Jialin Guo, Siqi Li  
**原文**：https://arxiv.org/abs/2609.37950  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Video-RSI uses fixed models to investigate video-agent failures, revise reusable executable harness code, and retain candidates through a private performance-cost gate. The gate allows either accuracy gain with bounded frame growth or sufficiently lower frame cost with bounded accuracy loss; only retained harnesses seed later attempts. Direct bounded RSI through persistent executable harness changes with frozen Solver/Editor weights; fixed services do not remove feedback or selection.

### 与 RSI 的具体关系

- Direct bounded RSI through persistent executable harness changes with frozen Solver/Editor weights; fixed services do not remove feedback or selection.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_e47daf7dae3d9497d8
Video-RSI uses fixed models to investigate video-agent failures, revise reusable executable harness code, and retain candidates through a private performance-cost gate. The gate allows either accuracy gain with bounded frame growth or sufficiently lower frame cost with bounded accuracy loss; only retained harnesses seed later attempts.

**适用版本**：2609.37950v1；**原文定位**：evolving harness with fixed models; PDF physical page 4, derived page-text lines 33-36 (one-based local extraction, not web-tool lines)；matched private gate; PDF physical page 5, derived page-text lines 36-40 (one-based local extraction, not web-tool lines)；attempt budget and acceptance directions; PDF physical page 6, derived page-text lines 31-35 (one-based local extraction, not web-tool lines)；visual cost excludes offline editor work; PDF physical page 6, derived page-text lines 45-47 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Multiple-choice accuracy and mean visual frames per full question execution; same private gate examples and matched conditions compare incumbent/candidate. Final accepted harness is frozen for held-out evaluation.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_e47daf7dae3d9497d8`**：Video-RSI uses fixed models to investigate video-agent failures, revise reusable executable harness code, and retain candidates through a private performance-cost gate. The gate allows either accuracy gain with bounded frame growth or sufficiently lower frame cost with bounded accuracy loss; only retained harnesses seed later attempts.
  - 来源版本：2609.37950v1；定位：evolving harness with fixed models; PDF physical page 4, derived page-text lines 33-36 (one-based local extraction, not web-tool lines)；matched private gate; PDF physical page 5, derived page-text lines 36-40 (one-based local extraction, not web-tool lines)；attempt budget and acceptance directions; PDF physical page 6, derived page-text lines 31-35 (one-based local extraction, not web-tool lines)；visual cost excludes offline editor work; PDF physical page 6, derived page-text lines 45-47 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · evolving harness with fixed models
**来源**：https://arxiv.org/pdf/2609.37950v1  
**实际版本**：2609.37950v1  
**精确定位**：PDF physical page 4, derived page-text lines 33-36 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e47daf7dae3d9497d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · matched private gate
**来源**：https://arxiv.org/pdf/2609.37950v1  
**实际版本**：2609.37950v1  
**精确定位**：PDF physical page 5, derived page-text lines 36-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e47daf7dae3d9497d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · attempt budget and acceptance directions
**来源**：https://arxiv.org/pdf/2609.37950v1  
**实际版本**：2609.37950v1  
**精确定位**：PDF physical page 6, derived page-text lines 31-35 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e47daf7dae3d9497d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · visual cost excludes offline editor work
**来源**：https://arxiv.org/pdf/2609.37950v1  
**实际版本**：2609.37950v1  
**精确定位**：PDF physical page 6, derived page-text lines 45-47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_e47daf7dae3d9497d8`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- An evolution attempt is not an accepted revision. The visual-cost metric counts frames from successful Solver visual calls; offline Editor observations are excluded, so reduced frame use is not an end-to-end optimization-cost or wall-clock acceleration result. Gate data and per-item outcomes stay private, while aggregate feedback is returned.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_e47daf7dae3d9497d8` · Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution · 2609.37950v1
  - https://arxiv.org/pdf/2609.37950v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e47daf7dae3d9497d8 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
