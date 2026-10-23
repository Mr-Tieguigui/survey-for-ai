# Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution

> 方法论文 · 2026 · `wf_efa518a42c1565bcee`

**作者**：Changzhi Liu, Yilun Liu, Sikuan Yan, Volker Tresp, Yunpu Ma  
**原文**：https://arxiv.org/abs/2608.07645  
**研究分支**：群体、自博弈与开放式探索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：coding-agent scaffold archive、task trajectory/outcome证据、HGM-style Thompson evaluation/expansion分配、三种diagnostic editing operator及固定软件任务验证；具体更新过程为：扩展时按可用证据选择CM单失败、RM同agent跨任务比较或CH不同agent同任务比较；target自己诊断并改代码，新child挂primary lineage。failed-task pool增加后续采样的跨lineage任务重叠；archive更新后影响后续选择和诊断；更新状态的保留与后继使用为：agent代码、任务成功失败counts、trajectory/outcome、clade统计及failed-task pool跨search expansion存续；CH是诊断性适应，不是直接splice reference源码。

## 2. 论文的核心内容与贡献

### configuration:cfg_mgm_comparative_archive_coding_agent_v1
archive/agent-code/比较证据闭环支持有界四条件；Mendel隐喻不是字面遗传交叉，不认证强RSI或无界更善改进。

**适用版本**：2608.07645v1；**原文定位**：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Mendel Gödel Machine v1 archive comparative-evidence code evolution
`cfg_mgm_comparative_archive_coding_agent_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | coding-agent scaffold archive、task trajectory/outcome证据、HGM-style Thompson evaluation/expansion分配、三种diagnostic editing operator及固定软件任务验证。 |
| 改进过程与下一轮参与 | 扩展时按可用证据选择CM单失败、RM同agent跨任务比较或CH不同agent同任务比较；target自己诊断并改代码，新child挂primary lineage。failed-task pool增加后续采样的跨lineage任务重叠；archive更新后影响后续选择和诊断。 |
| 保留的状态及时间尺度 | agent代码、任务成功失败counts、trajectory/outcome、clade统计及failed-task pool跨search expansion存续；CH是诊断性适应，不是直接splice reference源码。 |
| 外部固定部分 | - Thompson selection/tree-search policies与operator资格/权重规则 - 任务验证和预算 - main Qwen3.6-35B-A3B backbone；未推断参数训练 |
| 评价与选择设置 | - **backbone**：Qwen3.6-35B-A3B - **main budget**：200 phi evaluations;24 Phi expansions - **main sets**：SWE-bench Verified60 and Polyglot60 - **private tests**：not available during evolution |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2–3定义agent、archive及evaluation/expansion边界。（状态：`supported`；定位：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261）。
- **更新由什么过程产生**：被选agent按真实trajectory差异编辑后继scaffold。（状态：`supported`；定位：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261）。
- **状态怎样持久保留**：代码child和失败/成功历史保留在archive。（状态：`supported`；定位：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261）。
- **更新怎样进入后续改进**：新增证据更新node/clade选择、failed task采样以及下次CM/RM/CH的适用性。（状态：`supported`；定位：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261）。

**配置判定**：archive/agent-code/比较证据闭环支持有界四条件；Mendel隐喻不是字面遗传交叉，不认证强RSI或无界更善改进。

来源：https://arxiv.org/html/2608.07645v1；版本：2608.07645v1；定位：§2–3 archive/evidence tool L102–125；§3.1 three operators tool L131–162；§3.2 sampling/selection tool L168–184；Limitations tool L315–323；§5.1 benchmark/budget tool L247–261。

## 4. 实验、评价协议与结果的可解释范围


- **backbone**：Qwen3.6-35B-A3B
- **main budget**：200 phi evaluations;24 Phi expansions
- **main sets**：SWE-bench Verified60 and Polyglot60
- **private tests**：not available during evolution

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_mgm_comparative_archive_coding_agent_v1`**：archive/agent-code/比较证据闭环支持有界四条件；Mendel隐喻不是字面遗传交叉，不认证强RSI或无界更善改进。 扩展时按可用证据选择CM单失败、RM同agent跨任务比较或CH不同agent同任务比较；target自己诊断并改代码，新child挂primary lineage。failed-task pool增加后续采样的跨lineage任务重叠；archive更新后影响后续选择和诊断。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 主要演化为两个固定60-task子集、200evaluations和24expansions；full/heldout checks与同子集演化分列。
- 依赖历史积累和task overlap，早期可退化为单trajectory基线。
- LLM诊断不保证edit正确/泛化；additive fitness surrogate分析不证明真实scaffold的所有性质。
- 成本限制独立seed和参数扫描，公开benchmarks不外推非编码或开放维护。
- 主要演化为两个固定60-task子集、200evaluations和24expansions；full/heldout checks与同子集演化分列。; 依赖历史积累和task overlap，早期可退化为单trajectory基线。; LLM诊断不保证edit正确/泛化；additive fitness surrogate分析不证明真实scaffold的所有性质。; 成本限制独立seed和参数扫描，公开benchmarks不外推非编码或开放维护。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_mgm` · Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution · 2608.07645v1
  - https://arxiv.org/html/2608.07645v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_efa518a42c1565bcee --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
