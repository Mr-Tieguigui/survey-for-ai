# ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation

> 方法论文 · 2026 · `wf_95f9020f5a6910dbff`

**作者**：Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu  
**原文**：https://arxiv.org/abs/2609.39306  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ReSAIL在迭代privileged-information自蒸馏中选择信息步骤并约束学生保持下一轮教师行为；摘要报告三轮实验，不能外推无界增长。

## 2. 论文的核心内容与贡献

### configuration:cfg_resail_aitz_sgs_single_offline_cycle_v1
在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

**适用版本**：2609.39306v1；**原文定位**：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_resail_oel_three_cycle_retention_v1
在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

**适用版本**：2609.39306v1；**原文定位**：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `r4_role_review_wf_95f9020f5a6910dbff`
ReSAIL在迭代privileged-information自蒸馏中选择信息步骤并约束学生保持下一轮教师行为；摘要报告三轮实验，不能外推无界增长。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### ReSAIL + OEL: three-cycle offline privileged retention
`cfg_resail_oel_three_cycle_retention_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | ALFWorld/TextCraft的policy、按周期冻结的PI教师和下一周期部署—内化反馈链。 |
| 改进过程与下一轮参与 | cycle-start从当前policy复制teacher/student；OEL每update采样新ordinary responses，按teacher PI敏感性选步骤、按轨迹平衡KL，并对全部步骤加privileged retention；final学生进入下一cycle。 |
| 保留的状态及时间尺度 | 模型参数跨3周期保留；每cycle optimizer和random状态重置，旧轨迹集被新的自采轨迹替换。 |
| 外部固定部分 | - AdamW与loss/选择/保留公式 - PI提取模板与任务接口 - 每cycle冻结teacher - 外部环境和任务成功判据 |
| 评价与选择设置 | - **ALFWorld**：- **ID test**：128 - **OOD test**：128 - **batch trajectories**：32 - **retention weight**：0.5 - **rho**：0.05 - **trajectories per cycle**：960 - **TextCraft**：- **batch trajectories**：8 - **retention weight**：1.0 - **rho**：0.25 - **test**：100 - **trajectories per cycle**：240 - **cycles**：3 - **deployment PI**：False - **evaluation checkpoint**：final each cycle, no intermediate selection - **learning rate**：1e-06 - **models**：- Qwen3-4B - Qwen3-8B - **optimizer**：AdamW - **teacher schedule**：frozen within cycle; refreshed from preceding final student next cycle - **thinking**：False - **training seed variance**：not established by 3 decoding seeds - **updates per cycle**：30 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：声明policy、PI teacher及3周期收集/内化训练整体边界；固定外部环境和训练规则。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **更新由什么过程产生**：policy自行收集轨迹、提取summary并监督自身学生，参数据此更新。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **状态怎样持久保留**：前周期final模型参数成为下一周期起点；不是只保留本题答案。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **更新怎样进入后续改进**：更新student成为下周期PI教师、summary提取者和轨迹收集者，改变未来监督。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。

**配置判定**：在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

来源：https://arxiv.org/html/2609.39306v1；版本：2609.39306v1；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903。

### AITZ OEL + SGS: bounded single-cycle on-policy response distillation
`cfg_resail_aitz_sgs_single_offline_cycle_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Qwen3-VL-4B-Instruct在外部Aguvis CoAT日志上单cycle训练；SGS仅作固定离线数据过滤。 |
| 改进过程与下一轮参与 | 初始policy对日志history准备诊断与summary，teacher PI敏感性全局选80%步骤；保留OEL loss，不用TLB/PR，训练响应每update新采样，teacher全cycle冻结。 |
| 保留的状态及时间尺度 | 训练模型在100更新的单cycle内持续保留，每步更新student影响随后新采样响应；未演示新部署后刷新teacher或日志集。 |
| 外部固定部分 | - 外部Aguvis轨迹 - 一次固定SGS集合及PI - 冻结cycle-start teacher - OEL/AdamW loss及日志行动匹配器 |
| 评价与选择设置 | - **PR**：False - **SGS fraction**：0.8 - **TLB**：False - **batch trajectories**：16 - **cycles**：1 - **deployment PI**：False - **evaluation**：101 logged episodes,843 non-stop steps,ground-truth prior actions; no action execution - **model**：Qwen3-VL-4B-Instruct - **source trajectories**：1600 - **teacher schedule**：fixed throughout single cycle - **updates**：100 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：外部固定日志+OEL离线训练边界已声明。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **更新由什么过程产生**：学生参数按ordinary responses与privileged固定teacher匹配更新，但数据并非自主新环境采样。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **状态怎样持久保留**：更新后的模型checkpoint保留供后续输入行动预测。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。
- **更新怎样进入后续改进**：Appendix B.2 L745及E.4 L1404明确OEL/OEL+SGS每update从当前ordinary-view student新采样响应；更新参数改变下一步训练prefix/响应，回流后续蒸馏。该条件不额外要求教师或optimizer改写。（状态：`supported`；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903）。

**配置判定**：在此训练/生成/教师状态边界内支持结构四条件；固定优化器与目标不因此自改，不认证效率递增或无界增长。

