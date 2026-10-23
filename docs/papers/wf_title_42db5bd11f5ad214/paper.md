# Self-Modifying State Modeling for Simultaneous Machine Translation

> 方法论文 · 2024 · `wf_title_42db5bd11f5ad214`

**作者**：Donglei Yu, Xiaomian Kang, Yuchen Liu, Yu Zhou, Chengqing Zong  
**原文**：https://doi.org/10.18653/v1/2024.acl-long.528  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SM2 learns a confidence-based READ/WRITE policy for simultaneous machine translation. Its self-modifying process compares partial-source predictions with full-source translation to assess current-token credibility, and prefix sampling independently optimizes states before confidence-threshold inference. Primary-body scope exclusion: the selected mechanism has no substantive bridge to recursive self-improvement of the learning system; lexical self-modifying overlap alone is insufficient. Admit only bibliographic scope disposition, not technical claims for the RSI survey.

### 与 RSI 的具体关系

- Primary-body scope exclusion: the selected mechanism has no substantive bridge to recursive self-improvement of the learning system; lexical self-modifying overlap alone is insufficient. Admit only bibliographic scope disposition, not technical claims for the RSI survey.

## 2. 论文的核心内容与贡献
没有已准入的原子主张。下面的已存角色解释和历史证据只能按其各自权限使用，不自动用于技术结论。

### 已存角色解释 · `b570_08_role_wf_title_42db5bd11f5ad214`
SM2 learns a confidence-based READ/WRITE policy for simultaneous machine translation. Its self-modifying process compares partial-source predictions with full-source translation to assess current-token credibility, and prefix sampling independently optimizes states before confidence-threshold inference.

研究类型：method with author-reported evaluation；权限：`bibliographic_disposition_only_not_technical_claims`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Simultaneous-translation quality/latency and READ/WRITE decision states, rather than an RSI cycle or accepted system revision.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_08_ev_wf_title_42db5bd11f5ad214`**：SM2 learns a confidence-based READ/WRITE policy for simultaneous machine translation. Its self-modifying process compares partial-source predictions with full-source translation to assess current-token credibility, and prefix sampling independently optimizes states before confidence-threshold inference.
  - 来源版本：ACL 2024 long paper 528 publisher PDF；定位：prediction modification and confidence meaning; PDF physical page 3, derived page-text lines 57-75 (one-based local extraction, not web-tool lines)；prefix-state sampling; PDF physical page 4, derived page-text lines 45-58 (one-based local extraction, not web-tool lines)；decision-assessment and backbone limitations; PDF physical page 9, derived page-text lines 28-40 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · prediction modification and confidence meaning
**来源**：https://aclanthology.org/2024.acl-long.528.pdf  
**实际版本**：ACL 2024 long paper 528 publisher PDF  
**精确定位**：PDF physical page 3, derived page-text lines 57-75 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_title_42db5bd11f5ad214`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · prefix-state sampling
**来源**：https://aclanthology.org/2024.acl-long.528.pdf  
**实际版本**：ACL 2024 long paper 528 publisher PDF  
**精确定位**：PDF physical page 4, derived page-text lines 45-58 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_title_42db5bd11f5ad214`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · decision-assessment and backbone limitations
**来源**：https://aclanthology.org/2024.acl-long.528.pdf  
**实际版本**：ACL 2024 long paper 528 publisher PDF  
**精确定位**：PDF physical page 9, derived page-text lines 28-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_08_ev_wf_title_42db5bd11f5ad214`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The self-modification concerns translation prediction and state-level training, not persistent revision of a general agent, optimizer, code or improvement mechanism. Authors leave better independent decision assessment and transfer to other encoder-decoder backbones to future work.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_08_src_wf_title_42db5bd11f5ad214` · Self-Modifying State Modeling for Simultaneous Machine Translation · ACL 2024 long paper 528 publisher PDF
  - https://aclanthology.org/2024.acl-long.528.pdf；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reported empirical results are author claims, not independently replicated by this review.
- Detailed configurations, performance magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`bibliographic_disposition_only_not_technical_claims`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_42db5bd11f5ad214 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
