# SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?

> Benchmark/数据集/任务套件 · 2026 · `wf_5bcc65d4b4724d2a72`

**作者**：Yuqiao Tan, Shizhu He, Jun Zhao, Kang Liu  
**原文**：https://arxiv.org/abs/2609.09113  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SAEScientist-Bench测固定Gemma-2-9B-IT/Gemma Scope中单特征发现：代理自写contrastive probes、比较candidate并提交feature ID，冻结evaluation suite和expert reference用于事后Rank/Activation/Steering。相关激活、对照区分和因果steering必须分列；接入编辑或continual alignment闭环为未来工作。

## 2. 论文的核心内容与贡献

### role:r11_role_saescientist
SAEScientist-Bench测固定Gemma-2-9B-IT/Gemma Scope中单特征发现：代理自写contrastive probes、比较candidate并提交feature ID，冻结evaluation suite和expert reference用于事后Rank/Activation/Steering。相关激活、对照区分和因果steering必须分列；接入编辑或continual alignment闭环为未来工作。

**适用版本**：2609.09113v1；**原文定位**：§3.1–3.2 tasks/interface tool L138–145；§3.3 measurements tool L148–173；§4 setup/aggregation tool L175–196；§7 limitations tool L287–291。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：作者明确将表征审计定位为RSI的监测支柱；本协议没有训练新SAE或把feature送入持续模型编辑/对齐来验证下一代收益。
- **leakage and information boundary**：不允许发现阶段接触Expert/eval set且禁网络，是协议隔离；Expert部分来源公开Neuronpedia，不能据此认证无预训练污染。
- **metrics**：- Rank=100×2rexp/(rf+rexp)，范围0–200，expert parity100 - Activation=100×max(0,2AUROC−1)，positive对hard-negative+neutral controls - Steering为target relevance相对baseline和norm-matched random中较强者的净增加；instruction preservation/degeneration另报；Overall是三项算术均值
- **selection and reuse**：网络禁用、相同接口和任务指令；无人工step cap，代理自定queries/停止，model与harness共同执行。每任务等权，均值/SD来自三run。
- **split and visibility**：agent-written probes仅供discovery；Expert及positive/hard-negative/neutral evaluation texts留给提交后评测。替代feature的alpha先在五个held-out prompts校准。固定同base model+SAE。
- **task or data unit**：20个concept×layer任务，层9/20、每层131072维字典，10种agent配置，每任务三次独立调查；单次提交一个feature。
- **unknowns**：- judge人工一致性和Expert多参考敏感性unknown - 跨模型/多feature/下游编辑循环效果unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r11_ev_saescientist`**：SAEScientist-Bench测固定Gemma-2-9B-IT/Gemma Scope中单特征发现：代理自写contrastive probes、比较candidate并提交feature ID，冻结evaluation suite和expert reference用于事后Rank/Activation/Steering。相关激活、对照区分和因果steering必须分列；接入编辑或continual alignment闭环为未来工作。
  - 来源版本：2609.09113v1；定位：§3.1–3.2 tasks/interface tool L138–145；§3.3 measurements tool L148–173；§4 setup/aggregation tool L175–196；§7 limitations tool L287–291；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 固定单模型、两层、单feature和预设concept，不覆盖multi-feature circuit或开放假设研究。
- 固定专家/文本suite、LLM steering judge有偏差和噪声；总体复合分并非每个指标均0–100。
- 10模型与不同harness绑定，无统一step上限，不能把复合排行解释为等预算纯模型因果效应。
- 固定单模型、两层、单feature和预设concept，不覆盖multi-feature circuit或开放假设研究。; 固定专家/文本suite、LLM steering judge有偏差和噪声；总体复合分并非每个指标均0–100。; 10模型与不同harness绑定，无统一step上限，不能把复合排行解释为等预算纯模型因果效应。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_saescientist` · SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research? · 2609.09113v1
  - https://arxiv.org/html/2609.09113v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_5bcc65d4b4724d2a72 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
