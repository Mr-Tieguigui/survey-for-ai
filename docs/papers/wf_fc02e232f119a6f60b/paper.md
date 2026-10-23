# Smaller Large Language Models Can Do Moral Self-Correction

> 实证/审计/复现 · 2024 · `wf_fc02e232f119a6f60b`

**作者**：Guangliang Liu, Zhiyu Xue, Xitong Zhang, Rongrong Wang, Kristen Marie Johnson  
**原文**：https://arxiv.org/abs/2410.23496  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Smaller Large Language Models Can Do Moral Self-Correction (https://arxiv.org/html/2410.23496v1)。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
Moral self-correction is evaluated by prompted output changes on Winogender and ambiguous BBQ bias tasks. Winogender fairness counts they/their/them prefixes; BBQ requires the unknown/cannot-be-determined answer. Instruction specificity and negation compare behavior, and the most specific instruction contains the desired answer. Optional feedback/prompt-evaluation background; local moral response correction requires an explicit bridge before use in RSI capability claims.

### 与 RSI 的具体关系

- Optional feedback/prompt-evaluation background; local moral response correction requires an explicit bridge before use in RSI capability claims.

## 2. 论文的核心内容与贡献

### role:b570_02_role_wf_fc02e232f119a6f60b
Moral self-correction is evaluated by prompted output changes on Winogender and ambiguous BBQ bias tasks. Winogender fairness counts they/their/them prefixes; BBQ requires the unknown/cannot-be-determined answer. Instruction specificity and negation compare behavior, and the most specific instruction contains the desired answer.

**适用版本**：2410.23496v1；**原文定位**：§2 task units, instructions and scoring tool L53–78；§3 answer-containing specificity boundary tool L93–95；§5 limitations tool L104–106。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_02_ev_wf_fc02e232f119a6f60b`**：Moral self-correction is evaluated by prompted output changes on Winogender and ambiguous BBQ bias tasks. Winogender fairness counts they/their/them prefixes; BBQ requires the unknown/cannot-be-determined answer. Instruction specificity and negation compare behavior, and the most specific instruction contains the desired answer.
  - 来源版本：2410.23496v1；定位：§2 task units, instructions and scoring tool L53–78；§3 answer-containing specificity boundary tool L93–95；§5 limitations tool L104–106；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · §2 task units, instructions and scoring
**来源**：https://arxiv.org/html/2410.23496v1  
**实际版本**：2410.23496v1  
**精确定位**：tool L53–78  
**关联证据**：`b570_02_ev_wf_fc02e232f119a6f60b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · §3 answer-containing specificity boundary
**来源**：https://arxiv.org/html/2410.23496v1  
**实际版本**：2410.23496v1  
**精确定位**：tool L93–95  
**关联证据**：`b570_02_ev_wf_fc02e232f119a6f60b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · §5 limitations
**来源**：https://arxiv.org/html/2410.23496v1  
**实际版本**：2410.23496v1  
**精确定位**：tool L104–106  
**关联证据**：`b570_02_ev_wf_fc02e232f119a6f60b`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Model scale is confounded with architecture/training differences; the study observes outputs rather than internal flow, lacks token-importance analysis and warns quantization can change results. This selected evidence does not establish a universal3.8B threshold or a retained recursive improvement loop.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_02_src_wf_fc02e232f119a6f60b` · Smaller Large Language Models Can Do Moral Self-Correction (https://arxiv.org/html/2410.23496v1) · 2410.23496v1
  - https://arxiv.org/html/2410.23496v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_fc02e232f119a6f60b --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
