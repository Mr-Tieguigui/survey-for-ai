# WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

> Benchmark/数据集/任务套件 · 2026 · `wf_d647668c0e4e6129a2`

**作者**：Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, Yubo Ma, Haodong Duan, Jing Shao, Jiaqi Wang, Dahua Lin, Kai Chen, Yuhang Zang  
**原文**：https://arxiv.org/abs/2605.10912  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
WildClawBench在production-grade native harnesses中测60项long-horizon任务，混合规则、environment audit与LLM/VLM评分；single-turn instruction后agent自主执行到完成/超时。长轨迹不是系统跨任务自我改进，统一初始workspace也不是独立数据泛化证明。

## 2. 论文的核心内容与贡献

### role:r14_role_wild
WildClawBench在production-grade native harnesses中测60项long-horizon任务，混合规则、environment audit与LLM/VLM评分；single-turn instruction后agent自主执行到完成/超时。长轨迹不是系统跨任务自我改进，统一初始workspace也不是独立数据泛化证明。

**适用版本**：2605.10912v1；**原文定位**：§3.2–3.3 data/pilot selection tool L109–120；§3.4 execution/scoring tool L121–128；§4.1 grading isolation/aggregation tool L130–134；AppendixB limitations tool L274–276。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：可为自改harness/skills的真实工作负载测量提供背景；所读主协议测固定harness/model条件，不是在线自改实验。
- **metrics**：- task score组合rule、side-effect audit和GPT5.4 judge；overall按task counts加权 - time/cost/token/tool-call另报；timeout只评已产artifact，不当完成
- **selection and reuse**：8researchers2周作者/rubric/过滤/refine；pilot frontier model最大scoregap≥0.2保留，再human审ambiguity/leakage/环境。此discriminability选择不代表部署任务无偏抽样。
- **split and visibility**：grading-only assets/groundtruth在agent退出后才挂载；协议执行隔离不等于全新任务train/test拆分。
- **task or data unit**：60tasks，36English/24Chinese、26multimodal/34text，300–1200秒任务budget；每task×model/harness run初始化同workspace。
- **unknowns**：- 真实deployment任务分布覆盖率/预训练污染unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_wild`**：WildClawBench在production-grade native harnesses中测60项long-horizon任务，混合规则、environment audit与LLM/VLM评分；single-turn instruction后agent自主执行到完成/超时。长轨迹不是系统跨任务自我改进，统一初始workspace也不是独立数据泛化证明。
  - 来源版本：2605.10912v1；定位：§3.2–3.3 data/pilot selection tool L109–120；§3.4 execution/scoring tool L121–128；§4.1 grading isolation/aggregation tool L130–134；AppendixB limitations tool L274–276；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 当前single-turn无用户中途clarification/correction，60任务领域覆盖有限。
- mixed judge不同criteria不能当全deterministic评分；pilot selection及固定harness各自限定因果比较。
- GUI-heavy和specialist biology/finance/law覆盖轻；未独立运行任务/审所有评分可靠性。
- 当前single-turn无用户中途clarification/correction，60任务领域覆盖有限。; mixed judge不同criteria不能当全deterministic评分；pilot selection及固定harness各自限定因果比较。; GUI-heavy和specialist biology/finance/law覆盖轻；未独立运行任务/审所有评分可靠性。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_wild` · WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation · 2605.10912v1
  - https://arxiv.org/html/2605.10912v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d647668c0e4e6129a2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
