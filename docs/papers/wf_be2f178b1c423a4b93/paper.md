# PhyCritic: Multimodal Critic Models for Physical AI

> 方法论文 · 2026 · `wf_be2f178b1c423a4b93`

**作者**：Tianyi Xiong, Shihao Wang, Guilin Liu, Yi Dong, Ming Li, Heng Huang, Jan Kautz, Zhiding Yu  
**原文**：https://arxiv.org/abs/2602.11124  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Qwen2.5-VL-7B当前critic在固定物理问题/响应对上先自答再判优，外部答案与preference提供奖励；具体更新过程为：80步QA warmup后300步GRPO；每组当前模型生成自己的预测与critique，分别按固定答案和偏好及格式奖励更新同一模型；更新状态的保留与后继使用为：critic参数跨optimizer步骤保留，更新模型生成后续训练组自答和判优轨迹。

## 2. 论文的核心内容与贡献

### configuration:cfg_phycritic_self_referential_grpo_v1
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2602.11124v1；**原文定位**：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_be2f178b1c423a4b93`
PhyCritic 先作物理技能 RLVR 热身，再让 critic 先生成自身预测作为评价候选的内部参考；self-referential 是评价策略，摘要未证明 critic 与被评策略持续互相升级。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### PhyCritic: bounded on-policy self-referential critic training
`cfg_phycritic_self_referential_grpo_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Qwen2.5-VL-7B当前critic在固定物理问题/响应对上先自答再判优，外部答案与preference提供奖励。 |
| 改进过程与下一轮参与 | 80步QA warmup后300步GRPO；每组当前模型生成自己的预测与critique，分别按固定答案和偏好及格式奖励更新同一模型。 |
| 保留的状态及时间尺度 | critic参数跨optimizer步骤保留，更新模型生成后续训练组自答和判优轨迹。 |
| 外部固定部分 | - 训练问题及候选响应对 - ground-truth答案与GPT-4o辅助标注偏好 - GRPO/固定奖励权重与格式 - 固定优化超参数 |
| 评价与选择设置 | - **KL coefficient**：0.01 - **PhyCritic Bench items**：225 - **QA warmup steps**：80 - **batch size**：128 - **critic steps**：300 - **critic training pairs**：3258 - **learning rate**：1e-06 - **model**：Qwen2.5-VL-7B-Instruct |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：critic生成、judge训练和参数边界明确。（状态：`supported`；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214）。
- **更新由什么过程产生**：自己的预测/判断轨迹经外部奖励更新critic参数。（状态：`supported`；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214）。
- **状态怎样持久保留**：参数保留跨训练组。（状态：`supported`；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214）。
- **更新怎样进入后续改进**：GRPO公式从当前pi_theta采样，更新critic改变下一组内自参照训练轨迹。（状态：`supported`；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2602.11124v1；版本：2602.11124v1；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214。

## 4. 实验、评价协议与结果的可解释范围


- **KL coefficient**：0.01
- **PhyCritic Bench items**：225
- **QA warmup steps**：80
- **batch size**：128
- **critic steps**：300
- **critic training pairs**：3258
- **learning rate**：1e-06
- **model**：Qwen2.5-VL-7B-Instruct

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_be2f178b1c423a4b93`**：PhyCritic 先作物理技能 RLVR 热身，再让 critic 先生成自身预测作为评价候选的内部参考；self-referential 是评价策略，摘要未证明 critic 与被评策略持续互相升级。
  - 来源版本：2602.11124v1；定位：Atom entry http://arxiv.org/abs/2602.11124v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_phycritic_self_referential_grpo_v1`**：Qwen2.5-VL-7B当前critic在固定物理问题/响应对上先自答再判优，外部答案与preference提供奖励。 80步QA warmup后300步GRPO；每组当前模型生成自己的预测与critique，分别按固定答案和偏好及格式奖励更新同一模型。
  - 来源版本：2602.11124v1；定位：§3.1–3.3 tool L107–182；§3.4–§5 tool L183–214；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- core只指有界on-policy critic训练回流，不代表critic用于迭代训练另一policy或部署期持续自改；单次先自答再判优本身也不足以证明跨轮自改。
- 候选响应来自七个外部模型，偏好由有答案的GPT-4o核验构造；不是完全自生成ground truth或无外部监督。
- 训练和benchmark共享物理数据来源不等于已证明实例泄漏；本次未独立核对视频/问题去重及训练seed稳健性。
- paper另有推理选择/修订用途，本配置不将它们扩大为新的持续学习闭环。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_phycritic` · 已存来源 · 2602.11124v1
  - https://arxiv.org/html/2602.11124v1；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_216ceac5be60574c` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2602.08603%2C2602.08847%2C2602.09082%2C2602.09163%2C2602.09447%2C2602.09540%2C2602.09856%2C2602.09892%2C2602.10006%2C2602.10090%2C2602.10177%2C2602.10233%2C2602.10356%2C2602.10498%2C2602.10604%2C2602.10652%2C2602.10975%2C2602.10999%2C2602.11103%2C2602.11124%2C2602.11243%2C2602.11304%2C2602.11524%2C2602.11731%2C2602.11748%2C2602.11964%2C2602.11988%2C2602.12063%2C2602.12083%2C2602.12311%2C2602.12430%2C2602.12561%2C2602.12574%2C2602.12670%2C2602.12779%2C2602.12984%2C2602.13213%2C2602.13218%2C2602.13559%2C2602.13576%2C2602.13680%2C2602.13933%2C2602.14211%2C2602.14457%2C2602.14690%2C2602.14697%2C2602.14721%2C2602.14878%2C2602.15112%2C2602.15257%2C2602.15259%2C2602.15378%2C2602.15384%2C2602.15902%2C2602.15922%2C2602.16065%2C2602.16069%2C2602.16173%2C2602.16313%2C2602.16493%2C2602.16662%2C2602.16819%2C2602.16855%2C2602.16873%2C2602.16891%2C2602.16928%2C2602.16932%2C2602.17037%2C2602.17497%2C2602.17829%2C2602.17902%2C2602.18571%2C2602.18920%2C2602.19000%2C2602.19008%2C2602.19041%2C2602.19169%2C2602.19320%2C2602.19505%2C2602.19715%2C2602.19848%2C2602.20064%2C2602.20133%2C2602.20156%2C2602.20229%2C2602.20323%2C2602.20532%2C2602.20543%2C2602.20867%2C2602.20934%2C2602.21193%2C2602.21198%2C2602.21221%2C2602.21251%2C2602.21477%2C2602.21611%2C2602.21843%2C2602.22124%2C2602.22406%2C2602.22425&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_be2f178b1c423a4b93 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
