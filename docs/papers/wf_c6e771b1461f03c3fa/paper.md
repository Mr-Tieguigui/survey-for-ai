# Mixture of Self-Improving Branches For Agent Harness Optimization

> 方法论文 · 2026 · `wf_c6e771b1461f03c3fa`

**作者**：Haoyu Dong, Yuhang Zhou, Zihao Lin, Yifan Wu, Bo Peng, Mingyi Wang, Xiangjun Fan, Lizhu Zhang, Zhuokai Zhao  
**原文**：https://arxiv.org/abs/2609.37834  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：共享Claude Opus4.6 proposer、两个branch-local harness populations/history/SKILL.md/current dev subset、task evaluator及最后development-trained router；action models另固定；具体更新过程为：每branch proposer读现有harness-score/traces和guidance提新code，评价后写本地records供下一次。top-q frontiers coverage比较修dev ownership，周期性同proposer从近期证据重写SKILL.md；两更新均影响后继搜索。最终每branch按其dev选head并构router；更新状态的保留与后继使用为：branch source/score/trace、current task membership和proposal guidance跨20iterations；finalhead/source及development-only router保留部署。

## 2. 论文的核心内容与贡献

### configuration:cfg_mixture_branches_dynamic_development_guidance_v1
harness+local proposal guidance+搜索状态满足有界四条件；optimizer update在此是SKILL.md改写，不是权重或optimizer-code训练。

**适用版本**：2609.37834v1；**原文定位**：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Mixture branches v1 evolving harness/development ownership/guidance with deployment router
`cfg_mixture_branches_dynamic_development_guidance_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 共享Claude Opus4.6 proposer、两个branch-local harness populations/history/SKILL.md/current dev subset、task evaluator及最后development-trained router；action models另固定。 |
| 改进过程与下一轮参与 | 每branch proposer读现有harness-score/traces和guidance提新code，评价后写本地records供下一次。top-q frontiers coverage比较修dev ownership，周期性同proposer从近期证据重写SKILL.md；两更新均影响后继搜索。最终每branch按其dev选head并构router。 |
| 保留的状态及时间尺度 | branch source/score/trace、current task membership和proposal guidance跨20iterations；finalhead/source及development-only router保留部署。 |
| 外部固定部分 | - proposer与action model weights - coverage/pruning/ownership rule和update schedule - heldout test task checks及router deployment时不读expert outputs/correctness |
| 评价与选择设置 | - **branches**：2 - **development interval**：1 - **frontier q**：5 - **guidance interval**：5 - **iterations**：20 - **ownership margin**：2 - **proposer**：Claude Opus4.6 - **split**：math250dev/200test;Terminal88=30dev58test;SWE-lite300=50dev250test |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3区分branch状态、proposer和action model。（状态：`supported`；定位：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243）。
- **更新由什么过程产生**：proposer自主产生harness edit和本地proposal guidance。（状态：`supported`；定位：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243）。
- **状态怎样持久保留**：文件/记录/SKILL/devmembership跨iterations保留。（状态：`supported`；定位：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243）。
- **更新怎样进入后续改进**：前轮coverage改任务和ranking、guidance改下一提案；更新后状态均用于next iteration。（状态：`supported`；定位：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243）。

**配置判定**：harness+local proposal guidance+搜索状态满足有界四条件；optimizer update在此是SKILL.md改写，不是权重或optimizer-code训练。

来源：https://arxiv.org/html/2609.37834v1；版本：2609.37834v1；定位：§3 branch-local state/feedback tool L103–111；§3 dev pruning/guidance/routing tool L144–158；§4.1 setup/splits tool L174–184；§4.4–4.6 router and test-best limits tool L229–243。

## 4. 实验、评价协议与结果的可解释范围


- **branches**：2
- **development interval**：1
- **frontier q**：5
- **guidance interval**：5
- **iterations**：20
- **ownership margin**：2
- **proposer**：Claude Opus4.6
- **split**：math250dev/200test;Terminal88=30dev58test;SWE-lite300=50dev250test

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_mixture_branches_dynamic_development_guidance_v1`**：harness+local proposal guidance+搜索状态满足有界四条件；optimizer update在此是SKILL.md改写，不是权重或optimizer-code训练。 每branch proposer读现有harness-score/traces和guidance提新code，评价后写本地records供下一次。top-q frontiers coverage比较修dev ownership，周期性同proposer从近期证据重写SKILL.md；两更新均影响后继搜索。最终每branch按其dev选head并构router。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- final dev选择与test-best诊断严格分开；后者在test上乐观挑选，不能作为可部署无泄露主成绩。
- 两branch不同dev subset的head scores不可直接比较；default router在执行前选一head。
- combinedcoverage为oracle upper bound；实际router尚有4.4–5.5点缺口，增加上下文非稳定收益。
- 固定四设置/B2/N20不证明长期加速或无预算上界。
- final dev选择与test-best诊断严格分开；后者在test上乐观挑选，不能作为可部署无泄露主成绩。; 两branch不同dev subset的head scores不可直接比较；default router在执行前选一head。; combinedcoverage为oracle upper bound；实际router尚有4.4–5.5点缺口，增加上下文非稳定收益。; 固定四设置/B2/N20不证明长期加速或无预算上界。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_mixture` · Mixture of Self-Improving Branches For Agent Harness Optimization · 2609.37834v1
  - https://arxiv.org/html/2609.37834v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c6e771b1461f03c3fa --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
