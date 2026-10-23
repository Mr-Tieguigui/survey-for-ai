# A-MEM: Agentic Memory for LLM Agents

> 方法论文 · 2025 · `wf_1aacba116cbe3c5bc3`

**作者**：Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang  
**原文**：https://arxiv.org/abs/2502.12110  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：记忆集合及属性、嵌入和链接；具体更新过程为：演化后记忆替换旧项；后续检索到的集合继续输入链接与记忆演化；更新状态的保留与后继使用为：跨记忆写入与检索事件。

## 2. 论文的核心内容与贡献

### configuration:cfg_amem
核心是记忆状态参与后续记忆更新；未证明记忆管理算法或模型参数自改

**适用版本**：v11；**原文定位**：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_amem
`cfg_amem` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 记忆集合及属性、嵌入和链接 |
| 改进过程与下一轮参与 | 演化后记忆替换旧项；后续检索到的集合继续输入链接与记忆演化 |
| 保留的状态及时间尺度 | 跨记忆写入与检索事件 |
| 外部固定部分 | LLM、文本编码器、提示模板及top-k检索程序 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：记忆集合及属性、嵌入和链接（状态：`supported`；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1）。
- **更新由什么过程产生**：演化后记忆替换旧项；后续检索到的集合继续输入链接与记忆演化（状态：`supported`；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1）。
- **状态怎样持久保留**：跨记忆写入与检索事件（状态：`supported`；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1）。
- **更新怎样进入后续改进**：演化后记忆替换旧项；后续检索到的集合继续输入链接与记忆演化（状态：`supported`；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1）。

**配置判定**：核心是记忆状态参与后续记忆更新；未证明记忆管理算法或模型参数自改

来源：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_amem`**：演化后记忆替换旧项；后续检索到的集合继续输入链接与记忆演化
  - 来源版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；深度：`AI_primary_method_passage_recheck`。

- **`r4_memory_ev_amem_existing`**：LLM生成note语义、链接及邻近旧记忆更新，查询使用embedding相似检索。
  - 来源版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 核
- 心
- 是
- 记
- 忆
- 状
- 态
- 参
- 与
- 后
- 续
- 更
- 新
- ；
- 未
- 证
- 明
- 管
- 理
- 算
- 法
- 或
- 模
- 型
- 数
- 自
- 改

## 7. 与其他论文的具体关系

### [EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents](../r03_method/wf_6e6b14494848e97940.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_evolvemem_retrieval_diagnosis_loop_cfg_amem` · 当前展示权限：`primary_supported`。
EvolveMem监督失败诊断修改检索配置；A-MEM由新note触发LLM语义/链接/旧note更新，查询方法为embedding近邻。修改检索控制与修改存储知识应分开。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_evolvemem：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。
- r4_memory_src_evolvemem：https://arxiv.org/html/2605.13941v1；版本：v1；定位：§3.1–3.2, tool text L114–140；§3.3 Eq.3–4/Algorithm1, tool text L141–196；§4.1, tool text L200–211。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。

### [MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory](../r03_method/wf_d045f6a3ccf0df1e41.md)
关系：`contrasts_system_boundary_with` · `r4_memory_cfg_mindset_versioned_schema_controller_cfg_amem` · 当前展示权限：`primary_supported`。
MINDSET固定能量规则管理不可变episodes的版本schema；A-MEM通过LLM重写邻近note语义和链接。两者持久组织变化均不能自动推得控制器参数或改进规则自改。

**关系边界**：双端方法机制对照；非继承、共同实验臂、代码复用或性能优劣认证。

**已存关系来源与定位（保留原记录端点语义）**：
- r4_memory_src_mindset：https://arxiv.org/html/2610.08586v1；版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。
- r4_memory_src_mindset：https://arxiv.org/html/2610.08586v1；版本：v1；定位：§3.1–3.3, tool text L112–206；§3.5–3.7, tool text L210–240。
- r4_memory_src_amem_existing：https://arxiv.org/html/2502.12110v11；版本：v11；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_amem` · A-MEM · v11
  - https://arxiv.org/html/2502.12110v11；阅读深度：`未单列`。
- `r4_memory_src_amem_existing` · 已存来源 · v11
  - https://arxiv.org/html/2502.12110v11；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1aacba116cbe3c5bc3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
