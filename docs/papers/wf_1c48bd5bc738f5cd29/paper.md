# MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents

> Benchmark/数据集/任务套件 · 2026 · `wf_1c48bd5bc738f5cd29`

**作者**：Jingwei Song, Zhisheng Chen, Bingfan Zeng, Jing Tang, Yubo Hou, Jinhao Jing, Zhengwei Xie, Linfeng Zhang  
**原文**：https://arxiv.org/abs/2610.13829  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Persistent experience-use reference; audit does not demonstrate recursive target updates or stable transfer.

## 2. 论文的核心内容与贡献

### configuration:cfg_mc_evobench_jarvis_online_transfer
Persistent experience-use reference; audit does not demonstrate recursive target updates or stable transfer.

**适用版本**：2610.13829v1；**原文定位**：§3.1；§4.1；Appendix E.1–E.3；Appendix G.1–G.2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 任务、数据与评价设计

### cfg_mc_evobench_jarvis_online_transfer
`cfg_mc_evobench_jarvis_online_transfer` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | JARVIS online text planner, released controller, episode artifact; evaluator resets world. |
| 更新状态 | Episodes: instruction, plan, dispatch, status, visible state, advice. |
| 改进过程与下一轮参与 | Source reflection writes episodes; lexical retrieval conditions plans. |
| 保留的状态及时间尺度 | Source artifact crosses reset boundary; target read-only. |
| 外部固定部分 | Controller/planner, retrieval, resets, source budgets, verifiers. |

**配置判定**：Persistent experience-use reference; audit does not demonstrate recursive target updates or stable transfer.

来源：https://arxiv.org/html/2610.13829v1；版本：2610.13829v1；定位：§3.1；§4.1；Appendix E.1–E.3；Appendix G.1–G.2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Appendix E.1: headline paired results use JARVIS online extension only.
- §4/§5: low execution floor, five seeds, all transfer intervals include zero.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `src_w_mc_evobench` · 已存来源 · 2610.13829v1
  - https://arxiv.org/html/2610.13829v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_limits_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1c48bd5bc738f5cd29 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
