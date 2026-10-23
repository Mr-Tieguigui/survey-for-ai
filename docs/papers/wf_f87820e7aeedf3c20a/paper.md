# Self-Adapting Language Models

> 方法论文 · 2025 · `wf_f87820e7aeedf3c20a`

**作者**：Adam Zweiger, Jyothish Pari, Han Guo, Ekin Akyürek, Yoon Kim, Pulkit Agrawal  
**原文**：https://arxiv.org/abs/2506.10943  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：同模型自编辑生成策略的外层训练；具体更新过程为：当前模型提出自编辑，SFT后任务表现给外层反馈；更新生成策略继续提出自编辑；更新状态的保留与后继使用为：外层训练轮次；内层适应按实例另列。

## 2. 论文的核心内容与贡献

### configuration:cfg_seal
本判定限定外层训练；单次测试适应和顺序知识编辑不能自动继承核心；顺序编辑有遗忘报告

**适用版本**：v2；**原文定位**：S3.SS1.p1.1；S3.SS1.p3.1；S3.SS1.p4.1；S3.SS1.p5.1；S3.SS1.p6.2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_seal
`cfg_seal` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 同模型自编辑生成策略的外层训练 |
| 改进过程与下一轮参与 | 当前模型提出自编辑，SFT后任务表现给外层反馈；更新生成策略继续提出自编辑 |
| 保留的状态及时间尺度 | 外层训练轮次；内层适应按实例另列 |
| 外部固定部分 | SFT/LoRA、ReST-EM过滤、任务评价与工具函数 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：同模型自编辑生成策略的外层训练（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p3；S3.SS1.p4；S3.SS1.p5；S3.SS1.p7；S5.SS0.SSS0.Px1.p2）。
- **更新由什么过程产生**：当前模型提出自编辑，SFT后任务表现给外层反馈；更新生成策略继续提出自编辑（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p3；S3.SS1.p4；S3.SS1.p5；S3.SS1.p7；S5.SS0.SSS0.Px1.p2）。
- **状态怎样持久保留**：外层训练轮次；内层适应按实例另列（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p3；S3.SS1.p4；S3.SS1.p5；S3.SS1.p7；S5.SS0.SSS0.Px1.p2）。
- **更新怎样进入后续改进**：当前模型提出自编辑，SFT后任务表现给外层反馈；更新生成策略继续提出自编辑（状态：`supported`；定位：S3.SS1.p1；S3.SS1.p3；S3.SS1.p4；S3.SS1.p5；S3.SS1.p7；S5.SS0.SSS0.Px1.p2）。

**配置判定**：本判定限定外层训练；单次测试适应和顺序知识编辑不能自动继承核心；顺序编辑有遗忘报告

来源：https://arxiv.org/html/2506.10943v2；版本：v2；定位：S3.SS1.p1.1；S3.SS1.p3.1；S3.SS1.p4.1；S3.SS1.p5.1；S3.SS1.p6.2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_seal`**：当前模型提出自编辑，SFT后任务表现给外层反馈；更新生成策略继续提出自编辑
  - 来源版本：v2；定位：S3.SS1.p1；S3.SS1.p3；S3.SS1.p4；S3.SS1.p5；S3.SS1.p7；S5.SS0.SSS0.Px1.p2；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_r2_seal_restem_2`**：SEAL外层明确采用ReST-EM式过滤行为克隆：当前策略采样自编辑，经内层适应后的任务表现形成二元奖励，仅对成功自编辑执行外层SFT。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 核心判定限外层自编辑生成策略训练。
- 内层SFT模型用于产生奖励，不能把单实例内层适应与外层持久改进混为一个循环。
- 复用ReST-EM训练程序不继承ReST-EM每轮从base重训设置。
- 本
- 判
- 定
- 限
- 外
- 层
- 训
- 练
- ；
- 单
- 次
- 测
- 试
- 适
- 应
- 和
- 顺
- 序
- 知
- 识
- 编
- 辑
- 不
- 能
- 自
- 动
- 继
- 承
- 核
- 心
- 有
- 遗
- 忘
- 报
- 告
- 复用的端点仅是采样—成功过滤—SFT训练程序。SEAL优化自编辑的可学习性，奖励依赖内层适应后的模型；ReST-EM直接生成题目答案，并在各Improve轮从base重训。不能把后者的base重置、人类输出处理、math/code实验及EM单调保证自动迁移到SEAL。

## 7. 与其他论文的具体关系

### [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](../r03_method/wf_8c342e08652d44c7d7.md)
关系：`reuses_training_procedure_of` · `r2_seal_restem_2` · 当前展示权限：`primary_supported`。
SEAL外层明确采用ReST-EM式过滤行为克隆：当前策略采样自编辑，经内层适应后的任务表现形成二元奖励，仅对成功自编辑执行外层SFT。

**关系边界**：复用的端点仅是采样—成功过滤—SFT训练程序。SEAL优化自编辑的可学习性，奖励依赖内层适应后的模型；ReST-EM直接生成题目答案，并在各Improve轮从base重训。不能把后者的base重置、人类输出处理、math/code实验及EM单调保证自动迁移到SEAL。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2506.10943v2；版本：v2；定位：S3.SS1.p1.1；S3.SS1.p3.1；S3.SS1.p4.1；S3.SS1.p5.1；S3.SS1.p6.2。
- object：https://arxiv.org/html/2312.06585v4；版本：v4；定位：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p4.1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_restem` · ReST-EM · v4
  - https://arxiv.org/html/2312.06585v4；阅读深度：`未单列`。
- `expand_src_w_seal` · SEAL · v2
  - https://arxiv.org/html/2506.10943v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f87820e7aeedf3c20a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
