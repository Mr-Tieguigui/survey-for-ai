# Self-Refine: Iterative Refinement with Self-Feedback

> 方法论文 · 2023 · `wf_accef2157d87cf33be`

**作者**：Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark  
**原文**：https://arxiv.org/abs/2303.17651  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：单个输入的答案与反馈；具体更新过程为：固定LM及三类提示迭代修订同一答案，停止后返回最终输出；更新状态的保留与后继使用为：单个最终输出内部。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_refine
明确单次输出修订；条件3不成立，不把任务内历史当作跨输出系统更新

**适用版本**：v2；**原文定位**：S2.p1；S2.SS0.SSS0.Px2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2；S2.SS0.SSS0.Px3.p3；A15.p5。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_self_refine
`cfg_self_refine` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单个输入的答案与反馈 |
| 改进过程与下一轮参与 | 固定LM及三类提示迭代修订同一答案，停止后返回最终输出 |
| 保留的状态及时间尺度 | 单个最终输出内部 |
| 外部固定部分 | 模型参数与生成/反馈/修订提示 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：单个输入的答案与反馈（状态：`supported`；定位：S2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2）。
- **更新由什么过程产生**：固定LM及三类提示迭代修订同一答案，停止后返回最终输出（状态：`supported`；定位：S2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2）。
- **状态怎样持久保留**：单个最终输出内部（状态：`contradicted`；定位：S2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2）。
- **更新怎样进入后续改进**：明确单次输出修订；条件3不成立，不把任务内历史当作跨输出系统更新（状态：`contradicted`；定位：S2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2）。

**配置判定**：明确单次输出修订；条件3不成立，不把任务内历史当作跨输出系统更新

来源：https://arxiv.org/html/2303.17651v2；版本：v2；定位：S2.p1；S2.SS0.SSS0.Px2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2；S2.SS0.SSS0.Px3.p3；A15.p5。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_self_refine`**：固定LM及三类提示迭代修订同一答案，停止后返回最终输出
  - 来源版本：v2；定位：S2.p1；S2.SS0.SSS0.Px3.p1；S2.SS0.SSS0.Px3.p2；深度：`AI_primary_method_passage_recheck`。

- **`oct15_agents_ev_p2b1_rise_self_refine`**：RISE以多轮on-policy轨迹、教师或best-of-N重标注及加权回归训练单一模型，使其学会逐轮修订；Self-Refine原方法固定同一LM及生成/反馈/修订提示，在单输入内保留反馈历史、迭代改写输出。RISE附录另明确实现Self-Refine式评测基线。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_explicit_plus_two_endpoint_method_check`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 所有模块由固定同一LM提示执行，单输入内历史不认证跨最终输出持久学习。
- 数学推理附录A15.p5使用正确标签决定循环阶段；无额外模型训练不等于所有实验没有oracle反馈。
- 明
- 确
- 单
- 次
- 输
- 出
- 修
- 订
- ；
- 条
- 件
- 3
- 不
- 成
- 立
- ，
- 把
- 任
- 务
- 内
- 历
- 史
- 当
- 作
- 跨
- 系
- 统
- 更
- 新
- 主边比较RISE离线训练配置与Self-Refine单输入提示配置，不混入RISE单问题部署rollout。原Self-Refine数学推理附录A15.p5使用正确标签控制迭代；不可笼统声称其全部原实验无外部标签。RISE的Self-Refine适配基线与原Self-Refine各任务、后端、预算不等同；不推出公平统一性能排名、代码复用或历史继承。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_self_refine` · Self-Refine · v2
  - https://arxiv.org/html/2303.17651v2；阅读深度：`未单列`。
- `oct15_agents_src_w_rise` · 已存来源 · v2
  - https://arxiv.org/html/2407.18219v2；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `oct15_agents_src_w_self_refine` · 已存来源 · v2
  - https://arxiv.org/html/2303.17651v2；阅读深度：`selected_two_endpoint_primary_method_passages`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_accef2157d87cf33be --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
