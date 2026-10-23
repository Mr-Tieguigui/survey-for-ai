# AutoDataBench: Can Agents Write the Data That Feeds the Self-Improvement Loop?

> Benchmark/数据集/任务套件 · 2026 · `wf_129b00de4b5ac6f628`

**作者**：Haotian Luo, Haoyu Wang, Zeyu Qin, Huanjin Yao, Yibo Wang, Zhuotao Tian, Shuai Wang, Jiaya Jia  
**原文**：https://arxiv.org/abs/2609.35025  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已核官方全文评测对象、任务协议和限制；测量协议与被测研究方法分开。

## 2. 论文的核心内容与贡献

### configuration:cfg_autodatabench_per_artifact_acceptance_v1
adjacent评测协议：直接度量训练前单个任务的有效性、难度和行为覆盖；不把任务通过验收等同后训练增益或多轮模型自改。

**适用版本**：2609.35025v1；**原文定位**：§2.1–2.3 tool L86–119；§3.1 tool L120–123；Appendix A–E tool L210–292。
**引用权限**：`listed_configuration_scope_only`。

## 3. 任务、数据与评价设计

### AutoDataBench v1 pre-training per-artifact acceptance protocol
`cfg_autodatabench_per_artifact_acceptance_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单episode作者代理从原任务与目标模型轨迹交付一项可执行新任务；固定analyst生成隐藏mode rubric，固定judge与目标模型尝试共同决定分数。 |
| 改进过程与下一轮参与 | 协议评价交付任务的gate、目标模型难度带和隐藏rubric覆盖，三项相乘；不执行学生训练，也不依据训练后权重收益给单样本评分。 |
| 保留的状态及时间尺度 | 任务目录、轨迹和评分保留作评测记录；未证明作者跨episode学习或持续更新，亦未训练目标模型。 |
| 外部固定部分 | - suite/选定原任务、target model、analyst/judge、隐藏rubric、执行次数、gate规则、难度带与预算 |
| 评价与选择设置 | - **analyst and judge**：claude-opus-5 - **default author budget**：45 minutes per episode; 2 episodes per original - **difficulty band**：[0.125,0.75]; observed 1–4 successes of 6 - **original tasks**：24 fixed tasks; 8 from each of 3 suites - **score**：gate × difficulty × min(1, covered_modes/ceil(0.6×scoreable_modes)) - **suites**：- Terminal-Bench 4.0 - Terminal-Bench-Science - AutomationBench - **target attempts**：6 - **target model**：deepseek-v4-pro - **training run**：none |

**配置判定**：adjacent评测协议：直接度量训练前单个任务的有效性、难度和行为覆盖；不把任务通过验收等同后训练增益或多轮模型自改。

来源：https://arxiv.org/html/2609.35025v1；版本：2609.35025v1；定位：§2.1–2.3 tool L86–119；§3.1 tool L120–123；Appendix A–E tool L210–292。

## 4. 实验、评价协议与结果的可解释范围


- **analyst and judge**：claude-opus-5
- **default author budget**：45 minutes per episode; 2 episodes per original
- **difficulty band**：[0.125,0.75]; observed 1–4 successes of 6
- **original tasks**：24 fixed tasks; 8 from each of 3 suites
- **score**：gate × difficulty × min(1, covered_modes/ceil(0.6×scoreable_modes))
- **suites**：- Terminal-Bench 4.0 - Terminal-Bench-Science - AutomationBench
- **target attempts**：6
- **target model**：deepseek-v4-pro
- **training run**：none

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`db4_ev_cfg_autodatabench_per_artifact_acceptance_v1`**：adjacent评测协议：直接度量训练前单个任务的有效性、难度和行为覆盖；不把任务通过验收等同后训练增益或多轮模型自改。
  - 来源版本：unknown；定位：§2.1–2.3 tool L86–119；§3.1 tool L120–123；Appendix A–E tool L210–292；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 人工选定每suite8项且受host构建可行性筛选；不能外推整个suite或领域。
- gate和coverage部分由固定judge判断；verifier执行决定难度，不等于全部分数都是形式证明。
- 无质量信号episode排除并另计，不当零分；同原任务的episode先平均再suite聚合。
- 只有deepseek作者行与目标为同模型设定；即使同模型写任务也没有训练更新闭环。
- 主要费用表排除了作者调目标模型、官方K次尝试及judge等成本，不能当端到端总训练数据成本。
- 人工选定每suite8项且受host构建可行性筛选；不能外推整个suite或领域。; gate和coverage部分由固定judge判断；verifier执行决定难度，不等于全部分数都是形式证明。; 无质量信号episode排除并另计，不当零分；同原任务的episode先平均再suite聚合。; 只有deepseek作者行与目标为同模型设定；即使同模型写任务也没有训练更新闭环。; 主要费用表排除了作者调目标模型、官方K次尝试及judge等成本，不能当端到端总训练数据成本。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `db4_src_autodatabench` · 已存来源 · 2609.35025v1
  - https://arxiv.org/html/2609.35025v1；阅读深度：`selected_official_fulltext_protocol_and_limits`。

**证据深度**：original_abstract。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_129b00de4b5ac6f628 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
