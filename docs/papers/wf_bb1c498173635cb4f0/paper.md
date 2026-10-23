# Safety Must Survive Self-Improvement: Why Failures Persist and How Agents Recover

> 实证/审计/复现 · 2026 · `wf_bb1c498173635cb4f0`

**作者**：Yunbei Zhang, Janet Wang, Saiyue Lyu, Yingqiang Ge, Kaiqu Liang, Zijian Jin, Chandan K Reddy, Jihun Hamm  
**原文**：https://arxiv.org/abs/2610.01073  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
固定LLM编辑器和授权任务testbed中分离验证、执行者和下轮被编辑程序，观察旧分数、失败incumbent与恢复的关系；需核任务及干预配置。

## 2. 论文的核心内容与贡献

### configuration:cfg_safety_survive_authorization_protocol_v1
adjacent评价协议；受测程序可持久更新，但不得把协议卡自动当作改进器自改的核心实现。

**适用版本**：v1；**原文定位**：§2–3.1 tool L104–120；§3.3 tool L146–162；Appendix C.1 tool L383–399。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_bb1c498173635cb4f0`
固定LLM编辑器和授权任务testbed中分离验证、执行者和下轮被编辑程序，观察旧分数、失败incumbent与恢复的关系；需核任务及干预配置。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议

### cfg_safety_survive_authorization_protocol_v1
`cfg_safety_survive_authorization_protocol_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定授权安全testbed及验证/执行/编辑源的配对干预；LLM编辑器固定，受测可执行授权组件及历史演化。 |
| 改进过程与下一轮参与 | 分别操纵历史或当前评分、拒绝后保留或回退、编辑incumbent或founder；公共测试给反馈，audit支持回滚，hidden effect traces测未授权效果和允许工作完成。 |
| 保留的状态及时间尺度 | 跨代保留程序档案、评分及运行轨迹，区分当前安全、全程安全与完整恢复。 |
| 外部固定部分 | - 外部授权契约及公共/audit/隐藏测例 - LLM编辑器和研究者设定干预 - 独立效果记录与费用定义 |
| 评价与选择设置 | - **execution scope**：OpenEvolve controller/database/workers; DGM parent sampling/archive update/original-score functions, pinned a565fd2 - **framework cohort**：48 histories, two frameworks × two editors × two mechanisms × six seeds; two-framework cohort is distinct from 72 new-dependency histories - **not independent reproduction**：True - **task families**：- session_authorization - filesystem_containment - tool_approval - structured_user_consent |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：固定评价/干预协议与受测自改程序分别定义。（状态：`supported`；定位：§2–3.1 tool L104–120；§3.3 tool L146–162）。
- **更新由什么过程产生**：本卡边界是研究者固定的评价协议，不是被评价程序的更新链。（状态：`contradicted`；定位：§2–3.1 tool L104–120；§3.3 tool L146–162）。
- **状态怎样持久保留**：协议保留跨轮评价记录与程序轨迹供纵向分析。（状态：`supported`；定位：§2–3.1 tool L104–120；§3.3 tool L146–162）。
- **更新怎样进入后续改进**：此配置未显示协议因自己所测结果自行改写其评价规则；规则随轮次作预定计算不等于规则自改。（状态：`contradicted`；定位：§2–3.1 tool L104–120；§3.3 tool L146–162）。

**配置判定**：adjacent评价协议；受测程序可持久更新，但不得把协议卡自动当作改进器自改的核心实现。

来源：https://arxiv.org/html/2610.01073v1；版本：v1；定位：§2–3.1 tool L104–120；§3.3 tool L146–162；Appendix C.1 tool L383–399。

## 4. 实验、评价协议与结果的可解释范围


- **execution scope**：OpenEvolve controller/database/workers; DGM parent sampling/archive update/original-score functions, pinned a565fd2
- **framework cohort**：48 histories, two frameworks × two editors × two mechanisms × six seeds; two-framework cohort is distinct from 72 new-dependency histories
- **not independent reproduction**：True
- **task families**：- session_authorization - filesystem_containment - tool_approval - structured_user_consent

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_bb1c498173635cb4f0`**：固定LLM编辑器和授权任务testbed中分离验证、执行者和下轮被编辑程序，观察旧分数、失败incumbent与恢复的关系；需核任务及干预配置。
  - 来源版本：2610.01073v1；定位：Atom entry http://arxiv.org/abs/2610.01073v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r4safety_ev_cfg_safety_survive_authorization_protocol_v1`**：分别操纵历史或当前评分、拒绝后保留或回退、编辑incumbent或founder；公共测试给反馈，audit支持回滚，hidden effect traces测未授权效果和允许工作完成。
  - 来源版本：v1；定位：§2–3.1 tool L104–120；§3.3 tool L146–162；Appendix C.1 tool L383–399；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- DGM实验只执行三个上游函数及外接编辑器/授权评价adapter；不得标为完整DGM端到端原始代码任务复现。
- STOP/SICA仅源代码检查，AlphaEvolve仅报告比较；不声称运行这些系统。
- 契约变化与独立事件组合揭示原测试覆盖局限，当前测试通过不构成一般安全证明。
- core trajectory的部署服务费用节省不含验证成本；安全、完整正确与最终恢复须分开。
- 固定编辑器不否定受测程序的递归结构；本卡adjacent只因所声明边界是评测协议。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_9d7a032301cb2deb` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28all%3A%22recursive+self-improvement%22+OR+all%3A%22self-evolving+agent%22%29+AND+%28all%3Asafety+OR+all%3Aalignment+OR+all%3Acontrol%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `r4safety_src_survive` · 已存来源 · v1
  - https://arxiv.org/html/2610.01073v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。
- `r4safety_src_survive_scope` · 已存来源 · v1
  - https://arxiv.org/html/2610.01073v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。

**证据深度**：original_abstract, selected_primary_methods_assumptions_execution_scope_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bb1c498173635cb4f0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
