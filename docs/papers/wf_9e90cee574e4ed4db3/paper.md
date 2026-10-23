# A-Evolve-Training: Autonomous Post-Training of a 30B Model

> 方法论文 · 2026 · `wf_9e90cee574e4ed4db3`

**作者**：Zhan Shi, Bing He, Yisi Sang, Benoit Dumoulin, Hanqing Lu  
**原文**：https://arxiv.org/abs/2606.20657  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：rolling search policy及dead-end registry；具体更新过程为：元代理按round evidence重写下一轮搜索规则和经验阈值，后续workers继承策略；更新状态的保留与后继使用为：四轮campaign的策略保留。

## 2. 论文的核心内容与贡献

### configuration:cfg_aevolve_search_policy
单次未复核campaign；完整代码/模型释放时间待确认；不把训练产物晋升到substrate

**适用版本**：v3；**原文定位**：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_aevolve_search_policy
`cfg_aevolve_search_policy` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | rolling search policy及dead-end registry |
| 改进过程与下一轮参与 | 元代理按round evidence重写下一轮搜索规则和经验阈值，后续workers继承策略 |
| 保留的状态及时间尺度 | 四轮campaign的策略保留 |
| 外部固定部分 | 只读constitution、不可覆写substrate、固定证据schema |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：rolling search policy及dead-end registry（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1）。
- **更新由什么过程产生**：元代理按round evidence重写下一轮搜索规则和经验阈值，后续workers继承策略（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1）。
- **状态怎样持久保留**：四轮campaign的策略保留（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1）。
- **更新怎样进入后续改进**：元代理按round evidence重写下一轮搜索规则和经验阈值，后续workers继承策略（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1）。

**配置判定**：单次未复核campaign；完整代码/模型释放时间待确认；不把训练产物晋升到substrate

来源：https://arxiv.org/html/2606.20657v3；版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_aevolve_training`**：元代理按round evidence重写下一轮搜索规则和经验阈值，后续workers继承策略
  - 来源版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 单
- 次
- 未
- 复
- 核
- c
- a
- m
- p
- i
- g
- n
- ；
- 完
- 整
- 代
- 码
- /
- 模
- 型
- 释
- 放
- 时
- 间
- 待
- 确
- 认
- 不
- 把
- 训
- 练
- 产
- 物
- 晋
- 升
- 到
- s
- u
- b
- t
- r
- e

## 7. 与其他论文的具体关系

### [Bilevel Autoresearch: Meta-Autoresearching Itself](../r03_method/wf_7d83bc86747f407ae5.md)
关系：`contrasts_system_boundary_with` · `r2_aevolve_training_bilevel_14` · 当前展示权限：`primary_supported`。
A-Evolve-Training在不可覆写substrate与只读constitution约束下，由元代理依据轮次证据重写rolling search policy、继承配方、搜索轴和dead-end registry；Bilevel Autoresearch的Level 1.5更新SearchConfig，Level 2则生成Python机制并原位修补runner.py，经动态导入检查后激活或回退。两者改变后续搜索的载体分别是策略工件和活动执行器代码。

**关系边界**：比较对象是明确的改进表面，不是直接继承。A-Evolve-Training只报告单次未复现的四轮、单一30B模型后训练campaign；Bilevel只证明外层改善内层，未证明同一机制反哺Level 2或无界递归。动态导入检查也不等于功能/安全性证明。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2606.20657v3；版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。
- object：https://arxiv.org/html/2603.23420v2；版本：v2；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p2；S3.SS4.p3；S5.SS4.SSS0.Px5.p1。
- expand_src_w_aevolve_training：https://arxiv.org/html/2606.20657v3；版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。
- expand_src_w_bilevel：https://arxiv.org/html/2603.23420v2；版本：v2；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.p1；S3.SS4.p2；S3.SS4.p3；S5.SS4.SSS0.Px5.p1。

### [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](../r03_method/wf_c68aa5fb00021bf53f.md)
关系：`contrasts_system_boundary_with` · `r2_ai4ai_bench_aevolve_training_17` · 当前展示权限：`primary_supported`。
AI4AI-Bench将开发与验证严格隔开：4小时单B300开发后只提交源代码，不传递开发权重、缓存或笔记；训练任务从初始化执行至结束或12小时上限，非训练任务一次执行后评分。A-Evolve-Training的所查四轮campaign保留rolling policy、继承配方及dead-end registry，以一个公共排行榜作为外部锚点，基底不被胜出配方覆盖。因此两者规定的跨边界持久状态和评价对象不同。

**关系边界**：这是评价协议与campaign证据边界的双端比较；原文没有支持AI4AI-Bench实际评测了A-Evolve-Training，不应标为evaluates。12小时是上限而非所有任务固定训练时长；不能用AI4AI-Bench的独立从头运行保障为A-Evolve campaign背书。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2608.20318v1；版本：v1；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S2.SS5.p1。
- object：https://arxiv.org/html/2606.20657v3；版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。
- expand_src_w_ai4ai_bench：https://arxiv.org/html/2608.20318v1；版本：v1；定位：S2.SS1.p1；S2.SS3.p1；S2.SS3.p2；S2.SS5.p1。
- expand_src_w_aevolve_training：https://arxiv.org/html/2606.20657v3；版本：v3；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px3.p2；S6.SS1.p1；S7.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_aevolve_training` · A-Evolve-Training: Autonomous Post-Training of a 30B Model · v3
  - https://arxiv.org/html/2606.20657v3；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_9e90cee574e4ed4db3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
