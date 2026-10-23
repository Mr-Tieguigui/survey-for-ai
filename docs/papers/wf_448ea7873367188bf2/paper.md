# SBCO: Self-Supervised, Verifier-Grounded Harness Optimization For Planning Agents

> 方法论文 · 2026 · `wf_448ea7873367188bf2`

**作者**：Vivek Kulkarni, Sudipta Paul, Aounon Kumar, Nicholas Tzou, Srinivas Chappidi  
**原文**：https://arxiv.org/abs/2608.10157  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：task agent与可优化harness(P,V,Pi)及critic/strategist闭环；tools T冻结；learned constraint verifiers V可写，black-box benchmark reward与block optimizer M固定；具体更新过程为：textual gradients交替优化verifier signature/body、prompt和policy code；precision/recall floors准入V，keep-best保留block；downstream policy mismatch可上报重开upstream verifier；更新状态的保留与后继使用为：verifier bank、best prompt/policy及prior strategies/failures跨block/epoch保留，影响后继policy repair、strategic pivot及verifier再优化。

## 2. 论文的核心内容与贡献

### configuration:cfg_sbco_verifier_prompt_policy_block_feedback_v1
四条件支持固定optimizer下verifier/prompt/policy artifacts的有限反馈core；作者明确拒绝recursive/self-referential标签，该标签分歧单独保留。

**适用版本**：2608.10157v1；**原文定位**：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### SBCO v1 verifier/prompt/policy block feedback under fixed optimizer
`cfg_sbco_verifier_prompt_policy_block_feedback_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | task agent与可优化harness(P,V,Pi)及critic/strategist闭环；tools T冻结；learned constraint verifiers V可写，black-box benchmark reward与block optimizer M固定。 |
| 改进过程与下一轮参与 | textual gradients交替优化verifier signature/body、prompt和policy code；precision/recall floors准入V，keep-best保留block；downstream policy mismatch可上报重开upstream verifier。 |
| 保留的状态及时间尺度 | verifier bank、best prompt/policy及prior strategies/failures跨block/epoch保留，影响后继policy repair、strategic pivot及verifier再优化。 |
| 外部固定部分 | - GPT-5.4-mini task agent与GPT-5.4-medium critic/strategist角色 - frozen tools和固定optimizer M、benchmark reward - precision .80/recall .55 reliability floors |
| 评价与选择设置 | - **epochs**：3 - **evaluation**：same full training+validation task set; separate train/validation and cross-backbone transfer analyses - **max pivots**：2 - **reported policy runs**：2 - **tactical iterations**：5 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.1明确P,T,W和V/Pi可写边界。（状态：`supported`；定位：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218）。
- **更新由什么过程产生**：critic/strategist由模型自己的输出/reward提textual改动。（状态：`supported`；定位：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218）。
- **状态怎样持久保留**：bank及keep-best artifacts和历史失败跨iteration保留。（状态：`supported`；定位：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218）。
- **更新怎样进入后续改进**：policy读取learned V，mismatch可重开上游V，critic读取prior strategy failures再提出后继策略。（状态：`supported`；定位：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218）。

**配置判定**：四条件支持固定optimizer下verifier/prompt/policy artifacts的有限反馈core；作者明确拒绝recursive/self-referential标签，该标签分歧单独保留。

来源：https://arxiv.org/html/2608.10157v1；版本：2608.10157v1；定位：§3.1–3.4 writable verifiers and downstream escalation tool L98–120；Algorithm 2 keep-best and strategic history tool L150–192；§4 evaluation selection reuse tool L213–218。

## 4. 实验、评价协议与结果的可解释范围


- **epochs**：3
- **evaluation**：same full training+validation task set; separate train/validation and cross-backbone transfer analyses
- **max pivots**：2
- **reported policy runs**：2
- **tactical iterations**：5

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_sbco_verifier_prompt_policy_block_feedback_v1`**：四条件支持固定optimizer下verifier/prompt/policy artifacts的有限反馈core；作者明确拒绝recursive/self-referential标签，该标签分歧单独保留。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 作者§3.4明确称self-supervised但not recursive/self-referential；此处只按项目四条件承认ordinary bounded artifact feedback，保留原立场。
- reported full task set包含training+validation；不是独立held-out test，两个policy runs不能消除selection reuse。
- learned V的F1 surrogate与task reward不同；V可写不表示最终benchmark evaluator可写，optimizer本身固定。
- 作者§3.4明确称self-supervised但not recursive/self-referential；此处只按项目四条件承认ordinary bounded artifact feedback，保留原立场。; reported full task set包含training+validation；不是独立held-out test，两个policy runs不能消除selection reuse。; learned V的F1 surrogate与task reward不同；V可写不表示最终benchmark evaluator可写，optimizer本身固定。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_sbco` · SBCO: Self-Supervised, Verifier-Grounded Harness Optimization For Planning Agents · 2608.10157v1
  - https://arxiv.org/html/2608.10157v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_448ea7873367188bf2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
