# RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments

> 方法论文 · 2026 · `wf_697e14685d329eae62`

**作者**：Sibo Zhu, Shicheng Fan, Xinyue Wang, Wenyi Wu, Kun Zhou, Biwei Huang  
**原文**：https://arxiv.org/abs/2609.15364  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：actor、隔离context verifier和curriculum agent构成探索系统；actor使用持久memory。测试部署另冻结memory并禁curriculum/update；具体更新过程为：verifier直接读environment结果，actor增删改memory；curriculum根据memory和先前outcomes生成后继练习；BRS并行广探，DRS顺序加深；更新状态的保留与后继使用为：environment知识、程序/scripts、failure lessons由后继actor继承；每轮consolidate在下一练习提出前完成，记忆与反馈改变后续课程及执行。

## 2. 论文的核心内容与贡献

### configuration:cfg_rsiagent_broad_deep_memory_exploration_v1
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 verifier直接读environment结果，actor增删改memory；curriculum根据memory和先前outcomes生成后继练习；BRS并行广探，DRS顺序加深。

**适用版本**：2609.15364v1；**原文定位**：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### RSIAgent v1 broad/deep exploration with inherited memory
`cfg_rsiagent_broad_deep_memory_exploration_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | actor、隔离context verifier和curriculum agent构成探索系统；actor使用持久memory。测试部署另冻结memory并禁curriculum/update。 |
| 改进过程与下一轮参与 | verifier直接读environment结果，actor增删改memory；curriculum根据memory和先前outcomes生成后继练习；BRS并行广探，DRS顺序加深。 |
| 保留的状态及时间尺度 | environment知识、程序/scripts、failure lessons由后继actor继承；每轮consolidate在下一练习提出前完成，记忆与反馈改变后续课程及执行。 |
| 外部固定部分 | - GLM-5.3 actor；Kimi-K3 verifier/curriculum独立context - shared code-as-policy harness及verifier观察权限 - 测试阶段关闭curriculum和memory更新 |
| 评价与选择设置 | - **BRS**：nominal 8 projects; at most 4 concurrent; wave-boundary budget checks - **DRS**：sequential, curriculum stops when no further useful practice - **actor**：GLM-5.3 - **benchmarks**：82 OSWorld offline tasks, 67 ALE Near-term tasks - **verifier curriculum**：Kimi-K3 in separate contexts |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.1明确三个role及actor persistent memory。（状态：`supported`；定位：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232）。
- **更新由什么过程产生**：actor根据grounded verifier反馈添加、修改或删除memory。（状态：`supported`；定位：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232）。
- **状态怎样持久保留**：后继actor继承memory，冻结后亦供最终评价复用。（状态：`supported`；定位：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232）。
- **更新怎样进入后续改进**：curriculum读memory与previous outcomes形成后续练习；DRS先consolidate再生成下一task。（状态：`supported`；定位：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 verifier直接读environment结果，actor增删改memory；curriculum根据memory和先前outcomes生成后继练习；BRS并行广探，DRS顺序加深。

来源：https://arxiv.org/html/2609.15364v1；版本：2609.15364v1；定位：§3.1–3.2 inherited memory and feedback curriculum tool L193–218；§3.2 test freeze and §4.1 target-guided exploration setup tool L219–232。

## 4. 实验、评价协议与结果的可解释范围


- **BRS**：nominal 8 projects; at most 4 concurrent; wave-boundary budget checks
- **DRS**：sequential, curriculum stops when no further useful practice
- **actor**：GLM-5.3
- **benchmarks**：82 OSWorld offline tasks, 67 ALE Near-term tasks
- **verifier curriculum**：Kimi-K3 in separate contexts

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_rsiagent_broad_deep_memory_exploration_v1`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 verifier直接读environment结果，actor增删改memory；curriculum根据memory和先前outcomes生成后继练习；BRS并行广探，DRS顺序加深。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 该core配置是探索阶段，最终冻结memory部署本身不再闭合memory更新。
- 探索以target query为reference；不能称完全task-agnostic预训练或未接触target query的泛化。
- verifier是独立context模型而非绝对正确外部oracle；跨model公开baseline多来自报告，不是统一受控比较。
- 该core配置是探索阶段，最终冻结memory部署本身不再闭合memory更新。; 探索以target query为reference；不能称完全task-agnostic预训练或未接触target query的泛化。; verifier是独立context模型而非绝对正确外部oracle；跨model公开baseline多来自报告，不是统一受控比较。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_rsiagent` · RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments · 2609.15364v1
  - https://arxiv.org/html/2609.15364v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_697e14685d329eae62 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
