# A ‘Self-Referential’ Weight Matrix

> 方法论文 · 1993 · `wf_5592a7b5b8cfc46046`

**作者**：Jürgen Schmidhuber  
**原文**：https://doi.org/10.1007/978-1-4471-2063-6_107  
**研究分支**：历史基础与其他背景  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：4. CONCLUSION。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：理论指定的循环网络、可寻址weight matrix、ana/val/mod/delta和eval输入；固定activation/address gate/外层初始化训练；具体更新过程为：网络激活读取自身weight并发出带地址的delta写入任意weight；新matrix同时影响后续输出、分析/修改单元；外层Eq5只对initial weights做梯度；更新状态的保留与后继使用为：有限预先指定interaction sequence内weight(t)递推保留；训练sequence可串接，但跨任务泛化仅理论愿景。

## 2. 论文的核心内容与贡献

### configuration:cfg_srwm_1993_formal_addressed_weight_update
原文构造明确的自指weight读写与outer初始权重训练协议，提供形式上状态回流；§4自称thought experiment，作为历史形式邻接基础，不能当已运行实验或改进收益证据。

**适用版本**：author transcription of 1993 ICANN paper; footer2003-02-21；**原文定位**：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### 1993 self-referential weight matrix: proposed addressed read/write dynamics
`cfg_srwm_1993_formal_addressed_weight_update` · protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 理论指定的循环网络、可寻址weight matrix、ana/val/mod/delta和eval输入；固定activation/address gate/外层初始化训练。 |
| 改进过程与下一轮参与 | 网络激活读取自身weight并发出带地址的delta写入任意weight；新matrix同时影响后续输出、分析/修改单元；外层Eq5只对initial weights做梯度。 |
| 保留的状态及时间尺度 | 有限预先指定interaction sequence内weight(t)递推保留；训练sequence可串接，但跨任务泛化仅理论愿景。 |
| 外部固定部分 | - 地址编码与可微gate g - 固定activation函数/动力学形式 - 监督目标eval与初始weight外层gradient rule |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2明确network及特殊读写/eval单元。（状态：`supported`；定位：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3）。
- **更新由什么过程产生**：Eq3由network自身mod和delta activation产生weight修改。（状态：`supported`；定位：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3）。
- **状态怎样持久保留**：Eq1/3递推weight跨时步保留。（状态：`supported`；定位：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3）。
- **更新怎样进入后续改进**：更新weight影响下步network激活，包括产生后继读写地址与delta的单元；仅formal规定。（状态：`supported`；定位：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3）。

**配置判定**：原文构造明确的自指weight读写与outer初始权重训练协议，提供形式上状态回流；§4自称thought experiment，作为历史形式邻接基础，不能当已运行实验或改进收益证据。

来源：https://people.idsia.ch/~juergen/selfref/node2.html；版本：author transcription of 1993 ICANN paper; footer2003-02-21；定位：§2 numbered requirements1–4 tool L2–15；§2.1 Eqs1–4 tool L2–26；§3 Eq5 initial-weight outer gradient tool L3–7；§4 thought-experiment scope tool L1–3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r10_ev_cfg_srwm_1993_formal_addressed_weight_update`**：原文构造明确的自指weight读写与outer初始权重训练协议，提供形式上状态回流；§4自称thought experiment，作为历史形式邻接基础，不能当已运行实验或改进收益证据。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 四条件字段仅指所规定的理论动力学，不表示实证认证；此protocol不计实验core。
- initial weights的外层gradient优化与sequence内自改不同，不可说外层算法也由网络改写。
- 作者明确in principle可学习更新算法，本次没有实验/数值或完整梯度推导有效性认证。
- 主表1993印刷、2012数字上线与旧identity证据保留；网页footer2003是转录时间，不改出版年。
- - 四条件字段仅指所规定的理论动力学，不表示实证认证；此protocol不计实验core。 - initial weights的外层gradient优化与sequence内自改不同，不可说外层算法也由网络改写。 - 作者明确in principle可学习更新算法，本次没有实验/数值或完整梯度推导有效性认证。 - 主表1993印刷、2012数字上线与旧identity证据保留；网页footer2003是转录时间，不改出版年。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `hist_src_srwm1993` · 已存来源 · author HTML transcription of ICANN 1993; site footer 2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node3.html；阅读深度：`未单列`。
- `hist_src_srwm1993_setup` · 已存来源 · author HTML transcription of ICANN 1993; site footer 2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node2.html；阅读深度：`未单列`。
- `hist_src_srwm1993_initial` · 已存来源 · author HTML transcription of ICANN 1993; site footer 2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node4.html；阅读深度：`未单列`。
- `hist_src_srwm1993_publisher` · 已存来源 · ICANN 1993 print chapter; digital First Online 2012-04-10
  - https://link.springer.com/chapter/10.1007/978-1-4471-2063-6_107；阅读深度：`未单列`。
- `r10_src_srwm93_conclusion` · 4. CONCLUSION · author transcription of 1993 ICANN paper; footer2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node5.html；阅读深度：`未单列`。
- `r10_src_srwm93_dynamics` · 2.1 SELF-REFERENTIAL DYNAMICS AND OBJECTIVE FUNCTION · author transcription of 1993 ICANN paper; footer2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node3.html；阅读深度：`未单列`。
- `r10_src_srwm93_initial` · 3. INITIAL LEARNING ALGORITHM · author transcription of 1993 ICANN paper; footer2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node4.html；阅读深度：`未单列`。
- `r10_src_srwm93_setup` · 2. THE INTROSPECTIVE NETWORK · author transcription of 1993 ICANN paper; footer2003-02-21
  - https://people.idsia.ch/~juergen/selfref/node2.html；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_full_text_method_pass, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5592a7b5b8cfc46046 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
