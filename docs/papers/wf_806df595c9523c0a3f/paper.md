# MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves

> 综合系统/智能体 · 2026 · `wf_806df595c9523c0a3f`

**作者**：Zihan Tan, Leixin Sun, Zitong Shi, Yitao Liu, Jiajun Wu, Nathaniel Brooks, Jiaru Qian, Xiaoran Shang, Suyuan Huang, Yi Ding, Yangxu Liao, Mukai Li, Qiushi Sun, Shudong Liu, Xuankun Rong, Xiaohang Yu, Zhuo Chen, Hejia Geng, Chenxin Li, Aozhou Wang, Zengji Tu, Robert Tang, Yuxin Zhan, Eric Jiang, Yuxin Wu, Jianqing Zhang, Xiao Liang, Fang Wu, Haochi Zhang, Alexander Marlow, Guancheng Wan  
**原文**：https://arxiv.org/abs/2609.06396  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Qwen3.5-35B-A3B target S=(data,harness,weights)、D/H/M typed operators及proposal policies π、RSI² scheduler φ和固定meta-agent；编译learning signal、protected verifier/gate/ledger；具体更新过程为：每step执行typed操作后重新evaluate/recompile σ，gate晋级的checkpoint作为后继rollout基模；scheduler横向组合operators或按contract纵向改π。每term后固定meta-agent读sequence、signals、accepted edits、gate及成本改φ，下一term复用；更新状态的保留与后继使用为：released successor data/genome/checkpoint、typed lineage artifacts、operator policies与scheduler跨step/term返回；conditions间重置到同S0，不将跨condition累加当自改。

## 2. 论文的核心内容与贡献

### configuration:cfg_metarsi_openweight_composed_operators_v1
实读open-weight D/H/M组合及policy/scheduler反馈，支持有界四条件；paper所称improver增益为作者五seed/有限term实验，非独立认证强RSI或普遍加速。

**适用版本**：2609.06396v1；**原文定位**：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### MetaRSI-v1 open-weight composed D/H/M operators plus policy/scheduler feedback
`cfg_metarsi_openweight_composed_operators_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Qwen3.5-35B-A3B target S=(data,harness,weights)、D/H/M typed operators及proposal policies π、RSI² scheduler φ和固定meta-agent；编译learning signal、protected verifier/gate/ledger。 |
| 改进过程与下一轮参与 | 每step执行typed操作后重新evaluate/recompile σ，gate晋级的checkpoint作为后继rollout基模；scheduler横向组合operators或按contract纵向改π。每term后固定meta-agent读sequence、signals、accepted edits、gate及成本改φ，下一term复用。 |
| 保留的状态及时间尺度 | released successor data/genome/checkpoint、typed lineage artifacts、operator policies与scheduler跨step/term返回；conditions间重置到同S0，不将跨condition累加当自改。 |
| 外部固定部分 | - sealed score/taskset、release rule、ledger和schema/sandbox - 最外meta-agent参数及可行动作/adapter endpoints - equal token/GPU/hour/candidate/verifier budgets按term重新计量 |
| 评价与选择设置 | - **adaptation**：Model-RSI LoRA recipe space; promoted checkpoint is next rollout base - **reported runs**：five outer seeds; budget separately metered each term - **target**：Qwen3.5-35B-A3B, 64K context - **tracks**：Terminal-Bench2.1/SWE-benchPro vs prompt-only GPQA-hard100/AIME |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4.1和4.7区分mutable π/φ及protected判断。（状态：`supported`；定位：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580）。
- **更新由什么过程产生**：target自身实例化model-driven角色，自生成data/harness/LoRA候选。（状态：`supported`；定位：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580）。
- **状态怎样持久保留**：promoted checkpoint回作newbase，return successor/π/φ并跨term携带。（状态：`supported`；定位：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580）。
- **更新怎样进入后续改进**：更新后的system重新rollout形成σ，改π/φ控制后续提案和组成。（状态：`supported`；定位：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580）。

**配置判定**：实读open-weight D/H/M组合及policy/scheduler反馈，支持有界四条件；paper所称improver增益为作者五seed/有限term实验，非独立认证强RSI或普遍加速。

来源：https://arxiv.org/html/2609.06396v1；版本：2609.06396v1；定位：§4.1 loop/kernel/authority tool L177–205；§4.2–4.3 action surfaces/checkpoint/freshness tool L263–291；§4.4–4.5 policy and meta scheduler tool L325–341；§5.1 tracks/reset/sealed/budget tool L419–436；§5.4 same-successor improver comparison tool L475–481；§6.4–6.5 open empirical/physical limits tool L568–580。

## 4. 实验、评价协议与结果的可解释范围


- **adaptation**：Model-RSI LoRA recipe space; promoted checkpoint is next rollout base
- **reported runs**：five outer seeds; budget separately metered each term
- **target**：Qwen3.5-35B-A3B, 64K context
- **tracks**：Terminal-Bench2.1/SWE-benchPro vs prompt-only GPQA-hard100/AIME

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_metarsi_openweight_composed_operators_v1`**：实读open-weight D/H/M组合及policy/scheduler反馈，支持有界四条件；paper所称improver增益为作者五seed/有限term实验，非独立认证强RSI或普遍加速。 每step执行typed操作后重新evaluate/recompile σ，gate晋级的checkpoint作为后继rollout基模；scheduler横向组合operators或按contract纵向改π。每term后固定meta-agent读sequence、signals、accepted edits、gate及成本改φ，下一term复用。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本配置只open-weight main track；frontier API只能D/H，不能归入其LoRA权重更新。
- closed-form任务禁tool/skill/MCP且只改system-prompt slot；不是完整coding harness配置的同一surface。
- exact/numeric或软件tests作为protected oracle，不代表开放领域正确性；模型自判与环境oracle须分开。
- 每term重新给相同预算，五term不是单term相同总成本；多term同sealed splits涉及持续测量复用，不能泛化无限未见分布。
- 具体LoRA可训练层/rank范围与source commit本次未全核，保留参数细节unknown。
- §5.4同一S1分叉、相同budget比较中，meta更新改进器报告增加7.2点、原改进器4.9点；但term2至term5的每term收益均递减：meta从7.2降至1.4，original从4.9降至0.7。较有效的改进器与更晚plateau不是逐term收益加速，且这些数值未独立复现。
- 本配置只open-weight main track；frontier API只能D/H，不能归入其LoRA权重更新。; closed-form任务禁tool/skill/MCP且只改system-prompt slot；不是完整coding harness配置的同一surface。; exact/numeric或软件tests作为protected oracle，不代表开放领域正确性；模型自判与环境oracle须分开。; 每term重新给相同预算，五term不是单term相同总成本；多term同sealed splits涉及持续测量复用，不能泛化无限未见分布。; 具体LoRA可训练层/rank范围与source commit本次未全核，保留参数细节unknown。; §5.4同一S1分叉、相同budget比较中，meta更新改进器报告增加7.2点、原改进器4.9点；但term2至term5的每term收益均递减：meta从7.2降至1.4，original从4.9降至0.7。较有效的改进器与更晚plateau不是逐term收益加速，且这些数值未独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_meta` · MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves · 2609.06396v1
  - https://arxiv.org/html/2609.06396v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_806df595c9523c0a3f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
