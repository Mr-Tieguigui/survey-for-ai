# Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks

> 评测方法/测量科学 · 2026 · `wf_bc74c0c45e8da61ba7`

**作者**：Xiaojing Sun, Yuhan Zeng, Zihua She, Xiao Wang  
**原文**：https://arxiv.org/abs/2609.33180  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定统计晋升器Reuse与LLM生成的scikit-learn候选分类pipeline分开；重复使用有限评价集S；具体更新过程为：对候选与incumbent的配对结果作单侧检验，按全部可能晋升历史分配错误预算，仅把晋升决定传回proposer；累积改进证书不传回搜索；更新状态的保留与后继使用为：incumbent、晋升决定历史与审计证书跨200轮保留；评分规则和错误预算公式预先固定。

## 2. 论文的核心内容与贡献

### configuration:cfg_reuse_decision_only_promotion_protocol_v1
adjacent评价协议；受测程序可持久更新，但不得把协议卡自动当作改进器自改的核心实现。

**适用版本**：v1；**原文定位**：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215；§2.2 Eq2–4, Algorithm1 tool L135–174；§5 tool L251–255。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### cfg_reuse_decision_only_promotion_protocol_v1
`cfg_reuse_decision_only_promotion_protocol_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定统计晋升器Reuse与LLM生成的scikit-learn候选分类pipeline分开；重复使用有限评价集S。 |
| 改进过程与下一轮参与 | 对候选与incumbent的配对结果作单侧检验，按全部可能晋升历史分配错误预算，仅把晋升决定传回proposer；累积改进证书不传回搜索。 |
| 保留的状态及时间尺度 | incumbent、晋升决定历史与审计证书跨200轮保留；评分规则和错误预算公式预先固定。 |
| 外部固定部分 | - 独立iid评价集S与开发数据分离 - decision-only反馈约束 - 检验、预算及候选上限 - Qwen2.5-7B-Instruct和候选空间 |
| 评价与选择设置 | - **candidate changes**：at most two among model family, feature subset, preprocessing, hyperparameters - **candidates per round max**：8 - **development examples**：20000 - **evaluation pool**：60000 - **heldout examples**：50000 - **proposer**：Qwen2.5-7B-Instruct - **reused evaluation sizes**：- 2000 - 10000 - **rounds**：200 - **seeds per size**：30 - **task**：Covertype cover type2 vs remaining classes - **training examples**：50000 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：固定评价/干预协议与受测自改程序分别定义。（状态：`supported`；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215）。
- **更新由什么过程产生**：本卡边界是研究者固定的评价协议，不是被评价程序的更新链。（状态：`contradicted`；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215）。
- **状态怎样持久保留**：协议保留跨轮评价记录与程序轨迹供纵向分析。（状态：`supported`；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215）。
- **更新怎样进入后续改进**：此配置未显示协议因自己所测结果自行改写其评价规则；规则随轮次作预定计算不等于规则自改。（状态：`contradicted`；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215）。

**配置判定**：adjacent评价协议；受测程序可持久更新，但不得把协议卡自动当作改进器自改的核心实现。

来源：https://arxiv.org/html/2609.33180v1；版本：v1；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215；§2.2 Eq2–4, Algorithm1 tool L135–174；§5 tool L251–255。

## 4. 实验、评价协议与结果的可解释范围


- **candidate changes**：at most two among model family, feature subset, preprocessing, hyperparameters
- **candidates per round max**：8
- **development examples**：20000
- **evaluation pool**：60000
- **heldout examples**：50000
- **proposer**：Qwen2.5-7B-Instruct
- **reused evaluation sizes**：- 2000 - 10000
- **rounds**：200
- **seeds per size**：30
- **task**：Covertype cover type2 vs remaining classes
- **training examples**：50000

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4safety_ev_cfg_reuse_decision_only_promotion_protocol_v1`**：对候选与incumbent的配对结果作单侧检验，按全部可能晋升历史分配错误预算，仅把晋升决定传回proposer；累积改进证书不传回搜索。
  - 来源版本：v1；定位：§2.1 assumptions1–2 tool L108–134；§3.1 tool L205–215；§2.2 Eq2–4, Algorithm1 tool L135–174；§5 tool L251–255；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 统计保证依赖独立iid评价样本与decision-only反馈；不扩展到暴露细分分数、开发泄漏、分布漂移或任意开放代理。
- 实测仅Covertype二分类；H上改进是总体改进的估计而非可知真实总体。
- SICA-style/DGM-style为共同分类任务内的搜索/选择规则，非原编码系统完整运行；PACE-style也不是PAST-Bench。
- 30 seeds中零false promotions是指定实验结果，不是任意新任务零风险。
- 证书及晋升协议不自改；受测pipeline更新不等于LLM权重或改进器自改。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4safety_src_reuse` · 已存来源 · v1
  - https://arxiv.org/html/2609.33180v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。
- `r4safety_src_reuse_limits` · 已存来源 · v1
  - https://arxiv.org/html/2609.33180v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。
- `r4safety_src_reuse_rule` · 已存来源 · v1
  - https://arxiv.org/html/2609.33180v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_methods_assumptions_execution_scope_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bc74c0c45e8da61ba7 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
