# CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

> 方法论文 · 2023 · `wf_1ddc06c9b768404fc1`

**作者**：Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, Weizhu Chen  
**原文**：https://arxiv.org/abs/2305.11738  
**研究分支**：验证、批评与信用分配  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：单输入答案、工具查询及批评；具体更新过程为：外部工具核查后修订当前答案，达到停止条件结束；更新状态的保留与后继使用为：单个最终输出内部。

## 2. 论文的核心内容与贡献

### configuration:cfg_critic
工具反馈有用但未产生跨最终输出的持久系统更新

**适用版本**：v4；**原文定位**：S3.SS3.p1；S3.SS4.p1；S3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_critic
`cfg_critic` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单输入答案、工具查询及批评 |
| 改进过程与下一轮参与 | 外部工具核查后修订当前答案，达到停止条件结束 |
| 保留的状态及时间尺度 | 单个最终输出内部 |
| 外部固定部分 | 模型、任务对应工具及核查提示 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：单输入答案、工具查询及批评（状态：`supported`；定位：S3.p1；S3.SS3.p1；S3.SS4.p1）。
- **更新由什么过程产生**：外部工具核查后修订当前答案，达到停止条件结束（状态：`supported`；定位：S3.p1；S3.SS3.p1；S3.SS4.p1）。
- **状态怎样持久保留**：单个最终输出内部（状态：`contradicted`；定位：S3.p1；S3.SS3.p1；S3.SS4.p1）。
- **更新怎样进入后续改进**：工具反馈有用但未产生跨最终输出的持久系统更新（状态：`contradicted`；定位：S3.p1；S3.SS3.p1；S3.SS4.p1）。

**配置判定**：工具反馈有用但未产生跨最终输出的持久系统更新

来源：https://arxiv.org/html/2305.11738v4；版本：v4；定位：S3.SS3.p1；S3.SS4.p1；S3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_critic`**：外部工具核查后修订当前答案，达到停止条件结束
  - 来源版本：v4；定位：S3.p1；S3.SS3.p1；S3.SS4.p1；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 工
- 具
- 反
- 馈
- 有
- 用
- 但
- 未
- 产
- 生
- 跨
- 最
- 终
- 输
- 出
- 的
- 持
- 久
- 系
- 统
- 更
- 新

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_critic` · CRITIC · v4
  - https://arxiv.org/html/2305.11738v4；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1ddc06c9b768404fc1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
