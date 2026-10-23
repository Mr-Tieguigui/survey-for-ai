# Online Operator Design in Evolutionary Optimization for Flexible Job Shop Scheduling via Large Language Models

> 方法论文 · 2025 · `wf_6f229217325ac8e1d8`

**作者**：Rongjie Liao, Junhao Qiu, Xin Chen, Xiaoping Li  
**原文**：https://arxiv.org/abs/2511.16485  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：LLM4EO: Large Language Model for Evolutionary Optimization in Flexible Job Shop Scheduling。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：FJSP solution population P、Python gene-selector operator population Q、operator成功率及fixed LLM/prompting流程；具体更新过程为：以生成更好解的次数/使用次数评价Q，roulette选operator；停滞trigger后LLM读P变化与Q代码思想/fitness建议，生成可运行新operator替换worst，reset所有operator fitness再继续EA；更新状态的保留与后继使用为：Q内新代码与P跨iterations保留；后继P/Q结果再次触发LLM operator设计。

## 2. 论文的核心内容与贡献

### configuration:cfg_llm4eo_online_operator_population_v1
在线operator代码与solution population的双向反馈满足有界四条件；v1题名LLM4EO与规范表后续标题分开，按同arXiv家族绑定实际版本。

**适用版本**：2511.16485v1；**原文定位**：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### LLM4EO v1: online gene-selector operator replacement
`cfg_llm4eo_online_operator_population_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | FJSP solution population P、Python gene-selector operator population Q、operator成功率及fixed LLM/prompting流程。 |
| 改进过程与下一轮参与 | 以生成更好解的次数/使用次数评价Q，roulette选operator；停滞trigger后LLM读P变化与Q代码思想/fitness建议，生成可运行新operator替换worst，reset所有operator fitness再继续EA。 |
| 保留的状态及时间尺度 | Q内新代码与P跨iterations保留；后继P/Q结果再次触发LLM operator设计。 |
| 外部固定部分 | - 遗传表示/七features - 基础LLM及validity check - population sizes/trigger formula - evaluator makespan |
| 评价与选择设置 | - **crossover probability**：0.9 - **max iterations**：200 - **mutation probability**：0.9 - **operator population**：3 - **solution population**：100 - **trigger epsilon**：0.05 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§4.2/4.3明确P,Q和gene-selector函数。（状态：`supported`；定位：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377）。
- **更新由什么过程产生**：优化过程自己的P/Q表现驱动LLM生成后继operator。（状态：`supported`；定位：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377）。
- **状态怎样持久保留**：新operator替换worst并留Q供后续搜索。（状态：`supported`；定位：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377）。
- **更新怎样进入后续改进**：新Q影响P演化，新的P/Q统计再用于后继operator构造。（状态：`supported`；定位：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377）。

**配置判定**：在线operator代码与solution population的双向反馈满足有界四条件；v1题名LLM4EO与规范表后续标题分开，按同arXiv家族绑定实际版本。

来源：https://arxiv.org/html/2511.16485v1；版本：2511.16485v1；定位：§4.2.3 operator fitness tool L142–144；§4.3 Algorithm1 replacement/reset tool L145–199；§5.1 budgets/model API comparison tool L207–209；§6 conclusion task scope tool L374–377。

## 4. 实验、评价协议与结果的可解释范围


- **crossover probability**：0.9
- **max iterations**：200
- **mutation probability**：0.9
- **operator population**：3
- **solution population**：100
- **trigger epsilon**：0.05

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r10_ev_cfg_llm4eo_online_operator_population_v1`**：在线operator代码与solution population的双向反馈满足有界四条件；v1题名LLM4EO与规范表后续标题分开，按同arXiv家族绑定实际版本。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 新operator只要求can run就替换worst，不是先证fitness更好后accept，不能写每次replacement都提高。
- operator fitness在每次evolution后全部reset，不能声称跨全run累计成功率memory。
- 基础LLM调用不训练权重；fine-tune task description是prompt文字编辑，不是parameter finetuning。
- 200 iteration budget和FJSP/DFJSP benchmark不外推任意EA或真实生产保证。
- - 新operator只要求can run就替换worst，不是先证fitness更好后accept，不能写每次replacement都提高。 - operator fitness在每次evolution后全部reset，不能声称跨全run累计成功率memory。 - 基础LLM调用不训练权重；fine-tune task description是prompt文字编辑，不是parameter finetuning。 - 200 iteration budget和FJSP/DFJSP benchmark不外推任意EA或真实生产保证。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r10_src_online_operator` · LLM4EO: Large Language Model for Evolutionary Optimization in Flexible Job Shop Scheduling · 2511.16485v1
  - https://arxiv.org/html/2511.16485v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6f229217325ac8e1d8 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
