# Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA

> 方法论文 · 2026 · `wf_d7ba50f8bcf90a66d2`

**作者**：Mind Lab,  :, Vin Bo, Asher Cai, Jingwei Cao, Song Cao, Vic Cao, Amelia Chen, Andrew Chen, Kaijie Chen, Cleon Cheng, Steven Chiang, Kaixuan Fan, Hera Feng, Huan Feng, Arthur Fu, Aaron Guan, Jun Gao, Pyke Han, Nolan Ho, Ori Hong, Hailee Hou, Piers Hua, Charles Huang, Miles Jiang, Nora Jiang, Yuyi Jiang, Qiuyu Jin, Fancy Kong, Kuss Koo, Echo Lee, Jaron Lee, Andrew Lei, Alexy Li, Dawn Li, Lucian Li, Ray Li, Ricardo Li, Smith Li, Theo Li, Allen Lin, Elliot Lin, Fan Lin, Chen Ling, Kairus Liu, Kieran Liu, Logan Liu, Neo Liu, Xiang Liu, Yuxin Lu, Maeve Luo, Pony Ma, Verity Niu, Cole Qiao, Guian Qiu, Vince Qu,  Sentry, Zhuoran Shen, Niko Song, Vincent Wang, Bo Wu, Rio Yang, Schacter Yang, Evelyn Ye, Fiona Ye, Ina Ye, Regis Ye, Josh Ying, Atlas Zeng, Danney Zeng, Salmon Zhan, Anya Zhang, Di Zhang, Mia Zhang, Sueky Zhang, Xuening Zhang, Wei Zhao, Ada Zhou, Adrian Zhou, Yuhua Zhou, Juno Zhu, Murphy Zhuang, Mindverse Team  
**原文**：https://arxiv.org/abs/2608.09819  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：仅取已实测的expansion/AutoResearch配置搜索：冻结GLM-5.2-FP8和模型可见agent harness，搜索HCP resources、skills、tool exposure、hooks。完整三阶段adapter世代循环另为设计；具体更新过程为：模型提出配置改动，受影响benchmark slice执行反馈决定接受；后续job瞄准仍未覆盖任务，并继承已注册的HCP候选/覆盖记录；更新状态的保留与后继使用为：HCP、skills/hooks版本及其任务覆盖和evaluation证据跨69个按时间排序的job保留；反馈重定向后续配置搜索。

## 2. 论文的核心内容与贡献

### configuration:cfg_macaron_v1_measured_hcp_expansion_search
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 模型提出配置改动，受影响benchmark slice执行反馈决定接受；后续job瞄准仍未覆盖任务，并继承已注册的HCP候选/覆盖记录。

**适用版本**：2608.09819v1；**原文定位**：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Macaron-V1 v1 measured frozen-base HCP expansion search
`cfg_macaron_v1_measured_hcp_expansion_search` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 仅取已实测的expansion/AutoResearch配置搜索：冻结GLM-5.2-FP8和模型可见agent harness，搜索HCP resources、skills、tool exposure、hooks。完整三阶段adapter世代循环另为设计。 |
| 改进过程与下一轮参与 | 模型提出配置改动，受影响benchmark slice执行反馈决定接受；后续job瞄准仍未覆盖任务，并继承已注册的HCP候选/覆盖记录。 |
| 保留的状态及时间尺度 | HCP、skills/hooks版本及其任务覆盖和evaluation证据跨69个按时间排序的job保留；反馈重定向后续配置搜索。 |
| 外部固定部分 | - 冻结GLM-5.2-FP8；此实测无optimizer步骤 - 122个已知base失败simulation任务及官方reward - benchmark backend verifier/threshold；tool exposure或安全边界变化需human review |
| 评价与选择设置 | - **evaluation**：adaptive affected-slice execution; union coverage - **jobs**：69 - **measured slice**：122 base-failure simulation tasks from 29 TerminalBench 2.1 source families - **task attempts**：450 - **weight updates in slice**：0 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§3.2.1明确theta冻结，c与LoRA phi是不同对象。（状态：`supported`；定位：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597）。
- **更新由什么过程产生**：§3.2.4模型提HCP提示/skill/scaffold/tool-policy改动。（状态：`supported`；定位：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597）。
- **状态怎样持久保留**：MindForge记录parent/config/evaluation lineage；实测为69 chronological jobs。（状态：`supported`；定位：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597）。
- **更新怎样进入后续改进**：§3.2.5后续job根据未覆盖家族自适应target，改变c并继续执行评价。（状态：`supported`；定位：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 模型提出配置改动，受影响benchmark slice执行反馈决定接受；后续job瞄准仍未覆盖任务，并继承已注册的HCP候选/覆盖记录。

来源：https://arxiv.org/html/2608.09819v1；版本：2608.09819v1；定位：§3.2.1–3.2.3 changed objects and version retention tool L549–580；§3.2.4–3.2.5 model proposals and measured adaptive search tool L582–597；§3.1.4 present evaluation boundary tool L539–542；§3.2.5 adaptive selection and absent adapter transfer tool L589–597。

## 4. 实验、评价协议与结果的可解释范围


- **evaluation**：adaptive affected-slice execution; union coverage
- **jobs**：69
- **measured slice**：122 base-failure simulation tasks from 29 TerminalBench 2.1 source families
- **task attempts**：450
- **weight updates in slice**：0

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_macaron_v1_measured_hcp_expansion_search`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 模型提出配置改动，受影响benchmark slice执行反馈决定接受；后续job瞄准仍未覆盖任务，并继承已注册的HCP候选/覆盖记录。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 122/122是选定失败集的adaptive union coverage，并非单配置held-out pass rate；一次通过即可计覆盖。
- 69 jobs/450 attempts的phase任务组成与error率同时变化，不能把13倍yield当hooks因果效应。
- 本实验没有执行后续LoRA转移；未报告可分离weights/config attribution或反复adapter世代改进。
- 122/122是选定失败集的adaptive union coverage，并非单配置held-out pass rate；一次通过即可计覆盖。; 69 jobs/450 attempts的phase任务组成与error率同时变化，不能把13倍yield当hooks因果效应。; 本实验没有执行后续LoRA转移；未报告可分离weights/config attribution或反复adapter世代改进。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_macaron` · Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA · 2608.09819v1
  - https://arxiv.org/html/2608.09819v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d7ba50f8bcf90a66d2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
