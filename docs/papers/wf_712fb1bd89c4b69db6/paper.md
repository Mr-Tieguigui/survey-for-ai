# Large Language Models as Optimizers

> 方法论文 · 2023 · `wf_712fb1bd89c4b69db6`

**作者**：Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, Xinyun Chen  
**原文**：https://arxiv.org/html/2309.03409v2  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Configuration-specific structural and empirical boundary review; no universal RSI, autonomous researcher, or independent replication certification.

## 2. 论文的核心内容与贡献

### configuration:cfg_opro_prompt_trajectory_v2
在提示与评分轨迹状态边界内形成持续优化结构；底层模型和搜索控制不自改写。

**适用版本**：2309.03409v2；**原文定位**：§2.2–2.3 tool L105–117；§4.1–4.2 tool L182–205。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### opro prompt trajectory v2
`cfg_opro_prompt_trajectory_v2` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定优化LLM和scorer，历史提示–训练分数轨迹以及当前任务指令组成提示搜索系统。 |
| 改进过程与下一轮参与 | 优化器读取排序的历史候选和训练正确率，提出新提示；外部scorer评价后加入历史并用于下一搜索步。 |
| 保留的状态及时间尺度 | 候选历史跨优化步骤保留；选定提示用于测试例，跨不同数据集转移需单独评价。 |
| 外部固定部分 | - 优化器/scorer权重、外部训练标签、meta指令、候选排序截断和停止规则 |

**配置判定**：在提示与评分轨迹状态边界内形成持续优化结构；底层模型和搜索控制不自改写。

来源：https://arxiv.org/html/2309.03409v2；版本：2309.03409v2；定位：§2.2–2.3 tool L105–117；§4.1–4.2 tool L182–205。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`found4_ev_cfg_opro_prompt_trajectory_v2`**：在提示与评分轨迹状态边界内形成持续优化结构；底层模型和搜索控制不自改写。
  - 来源版本：unknown；定位：§2.2–2.3 tool L105–117；§4.1–4.2 tool L182–205；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 仅认证提示状态闭环，不认证优化器权重或meta规则自改。
- 训练标签用于评分；v2方法核查不能充当v3全文复核。
- 结构core不表示无界增长或跨领域普遍改进。
- 仅认证提示状态闭环，不认证优化器权重或meta规则自改。; 训练标签用于评分；v2方法核查不能充当v3全文复核。; 结构core不表示无界增长或跨领域普遍改进。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `found4_src_opro` · 已存来源 · 2309.03409v2
  - https://arxiv.org/html/2309.03409v2；阅读深度：`selected_official_fulltext_method_passages`。

**证据深度**：selected_official_fulltext_method_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_712fb1bd89c4b69db6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
