# Bootstrap Perception Under Hardware Depth Failure for Indoor Robot Navigation

> 背景/相邻基础 · 2026 · `wf_1ff2bd318af80ffba1`

**作者**：Nishant Pushparaju, Vivek Mattam, Aliasghar Arab  
**原文**：https://arxiv.org/abs/2603.28890  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
利用深度传感器幸存像素校准单目深度并融合LiDAR，self-referential指感知自校准；摘要没有改进器递归更新链。

### 与 RSI 的具体关系

- Adjacent bounded adaptation example, not RSI.

## 2. 论文的核心内容与贡献

### role:b570_16_role_wf_1ff2bd318af80ffba1
The navigation system uses surviving hardware-depth pixels to calibrate monocular relative depth and fill failed regions while retaining LiDAR as the geometric anchor.

**适用版本**：2603.28890v1；**原文定位**：PDF physical page 1, derived page-text lines 9-14 (one-based local extraction, not web-tool lines)；PDF physical page 1, derived page-text lines 48-53 (one-based local extraction, not web-tool lines)；PDF physical page 4, derived page-text lines 1-4 (one-based local extraction, not web-tool lines)；PDF physical page 5, derived page-text lines 24-29 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

### 已存角色解释 · `r4_role_review_wf_1ff2bd318af80ffba1`
利用深度传感器幸存像素校准单目深度并融合LiDAR，self-referential指感知自校准；摘要没有改进器递归更新链。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_1ff2bd318af80ffba1`**：利用深度传感器幸存像素校准单目深度并融合LiDAR，self-referential指感知自校准；摘要没有改进器递归更新链。
  - 来源版本：2603.28890v1；定位：Atom entry http://arxiv.org/abs/2603.28890v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_16_ev_wf_1ff2bd318af80ffba1`**：The navigation system uses surviving hardware-depth pixels to calibrate monocular relative depth and fill failed regions while retaining LiDAR as the geometric anchor.
  - 来源版本：2603.28890v1；定位：PDF physical page 1, derived page-text lines 9-14 (one-based local extraction, not web-tool lines)；PDF physical page 1, derived page-text lines 48-53 (one-based local extraction, not web-tool lines)；PDF physical page 4, derived page-text lines 1-4 (one-based local extraction, not web-tool lines)；PDF physical page 5, derived page-text lines 24-29 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://arxiv.org/pdf/2603.28890v1  
**实际版本**：2603.28890v1  
**精确定位**：PDF physical page 1, derived page-text lines 9-14 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_16_ev_wf_1ff2bd318af80ffba1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · selected mechanism or role passage
**来源**：https://arxiv.org/pdf/2603.28890v1  
**实际版本**：2603.28890v1  
**精确定位**：PDF physical page 1, derived page-text lines 48-53 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_16_ev_wf_1ff2bd318af80ffba1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · selected material-limit or boundary passage
**来源**：https://arxiv.org/pdf/2603.28890v1  
**实际版本**：2603.28890v1  
**精确定位**：PDF physical page 4, derived page-text lines 1-4 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_16_ev_wf_1ff2bd318af80ffba1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 限制 · selected material-limit or boundary passage
**来源**：https://arxiv.org/pdf/2603.28890v1  
**实际版本**：2603.28890v1  
**精确定位**：PDF physical page 5, derived page-text lines 24-29 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_16_ev_wf_1ff2bd318af80ffba1`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Learned depth complements rather than replaces LiDAR, heavy teachers remain off-board, and the adaptation repairs sensor gaps without modifying the system's own learning mechanism.
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_16_src_wf_1ff2bd318af80ffba1` · Bootstrap Perception Under Hardware Depth Failure for Indoor Robot Navigation · 2603.28890v1
  - https://arxiv.org/pdf/2603.28890v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。
- `r4_role_src_468996c5bf89fae4` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2603.22435%2C2603.22455%2C2603.22479%2C2603.22744%2C2603.22791%2C2603.22868%2C2603.23064%2C2603.23420%2C2603.23483%2C2603.23516%2C2603.23626%2C2603.23802%2C2603.23994%2C2603.24093%2C2603.24402%2C2603.24481%2C2603.24579%2C2603.24621%2C2603.24647%2C2603.25001%2C2603.25133%2C2603.25158%2C2603.25723%2C2603.25973%2C2603.26085%2C2603.26100%2C2603.26130%2C2603.26557%2C2603.26778%2C2603.27185%2C2603.27277%2C2603.27306%2C2603.27611%2C2603.27703%2C2603.27813%2C2603.27820%2C2603.27850%2C2603.27910%2C2603.28088%2C2603.28119%2C2603.28306%2C2603.28361%2C2603.28386%2C2603.28416%2C2603.28428%2C2603.28716%2C2603.28813%2C2603.28815%2C2603.28890%2C2603.28928%2C2603.28986%2C2603.28990%2C2603.29002%2C2603.29093%2C2603.29139%2C2603.29194%2C2603.29199%2C2603.29247%2C2603.29493%2C2603.29640%2C2603.29678%2C2603.29848%2C2603.29878%2C2603.29919%2C2604.00073%2C2604.00362%2C2604.00533%2C2604.00550%2C2604.00594%2C2604.00626%2C2604.00890%2C2604.00901%2C2604.01007%2C2604.01193%2C2604.01210%2C2604.01221%2C2604.01236%2C2604.01348%2C2604.01527%2C2604.01599%2C2604.01664%2C2604.01707%2C2604.02334%2C2604.02345%2C2604.02368%2C2604.02369%2C2604.02431%2C2604.02734%2C2604.02988%2C2604.03088%2C2604.03098%2C2604.03144%2C2604.03245%2C2604.03472%2C2604.03512%2C2604.03588%2C2604.03610%2C2604.03679%2C2604.04131%2C2604.04202&max_results=100；阅读深度：`未单列`。

**仍未核准的内容**：

- Numerical, configuration and relationship claims require separate evidence review.

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`role_and_relevance_boundary_only_not_technical_answer_evidence`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1ff2bd318af80ffba1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
