# Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite

> 方法论文 · 2026 · `wf_a6717735c45164ace6`

**作者**：Zongxia Li, Yucheng Shi, Zhongzhi Li, Junyao Yang, Ruhan Wang, Chengsong Huang, Fuxiao Liu, Haitao Mi, Jordan Boyd-Graber,  LeoweiLiang  
**原文**：https://arxiv.org/abs/2610.02826  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Recursive Self-Rewrite collects same-model multi-harness successes, rewrites via planner/critic/executor in a general harness, filters leakage and trains on public histories without private guides. Model learns from its own harness-assisted experiences; this does not establish evolution of the rewriting optimizer.

### 与 RSI 的具体关系

- Model learns from its own harness-assisted experiences; this does not establish evolution of the rewriting optimizer.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_a6717735c45164ace6
Recursive Self-Rewrite collects same-model multi-harness successes, rewrites via planner/critic/executor in a general harness, filters leakage and trains on public histories without private guides.

**适用版本**：2610.02826v1；**原文定位**：Same-model stages; PDF physical page 3, derived page-text lines 41-53 (one-based local extraction, not web-tool lines)；Leak filtering and training; PDF physical page 4, derived page-text lines 8-25 (one-based local extraction, not web-tool lines)；Model-mediated screening; PDF physical page 4, derived page-text lines 8-13 (one-based local extraction, not web-tool lines)；Finite attempts and rounding; PDF physical page 11, derived page-text lines 22-26 (one-based local extraction, not web-tool lines)；Benchmark scores; PDF physical page 11, derived page-text lines 18-26 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Terminal task: pass@3 is any success in three attempts, mean is individual pass-rate average, and LHTB uses process reward. Runbooks absent from SFT/inference.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_a6717735c45164ace6`**：Recursive Self-Rewrite collects same-model multi-harness successes, rewrites via planner/critic/executor in a general harness, filters leakage and trains on public histories without private guides.
  - 来源版本：2610.02826v1；定位：Same-model stages; PDF physical page 3, derived page-text lines 41-53 (one-based local extraction, not web-tool lines)；Leak filtering and training; PDF physical page 4, derived page-text lines 8-25 (one-based local extraction, not web-tool lines)；Model-mediated screening; PDF physical page 4, derived page-text lines 8-13 (one-based local extraction, not web-tool lines)；Finite attempts and rounding; PDF physical page 11, derived page-text lines 22-26 (one-based local extraction, not web-tool lines)；Benchmark scores; PDF physical page 11, derived page-text lines 18-26 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Same-model stages
**来源**：https://arxiv.org/pdf/2610.02826v1  
**实际版本**：2610.02826v1  
**精确定位**：PDF physical page 3, derived page-text lines 41-53 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a6717735c45164ace6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Leak filtering and training
**来源**：https://arxiv.org/pdf/2610.02826v1  
**实际版本**：2610.02826v1  
**精确定位**：PDF physical page 4, derived page-text lines 8-25 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a6717735c45164ace6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Benchmark scores
**来源**：https://arxiv.org/pdf/2610.02826v1  
**实际版本**：2610.02826v1  
**精确定位**：PDF physical page 11, derived page-text lines 18-26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a6717735c45164ace6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Model-mediated screening
**来源**：https://arxiv.org/pdf/2610.02826v1  
**实际版本**：2610.02826v1  
**精确定位**：PDF physical page 4, derived page-text lines 8-13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a6717735c45164ace6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Finite attempts and rounding
**来源**：https://arxiv.org/pdf/2610.02826v1  
**实际版本**：2610.02826v1  
**精确定位**：PDF physical page 11, derived page-text lines 22-26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_a6717735c45164ace6`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Leak screens use model judgments, not a soundness guarantee. Finite attempts and rounded counts limit precision; no repeated generational training sequence is certified.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_a6717735c45164ace6` · Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite · 2610.02826v1
  - https://arxiv.org/pdf/2610.02826v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- No independent leakage audit or generational acceleration certification.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a6717735c45164ace6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
