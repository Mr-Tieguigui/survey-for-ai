# PhysEvo: Astra Can Act, Let It

> 方法论文 · 2026 · `wf_7cdcb539a6f2ae8941`

**作者**：Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu, Liang Wang  
**原文**：https://arxiv.org/abs/2610.08995  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
PhysEvo uses one frozen model to act and revise task and diagnostic harnesses. Development tests support between-episode adoption; inherited diagnostic tools affect later improvement rounds. Direct physical RSI: meta-harness changes affect later diagnosis/revision. Model weights, robot dynamics and evaluator stay fixed.

### 与 RSI 的具体关系

- Direct physical RSI: meta-harness changes affect later diagnosis/revision. Model weights, robot dynamics and evaluator stay fixed.

## 2. 论文的核心内容与贡献

### role:b570_07_role_wf_7cdcb539a6f2ae8941
PhysEvo uses one frozen model to act and revise task and diagnostic harnesses. Development tests support between-episode adoption; inherited diagnostic tools affect later improvement rounds.

**适用版本**：2610.08995v1；**原文定位**：Two harnesses; HTML local derived paragraphs 21-26 (one-based local extraction, not web-tool lines)；Revision and recursive reuse; HTML local derived paragraphs 30-33 (one-based local extraction, not web-tool lines)；Fixed scored versions; HTML local derived paragraphs 49-51 (one-based local extraction, not web-tool lines)；Units and weighting; HTML local derived paragraphs 45-51 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

42 RoboDojo tasks, five held-out layouts each; score 0-100, success requires 100. Headline weights dimensions equally; equal-task average is separate. Development compares same task/initial scene.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_07_ev_wf_7cdcb539a6f2ae8941`**：PhysEvo uses one frozen model to act and revise task and diagnostic harnesses. Development tests support between-episode adoption; inherited diagnostic tools affect later improvement rounds.
  - 来源版本：2610.08995v1；定位：Two harnesses; HTML local derived paragraphs 21-26 (one-based local extraction, not web-tool lines)；Revision and recursive reuse; HTML local derived paragraphs 30-33 (one-based local extraction, not web-tool lines)；Fixed scored versions; HTML local derived paragraphs 49-51 (one-based local extraction, not web-tool lines)；Units and weighting; HTML local derived paragraphs 45-51 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Two harnesses
**来源**：https://arxiv.org/html/2610.08995v1  
**实际版本**：2610.08995v1  
**精确定位**：HTML local derived paragraphs 21-26 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7cdcb539a6f2ae8941`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Revision and recursive reuse
**来源**：https://arxiv.org/html/2610.08995v1  
**实际版本**：2610.08995v1  
**精确定位**：HTML local derived paragraphs 30-33 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7cdcb539a6f2ae8941`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · Units and weighting
**来源**：https://arxiv.org/html/2610.08995v1  
**实际版本**：2610.08995v1  
**精确定位**：HTML local derived paragraphs 45-51 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7cdcb539a6f2ae8941`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · Fixed scored versions
**来源**：https://arxiv.org/html/2610.08995v1  
**实际版本**：2610.08995v1  
**精确定位**：HTML local derived paragraphs 49-51 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_07_ev_wf_7cdcb539a6f2ae8941`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Held-out simulation layouts score retained fixed versions with persistent tools/skills unchanged. Real-hardware adaptation is a separate case series, not the same held-out protocol or broad deployment validation.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_07_src_wf_7cdcb539a6f2ae8941` · PhysEvo: Astra Can Act, Let It · 2610.08995v1
  - https://arxiv.org/html/2610.08995v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Version-specific official HTML recovered once after PDF size cap; no latest-version claim.
- All outcomes remain author reports.
- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7cdcb539a6f2ae8941 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
