# Reinforced Self-Training (ReST) for Language Modeling

> 方法论文 · 2023 · `wf_bd90935154aa7b75e6`

**作者**：Caglar Gulcehre, Tom Le Paine, Srivatsan Srinivasan, Ksenia Konyushkova, Lotte Weerts, Abhishek Sharma, Aditya Siddhant, Alex Ahern, Miaosen Wang, Chenjie Gu, Wolfgang Macherey, Arnaud Doucet, Orhan Firat, Nando de Freitas  
**原文**：https://arxiv.org/abs/2308.08998  
**研究分支**：偏好、自奖励与对齐训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：当前生成策略与奖励过滤轨迹；具体更新过程为：Grow从当前策略采样，Improve微调当前最好策略，再以更新策略Grow新数据；更新状态的保留与后继使用为：跨Grow/Improve轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_rest
与ReST-EM从base重训的选择不同；不能自动转换为无外部奖励、无原始任务输入

**适用版本**：v2；**原文定位**：S3.p2.1；S3.p3.1；S3.SS0.SSSx1.p1.1；S3.SS0.SSSx2.p2.1；S3.SS0.SSSx2.p4.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_rest
`cfg_rest` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前生成策略与奖励过滤轨迹 |
| 改进过程与下一轮参与 | Grow从当前策略采样，Improve微调当前最好策略，再以更新策略Grow新数据 |
| 保留的状态及时间尺度 | 跨Grow/Improve轮次 |
| 外部固定部分 | 奖励函数、阈值、原始输入数据和训练损失 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：当前生成策略与奖励过滤轨迹（状态：`supported`；定位：S3.SS0.SSSx1.p1；S3.SS0.SSSx2.p1；S3.SS0.SSSx2.p2）。
- **更新由什么过程产生**：Grow从当前策略采样，Improve微调当前最好策略，再以更新策略Grow新数据（状态：`supported`；定位：S3.SS0.SSSx1.p1；S3.SS0.SSSx2.p1；S3.SS0.SSSx2.p2）。
- **状态怎样持久保留**：跨Grow/Improve轮次（状态：`supported`；定位：S3.SS0.SSSx1.p1；S3.SS0.SSSx2.p1；S3.SS0.SSSx2.p2）。
- **更新怎样进入后续改进**：Grow从当前策略采样，Improve微调当前最好策略，再以更新策略Grow新数据（状态：`supported`；定位：S3.SS0.SSSx1.p1；S3.SS0.SSSx2.p1；S3.SS0.SSSx2.p2）。

**配置判定**：与ReST-EM从base重训的选择不同；不能自动转换为无外部奖励、无原始任务输入

来源：https://arxiv.org/html/2308.08998v2；版本：v2；定位：S3.p2.1；S3.p3.1；S3.SS0.SSSx1.p1.1；S3.SS0.SSSx2.p2.1；S3.SS0.SSSx2.p4.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e3_w_rest`**：Grow从当前策略采样，Improve微调当前最好策略，再以更新策略Grow新数据
  - 来源版本：v2；定位：S3.SS0.SSSx1.p1；S3.SS0.SSSx2.p1；S3.SS0.SSSx2.p2；深度：`未单列`。

- **`e3_training_r2_restem_rest_3`**：ReST-EM作者明确将其定义为ReST的简化训练版本；保留当前策略生成与过滤微调，并把主要实验改为二元奖励、每轮一次Improve、从base重训且不混入人类生成输出。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 保留原始输出数据混合；递增阈值执行多个Improve。
- 连续微调前一策略，不采用ReST-EM每轮base重置。
- 与
- R
- e
- S
- T
- -
- E
- M
- 从
- b
- a
- s
- 重
- 训
- 的
- 选
- 择
- 不
- 同
- ；
- 能
- 自
- 动
- 转
- 换
- 为
- 无
- 外
- 部
- 奖
- 励
- 、
- 原
- 始
- 任
- 务
- 输
- 入
- ReST原配置在数据混合中保留原始人类输出，连续微调当前最优策略，并对同一Grow数据递增奖励阈值执行多次Improve；ReST-EM依然使用原始任务输入和正确答案/测试奖励，不能表述为完全摆脱人类信息。两者方法继承不代表原实验结论及保证继承。

## 7. 与其他论文的具体关系

### [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](../r03_method/wf_8c342e08652d44c7d7.md)
关系：`modifies_component_of` · `r2_restem_rest_3` · 当前展示权限：`primary_supported`。
ReST-EM作者明确将其定义为ReST的简化训练版本；保留当前策略生成与过滤微调，并把主要实验改为二元奖励、每轮一次Improve、从base重训且不混入人类生成输出。

**关系边界**：ReST原配置在数据混合中保留原始人类输出，连续微调当前最优策略，并对同一Grow数据递增奖励阈值执行多次Improve；ReST-EM依然使用原始任务输入和正确答案/测试奖励，不能表述为完全摆脱人类信息。两者方法继承不代表原实验结论及保证继承。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2312.06585v4；版本：v4；定位：S3.SS0.SSS0.Px2.p1.1；S3.I2.i1.p1.1；S3.I2.i2.p1.1；S3.SS0.SSS0.Px2.p3.1；S3.SS0.SSS0.Px2.p4.1。
- object：https://arxiv.org/html/2308.08998v2；版本：v2；定位：S3.p2.1；S3.p3.1；S3.SS0.SSSx1.p1.1；S3.SS0.SSSx2.p2.1；S3.SS0.SSSx2.p4.1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_restem` · ReST-EM · v4
  - https://arxiv.org/html/2312.06585v4；阅读深度：`未单列`。
- `stage1_src_w_rest` · 已存来源 · v2
  - https://arxiv.org/html/2308.08998v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bd90935154aa7b75e6 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
