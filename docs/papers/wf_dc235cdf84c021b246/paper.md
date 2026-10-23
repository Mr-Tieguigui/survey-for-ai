# EvoX: Meta-Evolution for Automated Discovery

> 方法论文 · 2026 · `wf_dc235cdf84c021b246`

**作者**：Shu Liu, Shubham Agarwal, Monishwaran Maheswaran, Mert Cemri, Zhifei Li, Qiuyang Mang, Ashwin Naren, Ethan Boneh, Audrey Cheng, Melissa Z. Pan, Alexander Du, Kurt Keutzer, Alvin Cheung, Alexandros G. Dimakis, Koushik Sen, Matei Zaharia, Ion Stoica  
**原文**：https://arxiv.org/abs/2602.23413  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：候选数据库D、当前搜索策略S及策略/群体描述/窗口收益历史H；顶层策略生成器、评价与验证在外固定；具体更新过程为：停滞触发LLM修改选择父本、inspiration及variation偏好；经验证的S立即接管后续候选生成，D不重置；更新状态的保留与后继使用为：D和H在同一搜索运行跨窗口保留，更新S实际决定后续生成上下文。

## 2. 论文的核心内容与贡献

### configuration:cfg_evox_strategy_population_coevolution
声明的代码搜索边界内四条件满足；更新搜索策略而不是底层LLM权重，未证明顶层meta-generator递归更新。

**适用版本**：2602.23413v1；**原文定位**：v1 §3–4 Algorithm1 L143–281；v1 §6 L299–304。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### EvoX: candidate database plus evolved search strategies
`cfg_evox_strategy_population_coevolution` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 候选数据库D、当前搜索策略S及策略/群体描述/窗口收益历史H；顶层策略生成器、评价与验证在外固定。 |
| 改进过程与下一轮参与 | 停滞触发LLM修改选择父本、inspiration及variation偏好；经验证的S立即接管后续候选生成，D不重置。 |
| 保留的状态及时间尺度 | D和H在同一搜索运行跨窗口保留，更新S实际决定后续生成上下文。 |
| 外部固定部分 | - 任务评价器 - 固定solution/strategy LLM - 窗口和停滞阈值 - 策略validity与重试预算 - 变异操作语义 |
| 评价与选择设置 | - **AlphaEvolve comparison**：historical published numbers; original budget unavailable - **backbones**：- GPT-5 - Gemini-3.0-Pro - **default iterations**：100 - **independent runs**：3 - **strategy generator**：GPT-5 - **tasks**：196 - **window**：10% total iterations |

**配置判定**：声明的代码搜索边界内四条件满足；更新搜索策略而不是底层LLM权重，未证明顶层meta-generator递归更新。

来源：https://arxiv.org/html/2602.23413v1；版本：2602.23413v1；定位：v1 §3–4 Algorithm1 L143–281；v1 §6 L299–304。

## 4. 实验、评价协议与结果的可解释范围


- **AlphaEvolve comparison**：historical published numbers; original budget unavailable
- **backbones**：- GPT-5 - Gemini-3.0-Pro
- **default iterations**：100
- **independent runs**：3
- **strategy generator**：GPT-5
- **tasks**：196
- **window**：10% total iterations

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4training_ev_cfg_evox_strategy_population_coevolution`**：声明的代码搜索边界内四条件满足；更新搜索策略而不是底层LLM权重，未证明顶层meta-generator递归更新。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- AlphaEvolve数字取自原论文，其预算不可得，不构成同预算重跑。
- 跨任务的通用可迁移optimizer或无界增长未认证。
- 选段核查和有限任务配置；不是整篇逐段认证、跨领域保证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4training_src_w_evox` · 已存来源 · 2602.23413v1
  - https://arxiv.org/html/2602.23413v1；阅读深度：`targeted_primary_method_controls_and_limits`。

**证据深度**：original_abstract, targeted_primary_method_controls_limits_20261016。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_dc235cdf84c021b246 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
