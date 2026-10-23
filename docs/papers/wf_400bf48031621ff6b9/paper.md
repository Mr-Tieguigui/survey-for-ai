# Stabilizing Unsupervised Self-Evolution of MLLMs via Continuous Softened Retracing reSampling

> 方法论文 · 2026 · `wf_400bf48031621ff6b9`

**作者**：Yunyao Yu, Zhengxian Wu, Zhuohong Chen, Hangrui Xu, Zirui Liao, Xiangwen Deng, Zhifang Liu, Senyuan Shi, Haoqian Wang  
**原文**：https://arxiv.org/abs/2604.03647  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
CSRS 以锚点回溯重推理、按频率软化奖励及视觉语义扰动稳定 MLLM 无监督自演化；多数频率不等于客观真值，需全文核训练循环、奖励器固定与筛选过程。

## 2. 论文的核心内容与贡献

### configuration:cfg_csrs_online_soft_frequency_grpo_v2
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2604.03647v2；**原文定位**：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18ctx_role_review_wf_400bf48031621ff6b9`
CSRS 以锚点回溯重推理、按频率软化奖励及视觉语义扰动稳定 MLLM 无监督自演化；多数频率不等于客观真值，需全文核训练循环、奖励器固定与筛选过程。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### CSRS: online self-frequency reward with retracing
`cfg_csrs_online_soft_frequency_grpo_v2` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前MLLM生成母轨迹、固定位置截断重采样与扰动图像、软频率奖励、持续GRPO参数更新。 |
| 改进过程与下一轮参与 | 每minibatch用当前policy生成n母轨迹及每条m次retrace子轨迹；答案全体频率和子集变化构造固定tanh软奖励；GRPO更新模型并进入后续batch。 |
| 保留的状态及时间尺度 | 模型参数及optimizer跨minibatch保留，后续分布反馈奖励；不是仅同题推理扩样。 |
| 外部固定部分 | - GRPO/AdamW与奖励公式 - retracing rate/视觉扰动规则 - 无标签prompt-image训练集 - KL参照及超参规则 |
| 评价与选择设置 | - **KL coefficient**：0.01 - **epochs**：15 - **learning rate**：1e-06 - **optimizer**：AdamW - **task scope**：multimodal mathematical reasoning - **training sets**：- Geometry3K - GeoQA - MMR1 - **weight decay**：0.01 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：生成/奖励统计/训练边界明确。（状态：`supported`；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247）。
- **更新由什么过程产生**：自己的回答频率及重采一致性成为参数更新信号。（状态：`supported`；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247）。
- **状态怎样持久保留**：参数跨训练batch和15epoch保留。（状态：`supported`；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247）。
- **更新怎样进入后续改进**：Alg1每batch从当前theta重新采样，更新分布改变随后自奖励和训练轨迹。（状态：`supported`；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2604.03647v2；版本：2604.03647v2；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247。

## 4. 实验、评价协议与结果的可解释范围


- **KL coefficient**：0.01
- **epochs**：15
- **learning rate**：1e-06
- **optimizer**：AdamW
- **task scope**：multimodal mathematical reasoning
- **training sets**：- Geometry3K - GeoQA - MMR1
- **weight decay**：0.01

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_400bf48031621ff6b9`**：CSRS 以锚点回溯重推理、按频率软化奖励及视觉语义扰动稳定 MLLM 无监督自演化；多数频率不等于客观真值，需全文核训练循环、奖励器固定与筛选过程。
  - 来源版本：2604.03647v2；定位：Atom entry http://arxiv.org/abs/2604.03647v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_csrs_online_soft_frequency_grpo_v2`**：当前MLLM生成母轨迹、固定位置截断重采样与扰动图像、软频率奖励、持续GRPO参数更新。 每minibatch用当前policy生成n母轨迹及每条m次retrace子轨迹；答案全体频率和子集变化构造固定tanh软奖励；GRPO更新模型并进入后续batch。
  - 来源版本：2604.03647v2；定位：§3.1 Algorithm 1 tool L80–142；§3.2 tool L149–165, L200–208；§4.1 tool L218–221；Limitations tool L242–247；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 频率/局部一致性是proxy，不是真值；Gaussian扰动不会证明消除视觉shortcut或所有推理错误。
- 理论软奖励放缓polarization依赖理想更新及0<rho-epsilon<1等假设，非任意训练无collapse保证。
- 所谓critical pivot实际按omega长度位置截断，不是已学到语义关键步骤定位器。
- 不同答案频率公式/符号的实现与完整超参本次未复现；不能把采样分支round称独立参数代际或部署闭环。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_csrs` · 已存来源 · 2604.03647v2
  - https://arxiv.org/html/2604.03647v2；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18ctx_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_400bf48031621ff6b9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
