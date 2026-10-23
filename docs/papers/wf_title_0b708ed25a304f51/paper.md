# Can large language models invent algorithms to improve themselves?: algorithm discovery for recursive self-improvement through reinforcement learning

> 方法论文 · 2025 · `wf_title_0b708ed25a304f51`

**作者**：Y. Ishibashi, T. Yano, and M. Oyamada  
**原文**：https://doi.org/10.18653/v1/2025.naacl-long.519  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：Can Large Language Models Invent Algorithms to Improve Themselves?。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：algorithm-factory policy pi_g、Python merge算法、固定seed M0/三candidate task vectors、dev evaluator与DPO训练；具体更新过程为：factory生成merge code，过滤不可执行/timeout；算法对task vectors执行并加回M0；dev分数构good/bad code偏好对，DPO续训当前factory，下轮用更新factory生成；更新状态的保留与后继使用为：factory权重跨3轮续传；每轮合并始终从相同M0构造，不把merged模型作为后继factory。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_developing_dpo_algorithm_factory_acl_v2
DPO改进后的algorithm-factory保留参与下一轮自身算法生成，四结构条件在有限model-merging搜索/训练系统成立；被merge对象始终M0，不是逐轮merged-model自举。

**适用版本**：ACL Anthology2025.naacl-long.519v2；**原文定位**：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Self-Developing ACL v2: DPO-updated merge-algorithm factory
`cfg_self_developing_dpo_algorithm_factory_acl_v2` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | algorithm-factory policy pi_g、Python merge算法、固定seed M0/三candidate task vectors、dev evaluator与DPO训练。 |
| 改进过程与下一轮参与 | factory生成merge code，过滤不可执行/timeout；算法对task vectors执行并加回M0；dev分数构good/bad code偏好对，DPO续训当前factory，下轮用更新factory生成。 |
| 保留的状态及时间尺度 | factory权重跨3轮续传；每轮合并始终从相同M0构造，不把merged模型作为后继factory。 |
| 外部固定部分 | - M0和merge candidates - one-shot code prompt与dev scoring - DPO算法/temperature schedule |
| 评价与选择设置 | - **algorithms per iteration**：3000 - **iterations**：3 - **merges**：three Mistral7B-based fine-tunes - **prompt**：fixed across iterations - **seed**：openchat-3.5-1210 - **test**：top15 dev-selected models, final remaining test |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2明确factory、merge模型和评价边界。（状态：`supported`；定位：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103）。
- **更新由什么过程产生**：factory自己生成代码，其执行结果构成DPO数据。（状态：`supported`；定位：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103）。
- **状态怎样持久保留**：§2.4明示pi_g_t经DPO成pi_g_t+1。（状态：`supported`；定位：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103）。
- **更新怎样进入后续改进**：下轮明确用pi_g_t+1生成改进代码，改变后继训练数据来源。（状态：`supported`；定位：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103）。

**配置判定**：DPO改进后的algorithm-factory保留参与下一轮自身算法生成，四结构条件在有限model-merging搜索/训练系统成立；被merge对象始终M0，不是逐轮merged-model自举。

来源：https://aclanthology.org/2025.naacl-long.519v2.pdf；版本：ACL Anthology2025.naacl-long.519v2；定位：PDF physical pp2–4 §§2.1–2.4 tool L154–368；PDF physical pp4–5 §3.1 tool L372–424；PDF physical p10 Limitations tool L780–798；Original v1/Version2 and official PDF links tool L61–103。

## 4. 实验、评价协议与结果的可解释范围


- **algorithms per iteration**：3000
- **iterations**：3
- **merges**：three Mistral7B-based fine-tunes
- **prompt**：fixed across iterations
- **seed**：openchat-3.5-1210
- **test**：top15 dev-selected models, final remaining test

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r10_ev_cfg_self_developing_dpo_algorithm_factory_acl_v2`**：DPO改进后的algorithm-factory保留参与下一轮自身算法生成，四结构条件在有限model-merging搜索/训练系统成立；被merge对象始终M0，不是逐轮merged-model自举。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 明确采用官方ACL v2 PDF，不把v2内容无痕归给v1。
- GSM8k/MATH从原test划出dev，搜索只读dev；余下测试最终top15模型一次评估。
- 3轮各3000算法和数学任务不证明无界增长、通用新算法发现或计算调整后持续收益。
- 不依赖更强外部LLM生成算法，但仍使用外部预训练merge候选、真实答案evaluator和固定训练规则。
- - 明确采用官方ACL v2 PDF，不把v2内容无痕归给v1。 - GSM8k/MATH从原test划出dev，搜索只读dev；余下测试最终top15模型一次评估。 - 3轮各3000算法和数学任务不证明无界增长、通用新算法发现或计算调整后持续收益。 - 不依赖更强外部LLM生成算法，但仍使用外部预训练merge候选、真实答案evaluator和固定训练规则。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r10_src_selfdeveloping_v2` · Can Large Language Models Invent Algorithms to Improve Themselves? · ACL Anthology2025.naacl-long.519v2
  - https://aclanthology.org/2025.naacl-long.519v2.pdf；阅读深度：`未单列`。
- `r10_src_selfdeveloping_version` · ACL Anthology bibliographic/version record · official version listing observed2026-10-19
  - https://aclanthology.org/2025.naacl-long.519/；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_0b708ed25a304f51 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
