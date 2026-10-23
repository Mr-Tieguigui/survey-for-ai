# TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces

> Benchmark/数据集/任务套件 · 2026 · `wf_e04069610c4d92517f`

**作者**：Dehai Min, Daoan Zhang, Yiming Zeng, Huayi Zhang, Ziyi Chen, Yan Zhang, Qinbo Bai, Mengyuan Chao, Jing Ning, Qiyue Hua, Huiyi Chen, Hanrong Zhang, Henry Peng Zou, Jie Yang, Wei Xu, Philip S. Yu  
**原文**：https://arxiv.org/abs/2609.33295  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
TraceDance从deployment traces中按query合成/检索behavior anchor，确认坏行为发生点并切出统一prefix，评测模型下一turn是否满足rubric。它测已发生行为条件下的关键决策续写，不测deployment发生率或后续全任务成功。

## 2. 论文的核心内容与贡献

### role:r14_role_tracedance
TraceDance从deployment traces中按query合成/检索behavior anchor，确认坏行为发生点并切出统一prefix，评测模型下一turn是否满足rubric。它测已发生行为条件下的关键决策续写，不测deployment发生率或后续全任务成功。

**适用版本**：2609.33295v1；**原文定位**：§3 scope/anchor/instance/judge tool L103–118；§5.1–5.3 query/human validation tool L141–155；§5.2 construction counts tool L146–151；AppendixF limitations tool L602–608。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：与RSI失败挖掘、退化/持久行为监测有关的测量工具；本批不把anchor合成方法自动作RSI core。
- **metrics**：- construction success/rejection与human query/instance validity - 三LLM judge 0–5平均≥4为pass；benchmark passrate=下一turn通过比例 - 人标84/100确认行为、judge pass/fail与可用人标81%一致，非完整任务正确率
- **selection and reuse**：只可程序检索的可观察behavior；anchor安全/code review与FastModel confirmation，多轮修anchor，5–50instances边界；最多二behavior查询。
- **split and visibility**：source reasoning blocks去除，其余recordedprefix保留；source turn被留出供重答。没有reconstructed environment执行，因此不是传统end-to-end heldout任务。
- **task or data unit**：behavior-query构建benchmark；139test queries中107 build-target/32reject-target，最终107benchmarks/4125instances；每instance是记录prefix到cut的下一turn。
- **unknowns**：- cut后真实执行后果和deployment行为发生率unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_tracedance`**：TraceDance从deployment traces中按query合成/检索behavior anchor，确认坏行为发生点并切出统一prefix，评测模型下一turn是否满足rubric。它测已发生行为条件下的关键决策续写，不测deployment发生率或后续全任务成功。
  - 来源版本：2609.33295v1；定位：§3 scope/anchor/instance/judge tool L103–118；§5.1–5.3 query/human validation tool L141–155；§5.2 construction counts tool L146–151；AppendixF limitations tool L602–608；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- single next-turn不能观察以后适当行动或失败；passing不保证运行成功。
- 按已发生坏行为筛选，不能估计deployment prevalence；rubric可能比仅避免坏行为更严。
- 自动construction/grading不完美，judges相对human偏宽松；上下文来自源模型family，公平性需另审。
- single next-turn不能观察以后适当行动或失败；passing不保证运行成功。; 按已发生坏行为筛选，不能估计deployment prevalence；rubric可能比仅避免坏行为更严。; 自动construction/grading不完美，judges相对human偏宽松；上下文来自源模型family，公平性需另审。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_tracedance` · TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces · 2609.33295v1
  - https://arxiv.org/html/2609.33295v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_e04069610c4d92517f --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
