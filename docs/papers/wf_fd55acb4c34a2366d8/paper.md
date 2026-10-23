# Scaling Laws for Reward Model Overoptimization

> 失败/限制/风险 · 2022 · `wf_fd55acb4c34a2366d8`

**作者**：Leo Gao, John Schulman, Jacob Hilton  
**原文**：https://arxiv.org/abs/2210.10760  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
原文选段核查：以负结果、受控对照或有假设的边界分析为本survey提供评价限制，配置与原始方法分离。

## 2. 论文的核心内容与贡献

### configuration:cfg_reward_overopt_fixed_proxy_bon
BoN为固定模型候选选择负结果协议，与PPO训练配置分列；N增加不等于系统学习。

**适用版本**：2210.10760v1；**原文定位**：S1.p2；S1.p3；S2.p1；S2.p2；S2.p3；S2.p4；S2.SS1.p1；S3.SS1.p2；S3.SS6.p1；S4.SS1.p1；S4.I1.i2.p1；S4.I1.i8.p1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_reward_overopt_fixed_proxy_ppo
固定代理奖励下的策略优化与gold/proxy偏离测量，作为RSI评价风险的邻近证据；不是递归更新评价器的实证测试。

**适用版本**：2210.10760v1；**原文定位**：S1.p2；S1.p3；S2.p1；S2.p2；S2.p3；S2.p4；S2.SS1.p1；S3.SS1.p2；S3.SS6.p1；S4.SS1.p1；S4.I1.i2.p1；S4.I1.i8.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### Fixed synthetic proxy RM: PPO overoptimization audit
`cfg_reward_overopt_fixed_proxy_ppo` · negative_result_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | SFT后的GPT-3策略由PPO优化；固定proxy reward model给训练信号，独立6B gold RM给合成评价目标。 |
| 改进过程与下一轮参与 | PPO更新策略参数；本配置不更新proxy或gold RM，也不使策略改写PPO优化规则。 |
| 保留的状态及时间尺度 | 策略权重跨PPO步保留；评价与更新规则固定。 |
| 外部固定部分 | - PPO - 固定proxy/gold RMs - InstructGPT提示环境 - SFT与RM数据构造 |
| 评价与选择设置 | - **KL penalty**：0 except separate §3.6 experiments - **gold reward model parameters**：6B - **held out fraction**：0.1 - **initial policy**：pretrained GPT-3, SFT 2 epochs on human InstructGPT demonstrations - **optimizer**：PPO - **proxy reward model parameters**：3M–3B - **synthetic comparisons**：100000 |

**配置判定**：固定代理奖励下的策略优化与gold/proxy偏离测量，作为RSI评价风险的邻近证据；不是递归更新评价器的实证测试。

来源：https://arxiv.org/html/2210.10760v1；版本：2210.10760v1；定位：S1.p2；S1.p3；S2.p1；S2.p2；S2.p3；S2.p4；S2.SS1.p1；S3.SS1.p2；S3.SS6.p1；S4.SS1.p1；S4.I1.i2.p1；S4.I1.i8.p1。

### Fixed synthetic proxy RM: best-of-N selection audit
`cfg_reward_overopt_fixed_proxy_bon` · negative_result_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定策略采样N个候选，固定proxy RM选最高分；gold RM仅用于测量。 |
| 改进过程与下一轮参与 | 仅候选选择，无参数或持久学习状态更新。 |
| 保留的状态及时间尺度 | 本轮保留被选回答；未建立跨新问题保留的优化器或模型更新。 |
| 外部固定部分 | - 生成策略 - proxy/gold RMs - 候选数N - 解析KL与分数估计程序 |
| 评价与选择设置 | - **KL formula**：log(N)-(N-1)/N - **fit validation**：functional form hypothesized with N<=1000; extrapolation experiment N<=60000 - **gold reward model parameters**：6B - **proxy reward model parameters**：3M–3B - **selection**：highest proxy RM score among N policy trajectories |

**配置判定**：BoN为固定模型候选选择负结果协议，与PPO训练配置分列；N增加不等于系统学习。

来源：https://arxiv.org/html/2210.10760v1；版本：2210.10760v1；定位：S1.p2；S1.p3；S2.p1；S2.p2；S2.p3；S2.p4；S2.SS1.p1；S3.SS1.p2；S3.SS6.p1；S4.SS1.p1；S4.I1.i2.p1；S4.I1.i8.p1。

## 4. 实验、评价协议与结果的可解释范围


- **KL penalty**：0 except separate §3.6 experiments
- **gold reward model parameters**：6B
- **held out fraction**：0.1
- **initial policy**：pretrained GPT-3, SFT 2 epochs on human InstructGPT demonstrations
- **optimizer**：PPO
- **proxy reward model parameters**：3M–3B
- **synthetic comparisons**：100000


- **KL formula**：log(N)-(N-1)/N
- **fit validation**：functional form hypothesized with N<=1000; extrapolation experiment N<=60000
- **gold reward model parameters**：6B
- **proxy reward model parameters**：3M–3B
- **selection**：highest proxy RM score among N policy trajectories

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`accel_ev_reward_protocol_limit`**：主要实验为PPO和best-of-n，在合成gold/proxy奖励模型设置下分析过优化。
  - 来源版本：unknown；定位：§2 Methodology；§2.1 Synthetic Data Setup；§3.6；深度：`未单列`。

- **`round3_limits_ev_cfg_reward_overopt_fixed_proxy_ppo`**：固定代理奖励下的策略优化与gold/proxy偏离测量，作为RSI评价风险的邻近证据；不是递归更新评价器的实证测试。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`round3_limits_ev_cfg_reward_overopt_fixed_proxy_bon`**：BoN为固定模型候选选择负结果协议，与PPO训练配置分列；N增加不等于系统学习。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 同一synthetic gold/proxy环境，不能外推为真实偏好总是下降。
- 额外采样引起的选择效应不得混入自改进归因。
- gold信号是较大合成RM，不等同真实人类偏好。
- 作者把multi-iteration RLHF列为未来工作，不能写成已测Self-Rewarding的递归DPO。
- KL跨优化算法不构成统一优化量，KL penalty结论对超参数敏感。
- 不是DPO专项实验；不能把该结果写成DPO已被实证否定。
- 选段方法与控制变量核查；不是全文逐项复现，不认证无界或跨任务增益。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_reward_overopt` · 已存来源 · unversioned_served_document
  - https://arxiv.org/html/2210.10760；阅读深度：`未单列`。
- `round3_limits_src_w_reward_overopt` · 已存来源 · 2210.10760v1
  - https://arxiv.org/html/2210.10760v1；阅读深度：`targeted_original_method_evaluation_and_limit_passages`。

**证据深度**：primary_abstract_or_official_summary_review, selected_primary_method_controls_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_fd55acb4c34a2366d8 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
