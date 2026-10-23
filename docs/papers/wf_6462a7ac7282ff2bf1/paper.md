# Tamper-Proofing with Self-Modifying Code

> 背景/相邻基础 · 2026 · `wf_6462a7ac7282ff2bf1`

**作者**：Gregory Morse, Tamás Kozsik  
**原文**：https://arxiv.org/abs/2604.12407  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
The paper models introspective self-checksumming code that rewrites polymorphically during execution, binding runtime integrity checks to timing signals on an untrusted host. Curator-specified background relevance: integrity checking and external trust/timing conditions for self-modifying programs. This is a survey bridge to bounded assurance, not an author-reported RSI experiment.

### 与 RSI 的具体关系

- Curator-specified background relevance: integrity checking and external trust/timing conditions for self-modifying programs. This is a survey bridge to bounded assurance, not an author-reported RSI experiment.

## 2. 论文的核心内容与贡献

### role:b570_11_role_wf_6462a7ac7282ff2bf1
The paper models introspective self-checksumming code that rewrites polymorphically during execution, binding runtime integrity checks to timing signals on an untrusted host.

**适用版本**：arXiv:2604.12407v1；**原文定位**：Introspective polymorphic integrity model; PDF physical page 2, derived page-text lines 20-35 (one-based local extraction, not web-tool lines)；Runtime-protection aim and platform limits; PDF physical page 11, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Timing/checksum predicates and runtime integrity observations; no AI capability-improvement score.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_11_ev_wf_6462a7ac7282ff2bf1`**：The paper models introspective self-checksumming code that rewrites polymorphically during execution, binding runtime integrity checks to timing signals on an untrusted host.
  - 来源版本：arXiv:2604.12407v1；定位：Introspective polymorphic integrity model; PDF physical page 2, derived page-text lines 20-35 (one-based local extraction, not web-tool lines)；Runtime-protection aim and platform limits; PDF physical page 11, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Introspective polymorphic integrity model
**来源**：https://arxiv.org/pdf/2604.12407v1  
**实际版本**：arXiv:2604.12407v1  
**精确定位**：PDF physical page 2, derived page-text lines 20-35 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_6462a7ac7282ff2bf1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 限制 · Runtime-protection aim and platform limits
**来源**：https://arxiv.org/pdf/2604.12407v1  
**实际版本**：arXiv:2604.12407v1  
**精确定位**：PDF physical page 11, derived page-text lines 1-16 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_11_ev_wf_6462a7ac7282ff2bf1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The model depends on platform-specific timing thresholds, operating-system noise and hardware measurement conditions. It does not demonstrate learned or AI capability improvement, an RSI adoption process, or general safety of arbitrary self-modification.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_11_src_wf_6462a7ac7282ff2bf1` · Tamper-Proofing with Self-Modifying Code · arXiv:2604.12407v1
  - https://arxiv.org/pdf/2604.12407v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6462a7ac7282ff2bf1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
