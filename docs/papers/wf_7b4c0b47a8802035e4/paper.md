# SePO: Self-Evolving Prompt Agent for System Prompt Optimization

> 综合系统/智能体 · 2026 · `wf_7b4c0b47a8802035e4`

**作者**：Wangcheng Tao, Han Wu, Weng-Fai Wong  
**原文**：https://arxiv.org/abs/2606.04465  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定模型/工作流、prompt-agent自身系统提示、训练任务池与提示档案；具体更新过程为：当前parent提示作为prompt-agent系统提示生成自身child副本；按训练任务上提示改进能力评分，纳入archive供下一代采样；更新状态的保留与后继使用为：archive跨G代；输出tilde-p-star后下游fine-tuning固定它，不再同时升级prompt-agent。

## 2. 论文的核心内容与贡献

### configuration:cfg_sepo_generalist_prompt_agent_pretrain_v1
预训练阶段prompt-agent提示经自身提案、评分、保留参与后继自身提案，四结构条件在有限提示搜索中成立；pretraining不是参数训练。

**适用版本**：2606.04465v1；**原文定位**：§3.1–3.3 Algorithm1 tool L124–174；§4.1 tool L184–194；AppendixH tool L805–815。
**引用权限**：`listed_configuration_scope_only`。

## 3. 系统架构、组件与更新过程

### SePO-Generalist: archived self-referential prompt-agent pretraining
`cfg_sepo_generalist_prompt_agent_pretrain_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定模型/工作流、prompt-agent自身系统提示、训练任务池与提示档案。 |
| 改进过程与下一轮参与 | 当前parent提示作为prompt-agent系统提示生成自身child副本；按训练任务上提示改进能力评分，纳入archive供下一代采样。 |
| 保留的状态及时间尺度 | archive跨G代；输出tilde-p-star后下游fine-tuning固定它，不再同时升级prompt-agent。 |
| 外部固定部分 | - LM权重/代码/工具 - 评分与档案准入 - G=5,K=2 |
| 评价与选择设置 | - **G**：5 - **K**：2 - **data**：train optimization; test separate - **prompt model**：Gemini3.1ProPreview - **runs**：5 - **task model**：DeepSeek-V3.2 |

**配置判定**：预训练阶段prompt-agent提示经自身提案、评分、保留参与后继自身提案，四结构条件在有限提示搜索中成立；pretraining不是参数训练。

来源：https://arxiv.org/html/2606.04465v1；版本：2606.04465v1；定位：§3.1–3.3 Algorithm1 tool L124–174；§4.1 tool L184–194；AppendixH tool L805–815。

## 4. 实验、评价协议与结果的可解释范围


- **G**：5
- **K**：2
- **data**：train optimization; test separate
- **prompt model**：Gemini3.1ProPreview
- **runs**：5
- **task model**：DeepSeek-V3.2

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_sepo_generalist_prompt_agent_pretrain_v1`**：预训练阶段prompt-agent提示经自身提案、评分、保留参与后继自身提案，四结构条件在有限提示搜索中成立；pretraining不是参数训练。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Specialist单任务和Generalist多任务不同，本卡认证Generalist的自指预训练。
- 将fine-tuning失败再回流pretraining的多轮交替是未来工作。
- G>5只初步有限增益，不认证指数增长或五基准外通用性。
- - Specialist单任务和Generalist多任务不同，本卡认证Generalist的自指预训练。 - 将fine-tuning失败再回流pretraining的多轮交替是未来工作。 - G>5只初步有限增益，不认证指数增长或五基准外通用性。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_sepo_v1` · 已存来源 · 2606.04465v1
  - https://arxiv.org/html/2606.04465v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7b4c0b47a8802035e4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
