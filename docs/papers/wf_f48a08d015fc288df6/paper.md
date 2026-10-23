# UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement

> 方法论文 · 2026 · `wf_f48a08d015fc288df6`

**作者**：Fang Wu, Da Xing, Yanjie Huang, Junxi Wang, Ji Wang, Hejia Geng, Guancheng Wan, Bowen Zuo, Xiaomin Li, Shixiang Tang, Xinyu Xiang, Zehong Wang, Shiyi Du, Peng Xia, Shuangjia Zheng, Yining Hong, Li Erran Li, Jure Leskovec, Yejin Choi  
**原文**：https://arxiv.org/abs/2609.38721  
**研究分支**：多模态、医疗与视觉  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
UniEvo-VL 让同一多模态模型在普通问题与特权自批评上下文下分别作学生和教师，在学生轨迹上匹配去噪分布；摘要另比较外部 critic 并承认文本渲染表现混合，需核教师更新及任务差异。

## 2. 论文的核心内容与贡献

### configuration:cfg_unievo_vl_one_critique_inference_v1
保留相邻对照；不将单次离线训练或单题推理自动认证为改进器递归升级。

**适用版本**：2609.38721v1；**原文定位**：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_unievo_vl_verified_ema_training_v1
在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

**适用版本**：2609.38721v1；**原文定位**：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18ctx_role_review_wf_f48a08d015fc288df6`
UniEvo-VL 让同一多模态模型在普通问题与特权自批评上下文下分别作学生和教师，在学生轨迹上匹配去噪分布；摘要另比较外部 critic 并承认文本渲染表现混合，需核教师更新及任务差异。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### UniEvo-VL: verified corrective-prompt EMA distillation
`cfg_unievo_vl_verified_ema_training_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Qwen-Image-2512 student与EMA teacher生成适配器，固定Qwen3-VL critique/synthesis及原prompt后验接受门；只LoRA可学习。 |
| 改进过程与下一轮参与 | 用当前生成器草图得到修订prompt，仅接受在同noise下重生成被固定critic按原请求认可的修订；学生原prompt轨迹的六个最噪状态匹配EMA教师特权prompt转换，AdamW更新LoRA，teacher EMA吸收新LoRA。 |
| 保留的状态及时间尺度 | LoRA参数跨请求/更新保留，EMA teacher后续提供监督；base权重与critic冻结，非逐请求从初始adapter重启。 |
| 外部固定部分 | - Qwen-Image base权重 - Qwen3-VL-8B-Thinking critic与8B-Instruct synthesis - AdamW及latent transition MSE - 原请求接受规则与EMA0.999 |
| 评价与选择设置 | - **LoRA alpha**：16 - **LoRA rank**：16 - **acquisition**：one correction opportunity; same noise for revision - **critic**：fixed Qwen3-VL-8B-Thinking - **denoising steps**：20 - **deployment direct PI**：False - **generator**：Qwen-Image-2512 - **iterations**：reported optimizer checkpoint140 for verified GenEval table7; other coverage in supplementary data, not asserted fixed deployment-cycle count - **learning rate**：0.0003 - **optimizer**：AdamW - **post revision verification**：True - **synthesis**：fixed Qwen3-VL-8B-Instruct - **teacher EMA decay**：0.999 - **training scope**：generator LoRA only - **transition selected**：6 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：生成器student、EMA参考teacher及固定critic/synthesis获得反馈的训练系统已分离。（状态：`supported`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **更新由什么过程产生**：学生生成图像引出critic修订prompt，并沿自身状态轨迹蒸馏，更新generator LoRA。（状态：`supported`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **状态怎样持久保留**：生成器LoRA跨请求/optimizer steps保留，不为每图重置；EMA参考也继承。（状态：`supported`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **更新怎样进入后续改进**：更新生成器改变后续草图及训练轨迹，其LoRA又以EMA进入未来privileged教师目标；critic和optimizer未自改。（状态：`supported`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。

**配置判定**：在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

来源：https://arxiv.org/html/2609.38721v1；版本：2609.38721v1；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570。

