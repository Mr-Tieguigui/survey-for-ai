# Recursive Self-Improvement via On-Policy Distillation for Reasoning

> 方法论文 · 2026 · `wf_9e52af299c264dd718`

**作者**：Shangjian Yin, Zehao Zhao, Kavosh Asadi, Rui Liu, Yuchen Lu, Shike Mei, Hang Cui, Luke Simon, Zhouxing Shi, Hamed Firooz  
**原文**：https://arxiv.org/abs/2609.30652  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
DCE 使获得真值特权上下文的教师随学生跨轮共同演化，SRCL 另对已验证的精简重写训练；需区分动态教师、冻结教师 OPSD 对照和额外目标，不能只据摘要归因全部收益给递归。

## 2. 论文的核心内容与贡献

### configuration:cfg_dce_srcl_dynamic_privileged_teacher_v1
在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

**适用版本**：2609.30652v1；**原文定位**：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_opsd_tts_wait_inference_control_v1
保留相邻对照；不将单次离线训练或单题推理自动认证为改进器递归升级。

**适用版本**：2609.30652v1；**原文定位**：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18ctx_role_review_wf_9e52af299c264dd718`
DCE 使获得真值特权上下文的教师随学生跨轮共同演化，SRCL 另对已验证的精简重写训练；需区分动态教师、冻结教师 OPSD 对照和额外目标，不能只据摘要归因全部收益给递归。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### DCE + SRCL: every-step privileged-teacher refresh
`cfg_dce_srcl_dynamic_privileged_teacher_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 持久参数的数学推理student、同checkpoint的gold-conditioned detached teacher及无gold refiner；训练规则和答案验证器外置。 |
| 改进过程与下一轮参与 | 当前student产生on-policy响应；gold-conditioned教师前向KL监督，student同checkpoint无gold重写，较短/自然终止/结构及答案正确重写作SRCL目标；joint更新后两分支与refiner均继承新参数。 |
| 保留的状态及时间尺度 | LoRA/模型参数逐optimizer step连续继承，teacher每step同步；没有周期重置回初始基模。 |
| 外部固定部分 | - 14,717 OpenThoughts问题及gold - AdamW/前向KL/SRCL接受规则 - 基础模型未被代码自改的训练实现 |
| 评价与选择设置 | - **LoRA rank**：128 - **SRCL**：greedy12K rewrite without gold; gold only acceptance - **batch**：16 - **deployment PI**：False - **evaluation**：AIME24/25/26 and HMMT25 each30 questions;12 samples each,32K cap - **learning rate**：5e-06 - **max optimizer steps**：200 - **mode**：non-thinking - **optimizer**：AdamW - **primary models**：- Qwen3-1.7B - Qwen3-4B - Qwen3-8B - Qwen3-14B - **reference**：first512 reference tokens in privileged assistant-side context - **rollout**：one 12K maximum on-policy response each example - **teacher schedule**：copy current student every optimizer step; stopgrad target |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：当前模型student/gold-conditioned teacher/refiner作为训练系统，外部gold与optimizer固定。（状态：`supported`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **更新由什么过程产生**：当前模型生成on-policy回应和精简自重写，由其privileged分支产生监督后更新参数。（状态：`supported`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **状态怎样持久保留**：theta_k更新为theta_k+1并在后续训练与部署保留，非单题文本修订。（状态：`supported`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **更新怎样进入后续改进**：theta_k+1立即用作下一轮student、privileged teacher与重写者，已学修订回流未来监督。（状态：`supported`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。

**配置判定**：在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

来源：https://arxiv.org/html/2609.30652v1；版本：2609.30652v1；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779。

