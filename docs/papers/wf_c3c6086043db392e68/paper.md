# Self-Modifying Lean Proof Agents with Verifier-Grounded Benchmark Coevolution

> 方法论文 · 2026 · `wf_c3c6086043db392e68`

**作者**：Yuqing Li, Zeguan Wu, Yu Gan, Junyu Liu  
**原文**：https://arxiv.org/abs/2607.17352  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Lean 系统在固定可信 runtime 内演化工作流、提示和工具，champion 还更新课程并在新 benchmark 上重校准，成功由 Lean 验证；主角色应为方法而非仅 benchmark，可信验证范围和测试分离待全文核实。

## 2. 论文的核心内容与贡献

### configuration:cfg_lean_mutable_workflow_fixed_benchmark_v1
在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。

**适用版本**：v1；**原文定位**：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181；Appendix A L221–236。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_lean_workspace_curriculum_coevolution_v1
在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。

**适用版本**：v1；**原文定位**：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181；Appendix A L221–236。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_c3c6086043db392e68`
Lean 系统在固定可信 runtime 内演化工作流、提示和工具，champion 还更新课程并在新 benchmark 上重校准，成功由 Lean 验证；主角色应为方法而非仅 benchmark，可信验证范围和测试分离待全文核实。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Lean mutable proof workflow: fixed-benchmark ablation
`cfg_lean_mutable_workflow_fixed_benchmark_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定76题benchmark条件下的可编辑证明workflow、工具、prompts、meta修改逻辑与后代代码档案；可信Lean runtime固定。 |
| 改进过程与下一轮参与 | 代理通过受约束编辑接口改写自身工作区；代码smoke gate后由Lean独立验证证明，接受后代进入档案并可在同代或后代再次作为修改父代。 |
| 保留的状态及时间尺度 | 接受后的可编辑工作区在15代演化档案内跨证明任务和自修改保留；活动benchmark固定，非LLM权重训练。 |
| 外部固定部分 | - Lean/Mathlib和可信重验证runtime - proof-context groundedness约束 - 编辑接口、code smoke gates与隔离worker - DGM-style父代权重公式 - mastery阈值与候选任务池 - 基础LLM权重 |
| 评价与选择设置 | - **accepted children per generation max**：3 - **active generations**：15 - **active tasks**：76 - **api timeout seconds**：600 - **backend**：DeepSeek deepseek-v4-pro - **benchmark update threshold**：0.3 - **candidate level counts**：- 52 - 57 - 256 - **candidate pool**：365 - **curriculum replacement budget**：0 - **heldout dataset**：miniF2F test, disjoint from valid curriculum, never used for evolution selection - **heldout tasks**：244 - **initial active level counts**：- 27 - 46 - 3 - **mastery threshold**：0.7 - **mutation attempts per generation max**：6 - **recalibration epsilon**：0.1 - **reported runs**：single trajectory per arm, no variance estimates - **temperature**：0 - **verifier**：real Lean4/Mathlib v4.30.0 - **workflow timeout seconds**：1200 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：固定76题benchmark条件下的可编辑证明workflow、工具、prompts、meta修改逻辑与后代代码档案；可信Lean runtime固定。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **更新由什么过程产生**：§3.1明确工作区包括agent-facing workflow及适应它的meta-level逻辑，工作区为唯一演化对象。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **状态怎样持久保留**：§3.4接受后代立即进档案并可作后续父代；课程配置另外保留更新后的B和c。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **更新怎样进入后续改进**：§3.1的可变meta逻辑随工作区后代保留，§3.4后代被再次采样为父代；协同配置中后代解题表现亦回流到新课程及下一轮选择。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。

**配置判定**：在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。

来源：https://arxiv.org/html/2607.17352v1；版本：v1；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181；Appendix A L221–236。

