# EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

> 方法论文 · 2026 · `wf_6e6b14494848e97940`

**作者**：Jiaqi Liu, Xinyu Ye, Peng Xia, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao  
**原文**：https://arxiv.org/abs/2605.13941v1  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
依具体更新边界裁定；不按self-evolving标题认证递归性。

## 2. 论文的核心内容与贡献

### configuration:cfg_evolvemem_frozen_best_retrieval
由Algorithm1返回最佳配置后取出的部署视图；不声称作者另报该命名独立实验臂。

**适用版本**：v1；**原文定位**：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_evolvemem_retrieval_diagnosis_loop
core限有监督有限轮配置研究循环；不能外推为无标注部署期自主改进。

**适用版本**：v1；**原文定位**：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_evolvemem_retrieval_diagnosis_loop
`cfg_evolvemem_retrieval_diagnosis_loop` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | LLM诊断器、可变检索配置/typed memory及固定监督评分guard。 |
| 改进过程与下一轮参与 | 读取含标准答案和F1的逐题失败日志，提议检索/融合/上下文/回答风格调整；guard回退退化并扰动停滞配置，可触发重抽记忆。 |
| 保留的状态及时间尺度 | 配置及最佳checkpoint跨轮保留，影响后续检索、回答和诊断输入。 |
| 外部固定部分 | - 监督QA与评分 - guard阈值、参数clamp - 诊断rubric及基础模型 |

**配置判定**：core限有监督有限轮配置研究循环；不能外推为无标注部署期自主改进。

来源：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。

### cfg_evolvemem_frozen_best_retrieval
`cfg_evolvemem_frozen_best_retrieval` · curator_boundary_view

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 关闭诊断/guard搜索，仅部署最佳检索配置。 |
| 改进过程与下一轮参与 | 固定最佳融合与回答策略进行检索回答。 |
| 保留的状态及时间尺度 | 保留搜索产物，单独不形成新一轮配置改进。 |
| 外部固定部分 | - 最佳配置 - 基础模型和检索接口 |

**配置判定**：由Algorithm1返回最佳配置后取出的部署视图；不声称作者另报该命名独立实验臂。

来源：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_memory_ev_cfg_evolvemem_retrieval_diagnosis_loop`**：读取含标准答案和F1的逐题失败日志，提议检索/融合/上下文/回答风格调整；guard回退退化并扰动停滞配置，可触发重抽记忆。
  - 来源版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211；深度：`未单列`。

- **`r4_memory_ev_cfg_evolvemem_frozen_best_retrieval`**：固定最佳融合与回答策略进行检索回答。
  - 来源版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 这是明确抽取的控制边界视图，非额外论文或新的实测基线。
- §3.3同一Q用于优化目标；本批未确认独立未见QA选优隔离，不能认证无泄漏泛化。
- 最多7轮和作者报告的跨库迁移不证明无界增长或普适检索原则。
- 新参数维度是作者方法主张；本批未执行代码验证扩展可实现性。
- core限有监督有限轮配置研究循环；不能外推为无标注部署期自主改进。
- 由Algorithm1返回最佳配置后取出的部署视图；不声称作者另报该命名独立实验臂。

## 7. 与其他论文的具体关系

### [A-MEM: Agentic Memory for LLM Agents](../r03_method/wf_1aacba116cbe3c5bc3.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_evolvemem_retrieval_diagnosis_loop_cfg_amem` · 当前展示权限：`primary_supported`。
EvolveMem监督失败诊断修改检索配置；A-MEM由新note触发LLM语义/链接/旧note更新，查询方法为embedding近邻。修改检索控制与修改存储知识应分开。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_evolvemem：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。
- r4_memory_src_evolvemem：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。

## 8. 来源清单、复查入口与解析缺口
- `r4_memory_src_evolvemem` · 已存来源 · v1
  - https://arxiv.org/html/2605.13941v1；阅读深度：`未单列`。

**证据深度**：selected_primary_method_configuration_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6e6b14494848e97940 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
