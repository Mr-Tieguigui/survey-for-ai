# Eliminating Meta Optimization Through Self-Referential Meta Learning

> 方法论文 · 2022 · `wf_1f30dff0c96d60fb96`

**作者**：Louis Kirsch, Jürgen Schmidhuber  
**原文**：https://arxiv.org/abs/2212.14392  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Fitness Monotonic Execution empirical self-referential weight modification; theoretical expressivity analysis separately bounded.

## 2. 论文的核心内容与贡献

### configuration:cfg_fme_selfreferential_weights
在明确的自指权重和FME状态保留边界内满足四个结构条件；外部FME调度和网络结构仍固定，不据此声称无外部设计或无界增长。

**适用版本**：2212.14392v1；**原文定位**：PDF physical pp2–3 §2.2 Observation2.2；PDF physical pp3–4 §3 Fitness Monotonic Execution；PDF physical p4 Algorithm 1 and Eqs1–4；PDF physical pp4–5 §4 Experiments；PDF physical p5 §6 Limitations。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### FME with self-referential outer-product neural states
`cfg_fme_selfreferential_weights` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 自指网络变量φ及FME保留的候选状态集合Φ；架构、绩效评价和计算时间分配器在边界外固定。 |
| 改进过程与下一轮参与 | 当前W生成动作、key、query和学习率并以外积delta更新自身；更新后的W继续生成未来更新。FME按平均绩效单调分配执行概率。 |
| 保留的状态及时间尺度 | 一次FME运行内，更新后的φ进入Φ并可被再次执行；LRU会移除较旧候选，未认证跨独立实验永久保留。 |
| 外部固定部分 | - 自指网络架构和外积delta形式 - 环境/奖励 - FME概率分配和LRU分桶规则 - 执行片段长度与实验预算 |
| 评价与选择设置 | - **initialization**：random self-referential network states - **performance claim**：原文报告的小规模实证；本次不建立跨论文排名 - **tasks**：- 2-armed stationary bandit - Cartpole - nonstationary 2-armed bandit |
| 实际状态组件 | - 自指权重W，含输出、key、query和更新率的生成参数 - 候选φ与按绩效分桶的LRU保留集合Φ |

**配置判定**：在明确的自指权重和FME状态保留边界内满足四个结构条件；外部FME调度和网络结构仍固定，不据此声称无外部设计或无界增长。

来源：https://arxiv.org/pdf/2212.14392v1；版本：2212.14392v1；定位：PDF physical pp2–3 §2.2 Observation2.2；PDF physical pp3–4 §3 Fitness Monotonic Execution；PDF physical p4 Algorithm 1 and Eqs1–4；PDF physical pp4–5 §4 Experiments；PDF physical p5 §6 Limitations。

## 4. 实验、评价协议与结果的可解释范围


- **initialization**：random self-referential network states
- **performance claim**：原文报告的小规模实证；本次不建立跨论文排名
- **tasks**：- 2-armed stationary bandit - Cartpole - nonstationary 2-armed bandit

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`oct15_root_ev_fme_method`**：原文§3–4给出自指W更新、FME保留与按绩效分配执行，以及小规模任务实证。
  - 来源版本：unknown；定位：PDF physical pp2–3 §2.2 Observation2.2；PDF physical pp3–4 §3 Fitness Monotonic Execution；PDF physical p4 Algorithm 1 and Eqs1–4；PDF physical pp4–5 §4 Experiments；PDF physical p5 §6 Limitations；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- §2.2为充分表达条件下的表示等价，不是所有架构效率、优化难度或实测性能等价。
- 作者§6明确实证仍minimalistic；架构修改和候选通信仅提出的扩展。
- 避免显式meta参数优化不等于没有固定选择/计算资源分配规则。
- 在明确的自指权重和FME状态保留边界内满足四个结构条件；外部FME调度和网络结构仍固定，不据此声称无外部设计或无界增长。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `oct15_root_src_w_selfreferential_fme` · 已存来源 · 2212.14392v1
  - https://arxiv.org/pdf/2212.14392v1；阅读深度：`selected_primary_method_and_limits_passages`。

**证据深度**：original_abstract。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1f30dff0c96d60fb96 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
