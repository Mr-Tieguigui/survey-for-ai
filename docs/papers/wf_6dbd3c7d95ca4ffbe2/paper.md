# Adaptive Reinforcement Learning through Evolving Self-Modifying Neural Networks

> 方法论文 · 2020 · `wf_6dbd3c7d95ca4ffbe2`

**作者**：Samuel Schmidgall  
**原文**：https://arxiv.org/abs/2006.05832  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
研究演化的自修改可塑网络应对四足机器人肢体损坏，在线突触变化用于任务适应；外层演化、在线可塑规则和跨任务保留需全文分开配置。

## 2. 论文的核心内容与贡献

### configuration:cfg_evolved_neuromodulation_ant_es
在线塑性状态H反馈参与下一时步调制与动作，四结构条件在有寿命的plastic-policy边界内满足；不是ES顶层算法自行改写或跨episode持续自主增长。

**适用版本**：2006.05832v1；**原文定位**：PDF physical p1 §2.1 Eqs1–2 tool L60–77；PDF physical p2 §§2.1–2.3 tool L80–120；PDF physical p2 §3 tool L123–136。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_6dbd3c7d95ca4ffbe2`
研究演化的自修改可塑网络应对四足机器人肢体损坏，在线突触变化用于任务适应；外层演化、在线可塑规则和跨任务保留需全文分开配置。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Evolved neuromodulation: ES-trained plastic policy in Crippled-Ant
`cfg_evolved_neuromodulation_ant_es` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 策略慢权重w、塑性系数alpha、单层neuromodulator M和在线Hebbian trace H；外层OpenAI-ES训练这些参数。 |
| 改进过程与下一轮参与 | 动作激活由w+alphaH生成，H按M(x)调制前后突触活动递推并clip到[-1,1]；更新H改变后续动作和下一次自身更新。 |
| 保留的状态及时间尺度 | H在一次环境session的多时步保存；慢参数由ES fitness更新保留。未确认H跨独立episode继承。 |
| 外部固定部分 | - ES更新算法及环境reward - Hebbian递推形态和clip - 每次session随机损伤环境分布 |
| 评价与选择设置 | - **actuators**：12 - **comparator**：PPO vs OpenAI-ES, plastic vs fixed network - **environment**：Crippled-Ant - **state dim**：111 - **test**：5 trained models, mean over100 episodes |

**配置判定**：在线塑性状态H反馈参与下一时步调制与动作，四结构条件在有寿命的plastic-policy边界内满足；不是ES顶层算法自行改写或跨episode持续自主增长。

来源：https://arxiv.org/pdf/2006.05832v1；版本：2006.05832v1；定位：PDF physical p1 §2.1 Eqs1–2 tool L60–77；PDF physical p2 §§2.1–2.3 tool L80–120；PDF physical p2 §3 tool L123–136。

## 4. 实验、评价协议与结果的可解释范围


- **actuators**：12
- **comparator**：PPO vs OpenAI-ES, plastic vs fixed network
- **environment**：Crippled-Ant
- **state dim**：111
- **test**：5 trained models, mean over100 episodes

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_6dbd3c7d95ca4ffbe2`**：研究演化的自修改可塑网络应对四足机器人肢体损坏，在线突触变化用于任务适应；外层演化、在线可塑规则和跨任务保留需全文分开配置。
  - 来源版本：2006.05832v1；定位：Atom entry http://arxiv.org/abs/2006.05832v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_evolved_neuromodulation_ant_es`**：在线塑性状态H反馈参与下一时步调制与动作，四结构条件在有寿命的plastic-policy边界内满足；不是ES顶层算法自行改写或跨episode持续自主增长。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 2页GECCO companion论文，未给完整可复现实验配置与置信区间。
- 作者比较ES/PPO和塑性/固定网络，wall-clock非全场景样本效率；不认证所有RL均缺在线适应。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_evolved_neuromodulation` · 已存来源 · 2006.05832v1
  - https://arxiv.org/pdf/2006.05832v1；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `s18_role_src_4a72693a250c423c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-modifying%22+OR+ti%3A%22self-referential%22+OR+ti%3A%22self-rewriting%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6dbd3c7d95ca4ffbe2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
