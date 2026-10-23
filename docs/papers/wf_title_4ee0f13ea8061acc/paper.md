# Dream-RSI: Recursive Self-Improvement through Evolving Worlds

> 方法论文 · 2026 · `wf_title_4ee0f13ea8061acc`

**作者**：Tong Zheng, Xidong Wu, Zheng Zhang, Zhankui He, Chaoyi Zhang, Benjamin Coleman, Ruoqiao Wei, Di Bai, Haolin Liu, Rui Liu, Xue Wang, Yue Zhuan, Wang-Cheng Kang, Renkai Xiang, Heng Huang, Xinwu Cheng, Yunsong Guo  
**原文**：https://arxiv.org/abs/2609.14858  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定任务agent和执行接口、在线发现树历史、可修改探索策略代码构成meta-exploration系统；具体更新过程为：在线固定当前策略分配搜索；积累完整树后，外部代码代理修订策略，在已记录树上预算回放比较，保留较优策略供下一轮在线发现；更新状态的保留与后继使用为：跨在线/离线轮保留策略代码和已记录树。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_dream_policy_replay
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：2609.14858v2；**原文定位**：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Dream-RSI: retained exploration-policy code over accumulated discovery trees
`cfg_r8b_dream_policy_replay` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定任务agent和执行接口、在线发现树历史、可修改探索策略代码构成meta-exploration系统。 |
| 改进过程与下一轮参与 | 在线固定当前策略分配搜索；积累完整树后，外部代码代理修订策略，在已记录树上预算回放比较，保留较优策略供下一轮在线发现。 |
| 保留的状态及时间尺度 | 跨在线/离线轮保留策略代码和已记录树。 |
| 外部固定部分 | - 任务agent与其参数 - 环境和评价接口 - 回放只显露已经记录的子节点 - 候选生成/预算与选择框架 |
| 评价与选择设置 | - **mutable target**：executable exploration policy - **not model parameter training**：True - **replay budget preferences**：- 0 - 0.25 - 0.5 - 0.75 - 1 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：策略/树历史和任务agent分工明确。（状态：`supported`；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235）。
- **更新由什么过程产生**：自身在线轨迹与得分触发探索策略修改。（状态：`supported`；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235）。
- **状态怎样持久保留**：策略与历史跨轮保留。（状态：`supported`；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235）。
- **更新怎样进入后续改进**：新策略决定后续在线展开，再产生下一次策略优化历史。（状态：`supported`；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2609.14858；版本：2609.14858v2；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235。

## 4. 实验、评价协议与结果的可解释范围


- **mutable target**：executable exploration policy
- **not model parameter training**：True
- **replay budget preferences**：- 0 - 0.25 - 0.5 - 0.75 - 1

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_dream_policy_replay`**：固定任务agent和执行接口、在线发现树历史、可修改探索策略代码构成meta-exploration系统。 在线固定当前策略分配搜索；积累完整树后，外部代码代理修订策略，在已记录树上预算回放比较，保留较优策略供下一轮在线发现。
  - 来源版本：2609.14858v2；定位：§3 tool L96–126; §4 experimental protocol; §4.4 tool L209–235；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 回放不执行未记录节点；回放最优不保证新在线任务也最优。
- 只认证当前历史平均回放指标的保留规则；不认证全任务单调收益。
- 部分数学任务有退步；coding harness端没有相同昂贵固定策略对照。
- 成本主要计发现agent调用，不应当作完整meta计算总费用；Terminal-Bench全套反复用于搜索，不是独立held-out任务。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_dream` · 已存来源 · 2609.14858v2
  - https://arxiv.org/html/2609.14858；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_4ee0f13ea8061acc --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
