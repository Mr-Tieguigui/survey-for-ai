# MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

> 综合系统/智能体 · 2026 · `wf_ad3deac4b7265067d0`

**作者**：Qianshu Cai, Yonggang Zhang, Xianzhang Jia, Huajiang Zheng, Wei Xue, Jun Song, Xinmei Tian, Yike Guo  
**原文**：https://arxiv.org/abs/2605.22794  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：host-daemon、deterministic orchestration、外部可插拔coding-agent CLI、OpenClaw candidate代码/image、隔离trial、keypoint evaluator及受控apply/rollback组成完整改进边界；具体更新过程为：失败会话batch锁定baseline keypoints；七stage诊断/计划/审核/commit/运行trial/评判迭代。candidate qualitative keypoint matrix写入跨迭代历史并反馈下一轮定位和计划；CONVERGED后独立apply门决定部署；更新状态的保留与后继使用为：代码git commit/image、跨迭代keypoint矩阵、peak/last-known-good image保留；部署swap保留user-state volume。编辑器是外部子进程，不能把单一OpenClaw主体描述成独自改完整系统。

## 2. 论文的核心内容与贡献

### configuration:cfg_moss_bounded_failure_batch_source_rewrite_v1
包括外部editor的完整系统满足有界源码/证据反馈四条件；并不认证editor权重或编排器自升级。单iteration案例不证明已观测多代复利。

**适用版本**：2605.22794v1；**原文定位**：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### MOSS v1 failure-batch source rewrite with external editor inside declared boundary
`cfg_moss_bounded_failure_batch_source_rewrite_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | host-daemon、deterministic orchestration、外部可插拔coding-agent CLI、OpenClaw candidate代码/image、隔离trial、keypoint evaluator及受控apply/rollback组成完整改进边界。 |
| 改进过程与下一轮参与 | 失败会话batch锁定baseline keypoints；七stage诊断/计划/审核/commit/运行trial/评判迭代。candidate qualitative keypoint matrix写入跨迭代历史并反馈下一轮定位和计划；CONVERGED后独立apply门决定部署。 |
| 保留的状态及时间尺度 | 代码git commit/image、跨迭代keypoint矩阵、peak/last-known-good image保留；部署swap保留user-state volume。编辑器是外部子进程，不能把单一OpenClaw主体描述成独自改完整系统。 |
| 外部固定部分 | - deterministic stage ordering、预算/plateau guard及host lifecycle - loop内锁定keypoint集合 - 案例的DeepSeekV3.2 backbone及四claweval任务 |
| 评价与选择设置 | - **backbone case**：DeepSeek V3.2 - **deployment**：user apply, health probe/rollback; auto-ack only benchmark case - **numeric witness**：same four pre/post tasks, three trials each; internal keypoint matrix drives verdict - **tasks**：four claweval compliance-audit tasks, two bilingual task pairs |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2.3–2.5明确外部editor、host与被改容器，纳入同一边界。（状态：`supported`；定位：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200）。
- **更新由什么过程产生**：coding-agent在授权surface内生成源码commit，不是人工逐个写补丁。（状态：`supported`；定位：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200）。
- **状态怎样持久保留**：candidate/matrix跨迭代，合格image可swap且userstate持续。（状态：`supported`；定位：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200）。
- **更新怎样进入后续改进**：§3.2明确上轮candidate评价进入下一轮localization/planning；保留状态参与后续修补。（状态：`supported`；定位：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200）。

**配置判定**：包括外部editor的完整系统满足有界源码/证据反馈四条件；并不认证editor权重或编排器自升级。单iteration案例不证明已观测多代复利。

来源：https://arxiv.org/html/2605.22794v1；版本：2605.22794v1；定位：§2.3–2.5 external editor/state volume tool L88–108；§3.2–3.3 retained feedback/verdict tool L120–154；§3.4–4.1 runtime/apply/reused tasks tool L157–178；§4.2–4.3 one-iteration case/limits tool L181–200。

## 4. 实验、评价协议与结果的可解释范围


- **backbone case**：DeepSeek V3.2
- **deployment**：user apply, health probe/rollback; auto-ack only benchmark case
- **numeric witness**：same four pre/post tasks, three trials each; internal keypoint matrix drives verdict
- **tasks**：four claweval compliance-audit tasks, two bilingual task pairs

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r12_ev_cfg_moss_bounded_failure_batch_source_rewrite_v1`**：包括外部editor的完整系统满足有界源码/证据反馈四条件；并不认证editor权重或编排器自升级。单iteration案例不证明已观测多代复利。 失败会话batch锁定baseline keypoints；七stage诊断/计划/审核/commit/运行trial/评判迭代。candidate qualitative keypoint matrix写入跨迭代历史并反馈下一轮定位和计划；CONVERGED后独立apply门决定部署。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 四任务同时作为失败输入和重测集，三trial均值不是独立任务泛化。
- 内部Task-Evaluate是锁定keypoints的qualitative LLM评分；claweval numeric grader仅为外部witness，不能混作同一个选择器。
- 试验隔离userstate/真实traffic，所以trial通过仍可能live regression；常规需user apply，案例auto-ack不能泛化为默认无人授权部署。
- 案例仅iteration1；后续循环机制有方法文字支持，多代运行效果未独立验证。
- 四任务同时作为失败输入和重测集，三trial均值不是独立任务泛化。; 内部Task-Evaluate是锁定keypoints的qualitative LLM评分；claweval numeric grader仅为外部witness，不能混作同一个选择器。; 试验隔离userstate/真实traffic，所以trial通过仍可能live regression；常规需user apply，案例auto-ack不能泛化为默认无人授权部署。; 案例仅iteration1；后续循环机制有方法文字支持，多代运行效果未独立验证。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r12_src_moss` · MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems · 2605.22794v1
  - https://arxiv.org/html/2605.22794v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ad3deac4b7265067d0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
