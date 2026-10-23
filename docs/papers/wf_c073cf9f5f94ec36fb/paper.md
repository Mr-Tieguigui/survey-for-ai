# Luigi Usai Self Improving A.I. Agent: "KissMyAss"

> 方法论文 · 2026 · `wf_c073cf9f5f94ec36fb`

**作者**：Luigi Usai  
**原文**：https://doi.org/10.5281/zenodo.22099091  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
KissMyAss documentation specifies a ReAct/checkpoint loop, dynamically synthesized tools subject to AST checks/mutation tests, immutable/mutable/dynamic prompt tiers, decayed Bayesian heuristic utility, and multiobjective prompt tournaments with regression checks and rollback. Direct bounded RSI bridge: tool/prompt/heuristic changes are intended to persist and affect later task execution, while directives and regression gates stay fixed. Fixed gates do not remove adaptation; they do not prove universal safety.

### 与 RSI 的具体关系

- Direct bounded RSI bridge: tool/prompt/heuristic changes are intended to persist and affect later task execution, while directives and regression gates stay fixed. Fixed gates do not remove adaptation; they do not prove universal safety.

## 2. 论文的核心内容与贡献

### role:b570_09_role_wf_c073cf9f5f94ec36fb
KissMyAss documentation specifies a ReAct/checkpoint loop, dynamically synthesized tools subject to AST checks/mutation tests, immutable/mutable/dynamic prompt tiers, decayed Bayesian heuristic utility, and multiobjective prompt tournaments with regression checks and rollback.

**适用版本**：Zenodo 22102322；**原文定位**：tool generation, prompt tiers and heuristic utility; Document body section 1, local text lines 24-38 (one-based local extraction, not web-tool lines)；multiobjective/regression tournament and persistent telemetry; Document body section 1, local text lines 40-47 (one-based local extraction, not web-tool lines)；small documented task/mutation evidence; Document body section 1, local text lines 53-64 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Documented accuracy/token/latency/tool-error objectives, Golden-suite regression checks and tournament ratings; result tables and claimed test counts remain author-reported pending code/configuration review.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_09_ev_wf_c073cf9f5f94ec36fb`**：KissMyAss documentation specifies a ReAct/checkpoint loop, dynamically synthesized tools subject to AST checks/mutation tests, immutable/mutable/dynamic prompt tiers, decayed Bayesian heuristic utility, and multiobjective prompt tournaments with regression checks and rollback.
  - 来源版本：Zenodo 22102322；定位：tool generation, prompt tiers and heuristic utility; Document body section 1, local text lines 24-38 (one-based local extraction, not web-tool lines)；multiobjective/regression tournament and persistent telemetry; Document body section 1, local text lines 40-47 (one-based local extraction, not web-tool lines)；small documented task/mutation evidence; Document body section 1, local text lines 53-64 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · tool generation, prompt tiers and heuristic utility
**来源**：https://zenodo.org/api/records/22102322/files/self-improving-agent%20(3).tar/content  
**实际版本**：Zenodo 22102322  
**精确定位**：Document body section 1, local text lines 24-38 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c073cf9f5f94ec36fb`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · multiobjective/regression tournament and persistent telemetry
**来源**：https://zenodo.org/api/records/22102322/files/self-improving-agent%20(3).tar/content  
**实际版本**：Zenodo 22102322  
**精确定位**：Document body section 1, local text lines 40-47 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c073cf9f5f94ec36fb`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · small documented task/mutation evidence
**来源**：https://zenodo.org/api/records/22102322/files/self-improving-agent%20(3).tar/content  
**实际版本**：Zenodo 22102322  
**精确定位**：Document body section 1, local text lines 53-64 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_c073cf9f5f94ec36fb`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The reviewed evidence is official release documentation, not an executed code/proof audit. Its illustrated aggregate result covers 18 tasks and four mutation tests; headline mathematical verification, production security, zero-forgetting and broad safety claims are not established by those small documented examples.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_09_src_wf_c073cf9f5f94ec36fb` · Luigi Usai Self Improving A.I. Agent: "KissMyAss" · Zenodo 22102322
  - https://zenodo.org/api/records/22102322/files/self-improving-agent%20(3).tar/content；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Release description embeds older DOI 22099092; captured official version is 22102322. Preserve stale citation as an artifact variant, not current resolved DOI.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c073cf9f5f94ec36fb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