### UniEvo-VL: saved-adapter one-critique inference
`cfg_unievo_vl_one_critique_inference_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定保存的student adapter及每请求至多一次critic—prompt修订—重生成过程，训练不在此边界内。 |
| 改进过程与下一轮参与 | 原prompt生成草图；若被接受直接保留，否则一次critic修订后重生成，始终按原请求评分。 |
| 保留的状态及时间尺度 | 只在本请求保留草图/critique；模型adapter固定无optimizer更新。 |
| 外部固定部分 | - 已训练adapter - fixed critic/synthesis - 一次修订机会 - 评价原请求 |
| 评价与选择设置 | - **compute**：accepted drafts require no regeneration; same opportunity budget need not mean equal compute - **evaluation population**：all original benchmark prompts, not filtered by training acceptance - **max critique opportunities**：1 - **parameter updates**：0 - **saved student adapter**：True |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：保存student adapter上的单请求direct与一次critique推理协议。（状态：`supported`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **更新由什么过程产生**：修改prompt/重生成图像而非更新参数或训练teacher。（状态：`contradicted`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **状态怎样持久保留**：此推理配置未将当前请求反馈作为跨请求学习状态保留。（状态：`contradicted`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。
- **更新怎样进入后续改进**：当前图像修订不改变未来请求的训练器或教师。（状态：`contradicted`；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570）。

**配置判定**：保留相邻对照；不将单次离线训练或单题推理自动认证为改进器递归升级。

来源：https://arxiv.org/html/2609.38721v1；版本：2609.38721v1；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570。

## 4. 实验、评价协议与结果的可解释范围


- **LoRA alpha**：16
- **LoRA rank**：16
- **acquisition**：one correction opportunity; same noise for revision
- **critic**：fixed Qwen3-VL-8B-Thinking
- **denoising steps**：20
- **deployment direct PI**：False
- **generator**：Qwen-Image-2512
- **iterations**：reported optimizer checkpoint140 for verified GenEval table7; other coverage in supplementary data, not asserted fixed deployment-cycle count
- **learning rate**：0.0003
- **optimizer**：AdamW
- **post revision verification**：True
- **synthesis**：fixed Qwen3-VL-8B-Instruct
- **teacher EMA decay**：0.999
- **training scope**：generator LoRA only
- **transition selected**：6


- **compute**：accepted drafts require no regeneration; same opportunity budget need not mean equal compute
- **evaluation population**：all original benchmark prompts, not filtered by training acceptance
- **max critique opportunities**：1
- **parameter updates**：0
- **saved student adapter**：True

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_f48a08d015fc288df6`**：UniEvo-VL 让同一多模态模型在普通问题与特权自批评上下文下分别作学生和教师，在学生轨迹上匹配去噪分布；摘要另比较外部 critic 并承认文本渲染表现混合，需核教师更新及任务差异。
  - 来源版本：2609.38721v1；定位：Atom entry http://arxiv.org/abs/2609.38721v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5dist_ev_cfg_unievo_vl_verified_ema_training_v1`**：Qwen-Image-2512 student与EMA teacher生成适配器，固定Qwen3-VL critique/synthesis及原prompt后验接受门；只LoRA可学习。 用当前生成器草图得到修订prompt，仅接受在同noise下重生成被固定critic按原请求认可的修订；学生原prompt轨迹的六个最噪状态匹配EMA教师特权prompt转换，AdamW更新LoRA，teacher EMA吸收新LoRA。
  - 来源版本：2609.38721v1；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570；深度：`未单列`。

- **`r5dist_ev_cfg_unievo_vl_one_critique_inference_v1`**：固定保存的student adapter及每请求至多一次critic—prompt修订—重生成过程，训练不在此边界内。 原prompt生成草图；若被接受直接保留，否则一次critic修订后重生成，始终按原请求评分。
  - 来源版本：2609.38721v1；定位：§2.1–2.3 tool L132–238；§3.1 tool L241–247；§3.4.1–3.4.2 tool L303–337；Appendix A.2–A.5 tool L404–459；Appendix D.3–D.4 tool L539–570；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 推理修订与训练收益分列；+1critique不称另一训练周期。
- GenEval direct训练收益与reflection额外收益部分重叠；GenEval HumanPref reflected base仍略高，不能所有指标宣称训练+reflection最优。
- 模型已训练状态来自前置训练，但此配置只认证推理行为，不从前置训练借用core条件。
- 理论叙述使用统一多模态角色，但实际配置仅生成器LoRA更新，Qwen3-VL反馈pipeline固定；不可声称视觉critic共同训练或整个MMM全权重自改。
- EMA0.999在optimizer后刷新，minibatch内固定；不是DCE每步硬同步，更不是全run冻结teacher。
- 训练和推理分开：direct部署只原prompt，+1critique是额外推理计算；基于保存adapter，不在每个评价问题上更新参数。
- post-revision verification为固定critic判断是否满足原prompt，非形式正确性证明；重新生成图仅供过滤，不作图像蒸馏目标或标量训练reward。
- 只单task分别训练适配器；优化更新数非固定总compute。验证通过率约10–21%，每对需约5–10采集尝试，拒绝开销不能忽略。
- 比较有无verification的recipe还改变feedback、seed、学习率/梯度累积，不能从端点差异作verification单因素因果结论。
- 未验证recipe的GenEval2原生Qwen分数32.86→32.37，OCR曲线波动/部分质量下降；不能声称所有任务持续单调提升。
- HumanPref为自动评价proxy非真实人类偏好；Gemini及原生指标为不同单位，不混为同一分数。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5dist_src_unievo` · 已存来源 · 2609.38721v1
  - https://arxiv.org/html/2609.38721v1；阅读深度：`selected_primary_method_parameter_carry_teacher_refresh_and_limits`。
- `s18ctx_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_parameter_carry_teacher_refresh_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f48a08d015fc288df6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
