# EVOM: Agentic Meta-Evolution of Actor-Critic Architectures for Reinforcement Learning

> 方法论文 · 2026 · `wf_40d2b38870ca9fa9ee`

**作者**：Boyun Zhang, Chao Wang, Kai Wu  
**原文**：https://arxiv.org/abs/2606.26327  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：actor-critic架构程序群体；LLM设计器、选择规则和PPO内层训练器固定；具体更新过程为：固定LLM对elite架构进行mutation/crossover，100k PPO评估并top-N保留；新的elite架构实际作为后续生成父本与上下文。最终架构从头5M PPO训练；更新状态的保留与后继使用为：架构程序与反馈日志跨代保留；不认证PPO权重跨不同架构候选继承。

## 2. 论文的核心内容与贡献

### configuration:cfg_evom_actorcritic_nas
在声明的群体搜索状态反馈边界内，保留的新elite架构参与后续mutation/crossover，因此四项结构条件满足。core仅指bounded population-search，未认证LLM设计器权重或外部搜索规则自改、能力单调提升或无界增长。

**适用版本**：2606.26327v1；**原文定位**：v1 §3–4 Algorithm1 L83–149；v1 §5.1 L154–161；v1 §7 L207–211。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### EVOM: architecture evolution with low-fidelity PPO
`cfg_evom_actorcritic_nas` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | actor-critic架构程序群体；LLM设计器、选择规则和PPO内层训练器固定。 |
| 改进过程与下一轮参与 | 固定LLM对elite架构进行mutation/crossover，100k PPO评估并top-N保留；新的elite架构实际作为后续生成父本与上下文。最终架构从头5M PPO训练。 |
| 保留的状态及时间尺度 | 架构程序与反馈日志跨代保留；不认证PPO权重跨不同架构候选继承。 |
| 外部固定部分 | - LLM设计器与prompt templates - PPO evaluator - top-N selection - 可执行PolicyNet/ValueNet接口 - 任务/预算 |
| 评价与选择设置 | - **eval episodes**：3 - **final retraining**：from scratch - **final runs**：3 - **final timesteps**：5000000 - **generations**：20 - **low budget timesteps**：100000 - **mutation crossover**：N/2 each - **population**：16 |

**反馈闭环如何成立（按配置核查）**：
- **更新怎样进入后续改进**：EVOM v1 L114, L123–125 and L131–136: selected current elite programs enter next generation mutation/crossover prompt; updated population changes subsequent search operations.（状态：`supported`；定位：继承该配置来源定位）。

**配置判定**：在声明的群体搜索状态反馈边界内，保留的新elite架构参与后续mutation/crossover，因此四项结构条件满足。core仅指bounded population-search，未认证LLM设计器权重或外部搜索规则自改、能力单调提升或无界增长。

来源：https://arxiv.org/html/2606.26327v1；版本：2606.26327v1；定位：v1 §3–4 Algorithm1 L83–149；v1 §5.1 L154–161；v1 §7 L207–211。

## 4. 实验、评价协议与结果的可解释范围


- **eval episodes**：3
- **final retraining**：from scratch
- **final runs**：3
- **final timesteps**：5000000
- **generations**：20
- **low budget timesteps**：100000
- **mutation crossover**：N/2 each
- **population**：16

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4training_ev_cfg_evom_actorcritic_nas`**：在声明的群体搜索状态反馈边界内，保留的新elite架构参与后续mutation/crossover，因此四项结构条件满足。core仅指bounded population-search，未认证LLM设计器权重或外部搜索规则自改、能力单调提升或无界增长。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 低保真排名未必预测5M训练表现。
- 仅Ant-v4和HalfCheetah-v4；历史最好搜索曲线不同最终从头重训均值。
- PPO权重学习与LLM架构设计必须区分。
- 选段核查和有限任务配置；不是整篇逐段认证、跨领域保证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4training_src_w_evom` · 已存来源 · 2606.26327v1
  - https://arxiv.org/html/2606.26327v1；阅读深度：`targeted_primary_method_controls_and_limits`。

**证据深度**：original_abstract, targeted_primary_method_controls_limits_20261016。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_40d2b38870ca9fa9ee --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
