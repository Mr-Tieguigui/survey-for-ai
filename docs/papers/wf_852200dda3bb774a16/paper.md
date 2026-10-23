# Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?

> 方法论文 · 2025 · `wf_852200dda3bb774a16`

**作者**：Chunqiu Steven Xia, Zhe Wang, Yan Yang, Yuxiang Wei, Lingming Zhang  
**原文**：https://arxiv.org/abs/2511.13646  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：单个软件issue内的脚本工具生成、修改与后续调用；具体更新过程为：固定反思提示结合环境反馈生成或修订自定义工具；更新状态的保留与后继使用为：脚本在同一issue后续步骤可用；跨issue序列化与加载在v1为未来工作。

## 2. 论文的核心内容与贡献

### configuration:cfg_live_swe_issue_runtime
任务内系统改进支持；跨任务保留未实证，不判为跨任务核心。整个代理循环重写在讨论而非本方法实现。

**适用版本**：2511.13646v1；**原文定位**：S2.p2；S2.SS1.p3；S2.SS2.p1；S2.SS2.p5；S4.SS4.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_live_swe_issue_runtime
`cfg_live_swe_issue_runtime` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单个软件issue内的脚本工具生成、修改与后续调用 |
| 改进过程与下一轮参与 | 固定反思提示结合环境反馈生成或修订自定义工具 |
| 保留的状态及时间尺度 | 脚本在同一issue后续步骤可用；跨issue序列化与加载在v1为未来工作 |
| 外部固定部分 | 模型权重、初始提示、固定反思消息、外层代理循环 |

**配置判定**：任务内系统改进支持；跨任务保留未实证，不判为跨任务核心。整个代理循环重写在讨论而非本方法实现。

来源：https://arxiv.org/html/2511.13646v1；版本：2511.13646v1；定位：S2.p2；S2.SS1.p3；S2.SS2.p1；S2.SS2.p5；S4.SS4.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `completion_src_live_swe_v1` · 已存来源 · 2511.13646v1
  - https://arxiv.org/html/2511.13646v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_original_method_and_limits_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_852200dda3bb774a16 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
