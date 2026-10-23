# The Curse of Recursion: Training on Generated Data Makes Models Forget

> 失败/限制/风险 · 2023 · `wf_0da7913c890d2c36b0`

**作者**：Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson  
**原文**：https://arxiv.org/abs/2305.17493  
**研究分支**：失败、漂移、坍塌与误导性反馈  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
原文选段核查：以负结果、受控对照或有假设的边界分析为本survey提供评价限制，配置与原始方法分离。

## 2. 论文的核心内容与贡献

### configuration:cfg_model_collapse_opt125m_replacement
本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。

**适用版本**：2305.17493v3；**原文定位**：S3.SS1.p1；S3.SS1.p2；S4.p1；S4.SS3.p3；S5.SS2.p2；S5.SS2.p3；S5.SS2.p4；S5.SS2.p5；S5.SS2.p6；S5.SS2.p7；S5.SS2.p9。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_model_collapse_opt125m_tenpercent_real
本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。

**适用版本**：2305.17493v3；**原文定位**：S3.SS1.p1；S3.SS1.p2；S4.p1；S4.SS3.p3；S5.SS2.p2；S5.SS2.p3；S5.SS2.p4；S5.SS2.p5；S5.SS2.p6；S5.SS2.p7；S5.SS2.p9。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### OPT-125M generational data replacement audit
`cfg_model_collapse_opt125m_replacement` · negative_result_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定外部训练/采样协议下的一系列OPT-125M生成数据与后继fine-tuned模型；用于测量代际分布退化。 |
| 改进过程与下一轮参与 | 训练后的前代生成器产出下一代训练文本，下一代训练后的生成器继续供给后续代训练数据；由此更新后的生成状态实际参与后续学习。训练器和替代/混合方案固定不否定第四条件。 |
| 保留的状态及时间尺度 | 跨代传递依据是前代生成文本被后代训练使用、后代再次生成训练文本；不以同一个参数张量跨代连续继承为前提。§5.2称每周期从预训练模型开始并使用另一fine-tuned模型生成数据，又称按原始验证集选择后续代base；本次不把它改写为已核实的持续权重初始化谱系。 |
| 外部固定部分 | - OPT-125M基础架构和预训练模型 - WikiText2原始语料 - fine-tuning与采样规则 - 真数据保留比例与epochs |
| 评价与选择设置 | - **additional control**：repetition penalty 2.0 also examined - **backbone**：OPT-125M - **base selection**：best on original WikiText2 validation - **context block tokens**：64 - **dataset**：WikiText2 - **fine tuning epochs**：5 - **generation**：5-way beam search - **original data retained fraction**：0 - **predicted continuation tokens**：64 - **runs**：5 - **synthetic dataset size**：same size as original training set |

**配置判定**：本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。

来源：https://arxiv.org/html/2305.17493v3；版本：2305.17493v3；定位：S3.SS1.p1；S3.SS1.p2；S4.p1；S4.SS3.p3；S5.SS2.p2；S5.SS2.p3；S5.SS2.p4；S5.SS2.p5；S5.SS2.p6；S5.SS2.p7；S5.SS2.p9。

### OPT-125M generational audit with 10% original data
`cfg_model_collapse_opt125m_tenpercent_real` · negative_result_evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定外部训练/采样协议下的一系列OPT-125M生成数据与后继fine-tuned模型；用于测量代际分布退化。 |
| 改进过程与下一轮参与 | 训练后的前代生成器产出下一代训练文本，下一代训练后的生成器继续供给后续代训练数据；由此更新后的生成状态实际参与后续学习。训练器和替代/混合方案固定不否定第四条件。 |
| 保留的状态及时间尺度 | 跨代传递依据是前代生成文本被后代训练使用、后代再次生成训练文本；不以同一个参数张量跨代连续继承为前提。§5.2称每周期从预训练模型开始并使用另一fine-tuned模型生成数据，又称按原始验证集选择后续代base；本次不把它改写为已核实的持续权重初始化谱系。 |
| 外部固定部分 | - OPT-125M基础架构和预训练模型 - WikiText2原始语料 - fine-tuning与采样规则 - 真数据保留比例与epochs |
| 评价与选择设置 | - **additional control**：repetition penalty 2.0 also examined - **backbone**：OPT-125M - **base selection**：best on original WikiText2 validation - **context block tokens**：64 - **dataset**：WikiText2 - **fine tuning epochs**：10 - **generation**：5-way beam search - **original data retained fraction**：0.1 - **predicted continuation tokens**：64 - **runs**：5 - **synthetic dataset size**：same size as original training set |

