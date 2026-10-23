# Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory

> 方法论文 · 2025 · `wf_2f8b16edd0471632db`

**作者**：Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou  
**原文**：https://arxiv.org/abs/2504.07952  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
外部记忆由模型策展后用于后续问题；模型、检索和策展程序固定，属于核心记忆闭环。

## 2. 论文的核心内容与贡献

### configuration:cfg_dc_cumulative_v1
核心记忆闭环；不更新参数或改进器程序。

**适用版本**：2504.07952v1；**原文定位**：§2.1.1–2.1.2 Eq.1–2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dc_retrieval_synthesis_v1
DC-RS和DC-Cu写入时序不同；必须分别表示。

**适用版本**：2504.07952v1；**原文定位**：§2.2 Eq.3–5。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_dc_rs_faithfulness_audit
被审计实现，不与原论文不同模型的结果混用。

**适用版本**：2601.22436v1；**原文定位**：§2；§3.1–3.3；Figure 3；Appendix C Dynamic Cheatsheet。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_dc_cumulative_v1
`cfg_dc_cumulative_v1` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结Gen/Cur模型与持久外部记忆M |
| 改进过程与下一轮参与 | 答题后Cur更新记忆供后续问题使用 |
| 保留的状态及时间尺度 | 跨问题保留M |
| 外部固定部分 | 模型、策展提示和更新协议 |

**配置判定**：核心记忆闭环；不更新参数或改进器程序。

来源：https://arxiv.org/html/2504.07952v1；版本：2504.07952v1；定位：§2.1.1–2.1.2 Eq.1–2。

### cfg_dc_retrieval_synthesis_v1
`cfg_dc_retrieval_synthesis_v1` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结Gen/Cur、历史输入输出库、检索器和持久记忆M |
| 改进过程与下一轮参与 | 查询前检索历史输入输出、策展记忆，再生成当前答案 |
| 保留的状态及时间尺度 | 跨问题保留历史库与M |
| 外部固定部分 | 模型、嵌入、检索top-k和策展程序 |

**配置判定**：DC-RS和DC-Cu写入时序不同；必须分别表示。

来源：https://arxiv.org/html/2504.07952v1；版本：2504.07952v1；定位：§2.2 Eq.3–5。

### cfg_dc_rs_faithfulness_audit
`cfg_dc_rs_faithfulness_audit` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 忠实性研究实现的在线DC-RS记忆代理 |
| 改进过程与下一轮参与 | 历史轨迹与凝练经验进入后续查询并接受干预 |
| 保留的状态及时间尺度 | 跨问题记忆；测试时原始/凝练输入受干预 |
| 外部固定部分 | temperature 0、greedy、top-3历史输入输出和干预规则 |

**配置判定**：被审计实现，不与原论文不同模型的结果混用。

来源：https://arxiv.org/html/2601.22436v1；版本：2601.22436v1；定位：§2；§3.1–3.3；Figure 3；Appendix C Dynamic Cheatsheet。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_faithfulness_v1` · 已存来源 · v1
  - https://arxiv.org/html/2601.22436v1；阅读深度：`未单列`。
- `intake_src_w_dynamic_cheatsheet` · 已存来源 · 2504.07952v1
  - https://arxiv.org/html/2504.07952v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2f8b16edd0471632db --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
