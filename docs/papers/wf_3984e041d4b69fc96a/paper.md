# Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

> 实证/审计/复现 · 2026 · `wf_3984e041d4b69fc96a`

**作者**：Xianglin Yang, Yufei He, Shuo Ji, Bryan Hooi, Jin Song Dong  
**原文**：https://arxiv.org/abs/2602.15654  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已读原始评测协议和限制；区分作者实证观察与领域普遍结论。

## 2. 论文的核心内容与贡献

### configuration:cfg_zombie_persistence_security_protocol_v2
为持久记忆污染安全协议建立adjacent配置；其贡献是攻击与留存风险测量，不是RSI正向能力增益的证据。

**适用版本**：2602.15654v2；**原文定位**：S3.SS1.p1；S3.SS2.p1；S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px2.p1；S4.SS1.SSS0.Px1.p1；S4.SS1.SSS0.Px2.p1；S4.SS2.SSS0.Px2.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### v2: persistent memory-injection threat evaluation
`cfg_zombie_persistence_security_protocol_v2` · security_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 攻击者控制工具返回的外部内容，受测代理具有滑窗或RAG记忆；评价暴露与后续无关任务两个阶段。 |
| 改进过程与下一轮参与 | 研究的是不可信观察被写入后续记忆并影响未来任务的安全失效；不将攻击持久性等同于能力自改进。 |
| 保留的状态及时间尺度 | 滑窗和RAG分别测暴露后的20轮触发；RAG数据库3000项，污染暴露300轮；每设置3个随机种子运行。 |
| 外部固定部分 | - 攻击者权限边界、受测Gemini-2.5-Flash/GLM-4.7-Flash、任务、轮数、记忆架构、评测指标 |

**配置判定**：为持久记忆污染安全协议建立adjacent配置；其贡献是攻击与留存风险测量，不是RSI正向能力增益的证据。

来源：https://arxiv.org/html/2602.15654v2；版本：2602.15654v2；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px2.p1；S4.SS1.SSS0.Px1.p1；S4.SS1.SSS0.Px2.p1；S4.SS2.SSS0.Px2.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`accel_ev_zombie_named_system_limit`**：实验目标是滑窗和RAG两类记忆代理及指定骨干模型。
  - 来源版本：unknown；定位：§3.3 Scenarios A/B；§4.1 Evaluation Protocol；深度：`未单列`。

- **`eval3_ev_cfg_zombie_persistence_security_protocol_v2`**：为持久记忆污染安全协议建立adjacent配置；其贡献是攻击与留存风险测量，不是RSI正向能力增益的证据。
  - 来源版本：unknown；定位：S3.SS1.p1；S3.SS2.p1；S3.SS3.SSS0.Px1.p1；S3.SS3.SSS0.Px2.p1；S4.SS1.SSS0.Px1.p1；S4.SS1.SSS0.Px2.p1；S4.SS2.SSS0.Px2.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 原文实验的受测对象是两种记忆架构，未证实其实际评测A-MEM或ExpeL。
- 暴露依赖攻击者控制外部内容；后续效果不能外推到所有自主代理和防护。
- 记忆进化策略可降低作者报告ASR但未彻底消除；不据此宣称所有演化过滤绝对无效。
- 医疗和购物场景是作者定性案例，不是已验证的真实部署事故。
- Related Work中提及Reflexion、ExpeL不构成实际攻击评测证据。
- 原文实验的受测对象是两种记忆架构，未证实其实际评测A-MEM或ExpeL。；暴露依赖攻击者控制外部内容；后续效果不能外推到所有自主代理和防护。；记忆进化策略可降低作者报告ASR但未彻底消除；不据此宣称所有演化过滤绝对无效。；医疗和购物场景是作者定性案例，不是已验证的真实部署事故。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_zombie_v1` · 已存来源 · v1
  - https://arxiv.org/html/2602.15654v1；阅读深度：`未单列`。
- `eval3_src_zombie` · 已存来源 · 2602.15654v2
  - https://arxiv.org/html/2602.15654v2；阅读深度：`selected_primary_methods_and_limits`。

**证据深度**：primary_abstract_or_official_summary_review。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3984e041d4b69fc96a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
