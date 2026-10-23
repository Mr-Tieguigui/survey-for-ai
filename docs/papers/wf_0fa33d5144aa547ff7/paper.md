# MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution

> 方法论文 · 2026 · `wf_0fa33d5144aa547ff7`

**作者**：Zefeng Wang, Minxi Yan, Jinhe Bi, Sikuan Yan, Volker Tresp, Yunpu Ma  
**原文**：https://arxiv.org/abs/2607.05297  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定五agent pipeline、branch-local task skill s和五meta-skill文件m、SQLite DAG/archive/frontier、train failure mining/val utility evaluator；具体更新过程为：fast loop恢复parent s/m快照，train最差case驱动diagnose/retrieve/allocate/propose/execute，val评估child。每H步聚合历史子代ΔU为meta-failure，同pipeline重写全部五meta files，child携新m；后继从archive评分选parent并恢复其s/m；更新状态的保留与后继使用为：SQLite记录(s,m,U,ΔU,tag)、路径及访问count，failed/neutral节点也保留作inspiration；只有ΔU>0进deployable/parent archive。m分支局部存储，跨支只经retrieval传递。

## 2. 论文的核心内容与贡献

### configuration:cfg_metaskill_evolve_task_meta_skill_dag_v1
task/meta-skill文件与archive的两时标有界反馈支持四条件；不把五agent角色/wiring、H或模型weights描述为被进化。

**适用版本**：2607.05297v1；**原文定位**：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### MetaSkill-Evolve v1 branch task/meta files and two timescales
`cfg_metaskill_evolve_task_meta_skill_dag_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定五agent pipeline、branch-local task skill s和五meta-skill文件m、SQLite DAG/archive/frontier、train failure mining/val utility evaluator。 |
| 改进过程与下一轮参与 | fast loop恢复parent s/m快照，train最差case驱动diagnose/retrieve/allocate/propose/execute，val评估child。每H步聚合历史子代ΔU为meta-failure，同pipeline重写全部五meta files，child携新m；后继从archive评分选parent并恢复其s/m。 |
| 保留的状态及时间尺度 | SQLite记录(s,m,U,ΔU,tag)、路径及访问count，failed/neutral节点也保留作inspiration；只有ΔU>0进deployable/parent archive。m分支局部存储，跨支只经retrieval传递。 |
| 外部固定部分 | - frozen Gemma4 31B、五pipeline roles/wiring - slow-loop固定H触发 - 外部train/val/test split和reward |
| 评价与选择设置 | - **backbone**：Gemma4 31B frozen across five agents - **benchmarks**：OfficeQA, SealQA, ALFWorld - **meta**：every H fast iterations; branch-local files; cumulative meta children - **split**：stratified disjoint train/val/test |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.1–3.3明task/meta/state以及固定pipeline。（状态：`supported`；定位：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301）。
- **更新由什么过程产生**：自身失败与后继utility驱动skill/meta文件修改。（状态：`supported`；定位：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301）。
- **状态怎样持久保留**：节点及m快照落SQLite，后继恢复对应记录而非偶然workingtree。（状态：`supported`；定位：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301）。
- **更新怎样进入后续改进**：新m参数化下一轮五步骤，U/productivity/visitation改变frontier；negative evidence也可检索。（状态：`supported`；定位：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301）。

**配置判定**：task/meta-skill文件与archive的两时标有界反馈支持四条件；不把五agent角色/wiring、H或模型weights描述为被进化。

来源：https://arxiv.org/html/2607.05297v1；版本：2607.05297v1；定位：§3.2–3.3 branch state/archive tool L124–158；§3.4 fast loop/validation tool L177–196；§3.5 slow loop/accumulation tool L244–258；Limitations tool L358–360；§4.1 frozen model/splits tool L296–301。

## 4. 实验、评价协议与结果的可解释范围


- **backbone**：Gemma4 31B frozen across five agents
- **benchmarks**：OfficeQA, SealQA, ALFWorld
- **meta**：every H fast iterations; branch-local files; cumulative meta children
- **split**：stratified disjoint train/val/test

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_metaskill_evolve_task_meta_skill_dag_v1`**：task/meta-skill文件与archive的两时标有界反馈支持四条件；不把五agent角色/wiring、H或模型weights描述为被进化。 fast loop恢复parent s/m快照，train最差case驱动diagnose/retrieve/allocate/propose/execute，val评估child。每H步聚合历史子代ΔU为meta-failure，同pipeline重写全部五meta files，child携新m；后继从archive评分选parent并恢复其s/m。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 三curated benchmarks，long-horizon real-world noisy feedback未测。
- 慢层不是无限递归，H和pipeline本身固定；meta child累积写而非独立从parent并行生成。
- child utility用val反复选择，不将val称完全未参与优化；heldout test另做benchmark-mode。
- meta-update独立acceptance效度/参数敏感性未独立代码复现。
- 三curated benchmarks，long-horizon real-world noisy feedback未测。; 慢层不是无限递归，H和pipeline本身固定；meta child累积写而非独立从parent并行生成。; child utility用val反复选择，不将val称完全未参与优化；heldout test另做benchmark-mode。; meta-update独立acceptance效度/参数敏感性未独立代码复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_skill` · MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution · 2607.05297v1
  - https://arxiv.org/html/2607.05297v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0fa33d5144aa547ff7 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
