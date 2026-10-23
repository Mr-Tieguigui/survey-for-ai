# Large Language Models Cannot Self-Correct Reasoning Yet

> 失败/限制/风险 · 2023 · `wf_de57da1de7b7aa9892`

**作者**：Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou  
**原文**：https://arxiv.org/abs/2310.01798  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
原文选段核查：以负结果、受控对照或有假设的边界分析为本survey提供评价限制，配置与原始方法分离。

## 2. 论文的核心内容与贡献

### configuration:cfg_intrinsic_selfcorrection_two_round_audit
将其收录为有边界的负结果与评价协议：有限模型/任务/提示下无oracle的重答退化，以及同预算和初始提示完整性混杂；不认证所有未来模型均不能自纠正。

**适用版本**：2310.01798v2；**原文定位**：S2.p2；S2.p3；S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS2.p1；S3.SS2.p3；S3.SS2.p4；S4.p1；S4.p2；S5.p1；S5.p3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### Intrinsic self-correction versus oracle stopping: two-round reasoning audit
`cfg_intrinsic_selfcorrection_two_round_audit` · negative_result_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 同一问题的初始回答、反馈与最多两次重答；模型权重和三步提示框架固定。 |
| 改进过程与下一轮参与 | 固定模型先生成答案、再批评、再重答；oracle臂用真值决定停止，intrinsic臂由模型独立判断是否保留。 |
| 保留的状态及时间尺度 | 回答历史仅用于同一问题的有限轮次；未建立跨新问题保留的学习状态。 |
| 外部固定部分 | - 固定模型版本 - 问题集及真值仅用于最终计分或独立oracle臂 - 提示与两轮上限 - 解码配置 |
| 评价与选择设置 | - **controls**：- oracle stopping versus no oracle - multi-agent debate versus equal-response self-consistency - informative initial instruction in constrained generation - **maximum self correction rounds**：2 - **models**：- gpt-3.5-turbo-0613 - GPT-4 accessed 2023-08-29 - gpt-4-1106-preview - Llama-2-70b-chat - **sample size**：GPT-3.5 full sets; other models 200 per set except HotpotQA 100 - **tasks**：- GSM8K - CommonSenseQA - HotpotQA closed-book - **temperature**：- **GPT-3.5-Turbo**：1 - **GPT-4**：1 - **GPT-4-Turbo**：0 - **Llama-2**：0 |

**配置判定**：将其收录为有边界的负结果与评价协议：有限模型/任务/提示下无oracle的重答退化，以及同预算和初始提示完整性混杂；不认证所有未来模型均不能自纠正。

来源：https://arxiv.org/html/2310.01798v2；版本：2310.01798v2；定位：S2.p2；S2.p3；S3.SS1.p1；S3.SS1.p2；S3.SS1.p3；S3.SS2.p1；S3.SS2.p3；S3.SS2.p4；S4.p1；S4.p2；S5.p1；S5.p3。

## 4. 实验、评价协议与结果的可解释范围


- **controls**：- oracle stopping versus no oracle - multi-agent debate versus equal-response self-consistency - informative initial instruction in constrained generation
- **maximum self correction rounds**：2
- **models**：- gpt-3.5-turbo-0613 - GPT-4 accessed 2023-08-29 - gpt-4-1106-preview - Llama-2-70b-chat
- **sample size**：GPT-3.5 full sets; other models 200 per set except HotpotQA 100
- **tasks**：- GSM8K - CommonSenseQA - HotpotQA closed-book
- **temperature**：- **GPT-3.5-Turbo**：1 - **GPT-4**：1 - **GPT-4-Turbo**：0 - **Llama-2**：0

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`round3_limits_ev_cfg_intrinsic_selfcorrection_two_round_audit`**：将其收录为有边界的负结果与评价协议：有限模型/任务/提示下无oracle的重答退化，以及同预算和初始提示完整性混杂；不认证所有未来模型均不能自纠正。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- oracle臂可阻止正确答案被改错，不能混写为纯内生判断。
- §5直接检验Self-Refine式约束生成提示；不同原方法任务不可一概用此结果否定。
- 三项推理数据与所测旧模型不覆盖训练后增强、自验证器或工具反馈设定。
- 选段方法与控制变量核查；不是全文逐项复现，不认证无界或跨任务增益。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `round3_limits_src_w_self_correction_limit` · 已存来源 · 2310.01798v2
  - https://arxiv.org/html/2310.01798v2；阅读深度：`targeted_original_method_evaluation_and_limit_passages`。

**证据深度**：primary_abstract_or_official_summary_review, selected_primary_method_controls_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_de57da1de7b7aa9892 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
