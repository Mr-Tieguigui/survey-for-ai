# MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data

> 方法论文 · 2024 · `wf_a1e3d945218923b1bb`

**作者**：Yinya Huang, Xiaohan Lin, Zhengying Liu, Qingxing Cao, Huajian Xin, Haiming Wang, Zhenguo Li, Linqi Song, Xiaodan Liang  
**原文**：https://arxiv.org/abs/2402.08957  
**研究分支**：验证、批评与信用分配  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
MUSTARD生成数学题及形式证明并用Lean筛选，MUSTARDSAUCE作为数据集训练较小模型；摘要未说明更新后小模型反复生成后续训练数据。

## 2. 论文的核心内容与贡献

### configuration:cfg_mustard_lean3_generation_filter_train_v3
相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

**适用版本**：v3；**原文定位**：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185；§4.3 tool L202–212。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_a1e3d945218923b1bb`
MUSTARD生成数学题及形式证明并用Lean筛选，MUSTARDSAUCE作为数据集训练较小模型；摘要未说明更新后小模型反复生成后续训练数据。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### MUSTARD fixed generator + Lean3 filtering + downstream fine-tuning
`cfg_mustard_lean3_generation_filter_train_v3` · verified_data_generation_pipeline

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | GPT4固定生成器、概念池与Lean3 proof-error修复/过滤、数据集及较小学生fine-tuning；无学生回写生成器链。 |
| 改进过程与下一轮参与 | 采1–2数学概念生成自然命题/解答及Lean3证明，失败以error message重试，过prover则入数据集，再LoRA训练下游学生。 |
| 保留的状态及时间尺度 | 验证数据集跨样本保留供训练；证明修复只在本题上下文，未证明训练学生重生后续Mustard数据。 |
| 外部固定部分 | - 概念池及采样规则 - GPT4基础模型 - Lean3 verifier - 学生LoRA训练协议 |
| 评价与选择设置 | - **generator**：GPT4 - **students**：- GPT2-large - Llama2-7B - Llama2-70B - **training**：LoRA - **valid points**：5866 - **valid split**：- 4866 - 500 - 500 - **verifier**：Lean3 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3描述生成器/验证器/下游学生（状态：`supported`；定位：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185）。
- **更新由什么过程产生**：本题error修复但固定生成器未学习（状态：`partial`；定位：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185）。
- **状态怎样持久保留**：数据集持久供下游训练（状态：`supported`；定位：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185）。
- **更新怎样进入后续改进**：§4.3只显示小模型fine-tune，无更新学生回到生成器的后续回流（状态：`contradicted`；定位：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185）。

**配置判定**：相邻数据构建/外部安全协议配置；不把产物修订、基准难度增加或外部guard认证成学习改进器自改。

来源：https://arxiv.org/html/2402.08957v3；版本：v3；定位：§3.1–3.3 tool L100–134；§4.2 human inspection tool L174–185；§4.3 tool L202–212。

## 4. 实验、评价协议与结果的可解释范围


- **generator**：GPT4
- **students**：- GPT2-large - Llama2-7B - Llama2-70B
- **training**：LoRA
- **valid points**：5866
- **valid split**：- 4866 - 500 - 500
- **verifier**：Lean3

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_a1e3d945218923b1bb`**：MUSTARD生成数学题及形式证明并用Lean筛选，MUSTARDSAUCE作为数据集训练较小模型；摘要未说明更新后小模型反复生成后续训练数据。
  - 来源版本：2402.08957v3；定位：Atom entry http://arxiv.org/abs/2402.08957v3；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r6safe_ev_cfg_mustard_lean3_generation_filter_train_v3`**：采1–2数学概念生成自然命题/解答及Lean3证明，失败以error message重试，过prover则入数据集，再LoRA训练下游学生。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Lean3接受形式证明不认证自然命题/形式命题等价；人工valid集IS-FS alignment约74%、IP-FP约72%，不能声称自然语言全真。
- 通过率或修复次数是给定GPT4/模板下的难度proxy，不是客观数学难度。
- MustardSauce-valid 5866，训练4866/验证500/测试500；其他数据组合用途不同不混用。
- 下游优于random/invalid的作者报告不等于独立证明所有增益由formal filtering单因素造成。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_20fe003e28646d5b` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2402.08957%2C2402.09015%2C2402.09269%2C2402.09283%2C2402.09727%2C2402.09742%2C2402.09748%2C2402.10110%2C2402.10176%2C2402.10196%2C2402.10200%2C2402.10663%2C2402.10770%2C2402.10890%2C2402.10963%2C2402.10980%2C2402.10987%2C2402.11190%2C2402.11218%2C2402.11359%2C2402.11411%2C2402.11451%2C2402.11550%2C2402.11633%2C2402.11827%2C2402.11975%2C2402.12048%2C2402.12185%2C2402.12255%2C2402.12317%2C2402.12348%2C2402.12391%2C2402.12431%2C2402.12451%2C2402.12545%2C2402.12914%2C2402.12959%2C2402.13210%2C2402.13212%2C2402.13296%2C2402.13426%2C2402.13542%2C2402.13598%2C2402.13669%2C2402.13717%2C2402.14034%2C2402.14083%2C2402.14207%2C2402.14268%2C2402.14382%2C2402.15057%2C2402.15116%2C2402.15391%2C2402.15538%2C2402.15589%2C2402.15809%2C2402.15810%2C2402.16288%2C2402.16313%2C2402.16499%2C2402.16696%2C2402.16767%2C2402.16823%2C2402.16837%2C2402.16906%2C2402.16965%2C2402.17168%2C2402.17453%2C2402.17505%2C2402.17574%2C2402.17613%2C2402.17753%2C2402.18005%2C2402.18060%2C2402.18361%2C2402.18381%2C2402.18485%2C2402.19085%2C2402.19173%2C2402.19446%2C2402.19473%2C2403.00198%2C2403.00690%2C2403.00833%2C2403.00839%2C2403.01197%2C2403.01244%2C2403.01248%2C2403.01528%2C2403.02164%2C2403.02502%2C2403.02691%2C2403.02817%2C2403.02985%2C2403.03101%2C2403.03129%2C2403.03186%2C2403.03218%2C2403.03768%2C2403.03883&max_results=100；阅读深度：`未单列`。
- `r6safe_src_mustard` · 已存来源 · v3
  - https://arxiv.org/html/2402.08957v3；阅读深度：`selected_original_method_and_scope_limits`。
- `r6safe_src_mustard_setup` · 已存来源 · v3
  - https://arxiv.org/html/2402.08957v3；阅读深度：`selected_original_method_and_scope_limits`。

**证据深度**：selected_original_method_and_scope_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a1e3d945218923b1bb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
