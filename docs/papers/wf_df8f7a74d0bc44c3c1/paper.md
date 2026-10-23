# The Mighty ToRR: A Benchmark for Table Reasoning and Robustness

> Benchmark/数据集/任务套件 · 2025 · `wf_df8f7a74d0bc44c3c1`

**作者**：Shir Ashury-Tahan, Yifan Mai, Rajmohan C, Ariel Gera, Yotam Perlitz, Asaf Yehudai, Elron Bandel, Leshem Choshen, Eyal Shnarch, Percy Liang, Michal Shmueli-Scheuer  
**原文**：https://arxiv.org/abs/2502.19412  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ToRR综合现有表格任务，并对同例多种serialization/结构扰动测performance和robustness。目的是避免单一prompt配置误导排行；它测表格推理的格式稳定性，不直接测RSI状态更新或更善改进。

## 2. 论文的核心内容与贡献

### role:r14_role_torr
ToRR综合现有表格任务，并对同例多种serialization/结构扰动测performance和robustness。目的是避免单一prompt配置误导排行；它测表格推理的格式稳定性，不直接测RSI状态更新或更善改进。

**适用版本**：2502.19412v1；**原文定位**：§2 construction/configurations tool L124–142；§2.2 performance/robustness tool L145–151；§2.3 sampling/fewshot tool L169–174；§8 limitations tool L263–274。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：背景测量：可为自改prompt/harness的表格场景提供独立鲁棒性维度，但任何RSI桥接需另证。
- **metrics**：- 各源数据集score归一化后跨数据集/例/config平均performance - robustness为1减每例不同config分数range的平均，须与正确率分开
- **selection and reuse**：优先挑战且表格能直接嵌prompt的已有任务，14model、greedy/max512输出。比较多prompt配置；不是新训练流程。
- **split and visibility**：通常每数据集test抽100例，同模型相同例；TableBench FC为96例且79用于ToRR其余作demonstrations。5-shot，WikiTQ因长度例外1-shot。
- **task or data unit**：跨数据集的table example×prompt configuration×model；7serialization与4扰动加不扰动形成35configs。
- **unknowns**：- 各源数据集全量去重/污染审计unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_torr`**：ToRR综合现有表格任务，并对同例多种serialization/结构扰动测performance和robustness。目的是避免单一prompt配置误导排行；它测表格推理的格式稳定性，不直接测RSI状态更新或更善改进。
  - 来源版本：2502.19412v1；定位：§2 construction/configurations tool L124–142；§2.2 performance/robustness tool L145–151；§2.3 sampling/fewshot tool L169–174；§8 limitations tool L263–274；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 不覆盖先检索/抽取table的流程；外部数据和metric可能有偏差。
- 模型排行一致性作为可靠性proxy可能不等于真实表现；不可把稳定误差当高能力。
- 预训练污染和few-shot语义泄露未独立审计。
- 不覆盖先检索/抽取table的流程；外部数据和metric可能有偏差。; 模型排行一致性作为可靠性proxy可能不等于真实表现；不可把稳定误差当高能力。; 预训练污染和few-shot语义泄露未独立审计。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_torr` · The Mighty ToRR: A Benchmark for Table Reasoning and Robustness · 2502.19412v1
  - https://arxiv.org/html/2502.19412v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_df8f7a74d0bc44c3c1 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
