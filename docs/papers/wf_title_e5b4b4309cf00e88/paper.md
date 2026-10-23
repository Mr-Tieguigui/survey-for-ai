# LTL model checking of self modifying code

> 背景/相邻基础 · 2022 · `wf_title_e5b4b4309cf00e88`

**作者**：Tayssir Touili, Xin Ye  
**原文**：https://doi.org/10.1007/s10703-022-00394-8  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The paper models executable self-modifying code as self-modifying pushdown systems and checks LTL properties so malware behaviors hidden by code rewriting remain reachable in the analysis.

### 与 RSI 的具体关系

- Excluded from RSI technical evidence after primary-body review; retained as a boundary case for low-level code self-modification and verification.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `b570_9_role_wf_title_e5b4b4309cf00e88`
The paper models executable self-modifying code as self-modifying pushdown systems and checks LTL properties so malware behaviors hidden by code rewriting remain reachable in the analysis.

研究类型：self_modifying_code_model_checking；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_9_ev_wf_title_e5b4b4309cf00e88`**：The paper models executable self-modifying code as self-modifying pushdown systems and checks LTL properties so malware behaviors hidden by code rewriting remain reachable in the analysis.
  - 来源版本：captured source; no latest-version assertion；定位：PDF physical page 4, derived page-text lines 29-34 (one-based local extraction, not web-tool lines)；PDF physical page 26, derived page-text lines 7-12 (one-based local extraction, not web-tool lines)；PDF physical page 4, derived page-text lines 8-13 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://arxiv.org/pdf/1909.12635  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：PDF physical page 4, derived page-text lines 29-34 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_9_ev_wf_title_e5b4b4309cf00e88`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://arxiv.org/pdf/1909.12635  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：PDF physical page 26, derived page-text lines 7-12 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_9_ev_wf_title_e5b4b4309cf00e88`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · selected material-limit or boundary passage
**来源**：https://arxiv.org/pdf/1909.12635  
**实际版本**：captured source; no latest-version assertion  
**精确定位**：PDF physical page 4, derived page-text lines 8-13 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_9_ev_wf_title_e5b4b4309cf00e88`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The contribution analyzes externally given code and malware semantics; it does not describe an AI that evaluates, adopts, and retains improved successors. The comparison also notes limits of related analyses rather than RSI evidence.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_9_src_wf_title_e5b4b4309cf00e88` · LTL model checking of self modifying code · captured source; no latest-version assertion
  - https://arxiv.org/pdf/1909.12635；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Numerical, configuration and relationship claims require separate evidence review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_role_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_e5b4b4309cf00e88 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