**配置判定**：本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。

来源：https://arxiv.org/html/2305.17493v3；版本：2305.17493v3；定位：S3.SS1.p1；S3.SS1.p2；S4.p1；S4.SS3.p3；S5.SS2.p2；S5.SS2.p3；S5.SS2.p4；S5.SS2.p5；S5.SS2.p6；S5.SS2.p7；S5.SS2.p9。

## 4. 实验、评价协议与结果的可解释范围


- **additional control**：repetition penalty 2.0 also examined
- **backbone**：OPT-125M
- **base selection**：best on original WikiText2 validation
- **context block tokens**：64
- **dataset**：WikiText2
- **fine tuning epochs**：5
- **generation**：5-way beam search
- **original data retained fraction**：0
- **predicted continuation tokens**：64
- **runs**：5
- **synthetic dataset size**：same size as original training set


- **additional control**：repetition penalty 2.0 also examined
- **backbone**：OPT-125M
- **base selection**：best on original WikiText2 validation
- **context block tokens**：64
- **dataset**：WikiText2
- **fine tuning epochs**：10
- **generation**：5-way beam search
- **original data retained fraction**：0.1
- **predicted continuation tokens**：64
- **runs**：5
- **synthetic dataset size**：same size as original training set

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`accel_ev_collapse_protocol_limit`**：语言模型实验比较生成数据迭代及保留10%原始数据的设置。
  - 来源版本：unknown；定位：§5.2 pp.10–12；Figure 10–11；深度：`未单列`。

- **`round3_limits_ev_cfg_model_collapse_opt125m_replacement`**：本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`round3_limits_ev_cfg_model_collapse_opt125m_tenpercent_real`**：本次核实有限代际实验内四项结构条件：训练后的生成器通过后继训练数据参与下一轮更新。作为负结果/限制证据置于background；不是正向RSI方法配置或收益证明。保留数据比例和epochs同时不同，不将两臂差异解释为单独真数据比例的因果效果。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 有限采样理论有其分布和近似假设，不是对所有筛选、校验、外部真实数据或RL方案的普遍不可能定理。
- OPT-125M+WikiText2的生成续写重训不同于带答案真值过滤的STaR。
- 第四条件要求更新状态参与后续改进过程，不要求optimizer或训练算法自行改写。该实验显示退化，结构闭环不构成实际能力增益证据。
- 只有本原文明确实施的前代生成→后代训练→后代继续生成的多代实验支持上述结构判定；不能仅因其他论文使用合成数据便推定其满足递归条件。
- 未检查到STaR/SPIN专项评测；不能由此直接否定经验证筛选的所有自训练。
- 选段方法与控制变量核查；不是全文逐项复现，不认证无界或跨任务增益。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_model_collapse_pdf` · 已存来源 · unversioned_served_document
  - https://arxiv.org/pdf/2305.17493；阅读深度：`未单列`。
- `round3_limits_src_w_model_collapse` · 已存来源 · 2305.17493v3
  - https://arxiv.org/html/2305.17493v3；阅读深度：`targeted_original_method_evaluation_and_limit_passages`。

**证据深度**：primary_abstract_or_official_summary_review, selected_primary_method_controls_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0da7913c890d2c36b0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
