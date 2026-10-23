# Automated Design of Agentic Systems

> 综合系统/智能体 · 2024 · `wf_c9890d5668d1c1b33e`

**作者**：Shengran Hu, Cong Lu, Jeff Clune  
**原文**：https://arxiv.org/abs/2408.08435  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定元代理＋包含代码和评价的增长档案；具体更新过程为：更新档案直接条件化下一轮元代理设计和反思；档案作为改进者的持久上下文；更新状态的保留与后继使用为：跨Meta Agent Search迭代。

### 定点原文补充：具体问题与执行过程
把代理设计表达为可执行代码，用固定元代理根据不断扩展的目标代理档案搜索新设计。

1. 在所给框架中编写 forward 函数；先生成设计解释与代码，再做两轮自反思。
2. 目标代理在验证数据上评测；错误时最多五次反思修复，随后将代理与指标写入档案。

**实验与选择协议**：

- 研究覆盖 ARC、数学、阅读与推理，并检验跨任务和跨模型迁移。
- 搜索中用验证数据反馈，测试表现与搜索反馈必须区分。

**解释边界**：

- 核查实例的可写空间与框架 API 有约束；代码空间的理论表达力不意味着实际搜索无约束。
- 档案目标代理改变不等于元代理自身被更新；不能由主题相近自动连成继承。

来源：[2408.08435v2](https://arxiv.org/html/2408.08435v2)；定位：§3 Meta Agent Search；§4 Experiments；Appendix C; Appendix H。本补充只登记定点描述性阅读，不扩大旧配置或数值结果的准入权限。

## 2. 论文的核心内容与贡献

### configuration:cfg_adas
核心判定针对档案参与设计的完整边界；被发现的forward目标代理本身不自动成为自修改改进器

**适用版本**：v2；**原文定位**：S3.p1；S3.p2；S3.p3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_adas
`cfg_adas` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定元代理＋包含代码和评价的增长档案 |
| 改进过程与下一轮参与 | 更新档案直接条件化下一轮元代理设计和反思；档案作为改进者的持久上下文 |
| 保留的状态及时间尺度 | 跨Meta Agent Search迭代 |
| 外部固定部分 | 元代理FM、框架API、评价指标及最大轮数 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：固定元代理＋包含代码和评价的增长档案（状态：`supported`；定位：S3.p1；S3.p2；S3.p3）。
- **更新由什么过程产生**：更新档案直接条件化下一轮元代理设计和反思；档案作为改进者的持久上下文（状态：`supported`；定位：S3.p1；S3.p2；S3.p3）。
- **状态怎样持久保留**：跨Meta Agent Search迭代（状态：`supported`；定位：S3.p1；S3.p2；S3.p3）。
- **更新怎样进入后续改进**：更新档案直接条件化下一轮元代理设计和反思；档案作为改进者的持久上下文（状态：`supported`；定位：S3.p1；S3.p2；S3.p3）。

**配置判定**：核心判定针对档案参与设计的完整边界；被发现的forward目标代理本身不自动成为自修改改进器

来源：https://arxiv.org/html/2408.08435v2；版本：v2；定位：S3.p1；S3.p2；S3.p3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_adas`**：元代理以不断增长的目标代理档案为上下文，生成forward代码。
  - 来源版本：v2；定位：S3.p1；S3.p2；深度：`AI_rechecked_primary_text_author_report`。

- **`e2_w_adas`**：更新档案直接条件化下一轮元代理设计和反思；档案作为改进者的持久上下文
  - 来源版本：v2；定位：S3.p1；S3.p2；S3.p3；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 对固定元代理的认定另与SICA原文对照；配置范围保持待定
- 核
- 心
- 判
- 定
- 针
- 对
- 档
- 案
- 参
- 与
- 设
- 计
- 的
- 完
- 整
- 边
- 界
- ；
- 被
- 发
- 现
- f
- o
- r
- w
- a
- d
- 目
- 标
- 代
- 理
- 本
- 身
- 不
- 自
- 动
- 成
- 为
- 修
- 改
- 进
- 器

## 7. 与其他论文的具体关系

### [A Self-Improving Coding Agent](../r03_method/wf_f5d4d370636d9b3832.md)
关系：`adapts_design_of` · `r_sica_adas` · 当前展示权限：`primary_supported`。
SICA作者明确将其主循环与ADAS档案循环对照：保留代理档案与评测结果，但从档案选择最佳代理充当下一轮元代理，并允许编辑完整Python代码库；ADAS原配置是固定元代理生成目标代理forward函数。

**关系边界**：支持作者明确说明的循环改造，不认证源码复用；ADAS不修改元代理这一结论限于所核Meta Agent Search配置，不将作者对self-improving的术语立场当统一范围协议。

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2504.15228v2（v2；S3.p1.1；S2.p5.1）；https://arxiv.org/html/2408.08435v2（v2；S3.p1.1；S3.p2.1）。

### [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../r03_method/wf_c29f716871f8031486.md)
关系：`contrasts_system_boundary_with` · `r_dgm_adas` · 当前展示权限：`primary_supported`。
DGM由可演化代理修改自身代码，ADAS核查配置由固定元代理生成目标代理函数；DGM另实现固定元代理消融模拟ADAS式设计。

**关系边界**：DGM消融是该论文的重实现，不能称原ADAS代码或整个原实验被完全复现；档案、选择与评价仍有固定部分。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p2；S3.p2；S4.SS3.p1。
- object：https://arxiv.org/html/2408.08435v2；版本：v2；定位：S3.p1；S3.p2。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S2.p2；S4.SS3.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_adas` · ADAS / Meta Agent Search · v2
  - https://arxiv.org/html/2408.08435v2；阅读深度：`未单列`。
- `recheck_src_w_adas` · 已存来源 · v2
  - https://arxiv.org/html/2408.08435v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c9890d5668d1c1b33e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
