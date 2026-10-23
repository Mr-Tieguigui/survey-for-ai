# Developing self-modifying code model

> 方法论文 · 2016 · `wf_6ffda5354e277da0a0`

**作者**：Goran Đurić, Časlav Mitrović, Goran Vorotović, Ivan Blagojević, Miloš Vasić  
**原文**：https://doi.org/10.5937/jaes14-10931  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Movens proposes a coupled intelligent-development/executable-software system that repeats design, implementation and evaluation. Its TORCS demonstration uses genetic programming to generate controller programs, with a separate C# application controlling evolution and external compiling/testing; nested logical, implementation and parameter modification are the broader model. Historical bounded RSI bridge: evaluation feeds repeated generation of executable controller code inside a tightly coupled development/runtime system. The broader multi-level model must be distinguished from the actual fixed GP demonstration.

### 与 RSI 的具体关系

- Historical bounded RSI bridge: evaluation feeds repeated generation of executable controller code inside a tightly coupled development/runtime system. The broader multi-level model must be distinguished from the actual fixed GP demonstration.

## 2. 论文的核心内容与贡献

### role:b570_08_role_wf_6ffda5354e277da0a0
Movens proposes a coupled intelligent-development/executable-software system that repeats design, implementation and evaluation. Its TORCS demonstration uses genetic programming to generate controller programs, with a separate C# application controlling evolution and external compiling/testing; nested logical, implementation and parameter modification are the broader model.

**适用版本**：Journal of Applied Engineering Science 14(2016)2；**原文定位**：coupled redesign model; PDF physical page 2, derived page-text lines 50-64 (one-based local extraction, not web-tool lines)；automated external compile/test control; PDF physical page 7, derived page-text lines 18-28 (one-based local extraction, not web-tool lines)；compilation/simulation compute cost; PDF physical page 8, derived page-text lines 121-133 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

TORCS e-track-4 controller traversal time supplies fitness; the reported controller/evolution numbers are author results pending separate configuration verification.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_6ffda5354e277da0a0`**：Movens proposes a coupled intelligent-development/executable-software system that repeats design, implementation and evaluation. Its TORCS demonstration uses genetic programming to generate controller programs, with a separate C# application controlling evolution and external compiling/testing; nested logical, implementation and parameter modification are the broader model.
  - 来源版本：Journal of Applied Engineering Science 14(2016)2；定位：coupled redesign model; PDF physical page 2, derived page-text lines 50-64 (one-based local extraction, not web-tool lines)；automated external compile/test control; PDF physical page 7, derived page-text lines 18-28 (one-based local extraction, not web-tool lines)；compilation/simulation compute cost; PDF physical page 8, derived page-text lines 121-133 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · coupled redesign model
**来源**：https://scindeks-clanci.ceon.rs/data/pdf/1451-4117/2016/1451-41171602239D.pdf  
**实际版本**：Journal of Applied Engineering Science 14(2016)2  
**精确定位**：PDF physical page 2, derived page-text lines 50-64 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_6ffda5354e277da0a0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · automated external compile/test control
**来源**：https://scindeks-clanci.ceon.rs/data/pdf/1451-4117/2016/1451-41171602239D.pdf  
**实际版本**：Journal of Applied Engineering Science 14(2016)2  
**精确定位**：PDF physical page 7, derived page-text lines 18-28 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_6ffda5354e277da0a0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · compilation/simulation compute cost
**来源**：https://scindeks-clanci.ceon.rs/data/pdf/1451-4117/2016/1451-41171602239D.pdf  
**实际版本**：Journal of Applied Engineering Science 14(2016)2  
**精确定位**：PDF physical page 8, derived page-text lines 121-133 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_6ffda5354e277da0a0`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The reported example compiles and simulates controllers on one specified unobstructed track and has high computational demand. GP-within-GP parameter selection is proposed as future work, so the demonstration does not establish recursively adapting its GP search algorithm.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_6ffda5354e277da0a0` · Developing self-modifying code model · Journal of Applied Engineering Science 14(2016)2
  - https://scindeks-clanci.ceon.rs/data/pdf/1451-4117/2016/1451-41171602239D.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6ffda5354e277da0a0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
