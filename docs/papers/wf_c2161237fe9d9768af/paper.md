# MemEvolve: Meta-Evolution of Agent Memory Systems

> 综合系统/智能体 · 2025 · `wf_c2161237fe9d9768af`

**作者**：Guibin Zhang, Haotian Ren, Chong Zhan, Zhenhong Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng Yan  
**原文**：https://arxiv.org/abs/2512.18746  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：代理执行、经验状态与编码/存储/检索/管理架构的双层演化；具体更新过程为：内层轨迹反馈诊断父架构，固定设计算子生成子架构，Pareto选择保留父代；更新状态的保留与后继使用为：架构跨外层轮次保留；每个候选的经验池在每次外层迭代起点重置为空。

## 2. 论文的核心内容与贡献

### configuration:cfg_memevolve_dual_evolution
核心范围是架构及其执行反馈回路；不可称经验池跨外层连续积累或外算子本身自改。

**适用版本**：2512.18746v1；**原文定位**：S4.SS1.p2；S4.SS1.p3；S4.SS1.p4；S4.SS2.p2；S4.SS2.p4。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_memevolve_transfer_evaluation
目标迁移结果不等于目标数据上继续meta-evolution。目标GAIA使用其另列的演化方案，不能混同WebWalker/xBench迁移。

**适用版本**：2512.18746v1；**原文定位**：S5.SS2.p1；S5.SS3.p1；S9.SS1.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_memevolve_dual_evolution
`cfg_memevolve_dual_evolution` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 代理执行、经验状态与编码/存储/检索/管理架构的双层演化 |
| 改进过程与下一轮参与 | 内层轨迹反馈诊断父架构，固定设计算子生成子架构，Pareto选择保留父代 |
| 保留的状态及时间尺度 | 架构跨外层轮次保留；每个候选的经验池在每次外层迭代起点重置为空 |
| 外部固定部分 | LLM、四组件接口、Pareto选择规则、父代预算、诊断与设计外算子 |

**配置判定**：核心范围是架构及其执行反馈回路；不可称经验池跨外层连续积累或外算子本身自改。

来源：https://arxiv.org/html/2512.18746v1；版本：2512.18746v1；定位：S4.SS1.p2；S4.SS1.p3；S4.SS1.p4；S4.SS2.p2；S4.SS2.p4。

### cfg_memevolve_transfer_evaluation
`cfg_memevolve_transfer_evaluation` · evaluation_variant

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | TaskCraft演化所得架构固定后在目标任务框架内评测 |
| 改进过程与下一轮参与 | 目标任务不再开展任务专属架构演化；内层经验管理依赖选中的固定架构 |
| 保留的状态及时间尺度 | 演化后架构可跨基准转移；经验池具体初始化按运行协议，不混入外层连续保留 |
| 外部固定部分 | 冻结架构、目标LLM和代理框架、目标任务评价协议 |

**配置判定**：目标迁移结果不等于目标数据上继续meta-evolution。目标GAIA使用其另列的演化方案，不能混同WebWalker/xBench迁移。

来源：https://arxiv.org/html/2512.18746v1；版本：2512.18746v1；定位：S5.SS2.p1；S5.SS3.p1；S9.SS1.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `completion_src_memevolve_v1` · 已存来源 · 2512.18746v1
  - https://arxiv.org/html/2512.18746v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_original_method_and_limits_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c2161237fe9d9768af --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
