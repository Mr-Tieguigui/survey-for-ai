# Large Language Model Agents Are Not Always Faithful Self-Evolvers

> 实证/审计/复现 · 2026 · `wf_b75f095a545a1c7c3a`

**作者**：Weixiang Zhao, Yingshuo Wang, Yichen Zhang, Yang Deng, Yanyan Zhao, Wanxiang Che, Bing Qin, Ting Liu  
**原文**：https://arxiv.org/abs/2601.22436  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已读原始评测协议和限制；区分作者实证观察与领域普遍结论。

## 2. 论文的核心内容与贡献

### configuration:cfg_faithfulness_semantic_intervention_v3
为经验语义依赖测量协议建立adjacent配置；本v3报告多实现多任务差异，不能把摘要经验低敏感性外推为所有记忆无效。

**适用版本**：2601.22436v3；**原文定位**：S3.SS1.p1；S3.SS2.p2；S3.SS2.p3；S3.SS2.p4；S3.SS3.p2；S3.SS3.p3；S3.SS3.p4；S3.SS3.p5；S4.SS1.p2；S4.SS1.p3；S4.SS1.p5；S4.SS2.p2；S4.SS2.p3；S4.SS3.p4。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### v3: controlled experience-semantic intervention audit
`cfg_faithfulness_semantic_intervention_v3` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LLM骨干下的四种经验代理实现；审计者干预检索到的原始/凝练经验，比较任务表现。 |
| 改进过程与下一轮参与 | 评价协议本身不生成更强改进器；Empty/Shuffle/Irrelevant及Corrupt/Filler等干预用于区分经验有用性与对其语义的因果依赖。 |
| 保留的状态及时间尺度 | 被审计代理各自保留离线或在线经验；协议的内容替换是实验处理，不是持久自主更新算法。 |
| 外部固定部分 | - 任务集、LLM、各实现、干预分配及测量规则由研究者固定 |

**配置判定**：为经验语义依赖测量协议建立adjacent配置；本v3报告多实现多任务差异，不能把摘要经验低敏感性外推为所有记忆无效。

来源：https://arxiv.org/html/2601.22436v3；版本：2601.22436v3；定位：S3.SS1.p1；S3.SS2.p2；S3.SS2.p3；S3.SS2.p4；S3.SS3.p2；S3.SS3.p3；S3.SS3.p4；S3.SS3.p5；S4.SS1.p2；S4.SS1.p3；S4.SS1.p5；S4.SS2.p2；S4.SS2.p3；S4.SS3.p4。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`eval3_ev_cfg_faithfulness_semantic_intervention_v3`**：为经验语义依赖测量协议建立adjacent配置；本v3报告多实现多任务差异，不能把摘要经验低敏感性外推为所有记忆无效。
  - 来源版本：unknown；定位：S3.SS1.p1；S3.SS2.p2；S3.SS2.p3；S3.SS2.p4；S3.SS3.p2；S3.SS3.p3；S3.SS3.p4；S3.SS3.p5；S4.SS1.p2；S4.SS1.p3；S4.SS1.p5；S4.SS2.p2；S4.SS2.p3；S4.SS3.p4；深度：`未单列`。

- **`r4bench_ev_faithfulness_v3`**：固定基础模型的四经验代理上改变原始/凝练经验内容以测语义依赖；不是信任风险或长期资源斜率协议。
  - 来源版本：v3；定位：S3.SS1.p1；S3.SS2.p2；S3.SS2.p3；S3.SS2.p4；S3.SS3.p2；S3.SS3.p3；S3.SS3.p4；S3.SS3.p5；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本配置来源v3；已有v1审计实现边保留版本，不认证v3全部超参数与v1完全相同。
- 任务依赖明显，部分知识任务的原始和凝练经验敏感性更相近。
- 作者报告的干预结果不是独立复现，也不能单靠干预认证无偏因果识别或一般机理定理。
- 本配置来源v3；已有v1审计实现边保留版本，不认证v3全部超参数与v1完全相同。；任务依赖明显，部分知识任务的原始和凝练经验敏感性更相近。；作者报告的干预结果不是独立复现，也不能单靠干预认证无偏因果识别或一般机理定理。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `eval3_src_faithfulness` · 已存来源 · 2601.22436v3
  - https://arxiv.org/html/2601.22436v3；阅读深度：`selected_primary_methods_and_limits`。
- `r4bench_src_faithfulness_v3` · 已存来源 · v3
  - https://arxiv.org/html/2601.22436v3；阅读深度：`未单列`。

**证据深度**：primary_abstract_or_official_summary_review。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b75f095a545a1c7c3a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
