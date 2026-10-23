# Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models

> 方法论文 · 2023 · `wf_8c342e08652d44c7d7`

**作者**：Avi Singh, John D. Co-Reyes, Rishabh Agarwal, Ankesh Anand, Piyush Patil, Xavier Garcia, Peter J. Liu, James Harrison, Jaehoon Lee, Kelvin Xu, Aaron Parisi, Abhishek Kumar, Alex Alemi, Alex Rizkowsky, Azade Nova, Ben Adlam, Bernd Bohnet, Gamaleldin Elsayed, Hanie Sedghi, Igor Mordatch, Isabelle Simpson, Izzeddin Gur, Jasper Snoek, Jeffrey Pennington, Jiri Hron, Kathleen Kenealy, Kevin Swersky, Kshiteej Mahajan, Laura Culp, Lechao Xiao, Maxwell L. Bileschi, Noah Constant, Roman Novak, Rosanne Liu, Tris Warkentin, Yundi Qian, Yamini Bansal, Ethan Dyer, Behnam Neyshabur, Jascha Sohl-Dickstein, Noah Fiedel  
**原文**：https://arxiv.org/abs/2312.06585  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：当前生成策略与二元反馈样本；具体更新过程为：Generate使用当前策略，Improve每轮从基础模型微调，得到下一轮生成策略；更新状态的保留与后继使用为：跨Generate/Improve轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_restem
与ReST的连续微调不同；生成器依赖闭合不等于全部参数沿同一轨迹累加

**适用版本**：v4；**原文定位**：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p3.1；S3.SS0.SSS0.Px2.p4.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_restem
`cfg_restem` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前生成策略与二元反馈样本 |
| 改进过程与下一轮参与 | Generate使用当前策略，Improve每轮从基础模型微调，得到下一轮生成策略 |
| 保留的状态及时间尺度 | 跨Generate/Improve轮次 |
| 外部固定部分 | 原始输入题目、二元奖励和过滤微调 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：当前生成策略与二元反馈样本（状态：`supported`；定位：S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px2.p2；S3.SS0.SSS0.Px2.p3）。
- **更新由什么过程产生**：Generate使用当前策略，Improve每轮从基础模型微调，得到下一轮生成策略（状态：`supported`；定位：S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px2.p2；S3.SS0.SSS0.Px2.p3）。
- **状态怎样持久保留**：跨Generate/Improve轮次（状态：`supported`；定位：S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px2.p2；S3.SS0.SSS0.Px2.p3）。
- **更新怎样进入后续改进**：Generate使用当前策略，Improve每轮从基础模型微调，得到下一轮生成策略（状态：`supported`；定位：S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px2.p2；S3.SS0.SSS0.Px2.p3）。

**配置判定**：与ReST的连续微调不同；生成器依赖闭合不等于全部参数沿同一轨迹累加

