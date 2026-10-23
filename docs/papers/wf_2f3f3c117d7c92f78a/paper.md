# RSI-Anything: Unlocking Recursive Self-Improvement with World Models

> 综合系统/智能体 · 2026 · `wf_2f3f3c117d7c92f78a`

**作者**：Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang  
**原文**：https://arxiv.org/abs/2610.13912  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Specified recursive protocol; empirical completeness is domain-dependent.; Predictor adapts within feedback rounds; cross-problem carryover/reset unresolved. Pending persistent-system RSI determination.

## 2. 论文的核心内容与贡献

### configuration:cfg_rsi_anything_code_predictor_adaptation
在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。

**适用版本**：2610.13912v1；**原文定位**：§5–6.1 tool L273–299。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_rsi_anything_policy_model_protocol
Specified recursive protocol; empirical completeness is domain-dependent.

**适用版本**：2610.13912v1；**原文定位**：§2.1 Table1；§2.3–2.5 Eq.7–18。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### cfg_rsi_anything_policy_model_protocol
`cfg_rsi_anything_policy_model_protocol` · protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Policy/workflow, predictor, feedback records, component/pair gates. |
| 更新状态 | Policy/workflow and/or predictor. |
| 改进过程与下一轮参与 | Prediction-guided selection, feedback updates, conditional predictor adaptation, accepted-pair retention. |
| 保留的状态及时间尺度 | Accepted versions condition later learning cycles. |
| 外部固定部分 | Task, interfaces, scores, constraints, budget, acceptance/stopping rules. |
| 实验实现状态 | formal_shared_protocol; GUI §6.1 reports retained pair in later interactions, other domains have partial update scopes |

**配置判定**：Specified recursive protocol; empirical completeness is domain-dependent.

来源：https://arxiv.org/html/2610.13912v1；版本：2610.13912v1；定位：§2.1 Table1；§2.3–2.5 Eq.7–18。

### cfg_rsi_anything_code_predictor_adaptation
`cfg_rsi_anything_code_predictor_adaptation` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Fixed coder, W1 predictor, execution-test feedback. |
| 更新状态 | World-model predictor parameters. |
| 改进过程与下一轮参与 | Predictor adaptation reranks candidates. |
| 保留的状态及时间尺度 | 预测器参数在至多3feedback轮内保留，跨问题持久性未由本次原文建立。 |
| 外部固定部分 | Coder, four candidates, tests/budget. |
| 跨任务保留 | unknown |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。（状态：`supported`；定位：§5–6.1 tool L273–299）。
- **更新由什么过程产生**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。（状态：`supported`；定位：§5–6.1 tool L273–299）。
- **状态怎样持久保留**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。（状态：`supported`；定位：§5–6.1 tool L273–299）。
- **更新怎样进入后续改进**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。（状态：`supported`；定位：§5–6.1 tool L273–299）。

**配置判定**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。

来源：https://arxiv.org/html/2610.13912v1；版本：2610.13912v1；定位：§5–6.1 tool L273–299。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_rsi_anything_code_predictor_adaptation`**：在最多3次反馈轮的固定coder—可适配W1预测器边界内，已更新预测器保留供后继候选排序，再收执行反馈；跨问题或终身保留不是此有限结构认证的必要前提。
  - 来源版本：2610.13912v1；定位：§5–6.1 tool L273–299；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 仅认证within-run反馈边界；跨问题predictor carry/reset仍未知，不据此声称跨任务或终身增益。
- coder固定；不能把code设置推成policy+world-model实证互相递归升级。
- §5明确仍需联合多轮实验建立持续互相改进；隐藏测试仅最终报告成功，不能用于训练反馈。
- §5: sustained mutual policy/predictor improvement still needs joint multiround evaluation.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r7root_src_rsi_code_within_round` · 已存来源 · 2610.13912v1
  - https://arxiv.org/html/2610.13912v1；阅读深度：`未单列`。
- `r7root_src_rsi_version_contract` · 已存来源 · 2610.13912v1
  - https://arxiv.org/html/2610.13912v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_limits_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2f3f3c117d7c92f78a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
