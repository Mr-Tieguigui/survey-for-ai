# NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness

> 方法论文 · 2026 · `wf_0afc51b7af6ca1a424`

**作者**： NeoHorse Team, Guoliang Cao, Guohao Dai, Tianyu Guo, Kai Han, Hailin Hu, Zihan Jiang, Xiang Kuang, Boxun Li, Yulong Li, Zehua Pei, Yuchuan Tian, Jiamin Wang, Yu Wang, Yunhe Wang, Yihong Wu, Haiyang Xu, Shuo Zhang, Hang Zhou, Siyang Cheng, Jiayu Fan, Wei He, Qingrui Jiao, Hongguang Li, Zhiyuan Li, Runke Liu, Xi Liu, Xinchen Liu, Sinno Jialin Pan, Yi Ren, Liuyang Song, Chenyu Wang, Bei Yu, Quanlu Zhang, Xiangyu Zhang, Mengyu Zheng, Yingjie Zong  
**原文**：https://arxiv.org/abs/2609.08183  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
NeoHorse-1 converts routing-harness trajectories to supervision, evaluates deficiencies to rebalance training data and applies routing-scheduled on-policy distillation with a fixed teacher on student prefixes. Future feedback generations are described; only one evaluation-selection-update pass is validated. Direct bounded harness-mediated RSI pathway; routing scores, evaluation outcomes and teacher supervision have distinct roles and the single-pass boundary is retained.

### 与 RSI 的具体关系

- Direct bounded harness-mediated RSI pathway; routing scores, evaluation outcomes and teacher supervision have distinct roles and the single-pass boundary is retained.

## 2. 论文的核心内容与贡献

### role:b570_06_role_wf_0afc51b7af6ca1a424
NeoHorse-1 converts routing-harness trajectories to supervision, evaluates deficiencies to rebalance training data and applies routing-scheduled on-policy distillation with a fixed teacher on student prefixes. Future feedback generations are described; only one evaluation-selection-update pass is validated.

**适用版本**：arXiv:2609.08183v1；**原文定位**：Capability-guided allocation; PDF p8; derived text lines 20-41 (one-based local extraction, not web-tool lines)；Routing-guided on-policy distillation; PDF p11; derived text lines 22-45 (one-based local extraction, not web-tool lines)；Single-pass limit; PDF p18; derived text lines 33-40 (one-based local extraction, not web-tool lines)；User-turn and loss unit; PDF p9; derived text lines 8-43 (one-based local extraction, not web-tool lines)；Benchmark/return-to-harness claims; PDF p18; derived text lines 19-32 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节

### NeoHorse-1 v1 single-pass routing-harness post-training
`cfg_neohorse1_routing_posttraining_single_pass_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Routing harness→轨迹/quality标签→capability-guided data mixture→SFT/OPD checkpoint→回到model pool；所报结果只覆盖一轮。 |
| 改进过程与下一轮参与 | 当前checkpoint的分层评价构造deficiency profile以调整下次训练混合；routing-derived demand决定三阶段SFT/OPD课程；OPD有teacher监督。 |
| 保留的状态及时间尺度 | checkpoint、轨迹、routing prediction/adjusted/served与outcome记录保留，更新模型已返serving pool；新轨迹可seed下一代但未测试重复更新。 |
| 外部固定部分 | - 数据质量/去污染程序、课程和训练规则 - 外部teacher distillation supervision - 分层评价panel及harness接口 |
| 评价与选择设置 | - **evaluation**：ten benchmarks; data-source ablation uses same init/optimizer/seed with comparable budget - **models**：Qwen3.5 4B and 9B; SFT and routing-guided OPD - **reported loop passes**：1 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.4–3.5声明serving、数据分配与post-training边界。（状态：`supported`；定位：§3.4–3.5 routing retention and allocation design tool L148–162；§4.2–4.3 curriculum and teacher supervision tool L182–209；§6 single-pass limitation and future repeated iterations tool L303–317）。
- **更新由什么过程产生**：本轮执行SFT/OPD更新checkpoint。（状态：`supported`；定位：§3.4–3.5 routing retention and allocation design tool L148–162；§4.2–4.3 curriculum and teacher supervision tool L182–209；§6 single-pass limitation and future repeated iterations tool L303–317）。
- **状态怎样持久保留**：更新checkpoint和routing/outcome数据记录保留并返回pool。（状态：`supported`；定位：§3.4–3.5 routing retention and allocation design tool L148–162；§4.2–4.3 curriculum and teacher supervision tool L182–209；§6 single-pass limitation and future repeated iterations tool L303–317）。
- **更新怎样进入后续改进**：§6明确只验证single pass；后继轨迹再促成第二轮改进仍待实证。（状态：`unknown`；定位：§3.4–3.5 routing retention and allocation design tool L148–162；§4.2–4.3 curriculum and teacher supervision tool L182–209；§6 single-pass limitation and future repeated iterations tool L303–317）。

**配置判定**：一轮已执行权重改进及部署反馈基础得到支持；重复改进的第四条件在实证层面pending，不升级为已执行多轮core。

来源：https://arxiv.org/html/2609.08183v1；版本：2609.08183v1；定位：§3.4–3.5 routing retention and allocation design tool L148–162；§4.2–4.3 curriculum and teacher supervision tool L182–209；§6 single-pass limitation and future repeated iterations tool L303–317。

## 4. 实验、评价协议与结果的可解释范围

User-turn sequence/supervised assistant tokens; capability strata rebalance a mixture and ten benchmarks report scores. Three curriculum stages/rollout refreshes are not three accepted RSI generations.


- **evaluation**：ten benchmarks; data-source ablation uses same init/optimizer/seed with comparable budget
- **models**：Qwen3.5 4B and 9B; SFT and routing-guided OPD
- **reported loop passes**：1

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_neohorse1_routing_posttraining_single_pass_v1`**：一轮已执行权重改进及部署反馈基础得到支持；重复改进的第四条件在实证层面pending，不升级为已执行多轮core。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

