# Incorporating Self-Rewriting into Large Language Model Reasoning Reinforcement

> 方法论文 · 2025 · `wf_520fa46d20ba471010`

**作者**：Jiashu Yao, Heyan Huang, Shuang Zeng, Chuwei Luo, WangJie You, Jie Tang, Qingsong Liu, Yuhang Guo, Yangyang Kang  
**原文**：https://arxiv.org/abs/2511.16331  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：current policy、query group、correctness verifier、own rewrite/continued-answer采样与fixed GRPO step；具体更新过程为：先采G/2并验；全正确才用同模型改reasoning再续答，否则普通采样；全部仍正确时对rewritten给1/original给0，其他用correctness rewards；GRPO更新M后处理后继query；更新状态的保留与后继使用为：Algorithm1 M←step跨query保留，后续采样/rewriting由更新M执行；不是只输出层refine。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_rewriting_online_grpo_feedback_v1
自生成reasoning/rewrites进入GRPO并保留更新policy用于下一query，四结构条件在online RL训练闭环成立；self-rewriting不指修改模型源码。

**适用版本**：2511.16331v1；**原文定位**：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Self-Rewriting: selective own-reasoning generation in online GRPO
`cfg_self_rewriting_online_grpo_feedback_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | current policy、query group、correctness verifier、own rewrite/continued-answer采样与fixed GRPO step。 |
| 改进过程与下一轮参与 | 先采G/2并验；全正确才用同模型改reasoning再续答，否则普通采样；全部仍正确时对rewritten给1/original给0，其他用correctness rewards；GRPO更新M后处理后继query。 |
| 保留的状态及时间尺度 | Algorithm1 M←step跨query保留，后续采样/rewriting由更新M执行；不是只输出层refine。 |
| 外部固定部分 | - general rewrite instruction - 规则correctness verifier - GRPO/二段group采样与reward式 |
| 评价与选择设置 | - **evaluation**：MATH500/GPQA/ARC/MMLUPro; 4 sampled runs - **judging**：LLM-based internal-quality scores - **train data**：DeepMath-103K subset - **train samples**：10000 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3明确M, verifier和GRPO的复合训练边界。（状态：`supported`；定位：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303）。
- **更新由什么过程产生**：policy自己产生reasoning及rewrites影响当前policy训练。（状态：`supported`；定位：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303）。
- **状态怎样持久保留**：Algorithm1 step赋回M并继续query loop。（状态：`supported`；定位：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303）。
- **更新怎样进入后续改进**：更新M用于后继generation/rewriting，改变再训练信号。（状态：`supported`；定位：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303）。

**配置判定**：自生成reasoning/rewrites进入GRPO并保留更新policy用于下一query，四结构条件在online RL训练闭环成立；self-rewriting不指修改模型源码。

来源：https://arxiv.org/html/2511.16331v1；版本：2511.16331v1；定位：§3 Selective Rewriting/Optimization/Algorithm1 tool L119–183；§4.1 datasets/judge tool L217–225；§6 conclusion/task scope tool L285–303。

## 4. 实验、评价协议与结果的可解释范围


- **evaluation**：MATH500/GPQA/ARC/MMLUPro; 4 sampled runs
- **judging**：LLM-based internal-quality scores
- **train data**：DeepMath-103K subset
- **train samples**：10000

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r10_ev_cfg_self_rewriting_online_grpo_feedback_v1`**：自生成reasoning/rewrites进入GRPO并保留更新policy用于下一query，四结构条件在online RL训练闭环成立；self-rewriting不指修改模型源码。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 仅全正确半组触发rewriting且最终全组正确才产生rewrite偏好；不能称所有sample都被改写或只因更短直接奖励。
- 正确性仍外部verifier；DeepSeek-V3等更强LLM用于结果judge，不是训练无外部真值。
- reasoning内部质量是LLM judge proxy，不认证真实faithfulness或独立因果推理质量。
- 约10% overhead限报告batch实现/小规模post-tuning，不是任意预训练等效成本。
- - 仅全正确半组触发rewriting且最终全组正确才产生rewrite偏好；不能称所有sample都被改写或只因更短直接奖励。 - 正确性仍外部verifier；DeepSeek-V3等更强LLM用于结果judge，不是训练无外部真值。 - reasoning内部质量是LLM judge proxy，不认证真实faithfulness或独立因果推理质量。 - 约10% overhead限报告batch实现/小规模post-tuning，不是任意预训练等效成本。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r10_src_rewriting` · Incorporating Self-Rewriting into Large Language Model Reasoning Reinforcement · 2511.16331v1
  - https://arxiv.org/html/2511.16331v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_520fa46d20ba471010 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
