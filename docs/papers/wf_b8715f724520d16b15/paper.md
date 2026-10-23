# Training Language Models to Self-Correct via Reinforcement Learning

> 方法论文 · 2024 · `wf_b8715f724520d16b15`

**作者**：Aviral Kumar, Vincent Zhuang, Rishabh Agarwal, Yi Su, JD Co-Reyes, Avi Singh, Kate Baumli, Shariq Iqbal, Colton Bishop, Rebecca Roelofs, Lei M Zhang, Kay McKinney, Disha Shrivastava, Cosmin Paduraru, George Tucker, Doina Precup, Feryal Behbahani, Aleksandra Faust  
**原文**：https://arxiv.org/html/2409.12917v1  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Configuration-specific structural and empirical boundary review; no universal RSI, autonomous researcher, or independent replication certification.

## 2. 论文的核心内容与贡献

### configuration:cfg_score_intrinsic_inference_v1
测试纠错配置为邻接的单题输出修订；与训练期持久参数闭环分开。

**适用版本**：2409.12917v1；**原文定位**：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_score_two_stage_online_rl_v1
训练期策略与后续自生成样本组成局部权重闭环；自生成轨迹不意味着无监督训练。

**适用版本**：2409.12917v1；**原文定位**：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### score two stage online rl v1
`cfg_score_two_stage_online_rl_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 训练期策略参数及其自生成两回合纠错轨迹；奖励函数/参考策略与梯度更新器在外部固定。 |
| 改进过程与下一轮参与 | Stage I用第一答强KL约束与第二答奖励初始化；Stage II联合两答RL并加入正确性翻转奖励差；更新后策略生成后续on-policy训练数据。 |
| 保留的状态及时间尺度 | 权重跨梯度更新、训练迭代和测试问题保留。 |
| 外部固定部分 | - 带oracle答案的训练集/正确性奖励、KL基准、奖励系数、外部优化算法 |

**配置判定**：训练期策略与后续自生成样本组成局部权重闭环；自生成轨迹不意味着无监督训练。

来源：https://arxiv.org/html/2409.12917v1；版本：2409.12917v1；定位：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189。

### score intrinsic inference v1
`cfg_score_intrinsic_inference_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 已训练SCoRe模型的单问题两次回答，测试不访问奖励验证器。 |
| 改进过程与下一轮参与 | 模型基于第一答与固定纠错指令产生第二答；测试阶段未更新权重。 |
| 保留的状态及时间尺度 | 当前问题的历史保留至第二答，不支持将该过程直接解释为跨任务持续学习。 |
| 外部固定部分 | - 部署参数、纠错提示、回合数、解码规则 |

**配置判定**：测试纠错配置为邻接的单题输出修订；与训练期持久参数闭环分开。

来源：https://arxiv.org/html/2409.12917v1；版本：2409.12917v1；定位：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`found4_ev_cfg_score_two_stage_online_rl_v1`**：训练期策略与后续自生成样本组成局部权重闭环；自生成轨迹不意味着无监督训练。
  - 来源版本：unknown；定位：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189；深度：`未单列`。

- **`found4_ev_cfg_score_intrinsic_inference_v1`**：测试纠错配置为邻接的单题输出修订；与训练期持久参数闭环分开。
  - 来源版本：unknown；定位：§3 tool L80–91；§5.1–5.3 tool L161–181；§6 tool L185–189；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 该配置没有部署梯度或新记忆写入证据。
- 测试无oracle不消除训练期监督；不能宣称纯零外部信号自我提升。
- 原文§3明确训练访问oracle答案和奖励验证器；测试时无外部纠错信号是不同边界。
- 两阶段可交错，多轮训练不等同部署时继续学习或改写RL更新器。
- MATH划分将原test4500项用于训练，仅剩500项作测试；不与原始test结果直接混排。
- 原文§3明确训练访问oracle答案和奖励验证器；测试时无外部纠错信号是不同边界。; 两阶段可交错，多轮训练不等同部署时继续学习或改写RL更新器。; MATH划分将原test4500项用于训练，仅剩500项作测试；不与原始test结果直接混排。
- 该配置没有部署梯度或新记忆写入证据。; 测试无oracle不消除训练期监督；不能宣称纯零外部信号自我提升。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `found4_src_score` · 已存来源 · 2409.12917v1
  - https://arxiv.org/html/2409.12917v1；阅读深度：`selected_official_fulltext_method_passages`。

**证据深度**：selected_official_fulltext_method_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_b8715f724520d16b15 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
