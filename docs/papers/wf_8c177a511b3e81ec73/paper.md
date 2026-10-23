# Evolutionary Safety of Recursive Self-Improving AI: Taxonomy, Risk Discovery, and Evaluation

> 综述/系统综述/谱系 · 2026 · `wf_8c177a511b3e81ec73`

**作者**：Chang Gong, Jingping Bi, Di Yao, Xinjian Liang, Chao Xiang, Ruijie Guo  
**原文**：https://arxiv.org/abs/2609.31186  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Evolutionary Safety定义安全变化何时因保留、选择、继承和传播进入演化分析，并区分persistent agent state、model state、evaluation/environment feedback、computational substrate、meta-updater/co-evolution五域。提出state/update/trajectory/lineage四评价单位，是taxonomy和研究框架，非已完成所有风险因果实验或安全保证。

## 2. 论文的核心内容与贡献

### role:r14_role_safety
Evolutionary Safety定义安全变化何时因保留、选择、继承和传播进入演化分析，并区分persistent agent state、model state、evaluation/environment feedback、computational substrate、meta-updater/co-evolution五域。提出state/update/trajectory/lineage四评价单位，是taxonomy和研究框架，非已完成所有风险因果实验或安全保证。

**适用版本**：2609.31186v1；**原文定位**：§2.5–3 definition/units/taxonomy tool L140–153；§3.2–3.3 model/evaluation distinction tool L165–180；§3.5–4 meta/coevolution/units tool L198–216；§7 open problems/limits tool L294–309。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

### 已存角色解释 · `r4_role_review_wf_8c177a511b3e81ec73`
摘要提出Evolutionary Safety分类，讨论状态、更新、轨迹和谱系层风险；分类框架不直接证明每类风险普遍发生。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 综述范围、分类框架与覆盖
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：直接面向persistent self-improvement/RSI的安全范围和评价组织，引用关系及各defense效果仍需原paper核查。
- **metrics**：- risk readouts和control readouts按属性分报，不将分布failure自动等同safety failure - 评价单位框架不提供本批可认证的统一已校准风险总分
- **selection and reuse**：以文献及概念机制组织taxonomy；所选定义/taxonomy/open-problem段未给可复现数据库检索与系统纳排流程，不能认作完备系统检索。
- **split and visibility**：不适用单一train/test；建议控制任务/权限、比较frozen/updating state与干预疑似传播途径。
- **task or data unit**：安全属性随状态、单次更新、连续轨迹和后裔/群体传播的分析单位。
- **unknowns**：- 可复现文献检索边界/纳排与taxonomy覆盖率unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_8c177a511b3e81ec73`**：摘要提出Evolutionary Safety分类，讨论状态、更新、轨迹和谱系层风险；分类框架不直接证明每类风险普遍发生。
  - 来源版本：2609.31186v1；定位：Atom entry http://arxiv.org/abs/2609.31186v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r14_ev_safety`**：Evolutionary Safety定义安全变化何时因保留、选择、继承和传播进入演化分析，并区分persistent agent state、model state、evaluation/environment feedback、computational substrate、meta-updater/co-evolution五域。提出state/update/trajectory/lineage四评价单位，是taxonomy和研究框架，非已完成所有风险因果实验或安全保证。
  - 来源版本：2609.31186v1；定位：§2.5–3 definition/units/taxonomy tool L140–153；§3.2–3.3 model/evaluation distinction tool L165–180；§3.5–4 meta/coevolution/units tool L198–216；§7 open problems/limits tool L294–309；深度：`selected_primary_survey_definition_taxonomy_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 多数跨artifact/population传播、changing-judge和长期recovery要求为open problems/建议实验，不作已验证结论。
- 未知failure空间无可观测分母，发现更多failure不等同真实risk升高或全面安全覆盖。
- 未独立审全部引用或统一安全保证；仅所选scope/分类/评价段。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。
- 多数跨artifact/population传播、changing-judge和长期recovery要求为open problems/建议实验，不作已验证结论。; 未知failure空间无可观测分母，发现更多failure不等同真实risk升高或全面安全覆盖。; 未独立审全部引用或统一安全保证；仅所选scope/分类/评价段。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_safety` · Evolutionary Safety of Recursive Self-Improving AI: Taxonomy, Risk Discovery, and Evaluation · 2609.31186v1
  - https://arxiv.org/html/2609.31186v1；阅读深度：`selected_primary_survey_definition_taxonomy_scope_and_limits`。
- `r4_role_src_7297985cdee046c8` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Abenchmark+OR+ti%3Aevaluation%29+AND+%28all%3A%22self-evolving%22+OR+all%3A%22self-improving%22+OR+all%3A%22recursive+self-improvement%22%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_survey_definition_taxonomy_scope_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8c177a511b3e81ec73 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
