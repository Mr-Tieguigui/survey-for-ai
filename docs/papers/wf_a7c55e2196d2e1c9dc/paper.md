# Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision

> 方法论文 · 2026 · `wf_a7c55e2196d2e1c9dc`

**作者**：Yuzhi Zhang, Xinyu Liu, Yu Zhang  
**原文**：https://arxiv.org/abs/2610.05151  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：更新学生与固定teacher的恢复监督框架；具体更新过程为：新学生的失败及续跑能力决定下一轮恢复收集，PostTrain保留学生参数；更新状态的保留与后继使用为：框架规定跨收集训练轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_visuomotor_framework
核心是方法定义的递归配置；所查结果是初步研究，多轮对照尚列评价协议，不认证已实证递归收益

**适用版本**：v1；**原文定位**：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_visuomotor_framework
`cfg_visuomotor_framework` · method_framework_not_multi_round_experiment_certified

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 更新学生与固定teacher的恢复监督框架 |
| 改进过程与下一轮参与 | 新学生的失败及续跑能力决定下一轮恢复收集，PostTrain保留学生参数 |
| 保留的状态及时间尺度 | 框架规定跨收集训练轮次 |
| 外部固定部分 | teacher参数、审核和原生训练目标 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：更新学生与固定teacher的恢复监督框架（状态：`supported`；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1）。
- **更新由什么过程产生**：新学生的失败及续跑能力决定下一轮恢复收集，PostTrain保留学生参数（状态：`supported`；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1）。
- **状态怎样持久保留**：框架规定跨收集训练轮次（状态：`supported`；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1）。
- **更新怎样进入后续改进**：新学生的失败及续跑能力决定下一轮恢复收集，PostTrain保留学生参数（状态：`supported`；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1）。

**配置判定**：核心是方法定义的递归配置；所查结果是初步研究，多轮对照尚列评价协议，不认证已实证递归收益

来源：https://arxiv.org/html/2610.05151v1；版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_visuomotor_rsi`**：新学生的失败及续跑能力决定下一轮恢复收集，PostTrain保留学生参数
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 核
- 心
- 是
- 方
- 法
- 定
- 义
- 的
- 递
- 归
- 配
- 置
- ；
- 所
- 查
- 结
- 果
- 初
- 步
- 研
- 究
- ，
- 多
- 轮
- 对
- 照
- 尚
- 列
- 评
- 价
- 协
- 议
- 不
- 认
- 证
- 已
- 实
- 收
- 益

## 7. 与其他论文的具体关系

### [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](../r03_method/wf_fb639e0da250efca5c.md)
关系：`contrasts_system_boundary_with` · `r2_visuomotor_rsi_coap_16` · 当前展示权限：`primary_supported`。
Visuomotor RSI的方法框架以当前学生失败轨迹及修复后的续跑能力决定下一轮恢复监督，经PostTrain保留学生参数，教师参数跨轮固定；COAP离线开发由编码代理根据失败记录提出机器人库代码diff，经CPU检查、验证集成功数与兼容性约束选择分支，接受代码作为后续分支基底。其可变资产分别为学生策略参数与机器人库源代码。

**关系边界**：左端是所提多轮方法框架，原文将关键多轮对照列为评价协议，不能认证已有实证递归收益；右端只用离线开发配置，不能混入冻结的在线执行配置。COAP现有窄边界条件4仍待定；比较关系本身不升级核心归属。COAP所查结果仅模拟，未取得共同基准、直接继承或参数/代码收益等价证据。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2610.05151v1；版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。
- object：https://arxiv.org/html/2610.12369v1；版本：v1；定位：S3.SS3.p1；S3.SS4.p1；S3.SS4.p2；S5.SS4.p1；S5.SS4.p2。
- expand_src_w_visuomotor_rsi：https://arxiv.org/html/2610.05151v1；版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。
- expand_src_w_coap：https://arxiv.org/html/2610.12369v1；版本：v1；定位：S3.SS3.p1；S3.SS4.p1；S3.SS4.p2；S5.SS4.p1；S5.SS4.p2。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_visuomotor_rsi` · Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision · v1
  - https://arxiv.org/html/2610.05151v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a7c55e2196d2e1c9dc --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
