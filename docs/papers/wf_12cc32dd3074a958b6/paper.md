# TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking

> Benchmark/数据集/任务套件 · 2026 · `wf_12cc32dd3074a958b6`

**作者**：Yu Cheng, Yongkang Hu, Jiuan Zhou, Yushuo Zhang, Yihang Chen, Huichi Zhou, Mingang Chen, Zhizhong Zhang, Kun Shao, Yuan Xie, Zhaoxia Yin  
**原文**：https://arxiv.org/abs/2602.03224  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
adjacent评测协议：测持久状态的演化不等于协议自己递归改进；TAME双记忆算法是另一个待单列配置。

## 2. 论文的核心内容与贡献

### configuration:cfg_tame_trust_memevo_protocol_v1
adjacent评测协议：测持久状态的演化不等于协议自己递归改进；TAME双记忆算法是另一个待单列配置。

**适用版本**：v1；**原文定位**：§3.2–3.3 tool L114–128；§5.1 tool L203–209；Appendix B tool L402–406。
**引用权限**：`listed_configuration_scope_only`。

## 3. 任务、数据与评价设计

### cfg_tame_trust_memevo_protocol_v1
`cfg_tame_trust_memevo_protocol_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定Trust-Memevo双轨评价：良性任务演化集与配对信任测量集；受测代理记忆可变，协议本身固定。 |
| 改进过程与下一轮参与 | 对math/science/tool-use中的任务能力及五维信任随经验积累的变化作配对测量；作者列DC、Memento、ReasoningBank及其prompt/guard变体。 |
| 保留的状态及时间尺度 | 保留受测系统的跨任务经验和纵向测量记录；不是评价器在测试中自主改写评分协议。 |
| 外部固定部分 | - 良性任务序列、信任测试集、五维评分 - 研究者设定的模型和基线实现 - constitutional准则及成功判定 |

**配置判定**：adjacent评测协议：测持久状态的演化不等于协议自己递归改进；TAME双记忆算法是另一个待单列配置。

来源：https://arxiv.org/html/2602.03224v1；版本：v1；定位：§3.2–3.3 tool L114–128；§5.1 tool L203–209；Appendix B tool L402–406。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4bench_ev_cfg_tame_trust_memevo_protocol_v1`**：对math/science/tool-use中的任务能力及五维信任随经验积累的变化作配对测量；作者列DC、Memento、ReasoningBank及其prompt/guard变体。
  - 来源版本：v1；定位：§3.2–3.3 tool L114–128；§5.1 tool L203–209；Appendix B tool L402–406；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 作者报告Math领域退化不明显，不能把misevolution写成所有域普遍单调衰退。
- 信任下降与任务提升是有限设置观察；不接受§3中概率收敛表达为已证明的一般定理。
- 此配置没有宣称评测ExpeL、A-MEM、MINDSET或SEA-Eval。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4bench_src_tame` · 已存来源 · v1
  - https://arxiv.org/html/2602.03224v1；阅读深度：`selected_original_benchmark_protocol_and_limits`。

**证据深度**：unknown。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_12cc32dd3074a958b6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