来源：https://arxiv.org/html/2609.39306v1；版本：2609.39306v1；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903。

## 4. 实验、评价协议与结果的可解释范围


- **ALFWorld**：- **ID test**：128 - **OOD test**：128 - **batch trajectories**：32 - **retention weight**：0.5 - **rho**：0.05 - **trajectories per cycle**：960
- **TextCraft**：- **batch trajectories**：8 - **retention weight**：1.0 - **rho**：0.25 - **test**：100 - **trajectories per cycle**：240
- **cycles**：3
- **deployment PI**：False
- **evaluation checkpoint**：final each cycle, no intermediate selection
- **learning rate**：1e-06
- **models**：- Qwen3-4B - Qwen3-8B
- **optimizer**：AdamW
- **teacher schedule**：frozen within cycle; refreshed from preceding final student next cycle
- **thinking**：False
- **training seed variance**：not established by 3 decoding seeds
- **updates per cycle**：30


- **PR**：False
- **SGS fraction**：0.8
- **TLB**：False
- **batch trajectories**：16
- **cycles**：1
- **deployment PI**：False
- **evaluation**：101 logged episodes,843 non-stop steps,ground-truth prior actions; no action execution
- **model**：Qwen3-VL-4B-Instruct
- **source trajectories**：1600
- **teacher schedule**：fixed throughout single cycle
- **updates**：100

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_role_ev_wf_95f9020f5a6910dbff`**：ReSAIL在迭代privileged-information自蒸馏中选择信息步骤并约束学生保持下一轮教师行为；摘要报告三轮实验，不能外推无界增长。
  - 来源版本：2609.39306v1；定位：Atom entry http://arxiv.org/abs/2609.39306v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r5dist_ev_cfg_resail_oel_three_cycle_retention_v1`**：ALFWorld/TextCraft的policy、按周期冻结的PI教师和下一周期部署—内化反馈链。 cycle-start从当前policy复制teacher/student；OEL每update采样新ordinary responses，按teacher PI敏感性选步骤、按轨迹平衡KL，并对全部步骤加privileged retention；final学生进入下一cycle。
  - 来源版本：2609.39306v1；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903；深度：`未单列`。

- **`r5dist_ev_cfg_resail_aitz_sgs_single_offline_cycle_v1`**：Qwen3-VL-4B-Instruct在外部Aguvis CoAT日志上单cycle训练；SGS仅作固定离线数据过滤。 初始policy对日志history准备诊断与summary，teacher PI敏感性全局选80%步骤；保留OEL loss，不用TLB/PR，训练响应每update新采样，teacher全cycle冻结。
  - 来源版本：2609.39306v1；定位：§3.1–3.4 tool L129–181；§4.1 tool L187–196；Appendix A.1–A.3 tool L668–686；Appendix B.1–B.3 tool L696–776；Appendix D.1–D.3 tool L857–903；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 外部1,728条完整CoAT轨迹中固定抽1,600条，非此训练policy新探索；不能把文本3周期实验外推至GUI。
- 评估为teacher-forced日志逐步行动准确率，真实history给定；不是端到端GUI任务成功或部署闭环。
- SGS一次过滤，rho0.8，无TBSD轨迹平衡和PR；不能称完整ReSAIL三模块在线自改。
- 结构core仅限单cycle内student参数→fresh响应→蒸馏的回流，不因固定teacher而否认C4；不等于跨cycle教师升级或端到端GUI部署自举。
- 监控固定test子集每10更新，一固定解码seed；作者声明不用于调参/早停/选择，未独立代码审查。
- 文本只观察3个部署/内化周期，每周期30更新；3解码seed的SD是解码变异，不能误称3个独立训练seed。
- 模型参数跨周期继承，但optimizer与random状态每周期重置；不是每轮从原基模重训，也不是optimizer规则自改。
- 训练在已记录history上离线进行，不在训练内执行新的环境动作；下一周期用前一final policy重收轨迹并替换旧数据。
- PI为完整轨迹提取的summary，部署不输入PI；PI诊断固定128个OOD任务及固定Experience，不测试summary生成质量或后续教学生的因果效应。
- JSD敏感性用Top20+tail近似，仅分布变化非正确性；保留损失覆盖未选步骤，rho=1因归一化不同不必等同baseline。
- 本文观察特定SDPO-offline/OEL集成的退化与缓解，不能外推所有自蒸馏必崩溃或永不崩溃。
- 仅实读官方摘要作角色和范围判读，未核全文方法、实验、定理及数值；不得直接支持技术回答或继承关系。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_role_src_d65411d60f3e40c6` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?search_query=%28ti%3A%22recursive+self-improvement%22+OR+abs%3A%22recursive+self-improvement%22%29+AND+submittedDate%3A%5B190001010000+TO+202610112359%5D&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending；阅读深度：`未单列`。
- `r5dist_src_resail` · 已存来源 · 2609.39306v1
  - https://arxiv.org/html/2609.39306v1；阅读深度：`selected_primary_method_parameter_carry_teacher_refresh_and_limits`。

**证据深度**：original_abstract, selected_primary_method_parameter_carry_teacher_refresh_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_95f9020f5a6910dbff --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
