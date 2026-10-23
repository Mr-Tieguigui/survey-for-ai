# AQuA: Recursively Self-Improving Quantitative Trading Research Agents

> 方法论文 · 2026 · `wf_ac1e262bdc2c5397fc`

**作者**：Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jason Ge, Shushu Liang, Xu Kuang, Mengdi Wang  
**原文**：https://arxiv.org/abs/2608.12841  
**研究分支**：科研代理、实验与发现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Manager、六专门代理、因子/组合信号与Memory/Beliefs/Policy stores；不含Part II；具体更新过程为：提出可反驳机制，registry构造因子表达式，评价/方向校准/回测后Librarian写证据与belief；下轮Manager读memory改提案；更新状态的保留与后继使用为：跨研究run保留机制、失败、信号方向与经验。

## 2. 论文的核心内容与贡献

### configuration:cfg_aqua_factor_memory_belief_loop_v1
Part I自己实验更新持久研究状态并反馈后继Manager计划和因子探索，四结构条件在有界因子研究系统成立。

**适用版本**：2608.12841v1；**原文定位**：§3/3.1 tool L98–120；§4.1–4.3 tool L211–228；§4.4–4.5 tool L229–239。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_aqua_model_config_knowledge_loop_v1
Part II实验结果进入下一轮config提案，四结构条件限于这一独立模型开发系统；不能虚构两Part耦合。

**适用版本**：2608.12841v1；**原文定位**：§3/3.1 tool L100–115；§3.1 DSL tool L165–209；§5.1–5.3 tool L240–255。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### AQuA Part I: cross-run factor research beliefs
`cfg_aqua_factor_memory_belief_loop_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Manager、六专门代理、因子/组合信号与Memory/Beliefs/Policy stores；不含Part II。 |
| 改进过程与下一轮参与 | 提出可反驳机制，registry构造因子表达式，评价/方向校准/回测后Librarian写证据与belief；下轮Manager读memory改提案。 |
| 保留的状态及时间尺度 | 跨研究run保留机制、失败、信号方向与经验。 |
| 外部固定部分 | - 基础LM与evaluator - 因子算子/数据路径 - Part I/II无共享状态 |

**配置判定**：Part I自己实验更新持久研究状态并反馈后继Manager计划和因子探索，四结构条件在有界因子研究系统成立。

来源：https://arxiv.org/html/2608.12841v1；版本：2608.12841v1；定位：§3/3.1 tool L98–120；§4.1–4.3 tool L211–228；§4.4–4.5 tool L229–239。

### AQuA Part II: config-driven model development
`cfg_aqua_model_config_knowledge_loop_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 独立config训练/评价/知识库系统，architecture/loss/sampler/optimizer registries。 |
| 改进过程与下一轮参与 | 单config diff训练一个variant，经sealed validation评价后写knowledge store，下一hypothesis读取。 |
| 保留的状态及时间尺度 | 研究知识跨variants保留；不写Part I memory。 |
| 外部固定部分 | - frozen splits/features/labels/evaluator - 注册算子空间 - 模型只输出config不写数据代码 |

**配置判定**：Part II实验结果进入下一轮config提案，四结构条件限于这一独立模型开发系统；不能虚构两Part耦合。

来源：https://arxiv.org/html/2608.12841v1；版本：2608.12841v1；定位：§3/3.1 tool L100–115；§3.1 DSL tool L165–209；§5.1–5.3 tool L240–255。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_aqua_factor_memory_belief_loop_v1`**：Part I自己实验更新持久研究状态并反馈后继Manager计划和因子探索，四结构条件在有界因子研究系统成立。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`r8a_ev_cfg_aqua_model_config_knowledge_loop_v1`**：Part II实验结果进入下一轮config提案，四结构条件限于这一独立模型开发系统；不能虚构两Part耦合。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 具体部署表达式未公开，不能称完整复现。
- combined validation IC不是Part II per-stock IC；两个值不可直接比较。
- 基础LM/evaluator固定，未认证持续加速或实盘收益。
- 作者称最终2021–2025 test冻结后才评分，不能写搜索读取test反馈。
- 精确features/labels/normalization及卷积配置未公开。
- 模型收益为作者报告，不是实盘盈利或一般研究能力提升的认证。
- - 具体部署表达式未公开，不能称完整复现。 - combined validation IC不是Part II per-stock IC；两个值不可直接比较。 - 基础LM/evaluator固定，未认证持续加速或实盘收益。
- - 作者称最终2021–2025 test冻结后才评分，不能写搜索读取test反馈。 - 精确features/labels/normalization及卷积配置未公开。 - 模型收益为作者报告，不是实盘盈利或一般研究能力提升的认证。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_aqua_v1` · 已存来源 · 2608.12841v1
  - https://arxiv.org/html/2608.12841v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_ac1e262bdc2c5397fc --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
