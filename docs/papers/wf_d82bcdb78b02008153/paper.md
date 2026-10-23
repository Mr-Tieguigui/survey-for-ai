# Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

> 方法论文 · 2026 · `wf_d82bcdb78b02008153`

**作者**：Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, Vahab Mirrokni  
**原文**：https://arxiv.org/abs/2606.03979  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：CMS不同频率memory参数、激活/低秩扩展和梦生成模型；外部任务tau、选择/蒸馏/ReSTEM流程固定；具体更新过程为：巩固把快memory知识蒸馏入新慢参数；当前模型生成dream，经选样SFT隔离副本与任务增益奖励，再以ReSTEM强化好dream生成器；更新状态的保留与后继使用为：新增慢memory保留；快块低秩参数在巩固后重置；外层训练后的dream生成参数用于后续生成。

## 2. 论文的核心内容与贡献

### configuration:cfg_sleep_dreaming_seal_extension
全流程中训练后的模型继续生成后续自编辑训练数据，满足声明边界内四条件；只含memory consolidation的§4.1实验不能代替dream闭环证据。

**适用版本**：2606.03979v1；**原文定位**：v1 §3.2–3.4 L154–208；v1 §4.1 L228–229；v1 §4 L298。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Sleep: consolidation plus trained dream generation
`cfg_sleep_dreaming_seal_extension` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | CMS不同频率memory参数、激活/低秩扩展和梦生成模型；外部任务tau、选择/蒸馏/ReSTEM流程固定。 |
| 改进过程与下一轮参与 | 巩固把快memory知识蒸馏入新慢参数；当前模型生成dream，经选样SFT隔离副本与任务增益奖励，再以ReSTEM强化好dream生成器。 |
| 保留的状态及时间尺度 | 新增慢memory保留；快块低秩参数在巩固后重置；外层训练后的dream生成参数用于后续生成。 |
| 外部固定部分 | - CMS频率/触发时机 - 参数扩展与冻结策略 - LoRA/SFT - 固定语义reward model与编辑距离 - 任务tau - ReSTEM |
| 评价与选择设置 | - **consolidation only**：Llama 3B/8B continual classification, separate from dreaming - **dream inner update**：isolated per-dream LoRA SFT model - **dream outer update**：ReSTEM on binary task performance gain - **dream selection**：top-k importance plus b random samples; selected passage does not supply exact k,b - **knowledge incorporation**：SQuAD, SEAL setup |

**配置判定**：全流程中训练后的模型继续生成后续自编辑训练数据，满足声明边界内四条件；只含memory consolidation的§4.1实验不能代替dream闭环证据。

来源：https://arxiv.org/html/2606.03979v1；版本：2606.03979v1；定位：v1 §3.2–3.4 L154–208；v1 §4.1 L228–229；v1 §4 L298。

## 4. 实验、评价协议与结果的可解释范围


- **consolidation only**：Llama 3B/8B continual classification, separate from dreaming
- **dream inner update**：isolated per-dream LoRA SFT model
- **dream outer update**：ReSTEM on binary task performance gain
- **dream selection**：top-k importance plus b random samples; selected passage does not supply exact k,b
- **knowledge incorporation**：SQuAD, SEAL setup

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4training_ev_cfg_sleep_dreaming_seal_extension`**：全流程中训练后的模型继续生成后续自编辑训练数据，满足声明边界内四条件；只含memory consolidation的§4.1实验不能代替dream闭环证据。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- §4.1明确不含self-improvement/dreaming，应与完整流程结果分开。
- 语义reward model固定；扩展可用预分配masked参数实现，不意味着物理容量无界增长。
- 任务真值评价、种子上下文与固定外层优化仍存在；不能写成无外部数据/设计。
- 选段核查和有限任务配置；不是整篇逐段认证、跨领域保证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4training_src_w_lm_sleep` · 已存来源 · 2606.03979v1
  - https://arxiv.org/html/2606.03979v1；阅读深度：`targeted_primary_method_controls_and_limits`。

**证据深度**：original_abstract, targeted_primary_method_controls_limits_20261016。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d82bcdb78b02008153 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