- **`b570_06_ev_wf_0afc51b7af6ca1a424`**：NeoHorse-1 converts routing-harness trajectories to supervision, evaluates deficiencies to rebalance training data and applies routing-scheduled on-policy distillation with a fixed teacher on student prefixes. Future feedback generations are described; only one evaluation-selection-update pass is validated.
  - 来源版本：arXiv:2609.08183v1；定位：Capability-guided allocation; PDF p8; derived text lines 20-41 (one-based local extraction, not web-tool lines)；Routing-guided on-policy distillation; PDF p11; derived text lines 22-45 (one-based local extraction, not web-tool lines)；Single-pass limit; PDF p18; derived text lines 33-40 (one-based local extraction, not web-tool lines)；User-turn and loss unit; PDF p9; derived text lines 8-43 (one-based local extraction, not web-tool lines)；Benchmark/return-to-harness claims; PDF p18; derived text lines 19-32 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · Capability-guided allocation
**来源**：https://arxiv.org/pdf/2609.08183v1  
**实际版本**：arXiv:2609.08183v1  
**精确定位**：PDF p8; derived text lines 20-41 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0afc51b7af6ca1a424`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · Routing-guided on-policy distillation
**来源**：https://arxiv.org/pdf/2609.08183v1  
**实际版本**：arXiv:2609.08183v1  
**精确定位**：PDF p11; derived text lines 22-45 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0afc51b7af6ca1a424`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 测量 / 结果 · User-turn and loss unit
**来源**：https://arxiv.org/pdf/2609.08183v1  
**实际版本**：arXiv:2609.08183v1  
**精确定位**：PDF p9; derived text lines 8-43 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0afc51b7af6ca1a424`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 4 · 测量 / 结果 · Benchmark/return-to-harness claims
**来源**：https://arxiv.org/pdf/2609.08183v1  
**实际版本**：arXiv:2609.08183v1  
**精确定位**：PDF p18; derived text lines 19-32 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0afc51b7af6ca1a424`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 5 · 限制 · Single-pass limit
**来源**：https://arxiv.org/pdf/2609.08183v1  
**实际版本**：arXiv:2609.08183v1  
**精确定位**：PDF p18; derived text lines 33-40 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_06_ev_wf_0afc51b7af6ca1a424`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- Conclusion explicitly limits evidence to one pass and a subset of agent/coding/tool/instruction capabilities. Successive accumulation/broader transfer are future work; no new configuration or generation chain is certified.
- 一轮post-training收益不证明已执行跨世代循环或持续累积。
- 不能把路由器自身学习作为已实现更新；§6列为未来工作。
- OPD使用teacher，非无外部监督或自主训练算法自改。
- 一轮post-training收益不证明已执行跨世代循环或持续累积。; 不能把路由器自身学习作为已实现更新；§6列为未来工作。; OPD使用teacher，非无外部监督或自主训练算法自改。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_neohorse` · NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness · 2609.08183v1
  - https://arxiv.org/html/2609.08183v1；阅读深度：`未单列`。
- `b570_06_src_wf_0afc51b7af6ca1a424` · NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness · arXiv:2609.08183v1
  - https://arxiv.org/pdf/2609.08183v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Repeated accumulation after returning checkpoints to deployment remains untested.

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`pending_scope_only_no_configuration_claim_admission`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0afc51b7af6ca1a424 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
