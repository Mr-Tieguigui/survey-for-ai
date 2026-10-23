# Self-Healing Harness for Runtime Oversight of Agent Self-Modification

> 方法论文 · 2026 · `wf_d35a290c707af8b570`

**作者**：Sina Tayebati, Divake Kumar, Nastaran Darabi, Ranganath Krishnan, Amit Ranjan Trivedi  
**原文**：https://arxiv.org/abs/2609.24130  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Self-Healing Harness 允许代理提规则，由外部运行门控按触发失败改善、保护例不回归及累计规则复测决定跨 episode 持久化；回放和前向试验强度不同，模型权重固定，应优先核上下文自改配置。

## 2. 论文的核心内容与贡献

### configuration:cfg_selfheal_agent_rule_workspace_v1
声明agent+外部规则状态边界内的结构core；固定guard不作为自改对象，不认证安全、因果增益或无限改进。

**适用版本**：v1；**原文定位**：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183；Validate and guard tool L97–105；Limitations tool L197–205；Appendix Algorithm1 tool L358–430。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_d35a290c707af8b570`
Self-Healing Harness 允许代理提规则，由外部运行门控按触发失败改善、保护例不回归及累计规则复测决定跨 episode 持久化；回放和前向试验强度不同，模型权重固定，应优先核上下文自改配置。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Self-Healing Harness agent + evolving rule workspace
`cfg_selfheal_agent_rule_workspace_v1` · implemented_persistent_rule_adaptation

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定模型agent与其自写external operating-rule集合R；读入规则影响agent下一轮行为及新rule编写；外部detect/notice/validation/guard固定。 |
| 改进过程与下一轮参与 | 收到notice的agent检查trace并读取scope rules后写candidate；候选在试验中临时有效，replay非退化检查或弱forward trial决定跨episode持久；规则再影响后续agent turn和再次修复。 |
| 保留的状态及时间尺度 | 晋升规则跨episode保留，触发案例/trace与活动集合继续用于新提案和corpus guard。 |
| 外部固定部分 | - agent模型权重与root protocol - 分层度量、gate阈值和per-turn barrier - replay/forward admission与corpus guard代码 - 检索topk与scope规则 |
| 评价与选择设置 | - **benchmarks**：- AppWorld - Terminal-Bench - tau2 airline/retail - **failure cases max**：3 - **forward sessions**：3 - **gate window**：10 - **matched pairs**：16 - **models**：4 - **promotion margin**：0.05 - **protected cases max**：2 - **regression margin**：0.05 - **seed**：1 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：runtime和R分离，R是可变policy-inducing context（状态：`supported`；定位：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183）。
- **更新由什么过程产生**：agent自己读取notice与scope后写candidate rule（状态：`supported`；定位：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183）。
- **状态怎样持久保留**：promotion决定规则跨episode保留（状态：`supported`；定位：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183）。
- **更新怎样进入后续改进**：Algorithm1下一轮用R组成context，并在新rule编写前读取scope；变化规则参与持续修复链，guard本身不变（状态：`supported`；定位：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183）。

**配置判定**：声明agent+外部规则状态边界内的结构core；固定guard不作为自改对象，不认证安全、因果增益或无限改进。

来源：https://arxiv.org/html/2609.24130v1；版本：v1；定位：The Self-Healing Harness tool L85–102；Results RQ2–3 tool L144–183；Validate and guard tool L97–105；Limitations tool L197–205；Appendix Algorithm1 tool L358–430。

## 4. 实验、评价协议与结果的可解释范围


- **benchmarks**：- AppWorld - Terminal-Bench - tau2 airline/retail
- **failure cases max**：3
- **forward sessions**：3
- **gate window**：10
- **matched pairs**：16
- **models**：4
- **promotion margin**：0.05
- **protected cases max**：2
- **regression margin**：0.05
- **seed**：1

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_d35a290c707af8b570`**：Self-Healing Harness 允许代理提规则，由外部运行门控按触发失败改善、保护例不回归及累计规则复测决定跨 episode 持久化；回放和前向试验强度不同，模型权重固定，应优先核上下文自改配置。
  - 来源版本：2609.24130v1；定位：Atom entry http://arxiv.org/abs/2609.24130v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5safe_ev_cfg_selfheal_agent_rule_workspace_v1`**：收到notice的agent检查trace并读取scope rules后写candidate；候选在试验中临时有效，replay非退化检查或弱forward trial决定跨episode持久；规则再影响后续agent turn和再次修复。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- core只对应agent+R明确边界；不声称模型权重、judge或external admission/guard自主改写。
- 最多3 failure+2未按相关性排序protected case的replay，有限测量非因果证书；更广泛行为可能漏检。
- forward fallback仅3后续session且无protected-case分量，默认p0=1；TerminalBench全部forward无replay测试，不能把非退化保证移植过去。
- tau2 airline存在turn/message-hop预算错配而较弱验证；不同路径比例是观察而非消融。
- 仅seed1，16对比仅2区间排除0；未跑立即接受同rule集合的B-prime臂，不能归因全部收益为预准入gating。
- online adaptation非held-out transfer；累积检索稀释可使live漂移未由replay复现；不是普遍alignment或安全保证。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5safe_src_selfheal` · 已存来源 · v1
  - https://arxiv.org/html/2609.24130v1；阅读深度：`selected_primary_methods_version_changes_assumptions_and_limits`。
- `r5safe_src_selfheal_loop` · 已存来源 · v1
  - https://arxiv.org/html/2609.24130v1；阅读深度：`selected_primary_methods_version_changes_assumptions_and_limits`。
- `s18_role_src_d6f9c35358996ce4` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22intelligence+explosion%22+OR+ti%3A%22recursive+self-improvement%22+OR+ti%3A%22reflective+oracle%22+OR+ti%3A%22self+modification%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_methods_version_changes_assumptions_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d35a290c707af8b570 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