### OPSD-TTS: fixed-parameter Wait continuation control
`cfg_opsd_tts_wait_inference_control_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 已训练OPSD固定checkpoint上的单题预算强制续写；不包括生成该checkpoint的训练过程。 |
| 改进过程与下一轮参与 | 回应早终止时注入Wait直至精确8K或16K输出预算，以检验仅增加推理token能否解释训练效果。 |
| 保留的状态及时间尺度 | 仅保留当前题文本到预算结束；论文明确该对照不修改模型参数。 |
| 外部固定部分 | - 固定OPSD权重 - Wait及8K/16K预算 - 问题与评价器 |
| 评价与选择设置 | - **PI at inference**：False - **evaluation**：same four math benchmarks, Average@12 - **forced budgets**：- 8192 - 16384 - **model scales**：- Qwen3-1.7B - Qwen3-4B - Qwen3-8B - **parameter updates**：0 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：冻结OPSD checkpoint及单题Wait续写界限明确。（状态：`supported`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **更新由什么过程产生**：OPSD-TTS仅续写文本，不改模型参数、教师或更新规则。（状态：`contradicted`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **状态怎样持久保留**：在此inference-only配置内未保留跨问题学习状态。（状态：`contradicted`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。
- **更新怎样进入后续改进**：本题续写不变成后续训练监督或改进器。（状态：`contradicted`；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779）。

**配置判定**：保留相邻对照；不将单次离线训练或单题推理自动认证为改进器递归升级。

来源：https://arxiv.org/html/2609.30652v1；版本：2609.30652v1；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779。

## 4. 实验、评价协议与结果的可解释范围


- **LoRA rank**：128
- **SRCL**：greedy12K rewrite without gold; gold only acceptance
- **batch**：16
- **deployment PI**：False
- **evaluation**：AIME24/25/26 and HMMT25 each30 questions;12 samples each,32K cap
- **learning rate**：5e-06
- **max optimizer steps**：200
- **mode**：non-thinking
- **optimizer**：AdamW
- **primary models**：- Qwen3-1.7B - Qwen3-4B - Qwen3-8B - Qwen3-14B
- **reference**：first512 reference tokens in privileged assistant-side context
- **rollout**：one 12K maximum on-policy response each example
- **teacher schedule**：copy current student every optimizer step; stopgrad target


- **PI at inference**：False
- **evaluation**：same four math benchmarks, Average@12
- **forced budgets**：- 8192 - 16384
- **model scales**：- Qwen3-1.7B - Qwen3-4B - Qwen3-8B
- **parameter updates**：0

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_9e52af299c264dd718`**：DCE 使获得真值特权上下文的教师随学生跨轮共同演化，SRCL 另对已验证的精简重写训练；需区分动态教师、冻结教师 OPSD 对照和额外目标，不能只据摘要归因全部收益给递归。
  - 来源版本：2609.30652v1；定位：Atom entry http://arxiv.org/abs/2609.30652v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5dist_ev_cfg_dce_srcl_dynamic_privileged_teacher_v1`**：持久参数的数学推理student、同checkpoint的gold-conditioned detached teacher及无gold refiner；训练规则和答案验证器外置。 当前student产生on-policy响应；gold-conditioned教师前向KL监督，student同checkpoint无gold重写，较短/自然终止/结构及答案正确重写作SRCL目标；joint更新后两分支与refiner均继承新参数。
  - 来源版本：2609.30652v1；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779；深度：`未单列`。

- **`r5dist_ev_cfg_opsd_tts_wait_inference_control_v1`**：已训练OPSD固定checkpoint上的单题预算强制续写；不包括生成该checkpoint的训练过程。 回应早终止时注入Wait直至精确8K或16K输出预算，以检验仅增加推理token能否解释训练效果。
  - 来源版本：2609.30652v1；定位：§3.1–3.3 tool L127–209；§4.1–4.3 tool L212–224；§5.6 tool L330–336；Appendix D tool L520–564；Appendix J tool L687–708；Appendix M tool L748–779；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 训练轮k对应minibatch/optimizer step，最多200步；不等于200次完整数据集代际训练或部署重启。
- teacher是当前checkpoint在gold上下文的stop-gradient分支，每step刷新；无独立teacher优化器，AdamW和前向KL规则固定。
- gold在教师上下文提供特权信息；学生rollout及SRCL重写不见gold，但SRCL接受与答案验证依赖gold，非无外部监督。
- 同一训练问题构造两上下文而非新增两套问题；14,717训练问题；未独立审查数据泄漏或模型预训练污染。
- SRCL与teacher refresh及gold放置均可影响效果；不能把joint相对OPSD增益全部归因递归性，ablation按实际同条件范围读。
- Appendix D每teacher schedule一条训练轨迹；小差异不可当跨seed稳健提升，列出的checkpoint步数有差异。
- 广域额外benchmark中准确率改善常伴更长输出，不是所有任务都更简短；无无界或单调增益认证。
- 推理token预算控制非训练消融；强制长生成未再现DCE收益，不等于任意test-time scaling无效。
- 8K与16K只在本文OPSD checkpoint、数据与Wait干预上比较；不能外推搜索/多采样策略。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r5dist_src_dce` · 已存来源 · 2609.30652v1
  - https://arxiv.org/html/2609.30652v1；阅读深度：`selected_primary_method_parameter_carry_teacher_refresh_and_limits`。
- `s18ctx_role_src_cf0403161b25df87` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22self-improving%22+AND+%28all%3Aagent+OR+all%3Alanguage%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_parameter_carry_teacher_refresh_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_9e52af299c264dd718 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
