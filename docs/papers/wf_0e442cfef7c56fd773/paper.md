# Self-Instruct: Aligning Language Models with Self-Generated Instructions

> 方法论文 · 2022 · `wf_0e442cfef7c56fd773`

**作者**：Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, Hannaneh Hajishirzi  
**原文**：https://aclanthology.org/2023.acl-long.754/  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Configuration-specific structural and empirical boundary review; no universal RSI, autonomous researcher, or independent replication certification.

## 2. 论文的核心内容与贡献

### configuration:cfg_self_instruct_data_pool_bootstrap
在任务池搜索状态与反馈边界内满足四个结构条件；core只指保留任务池参与后续生成的有界闭环，不证明教师权重或更新器自改。

**适用版本**：ACL-2023-camera-ready；**原文定位**：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_self_instruct_data_then_sft
邻接的最终学生权重训练/部署配置；没有把数据池的迭代保留当成学生参数参与后续改进循环的证据。

**适用版本**：ACL-2023-camera-ready；**原文定位**：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### self instruct data then sft
`cfg_self_instruct_data_then_sft` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 最终学生模型的SFT权重更新和随后部署视图；已完成的自生成指令数据集作为固定训练输入，数据池生成循环在本配置边界外。 |
| 改进过程与下一轮参与 | 按§2.3在已合成数据上标准监督微调原GPT3，最终学生接受任务指令并产生回答；未展示微调学生返回下一轮数据生成。 |
| 保留的状态及时间尺度 | 训练所得权重跨部署测试任务保留；本视图没有部署后持续更新或学生→生成教师反馈的证据。 |
| 外部固定部分 | - 已完成的合成训练集、SFT目标和优化算法、模板、部署解码 |

**配置判定**：邻接的最终学生权重训练/部署配置；没有把数据池的迭代保留当成学生参数参与后续改进循环的证据。

来源：https://aclanthology.org/2023.acl-long.754.pdf；版本：ACL-2023-camera-ready；定位：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271。

### self instruct data pool bootstrap
`cfg_self_instruct_data_pool_bootstrap` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定GPT3生成器、人工种子和持续扩充的指令任务池组成的数据自举搜索系统；不包含最终SFT学生参数更新。 |
| 改进过程与下一轮参与 | 每步从池中取8条示例（6个人工种子、2个此前已生成任务），生成新指令与实例，经相似度/格式过滤后加入任务池；更新后的池再次提供生成上下文。 |
| 保留的状态及时间尺度 | 新任务跨生成步骤保留并影响后续任务生成；最终数据可用于独立的SFT阶段。 |
| 外部固定部分 | - GPT3教师权重、175人工种子、6+2采样比例、ROUGE-L<0.7等过滤规则、提示模板 |

**配置判定**：在任务池搜索状态与反馈边界内满足四个结构条件；core只指保留任务池参与后续生成的有界闭环，不证明教师权重或更新器自改。

来源：https://aclanthology.org/2023.acl-long.754.pdf；版本：ACL-2023-camera-ready；定位：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`found4_ev_cfg_self_instruct_data_then_sft`**：邻接的最终学生权重训练/部署配置；没有把数据池的迭代保留当成学生参数参与后续改进循环的证据。
  - 来源版本：unknown；定位：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271；深度：`未单列`。

- **`found4_ev_cfg_self_instruct_data_pool_bootstrap`**：在任务池搜索状态与反馈边界内满足四个结构条件；core只指保留任务池参与后续生成的有界闭环，不证明教师权重或更新器自改。
  - 来源版本：unknown；定位：PDF physical pp2–4 Figure2 and §§2.1–2.3；tool lines L122–126/L170–271；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 教师模型在该自举循环中固定，更新后的学生不返回循环。
- 固定的过滤和种子采样规则不自我改写；未认证改进器增益、无界增长或独立复现。
- 该结构判断不依赖最终SFT收益，也不把合成任务数量当自主能力增益。
- 原文未展示微调学生重新生成下一轮训练数据；数据池自举另建配置。
- 自生成训练数据来源与学生权重自主改写、部署持续学习是不同主张。
- 依赖人工种子与启发式过滤；无独立复现实证。
- 原文未展示微调学生重新生成下一轮训练数据；数据池自举另建配置。; 自生成训练数据来源与学生权重自主改写、部署持续学习是不同主张。; 依赖人工种子与启发式过滤；无独立复现实证。
- 教师模型在该自举循环中固定，更新后的学生不返回循环。; 固定的过滤和种子采样规则不自我改写；未认证改进器增益、无界增长或独立复现。; 该结构判断不依赖最终SFT收益，也不把合成任务数量当自主能力增益。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `found4_src_self_instruct` · 已存来源 · ACL-2023-camera-ready
  - https://aclanthology.org/2023.acl-long.754.pdf；阅读深度：`selected_official_fulltext_method_passages`。

**证据深度**：selected_official_fulltext_method_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0e442cfef7c56fd773 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
