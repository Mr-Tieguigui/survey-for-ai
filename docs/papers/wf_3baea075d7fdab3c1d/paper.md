# Learning to learn by gradient descent by gradient descent

> 方法论文 · 2016 · `wf_3baea075d7fdab3c1d`

**作者**：Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W. Hoffman, David Pfau, Tom Schaul, Brendan Shillingford, Nando de Freitas  
**原文**：https://arxiv.org/abs/1606.04474  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：优化器phi的外层训练及目标模型theta；具体更新过程为：phi由外部梯度下降训练；学得LSTM输出目标参数更新；更新状态的保留与后继使用为：跨训练任务的学得phi；h是内层轨迹状态。

## 2. 论文的核心内容与贡献

### configuration:cfg_learned_optimizer
本配置是学习优化器参数；不能证明学得优化器更新自身phi；内层h状态须单列研究

**适用版本**：v2；**原文定位**：S2.SS1.p3；S2.p1；S2.p2。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_learned_optimizer
`cfg_learned_optimizer` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 优化器phi的外层训练及目标模型theta |
| 改进过程与下一轮参与 | phi由外部梯度下降训练；学得LSTM输出目标参数更新 |
| 保留的状态及时间尺度 | 跨训练任务的学得phi；h是内层轨迹状态 |
| 外部固定部分 | 训练phi的梯度下降及BPTT |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：优化器phi的外层训练及目标模型theta（状态：`supported`；定位：S2.p1；S2.p2；S2.SS1.p3）。
- **更新由什么过程产生**：phi由外部梯度下降训练；学得LSTM输出目标参数更新（状态：`supported`；定位：S2.p1；S2.p2；S2.SS1.p3）。
- **状态怎样持久保留**：跨训练任务的学得phi；h是内层轨迹状态（状态：`supported`；定位：S2.p1；S2.p2；S2.SS1.p3）。
- **更新怎样进入后续改进**：本配置是学习优化器参数；不能证明学得优化器更新自身phi；内层h状态须单列研究（状态：`contradicted`；定位：S2.p1；S2.p2；S2.SS1.p3）。

**配置判定**：本配置是学习优化器参数；不能证明学得优化器更新自身phi；内层h状态须单列研究

来源：https://arxiv.org/html/1606.04474v2；版本：v2；定位：S2.SS1.p3；S2.p1；S2.p2。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_learned_optimizer`**：phi由外部梯度下降训练；学得LSTM输出目标参数更新
  - 来源版本：v2；定位：S2.p1；S2.p2；S2.SS1.p3；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本
- 配
- 置
- 是
- 学
- 习
- 优
- 化
- 器
- 参
- 数
- ；
- 不
- 能
- 证
- 明
- 得
- 更
- 新
- 自
- 身
- p
- h
- i
- 内
- 层
- 状
- 态
- 须
- 单
- 列
- 研
- 究

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_learned_optimizer` · Learning to Learn · v2
  - https://arxiv.org/html/1606.04474v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3baea075d7fdab3c1d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
