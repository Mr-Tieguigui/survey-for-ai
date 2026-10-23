# Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation

> 方法论文 · 2026 · `wf_7bde67cea428626c0d`

**作者**：Haozhe Wang, Weijia Feng, Jinpeng Yu, Che Liu, Ping Nie, Fangzhen Lin, Jiaming Liu, Ruihua Huang, Jimmy Lin, Wenhu Chen, Cong Wei  
**原文**：https://arxiv.org/abs/2607.05382  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
SearchGen 同时提供知识长尾视觉生成数据及 benchmark，并用 teach-then-search 协同训练寻找生成器知识边界；摘要将其称递归改进基础，实际生成器和检索策略更新链仍需正文核实。

## 2. 论文的核心内容与贡献

### configuration:cfg_search_beyond_online_generator_dpo_v4
仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

**适用版本**：2607.05382v4；**原文定位**：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_search_beyond_single_fixed_rft_v4
按原文保留有界相邻或待定配置，不从训练或验证名称推断递归闭合。

**适用版本**：2607.05382v4；**原文定位**：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_7bde67cea428626c0d`
SearchGen 同时提供知识长尾视觉生成数据及 benchmark，并用 teach-then-search 协同训练寻找生成器知识边界；摘要将其称递归改进基础，实际生成器和检索策略更新链仍需正文核实。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Search Beyond: online generator DPO then reasoner recalibration
`cfg_search_beyond_online_generator_dpo_v4` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定search reasoner和VLM judge辅助当前视觉生成器LoRA的在线DPO训练；随后一次reasoner RFT是分阶段扩展。 |
| 改进过程与下一轮参与 | 每episode当前generator采样图像，外部judge选best/worst偏好更新generator，EMA参考随训练更新；后续episode由新generator产生成对训练样本。 |
| 保留的状态及时间尺度 | generator参数与EMA参考跨episode保留；不是部署时一次查询产生的新答案。 |
| 外部固定部分 | - VLM judge与SearchGen评分规则 - Phase0 reasoner及检索接口 - DPO/AdamW规则及超参 |
| 评价与选择设置 | - **DPO beta**：100 - **EMA decay**：0.99 - **EMA interval steps**：4 - **actual phase schedule**：one DPO pass then one RFT pass; no repeated alternation - **candidates per prompt**：5 - **documented Flux LoRA alpha**：128 - **documented Flux LoRA rank**：64 - **open generator examples**：- Flux.2-Klein-4B - Bagel-7B |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：当前generator与偏好更新边界明确。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **更新由什么过程产生**：自己的新生成图像产生下一次偏好训练信号。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **状态怎样持久保留**：generator LoRA和EMA跨episode保留。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **更新怎样进入后续改进**：Alg1在线episode从当前Gtheta采样，参数更新改变后续训练候选和偏好。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。

**配置判定**：仅在已声明状态和回流边界支持四条件；不认证优化器自改、加速或部署自主性。

来源：https://arxiv.org/html/2607.05382v4；版本：2607.05382v4；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652。

### Search Beyond: one fixed rejection-finetuning reasoner pass
`cfg_search_beyond_single_fixed_rft_v4` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 强化generator固定，Phase0 reasoner一次rollout构造筛选数据，再训练reasoner。 |
| 改进过程与下一轮参与 | 用group-relative positive advantage筛Phase0搜索轨迹后SFT；没有把R_phi_prime再投入相同RFT采样。 |
| 保留的状态及时间尺度 | reasoner训练参数保留供推理；此view没有后续reasoner反馈训练。 |
| 外部固定部分 | - 固定强化generator - 一次Phase0 rollout数据 - 固定filter和SFT |
| 评价与选择设置 | - **RFT passes**：1 - **generator during RFT**：G_theta_prime fixed - **rollout reasoner**：R_phi0 before Phase2 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：单次RFT边界明确。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **更新由什么过程产生**：自身Phase0轨迹选择形成训练数据。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **状态怎样持久保留**：参数保存供部署。（状态：`supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。
- **更新怎样进入后续改进**：更新reasoner未在算法中再采样改善数据；多轮交替明确留未来。（状态：`not_supported`；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652）。

**配置判定**：按原文保留有界相邻或待定配置，不从训练或验证名称推断递归闭合。

来源：https://arxiv.org/html/2607.05382v4；版本：2607.05382v4；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652。

## 4. 实验、评价协议与结果的可解释范围


- **DPO beta**：100
- **EMA decay**：0.99
- **EMA interval steps**：4
- **actual phase schedule**：one DPO pass then one RFT pass; no repeated alternation
- **candidates per prompt**：5
- **documented Flux LoRA alpha**：128
- **documented Flux LoRA rank**：64
- **open generator examples**：- Flux.2-Klein-4B - Bagel-7B


- **RFT passes**：1
- **generator during RFT**：G_theta_prime fixed
- **rollout reasoner**：R_phi0 before Phase2

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_7bde67cea428626c0d`**：SearchGen 同时提供知识长尾视觉生成数据及 benchmark，并用 teach-then-search 协同训练寻找生成器知识边界；摘要将其称递归改进基础，实际生成器和检索策略更新链仍需正文核实。
  - 来源版本：2607.05382v4；定位：Atom entry http://arxiv.org/abs/2607.05382v4；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6app_ev_cfg_search_beyond_online_generator_dpo_v4`**：固定search reasoner和VLM judge辅助当前视觉生成器LoRA的在线DPO训练；随后一次reasoner RFT是分阶段扩展。 每episode当前generator采样图像，外部judge选best/worst偏好更新generator，EMA参考随训练更新；后续episode由新generator产生成对训练样本。
  - 来源版本：2607.05382v4；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652；深度：`未单列`。

- **`r6app_ev_cfg_search_beyond_single_fixed_rft_v4`**：强化generator固定，Phase0 reasoner一次rollout构造筛选数据，再训练reasoner。 用group-relative positive advantage筛Phase0搜索轨迹后SFT；没有把R_phi_prime再投入相同RFT采样。
  - 来源版本：2607.05382v4；定位：§3.3 Algorithm 1 tool L235–306；Appendix E tool L559–628；Appendix F tool L642–652；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Appendix F明确只一遍DPO后一遍RFT，多轮共训练是未来工作；core支持DPO内部feedback，不把Phase1/2当多代循环。
- Phase2所有trajectory来自Phase0 R_phi0，过滤后一次SFT，未显示更新reasoner再生成下一轮训练轨迹。
- 正文Phase0约10K与Alg1/Appendix E约20K warmstart计数不一致，保留待澄清；不选一数掩平。
- 训练judge Appendix E为Qwen3-VL-8B；评估局限提Gemini-3-Flash，两者不可混为同一judge。
- 搜索可伤害部分prompt；一次protocol的stratum改善不证明无界单调收益。
- 不因总系统在线DPO为core就把每个离线view都视为闭环；也不否认generator内部循环。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r6app_src_search` · 已存来源 · 2607.05382v4
  - https://arxiv.org/html/2607.05382v4；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_7edd05d3174e0b70` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28%28ti%3Aevolving+OR+ti%3A%22self-improvement%22+OR+ti%3A%22self-evolution%22%29+AND+%28all%3Arobot+OR+all%3Aembodied+OR+all%3Amultimodal%29%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7bde67cea428626c0d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
