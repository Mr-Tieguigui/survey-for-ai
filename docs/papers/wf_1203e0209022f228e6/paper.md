# The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> 方法论文 · 2025 · `wf_1203e0209022f228e6`

**作者**：Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha  
**原文**：https://arxiv.org/abs/2504.08066  
**研究分支**：科研代理、实验与发现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：实验节点树与状态/指标/VLM反馈；具体更新过程为：历史节点保存实验、图表和反馈，后续LLM据指标/动态/图质选择扩展并提案；更新状态的保留与后继使用为：跨完整实验节点。

## 2. 论文的核心内容与贡献

### configuration:cfg_ai_scientist_v2
范围为实验搜索状态参与后续研究提案；论文通过workshop评审不等于改进者自身性能提高

**适用版本**：v1；**原文定位**：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_ai_scientist_v2
`cfg_ai_scientist_v2` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 实验节点树与状态/指标/VLM反馈 |
| 改进过程与下一轮参与 | 历史节点保存实验、图表和反馈，后续LLM据指标/动态/图质选择扩展并提案 |
| 保留的状态及时间尺度 | 跨完整实验节点 |
| 外部固定部分 | 进度管理框架、搜索选择规则、LLM与评价程序 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：实验节点树与状态/指标/VLM反馈（状态：`supported`；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5）。
- **更新由什么过程产生**：历史节点保存实验、图表和反馈，后续LLM据指标/动态/图质选择扩展并提案（状态：`supported`；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5）。
- **状态怎样持久保留**：跨完整实验节点（状态：`supported`；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5）。
- **更新怎样进入后续改进**：历史节点保存实验、图表和反馈，后续LLM据指标/动态/图质选择扩展并提案（状态：`supported`；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5）。

**配置判定**：范围为实验搜索状态参与后续研究提案；论文通过workshop评审不等于改进者自身性能提高

来源：https://arxiv.org/html/2504.08066v1；版本：v1；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e3_w_ai_scientist_v2`**：历史节点保存实验、图表和反馈，后续LLM据指标/动态/图质选择扩展并提案
  - 来源版本：v1；定位：S3.SS2.SSS1.p1；S3.SS2.SSS2.p3；S3.SS2.SSS2.p4；S3.SS2.SSS2.p5；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 范
- 围
- 为
- 实
- 验
- 搜
- 索
- 状
- 态
- 参
- 与
- 后
- 续
- 研
- 究
- 提
- 案
- ；
- 论
- 文
- 通
- 过
- w
- o
- r
- k
- s
- h
- p
- 评
- 审
- 不
- 等
- 于
- 改
- 进
- 者
- 自
- 身
- 性
- 能
- 高

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `stage1_src_w_ai_scientist_v2` · 已存来源 · v1
  - https://arxiv.org/html/2504.08066v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1203e0209022f228e6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
