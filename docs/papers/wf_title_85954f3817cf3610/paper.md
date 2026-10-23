# Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

> 方法论文 · 2023 · `wf_title_85954f3817cf3610`

**作者**：Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, Tim Rocktäschel  
**原文**：https://arxiv.org/abs/2309.16797  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：任务提示P与变异提示M共同演化的提示人口；具体更新过程为：后继M指导下一代任务提示生成；变异提示自身也被更新；更新状态的保留与后继使用为：跨提示进化代。

## 2. 论文的核心内容与贡献

### configuration:cfg_promptbreeder
任务与变异提示共同跨代保留，变异提示驱动后代生成；基础LM、选择与fitness固定。

**适用版本**：1；**原文定位**：S1.p3; S3.p3-p5; A6.p3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_promptbreeder
`cfg_promptbreeder` · explicit_boundary_from_previous_primary_recheck

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 任务提示P与变异提示M共同演化的提示人口 |
| 改进过程与下一轮参与 | 后继M指导下一代任务提示生成；变异提示自身也被更新 |
| 保留的状态及时间尺度 | 跨提示进化代 |
| 外部固定部分 | LM、遗传选择框架与外部fitness |

**配置判定**：任务与变异提示共同跨代保留，变异提示驱动后代生成；基础LM、选择与fitness固定。

来源：https://arxiv.org/html/2309.16797v1；版本：1；定位：S1.p3; S3.p3-p5; A6.p3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_promptbreeder`**：任务提示及变异提示共同跨代保留；后继变异提示驱动后代生成。
  - 来源版本：v1；定位：S1.p3；S3.p3；S3.p4；S3.p5；A6.p3；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- LM、选择框架与外部fitness固定；不认证无限增长

## 7. 与其他论文的具体关系

### [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](../r03_method/wf_c1ef72d96fa3292590.md)
关系：`contrasts_system_boundary_with` · `r2_gepa_promptbreeder_6` · 当前展示权限：`primary_supported`。
GEPA用固定反思模板处理候选执行轨迹/文字反馈并改写模块指令；Promptbreeder共同演化任务提示及其变异提示。

**关系边界**：GEPA确有相关工作引用，机制对照由整理者双端核查得出；引用不证明派生、共用代码或等预算优越。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2507.19457v2；版本：v2；定位：S3.p4；S6.p1。
- object：https://arxiv.org/html/2309.16797v1；版本：v1；定位：S3.p3；S3.p4；S3.p5；S3.SS2.SSS3.p3。
- expand_src_w_gepa：https://arxiv.org/html/2507.19457v2；版本：v2；定位：S3.p1；S3.p2；S3.p3；S3.p4；S3.SS1.p1；S6.p1。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_promptbreeder` · 已存来源 · v1
  - https://arxiv.org/html/2309.16797v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_85954f3817cf3610 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
