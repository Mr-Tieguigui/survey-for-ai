# Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding

> 失败/限制/风险 · 2026 · `wf_c1155d6197cc62bf78`

**作者**：Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin  
**原文**：https://arxiv.org/abs/2609.34924  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
以有界质量与持续改进假设分析饱和，冻结权重上界进一步依赖M1/M2；scaffold可变不等于已证明无界增益。Agentic Boosting保留/重加权协议明确尚未构建。

## 2. 论文的核心内容与贡献

### role:r4safety_role_audit_scaffold
以有界质量与持续改进假设分析饱和，冻结权重上界进一步依赖M1/M2；scaffold可变不等于已证明无界增益。Agentic Boosting保留/重加权协议明确尚未构建。

**适用版本**：v1；**原文定位**：§4 Theorem2/Proposition3 tool L184–191；§4 Corollary4 tool L193–198；§3 tool L168–169；§4 tool L174–183。
**引用权限**：`selected_role_claim_only_no_configuration_certification`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4safety_ev_audit_scaffold`**：以有界质量与持续改进假设分析饱和，冻结权重上界进一步依赖M1/M2；scaffold可变不等于已证明无界增益。Agentic Boosting保留/重加权协议明确尚未构建。
  - 来源版本：unknown；定位：§4 Theorem2/Proposition3 tool L184–191；§4 Corollary4 tool L193–198；§3 tool L168–169；§4 tool L174–183；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 选读定理、假设和未实现声明；未独立检查Lean证明或复算生产/SWE-bench实验。
- Theorem2先假设每轮期望改进；M1/M2是建模假设，不是定理。
- 固定权重的最终上界不等于过程stationarity或通用安全认证；经验饱和不证明固定假设类是因果机制。
- 本文不接入一个虚构已实现的Agentic Boosting核心配置。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4safety_src_audit_scaffold` · 已存来源 · v1
  - https://arxiv.org/html/2609.34924v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。
- `r4safety_src_audit_unbuilt` · 已存来源 · v1
  - https://arxiv.org/html/2609.34924v1；阅读深度：`selected_original_methods_assumptions_execution_scope_and_limits`。

**证据深度**：original_abstract。
**当前引用权限**：`selected_role_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c1155d6197cc62bf78 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
