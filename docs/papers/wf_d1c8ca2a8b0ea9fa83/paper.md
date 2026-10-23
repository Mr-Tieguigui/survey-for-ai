# EvalResearchBench: Can AI Agents Design Their Own Evaluations?

> Benchmark/数据集/任务套件 · 2026 · `wf_d1c8ca2a8b0ea9fa83`

**作者**：Yaolun Zhang, Tianyi Xu, Yujie Zhao, Jishen Zhao, Qingyun Wu, Huazheng Wang  
**原文**：https://arxiv.org/abs/2610.04184  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
现有材料未形成可采用的具体内容解析。本卡保留身份、阅读位置与核查缺口，不以题名推断贡献。

## 2. 论文的核心内容与贡献

### role:r11_role_evalresearch
EvalResearchBench评测代理构造可复用评测器的能力：研究episode可根据开发pilot修题、grader和权重，交付后冻结，再在开发/密封候选模型和target references上独立执行。CCC分数一致性与成对排序准确率分开衡量；测量工具设计能力不等于已完成系统能力递归增长。

**适用版本**：2610.04184v1；**原文定位**：§3.1 research task/submission tool L119–130；§3.2–3.3 independent assessment/metrics tool L131–151；§4.1 setup/budgets tool L158–174；§4.2 transfer/baseline limitations tool L202–207。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：作者把它定位为RSI反馈仪器本身的研究；存在开发pilot反馈循环，但本批只认证其评测协议及适用限制，不另造一个通用RSI方法配置。
- **leakage and information boundary**：sealed表示研究过程不可访问，不代表reference或原题在全网/预训练不可得；正文称reference为固定公共快照。冻结程序不得根据候选identity查表或评测时读取reference。
- **metrics**：- Score=100×CCC，包含相关性、均值和尺度吻合；PA衡量reference非平分候选对排序，测量平局计半分 - 按目标等权聚合；记录覆盖率、不完整执行和开发/研究推理/独立assessment开销
- **selection and reuse**：研究者可选公共题、合成新题、修grader和调整weights；3小时，研究推理$100、开发/helper测试$100；assessment另有总$120与每候选$30上限。
- **split and visibility**：4个候选开发可见、9个sealed；6个target开发可见、8个sealed。候选API访问和target-reference访问独立分配；题目、grader、weights先冻结。独立assessment结果不返还供修订。
- **task or data unit**：单元为某model+harness的一次预算研究episode交付的执行评测器，至少100道distinct scored questions，覆盖coding/co-work/reasoning；13候选、14目标benchmark。
- **unknowns**：- 多episode方差和新候选/新target的长期迁移unknown - 源码级信息隔离及所有reference尺度兼容证明未复核

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r11_ev_evalresearch`**：EvalResearchBench评测代理构造可复用评测器的能力：研究episode可根据开发pilot修题、grader和权重，交付后冻结，再在开发/密封候选模型和target references上独立执行。CCC分数一致性与成对排序准确率分开衡量；测量工具设计能力不等于已完成系统能力递归增长。
  - 来源版本：2610.04184v1；定位：§3.1 research task/submission tool L119–130；§3.2–3.3 independent assessment/metrics tool L131–151；§4.1 setup/budgets tool L158–174；§4.2 transfer/baseline limitations tool L202–207；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 每研究者仅一个episode，模型和harness绑定，不能分离独立组件效果。
- 开发最好不等于sealed最好；公共任务抽样Random120是强基线。
- 输出截断、预算耗尽和少量高权重题可影响结果；固定13候选/14目标面板不能证明未来模型的广泛效度。
- 每研究者仅一个episode，模型和harness绑定，不能分离独立组件效果。; 开发最好不等于sealed最好；公共任务抽样Random120是强基线。; 输出截断、预算耗尽和少量高权重题可影响结果；固定13候选/14目标面板不能证明未来模型的广泛效度。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_evalresearch` · EvalResearchBench: Can AI Agents Design Their Own Evaluations? · 2610.04184v1
  - https://arxiv.org/html/2610.04184v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d1c8ca2a8b0ea9fa83 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
