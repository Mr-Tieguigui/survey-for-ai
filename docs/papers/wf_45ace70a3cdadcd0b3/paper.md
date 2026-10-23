# RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

> 方法论文 · 2026 · `wf_45ace70a3cdadcd0b3`

**作者**：Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhuang, Yoonho Lee, Chengsong Huang, Han Yu, Zhongying CuiZhu, Yifei Ming, Huaxiu Yao, Burak Gokturk, Tomas Pfister, Chen-Yu Lee  
**原文**：https://arxiv.org/abs/2609.24972  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：冻结policy、可改harness H、proposer/analyst/leakage critic、finite evolve tasks、score/token-cost评估、retained diff/hypothesis历史及incumbent；具体更新过程为：proposer按前轮失败/全部candidate组件假设diff/score/cost/acceptance历史提案；annealed edit预算与stall探索调提案分配，critic先排显式task泄露，再依据noise-adjusted best score floor和cost条件选择下轮H；长期无用组件后续提议删除；更新状态的保留与后继使用为：harness代码及组件状态、所有被评candidate历史包含rejected negative evidence、S*及noise band跨round保存；新H执行得到后继轨迹并驱动下轮。

## 2. 论文的核心内容与贡献

### configuration:cfg_rrsi_regularized_harness_search_v1
finite harness/search-state反馈支持四条件；固定规则与冻结模型不否定C4。正则化为离散更新/选择类比，不认证参数范数优化或强RSI。

**适用版本**：2609.24972v1；**原文定位**：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### RRSI v1 sparse/evidence-aware proposals and conservative harness acceptance
`cfg_rrsi_regularized_harness_search_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结policy、可改harness H、proposer/analyst/leakage critic、finite evolve tasks、score/token-cost评估、retained diff/hypothesis历史及incumbent。 |
| 改进过程与下一轮参与 | proposer按前轮失败/全部candidate组件假设diff/score/cost/acceptance历史提案；annealed edit预算与stall探索调提案分配，critic先排显式task泄露，再依据noise-adjusted best score floor和cost条件选择下轮H；长期无用组件后续提议删除。 |
| 保留的状态及时间尺度 | harness代码及组件状态、所有被评candidate历史包含rejected negative evidence、S*及noise band跨round保存；新H执行得到后继轨迹并驱动下轮。 |
| 外部固定部分 | - frozen backbone和通常同模型proposer/analyst/critic - evolve-set及protected transfer sets - noise/cost/annealing/pruning rules；并非正式L0/L1/L2参数正则训练 |
| 评价与选择设置 | - **main domains**：coding/workspace/engineering - **main policy**：Claude Opus4.8 frozen - **proposal analyst critic**：Claude Opus4.8 - **selection**：explicit leakage screen; S(candidate)>=S*−δ; for gain>δ cost growth<=beta0+beta1*gain |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2–3明确policy/harness/evaluator边界。（状态：`supported`；定位：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238）。
- **更新由什么过程产生**：proposer从自身轨迹反馈生成源码改动。（状态：`supported`；定位：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238）。
- **状态怎样持久保留**：incumbent和所有candidate证据跨round保留。（状态：`supported`；定位：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238）。
- **更新怎样进入后续改进**：历史改变后继假设/探索/删除，accepted H决定新轨迹和下一次改进反馈。（状态：`supported`；定位：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238）。

**配置判定**：finite harness/search-state反馈支持四条件；固定规则与冻结模型不否定C4。正则化为离散更新/选择类比，不认证参数范数优化或强RSI。

来源：https://arxiv.org/html/2609.24972v1；版本：2609.24972v1；定位：§2 generic harness loop tool L94–108；§3.1–3.3 history/proposal/leakage tool L112–136；§3.3–4.1 acceptance/pruning/setup tool L140–168；Limitations tool L236–238。

## 4. 实验、评价协议与结果的可解释范围


- **main domains**：coding/workspace/engineering
- **main policy**：Claude Opus4.8 frozen
- **proposal analyst critic**：Claude Opus4.8
- **selection**：explicit leakage screen; S(candidate)>=S*−δ; for gain>δ cost growth<=beta0+beta1*gain

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_rrsi_regularized_harness_search_v1`**：finite harness/search-state反馈支持四条件；固定规则与冻结模型不否定C4。正则化为离散更新/选择类比，不认证参数范数优化或强RSI。 proposer按前轮失败/全部candidate组件假设diff/score/cost/acceptance历史提案；annealed edit预算与stall探索调提案分配，critic先排显式task泄露，再依据noise-adjusted best score floor和cost条件选择下轮H；长期无用组件后续提议删除。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 有限evolve set反复自适应使用及regularization hyperparameters，效果依赖反馈/预算。
- workspace部分LLM judge，工程设计/代码test为另一裁判类型，不混作所有任务全deterministic。
- 只核gain>δ的cost门及score floor；noise-band内细分acceptance AppendixC.3本次未核，不能把简化概述冒充完整执行算法。
- 跨领域/模型transfer不等于任意架构、tool ecosystem或更长运行的普遍保证；未更新model weights。
- 有限evolve set反复自适应使用及regularization hyperparameters，效果依赖反馈/预算。; workspace部分LLM judge，工程设计/代码test为另一裁判类型，不混作所有任务全deterministic。; 只核gain>δ的cost门及score floor；noise-band内细分acceptance AppendixC.3本次未核，不能把简化概述冒充完整执行算法。; 跨领域/模型transfer不等于任意架构、tool ecosystem或更长运行的普遍保证；未更新model weights。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_rrsi` · RRSI: Regularized Recursive Self-Improvement of Agent Harnesses · 2609.24972v1
  - https://arxiv.org/html/2609.24972v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_45ace70a3cdadcd0b3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