### Lean workspace + verifier-grounded benchmark coevolution
`cfg_lean_workspace_curriculum_coevolution_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 可编辑证明工作区、meta修改逻辑、代码档案及champion驱动的活动课程B和系数c；可信验证与课程规则固定。 |
| 改进过程与下一轮参与 | 选中父工作区产生后代；Lean验证记录决定champion及档案弱点，按固定mastery规则替换活动课程任务并重评champion更新c；更新的代码、B和c影响后续变体选择与验证反馈。 |
| 保留的状态及时间尺度 | 接受后的可编辑工作区在15代演化档案内跨证明任务和自修改保留；课程B与系数c跨代传递。 |
| 外部固定部分 | - Lean/Mathlib和可信重验证runtime - proof-context groundedness约束 - 编辑接口、code smoke gates与隔离worker - DGM-style父代权重公式 - mastery阈值与候选任务池 - 基础LLM权重 |
| 评价与选择设置 | - **accepted children per generation max**：3 - **active generations**：15 - **active tasks**：76 - **api timeout seconds**：600 - **backend**：DeepSeek deepseek-v4-pro - **benchmark update threshold**：0.3 - **candidate level counts**：- 52 - 57 - 256 - **candidate pool**：365 - **curriculum replacement budget**：6 - **heldout dataset**：miniF2F test, disjoint from valid curriculum, never used for evolution selection - **heldout tasks**：244 - **initial active level counts**：- 27 - 46 - 3 - **mastery threshold**：0.7 - **mutation attempts per generation max**：6 - **recalibration epsilon**：0.1 - **reported runs**：single trajectory per arm, no variance estimates - **temperature**：0 - **verifier**：real Lean4/Mathlib v4.30.0 - **workflow timeout seconds**：1200 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：可编辑证明工作区、meta修改逻辑、代码档案及champion驱动的活动课程B和系数c；可信验证与课程规则固定。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **更新由什么过程产生**：§3.1明确工作区包括agent-facing workflow及适应它的meta-level逻辑，工作区为唯一演化对象。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **状态怎样持久保留**：§3.4接受后代立即进档案并可作后续父代；课程配置另外保留更新后的B和c。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。
- **更新怎样进入后续改进**：§3.1的可变meta逻辑随工作区后代保留，§3.4后代被再次采样为父代；协同配置中后代解题表现亦回流到新课程及下一轮选择。（状态：`supported`；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181）。

**配置判定**：在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。

来源：https://arxiv.org/html/2607.17352v1；版本：v1；定位：§3.1–3.2 tool L121–138；§3.3–3.4 tool L139–162；§4 tool L165–181；Appendix A L221–236。

## 4. 实验、评价协议与结果的可解释范围


- **accepted children per generation max**：3
- **active generations**：15
- **active tasks**：76
- **api timeout seconds**：600
- **backend**：DeepSeek deepseek-v4-pro
- **benchmark update threshold**：0.3
- **candidate level counts**：- 52 - 57 - 256
- **candidate pool**：365
- **curriculum replacement budget**：0
- **heldout dataset**：miniF2F test, disjoint from valid curriculum, never used for evolution selection
- **heldout tasks**：244
- **initial active level counts**：- 27 - 46 - 3
- **mastery threshold**：0.7
- **mutation attempts per generation max**：6
- **recalibration epsilon**：0.1
- **reported runs**：single trajectory per arm, no variance estimates
- **temperature**：0
- **verifier**：real Lean4/Mathlib v4.30.0
- **workflow timeout seconds**：1200


- **accepted children per generation max**：3
- **active generations**：15
- **active tasks**：76
- **api timeout seconds**：600
- **backend**：DeepSeek deepseek-v4-pro
- **benchmark update threshold**：0.3
- **candidate level counts**：- 52 - 57 - 256
- **candidate pool**：365
- **curriculum replacement budget**：6
- **heldout dataset**：miniF2F test, disjoint from valid curriculum, never used for evolution selection
- **heldout tasks**：244
- **initial active level counts**：- 27 - 46 - 3
- **mastery threshold**：0.7
- **mutation attempts per generation max**：6
- **recalibration epsilon**：0.1
- **reported runs**：single trajectory per arm, no variance estimates
- **temperature**：0
- **verifier**：real Lean4/Mathlib v4.30.0
- **workflow timeout seconds**：1200

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_c3c6086043db392e68`**：Lean 系统在固定可信 runtime 内演化工作流、提示和工具，champion 还更新课程并在新 benchmark 上重校准，成功由 Lean 验证；主角色应为方法而非仅 benchmark，可信验证范围和测试分离待全文核实。
  - 来源版本：2607.17352v1；定位：Atom entry http://arxiv.org/abs/2607.17352v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`scope18_lean_ev_cfg_lean_mutable_workflow_fixed_benchmark_v1`**：在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`scope18_lean_ev_cfg_lean_workspace_curriculum_coevolution_v1`**：在明确可编辑工作区及档案边界内支持结构四条件；不认证改进效率递增、全自主或无限能力增长。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 单次运行研究，无跨seed方差估计（Appendix A L221）；不认证一般增益、独立复现或开放式持续加速。
- 固定DeepSeek deepseek-v4-pro服务于证明与自修改；温度0仍存在输出不稳定，不能视作严格确定性。
- 可信Lean4/Mathlib v4.30.0、评分和benchmark管理runtime不在演化范围；改进代码与证明结果必须分别通过smoke gate和可信重验证。
- 禁止sorry/admit并隔离mutable进程等是声明threat model下的控制；未独立执行安全测试，不断言对任意恶意环境绝对免疫。
- proof context的结构质量仅记录、不奖励；高solve率未等于形成深层耐久证明DAG。
- miniF2F valid进入课程，244题test与之分离且不参与演化选择；评估了不同数量的run候选，不能作等量候选无偏最优比较。
- 该消融kappa=0，不能将协同臂任务替换/重校准归因到固定benchmark配置。
- champion单锚缩放只固定该anchor的归一分数，且r_new<epsilon时并非严格保分；不证明任意代理跨课程的可比性或无selection bias。
- 课程只在既有365题分层池内更换；未生成新定理，未改变Lean正确性标准或自改benchmark规则。
- 45.1%为所选9个协同轨迹检查点的最佳held-out结果；固定臂只对最高活动分数的2个代理做held-out，不是同量候选的随机多次运行对照。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `s18_role_src_296fdf533f23d85c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Averifier+OR+ti%3A%22process+reward%22+OR+ti%3A%22feedback+reliability%22%29+AND+%28all%3Areasoning+OR+all%3Aagent%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=200&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `scope18_lean_src_method` · 已存来源 · v1
  - https://arxiv.org/html/2607.17352v1；阅读深度：`selected_primary_method_trusted_boundary_and_experimental_protocol`。
- `scope18_lean_src_settings` · 已存来源 · v1
  - https://arxiv.org/html/2607.17352v1；阅读深度：`selected_primary_method_trusted_boundary_and_experimental_protocol`。

**证据深度**：original_abstract, selected_primary_method_trusted_boundary_and_experimental_protocol。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c3c6086043db392e68 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
