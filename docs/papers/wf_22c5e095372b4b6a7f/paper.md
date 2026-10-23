# Evaluating Collective Behaviour of Hundreds of LLM Agents

> 评测方法/测量科学 · 2026 · `wf_22c5e095372b4b6a7f`

**作者**：Richard Willis, Jianing Zhao, Yali Du, Joel Z. Leibo  
**原文**：https://arxiv.org/abs/2602.16662  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
该评测先让LLM写合作/剥削attitude策略，再把策略编码为game-history到Cooperate/Defect算法；比较social dilemmas中群体福利及模拟cultural evolution。基因是用户的model/attitude选择，复制/变异/从固定池重采策略并不是对LLM权重训练或生成新改进算子。

## 2. 论文的核心内容与贡献

### role:r14_role_collective
该评测先让LLM写合作/剥削attitude策略，再把策略编码为game-history到Cooperate/Defect算法；比较social dilemmas中群体福利及模拟cultural evolution。基因是用户的model/attitude选择，复制/变异/从固定池重采策略并不是对LLM权重训练或生成新改进算子。

**适用版本**：2602.16662v1；**原文定位**：§4.1 generated strategy/selection bias tool L181–192；§5.1 selfplay/welfare tool L219–224；§6.1 cultural genes/selection/stopping tool L281–300；§7 conclusion/scope tool L326–330。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：与RSI群体选择/协同安全相关的外部群体实验背景；本批不把gene frequency变化当模型自训练。
- **metrics**：- mean normalized reward=总game reward/agents/rounds，衡量social welfare - cultural equilibrium按终止时占比最大gene；终止一gene≥75%或200generations，非通用智能分数
- **selection and reuse**：每model/attitude512策略；不能实现的一些小模型生成600描述只保留成功实现，可能偏简单。文化选择按payoff复制gene、10%mutation并重新sample strategy。
- **split and visibility**：固定生成strategy pools用于后续抽样，非train/test学习拆分；self-play每组从对应attitude池无放回采样。
- **task or data unit**：六模型×两attitude的生成策略池；Public Goods/Collective Risk/Common Pool三类game，self-play群体n=4/16/64/256；文化人口512。
- **unknowns**：- 真实用户选择行为/长期社会外部效度unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_collective`**：该评测先让LLM写合作/剥削attitude策略，再把策略编码为game-history到Cooperate/Defect算法；比较social dilemmas中群体福利及模拟cultural evolution。基因是用户的model/attitude选择，复制/变异/从固定池重采策略并不是对LLM权重训练或生成新改进算子。
  - 来源版本：2602.16662v1；定位：§4.1 generated strategy/selection bias tool L181–192；§5.1 selfplay/welfare tool L219–224；§6.1 cultural genes/selection/stopping tool L281–300；§7 conclusion/scope tool L326–330；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 自然语言attitude不另定义，模型解释和game framing可能影响结果。
- 执行安全测试过滤并重生成实现，故不是无选择偏差的原始模型策略分布。
- 三社会博弈和模拟人类选agent，不代表真实社会或无限群体演化；代码逻辑错误刻意不手修。
- 自然语言attitude不另定义，模型解释和game framing可能影响结果。; 执行安全测试过滤并重生成实现，故不是无选择偏差的原始模型策略分布。; 三社会博弈和模拟人类选agent，不代表真实社会或无限群体演化；代码逻辑错误刻意不手修。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_collective` · Evaluating Collective Behaviour of Hundreds of LLM Agents · 2602.16662v1
  - https://arxiv.org/html/2602.16662v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_22c5e095372b4b6a7f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
