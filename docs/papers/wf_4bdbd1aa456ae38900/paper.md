# Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver

> Benchmark/数据集/任务套件 · 2026 · `wf_4bdbd1aa456ae38900`

**作者**：Joshua Sherwood, Ben Aybar, Benjamin Kaplan  
**原文**：https://arxiv.org/abs/2604.25067  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
This proof-of-concept gives coding agents three hours and one consumer GPU to implement an AlphaZero-style Connect Four self-play pipeline. Main evaluation uses eight trials per agent (32), plus 16 exploratory GPT probe trials. A fixed 49-player round robin includes Pascal Pons, with Bradley–Terry ratings and solver-relative outcomes; four of eight Opus 4.7 trials match or exceed the anchored rating. Measures AI-building-AI and bounded self-play learning prerequisites; not multi-generation recursive improvement of the coding agent.

### 与 RSI 的具体关系

- Measures AI-building-AI and bounded self-play learning prerequisites; not multi-generation recursive improvement of the coding agent.

## 2. 论文的核心内容与贡献

### role:b570_03_role_wf_4bdbd1aa456ae38900
This proof-of-concept gives coding agents three hours and one consumer GPU to implement an AlphaZero-style Connect Four self-play pipeline. Main evaluation uses eight trials per agent (32), plus 16 exploratory GPT probe trials. A fixed 49-player round robin includes Pascal Pons, with Bradley–Terry ratings and solver-relative outcomes; four of eight Opus 4.7 trials match or exceed the anchored rating.

**适用版本**：2604.25067v1；**原文定位**：§2 Task implementation and specification; PDF p4; derived page text lines 1–30 (one-based local extraction, not web-tool lines)；§4 Tournament and rating; PDF p8; derived page text lines 10–49 (one-based local extraction, not web-tool lines)；§5.1 Main evaluation; PDF p10; derived page text lines 9–23 (one-based local extraction, not web-tool lines)；§7.2–7.3 Results boundary and limitations; PDF p20; derived page text lines 28–46 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_03_ev_wf_4bdbd1aa456ae38900`**：This proof-of-concept gives coding agents three hours and one consumer GPU to implement an AlphaZero-style Connect Four self-play pipeline. Main evaluation uses eight trials per agent (32), plus 16 exploratory GPT probe trials. A fixed 49-player round robin includes Pascal Pons, with Bradley–Terry ratings and solver-relative outcomes; four of eight Opus 4.7 trials match or exceed the anchored rating.
  - 来源版本：2604.25067v1；定位：§2 Task implementation and specification; PDF p4; derived page text lines 1–30 (one-based local extraction, not web-tool lines)；§4 Tournament and rating; PDF p8; derived page text lines 10–49 (one-based local extraction, not web-tool lines)；§5.1 Main evaluation; PDF p10; derived page text lines 9–23 (one-based local extraction, not web-tool lines)；§7.2–7.3 Results boundary and limitations; PDF p20; derived page text lines 28–46 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2 Task implementation and specification
**来源**：https://arxiv.org/pdf/2604.25067v1  
**实际版本**：2604.25067v1  
**精确定位**：PDF p4; derived page text lines 1–30 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_4bdbd1aa456ae38900`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §4 Tournament and rating
**来源**：https://arxiv.org/pdf/2604.25067v1  
**实际版本**：2604.25067v1  
**精确定位**：PDF p8; derived page text lines 10–49 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_4bdbd1aa456ae38900`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 机制 / 定义 · §5.1 Main evaluation
**来源**：https://arxiv.org/pdf/2604.25067v1  
**实际版本**：2604.25067v1  
**精确定位**：PDF p10; derived page text lines 9–23 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_4bdbd1aa456ae38900`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · §7.2–7.3 Results boundary and limitations
**来源**：https://arxiv.org/pdf/2604.25067v1  
**实际版本**：2604.25067v1  
**精确定位**：PDF p20; derived page text lines 28–46 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_03_ev_wf_4bdbd1aa456ae38900`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- One task and small groups limit generalization. Higher tournament rating can reflect exploiting imperfect opponents and is not outperforming perfect optimal play. Sandbagging evidence is inconclusive; prompt/sandbox differences may confound comparisons. Agents have no trial-persistent memory and are not shown recursively improving their development mechanism.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_03_src_wf_4bdbd1aa456ae38900` · Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver · 2604.25067v1
  - https://arxiv.org/pdf/2604.25067v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4bdbd1aa456ae38900 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
