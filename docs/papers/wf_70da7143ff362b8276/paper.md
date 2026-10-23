# Self-Preference Bias in Rubric-Based Evaluation of Large Language Models

> 评测方法/测量科学 · 2026 · `wf_70da7143ff362b8276`

**作者**：José Pombal, Ricardo Rei, André F. T. Martins  
**原文**：https://arxiv.org/abs/2604.06996  
**研究分支**：评价协议、因果归因与复现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
该研究在objective IFEval与subjective HealthBench比较LLM judges对自身/同family输出的偏好。rubric-based评价并不自动消除self-preference；HealthBench reference是模型多数票proxy，不能当独立人类gold。

## 2. 论文的核心内容与贡献

### role:r14_role_preference
该研究在objective IFEval与subjective HealthBench比较LLM judges对自身/同family输出的偏好。rubric-based评价并不自动消除self-preference；HealthBench reference是模型多数票proxy，不能当独立人类gold。

**适用版本**：2604.06996v1；**原文定位**：§2.2–2.4 metrics/models/reference tool L97–110；§3 objective/self-family/ensemble tool L132–140；§4 subjective/cuts tool L141–154；§6 conclusion tool L166–168。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：为RSI自生成/自评/候选选择提供评价偏差证据；关联是策展者对反馈仪器的解释，不认证本文运行RSI训练。
- **metrics**：- Mean Rubric Accuracy匹配reference的比例 - self/family overestimation与HealthBench centered score delta；pairwise比较交换呈现次序，ensemble减偏但未完全消除
- **selection and reuse**：多family多规模judge/generator，成本使proprietary模型未进AR/DA/PWC全部experiment，不能当完整同矩阵比较。
- **split and visibility**：这是generated-output cross-judge评测，不是学习train/test split；IFEval程序验证作为objective reference，HealthBench以五family最大judge多数票reference。
- **task or data unit**：judge×generator×prompt×binary rubric verdict，以及汇总instance/system score；IFEval541 prompts，HealthBench5000 instances/48562 unique rubrics。
- **unknowns**：- 模型reference与真实人类标准的全部一致性unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_preference`**：该研究在objective IFEval与subjective HealthBench比较LLM judges对自身/同family输出的偏好。rubric-based评价并不自动消除self-preference；HealthBench reference是模型多数票proxy，不能当独立人类gold。
  - 来源版本：2604.06996v1；定位：§2.2–2.4 metrics/models/reference tool L97–110；§3 objective/self-family/ensemble tool L132–140；§4 subjective/cuts tool L141–154；§6 conclusion tool L166–168；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- HealthBench多数票不完美且包含各model family，可能低估偏好。
- 同模型/同family偏好不对每rubric/领域一律相同；negative/长短rubric等只是本setting切片。
- 未实读全部metric推导或源码复现，不能外推所有judge prompt/未来模型。
- HealthBench多数票不完美且包含各model family，可能低估偏好。; 同模型/同family偏好不对每rubric/领域一律相同；negative/长短rubric等只是本setting切片。; 未实读全部metric推导或源码复现，不能外推所有judge prompt/未来模型。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_preference` · Self-Preference Bias in Rubric-Based Evaluation of Large Language Models · 2604.06996v1
  - https://arxiv.org/html/2604.06996v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_70da7143ff362b8276 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