来源：https://arxiv.org/html/2312.06585v4；版本：v4；定位：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p3.1；S3.SS0.SSS0.Px2.p4.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_restem`**：Generate使用当前策略，Improve每轮从基础模型微调，得到下一轮生成策略
  - 来源版本：v4；定位：S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px2.p2；S3.SS0.SSS0.Px2.p3；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_p2c_restem_star_sampling_boundary`**：ReST-EM原文明确比较STaR的单次贪心生成与自身温度多样本生成；STaR还用正确答案提示对失败题进行rationalization，再按最终答案正确性过滤。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`e3_training_r2_restem_rest_3`**：ReST-EM作者明确将其定义为ReST的简化训练版本；保留当前策略生成与过滤微调，并把主要实验改为二元奖励、每轮一次Improve、从base重训且不混入人类生成输出。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`e3_training_r2_seal_restem_2`**：SEAL外层明确采用ReST-EM式过滤行为克隆：当前策略采样自编辑，经内层适应后的任务表现形成二元奖励，仅对成功自编辑执行外层SFT。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 每轮从base重新微调；跨轮保留的是更新模型生成下一轮数据的依赖。
- 仍使用原始输入题目与二元正确性反馈，不混人类输出并非无原始数据。
- 与
- R
- e
- S
- T
- 的
- 连
- 续
- 微
- 调
- 不
- 同
- ；
- 生
- 成
- 器
- 依
- 赖
- 闭
- 合
- 等
- 于
- 全
- 部
- 参
- 数
- 沿
- 一
- 轨
- 迹
- 累
- 加
- 这是作者明确的采样与失败题处理机制比较，不证明ReST-EM完整继承STaR。ReST-EM关于rationalization错误推理/正确答案的观察限定其初步实验，不是跨数据集复现STaR或证明全部rationalization不忠实；两者都从base重训生成新策略。
- ReST原配置在数据混合中保留原始人类输出，连续微调当前最优策略，并对同一Grow数据递增奖励阈值执行多次Improve；ReST-EM依然使用原始任务输入和正确答案/测试奖励，不能表述为完全摆脱人类信息。两者方法继承不代表原实验结论及保证继承。
- 复用的端点仅是采样—成功过滤—SFT训练程序。SEAL优化自编辑的可学习性，奖励依赖内层适应后的模型；ReST-EM直接生成题目答案，并在各Improve轮从base重训。不能把后者的base重置、人类输出处理、math/code实验及EM单调保证自动迁移到SEAL。

## 7. 与其他论文的具体关系

### [Self-Adapting Language Models](../r03_method/wf_f87820e7aeedf3c20a.md)
关系：`reuses_training_procedure_of` · `r2_seal_restem_2` · 当前展示权限：`primary_supported`。
SEAL外层明确采用ReST-EM式过滤行为克隆：当前策略采样自编辑，经内层适应后的任务表现形成二元奖励，仅对成功自编辑执行外层SFT。

**关系边界**：复用的端点仅是采样—成功过滤—SFT训练程序。SEAL优化自编辑的可学习性，奖励依赖内层适应后的模型；ReST-EM直接生成题目答案，并在各Improve轮从base重训。不能把后者的base重置、人类输出处理、math/code实验及EM单调保证自动迁移到SEAL。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2506.10943v2；版本：v2；定位：S3.SS1.p1.1；S3.SS1.p3.1；S3.SS1.p4.1；S3.SS1.p5.1；S3.SS1.p6.2。
- object：https://arxiv.org/html/2312.06585v4；版本：v4；定位：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p4.1。

### [Reinforced Self-Training (ReST) for Language Modeling](../r03_method/wf_bd90935154aa7b75e6.md)
关系：`modifies_component_of` · `r2_restem_rest_3` · 当前展示权限：`primary_supported`。
ReST-EM作者明确将其定义为ReST的简化训练版本；保留当前策略生成与过滤微调，并把主要实验改为二元奖励、每轮一次Improve、从base重训且不混入人类生成输出。

**关系边界**：ReST原配置在数据混合中保留原始人类输出，连续微调当前最优策略，并对同一Grow数据递增奖励阈值执行多次Improve；ReST-EM依然使用原始任务输入和正确答案/测试奖励，不能表述为完全摆脱人类信息。两者方法继承不代表原实验结论及保证继承。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2312.06585v4；版本：v4；定位：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p3.1；S3.SS0.SSS0.Px2.p4.1。
- object：https://arxiv.org/html/2308.08998v2；版本：v2；定位：S3.p2.1；S3.p3.1；S3.SS0.SSSx1.p1.1；S3.SS0.SSSx2.p2.1；S3.SS0.SSSx2.p4.1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_restem` · ReST-EM · v4
  - https://arxiv.org/html/2312.06585v4；阅读深度：`未单列`。
- `expand_src_w_seal` · SEAL · v2
  - https://arxiv.org/html/2506.10943v2；阅读深度：`未单列`。
- `expand_src_w_star` · STaR · v2
  - https://arxiv.org/html/2203.14465v2；阅读深度：`未单列`。
- `stage1_src_w_rest` · 已存来源 · v2
  - https://arxiv.org/html/2308.08998v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8c342e08652d44c7d7 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
