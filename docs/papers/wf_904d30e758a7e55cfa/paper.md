# Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

> 综合系统/智能体 · 2026 · `wf_904d30e758a7e55cfa`

**作者**：Alberto Pepe, Chien-Yu Lin, Despoina Magka, Bilge Acun, Thomas Simon Foster, Yannan Nellie Wu, Anton Protopopov, Carole-Jean Wu, Yoram Bachrach  
**原文**：https://arxiv.org/abs/2605.15871  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定AIRA-dojo/LM、16层primitive字符串、候选树、validation与独立scorer；具体更新过程为：draft5候选，选highest-validation node，读parent理由/分数后improve；错误debug；训练proxy后继续搜索；更新状态的保留与后继使用为：架构节点、代码与评分跨search steps保存供选父。

## 2. 论文的核心内容与贡献

### configuration:cfg_aira_compose_greedy_proxy_search_v1
greedy Compose候选树保留与选父反馈满足有界四条件；one-shot没有这一反馈循环。

**适用版本**：2605.15871v1；**原文定位**：§2 tool L96–116；§3 tool L139–155；§5 tool L174–179；limits tool L365–369。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_aira_design_greedy_code_search_v1
greedy Design保留可运行代码及validation反馈进入下一提案，四结构条件在代码搜索边界成立，不认证one-shot或无界科学创新。

**适用版本**：2605.15871v1；**原文定位**：§2 tool L96–116；§4–5 tool L156–177；limits tool L370–371。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### AIRA-Compose: greedy tree over primitive arrangements
`cfg_aira_compose_greedy_proxy_search_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定AIRA-dojo/LM、16层primitive字符串、候选树、validation与独立scorer。 |
| 改进过程与下一轮参与 | draft5候选，选highest-validation node，读parent理由/分数后improve；错误debug；训练proxy后继续搜索。 |
| 保留的状态及时间尺度 | 架构节点、代码与评分跨search steps保存供选父。 |
| 外部固定部分 | - greedy/draft/debug/improve/analyze规则 - proxy任务/primitive集合 - 非agentic aggregation/extrapolation |

**配置判定**：greedy Compose候选树保留与选父反馈满足有界四条件；one-shot没有这一反馈循环。

来源：https://arxiv.org/html/2605.15871v1；版本：2605.15871v1；定位：§2 tool L96–116；§3 tool L139–155；§5 tool L174–179；limits tool L365–369。

### AIRA-Design: greedy model.py/train.py improvement
`cfg_aira_design_greedy_code_search_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定AIRA-dojo/LM、可写model.py或train.py、solution tree和validation。 |
| 改进过程与下一轮参与 | 沿高validation候选debug/improve新模型机制或训练脚本；LRA实现JAX模型，Autoresearch改训练/架构超参。 |
| 保留的状态及时间尺度 | 工作脚本和理由/评分作为下一parent，固定搜索LM不更新。 |
| 外部固定部分 | - 只读数据/tokenizer/evaluation harness - greedy operators - GPU/time预算 |

**配置判定**：greedy Design保留可运行代码及validation反馈进入下一提案，四结构条件在代码搜索边界成立，不认证one-shot或无界科学创新。

来源：https://arxiv.org/html/2605.15871v1；版本：2605.15871v1；定位：§2 tool L96–116；§4–5 tool L156–177；limits tool L370–371。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_aira_compose_greedy_proxy_search_v1`**：greedy Compose候选树保留与选父反馈满足有界四条件；one-shot没有这一反馈循环。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`r8a_ev_cfg_aira_design_greedy_code_search_v1`**：greedy Design保留可运行代码及validation反馈进入下一提案，四结构条件在代码搜索边界成立，不认证one-shot或无界科学创新。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- small proxy不能保证large-scale排名，aggregation/scaling仍非agentic。
- L146聚合读取跨步骤test scores，因此整个扩大pipeline不能称从未test选择。
- 发现架构未重新部署成搜索LM，不认证基础代理权重自升级。
- LRA held-out test只最终训评；Autoresearch指标是validation BPB，不能冒称另有未见final test。
- LRA多为已有机制组合；扩展可调空间使弱模型退化。
- 单GPU5分钟训练指标不等于总研究成本或大规模收益。
- - small proxy不能保证large-scale排名，aggregation/scaling仍非agentic。 - L146聚合读取跨步骤test scores，因此整个扩大pipeline不能称从未test选择。 - 发现架构未重新部署成搜索LM，不认证基础代理权重自升级。
- - LRA held-out test只最终训评；Autoresearch指标是validation BPB，不能冒称另有未见final test。 - LRA多为已有机制组合；扩展可调空间使弱模型退化。 - 单GPU5分钟训练指标不等于总研究成本或大规模收益。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_aira_architectures_v1` · 已存来源 · 2605.15871v1
  - https://arxiv.org/html/2605.15871v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_904d30e758a7e55cfa --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
