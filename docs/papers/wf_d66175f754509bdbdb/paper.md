# AutoML-Zero: Evolving Machine Learning Algorithms From Scratch

> 方法论文 · 2020 · `wf_d66175f754509bdbdb`

**作者**：Esteban Real, Chen Liang, David R. So, Quoc V. Le  
**原文**：https://arxiv.org/abs/2003.03384  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Setup/Predict/Learn候选算法人口；具体更新过程为：固定锦标赛和随机变异更新候选；候选Learn更新的是目标模型，不是搜索自身；更新状态的保留与后继使用为：跨搜索代；内部虚拟内存在单次算法评价保留。

## 2. 论文的核心内容与贡献

### configuration:cfg_automl_zero
AutoML-Zero §3.2 explicitly retains mutated child algorithms in the population; later tournaments sample this changed population and mutate the selected current parent. Condition4 supported within bounded population-search state feedback. Fixed tournament/mutation rules do not invalidate the condition; no self-rewrite of outer evolution or unbounded improvement is certified.

**适用版本**：v2；**原文定位**：S3.SS1.p2；S3.SS2.p1；S3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_automl_zero
`cfg_automl_zero` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Setup/Predict/Learn候选算法人口 |
| 改进过程与下一轮参与 | 固定锦标赛和随机变异更新候选；候选Learn更新的是目标模型，不是搜索自身 |
| 保留的状态及时间尺度 | 跨搜索代；内部虚拟内存在单次算法评价保留 |
| 外部固定部分 | regularized evolution、变异动作、任务评价 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Setup/Predict/Learn候选算法人口（状态：`supported`；定位：S3.p1；S3.SS1.p2；S3.SS2.p1）。
- **更新由什么过程产生**：固定锦标赛和随机变异更新候选；候选Learn更新的是目标模型，不是搜索自身（状态：`supported`；定位：S3.p1；S3.SS1.p2；S3.SS2.p1）。
- **状态怎样持久保留**：跨搜索代；内部虚拟内存在单次算法评价保留（状态：`supported`；定位：S3.p1；S3.SS1.p2；S3.SS2.p1）。
- **更新怎样进入后续改进**：Copied and mutated child enters P while oldest exits; subsequent tournament selection chooses parent from updated P, so changed program state is consumed by later search.（状态：`supported`；定位：S3.SS2.p1）。

**配置判定**：AutoML-Zero §3.2 explicitly retains mutated child algorithms in the population; later tournaments sample this changed population and mutate the selected current parent. Condition4 supported within bounded population-search state feedback. Fixed tournament/mutation rules do not invalidate the condition; no self-rewrite of outer evolution or unbounded improvement is certified.

来源：https://arxiv.org/html/2003.03384v2；版本：v2；定位：S3.SS1.p2；S3.SS2.p1；S3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_automl_zero`**：固定锦标赛和随机变异更新候选；候选Learn更新的是目标模型，不是搜索自身
  - 来源版本：v2；定位：S3.p1；S3.SS1.p2；S3.SS2.p1；深度：`AI_primary_method_passage_recheck`。

- **`r4training_ev_automlzero_condition4_revision`**：AutoML-Zero §3.2 explicitly retains mutated child algorithms in the population; later tournaments sample this changed population and mutate the selected current parent. Condition4 supported within bounded population-search state feedback. Fixed tournament/mutation rules do not invalidate the condition; no self-rewrite of outer evolution or unbounded improvement is certified.
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 优
- 化
- 算
- 法
- 程
- 序
- 不
- 等
- 于
- 候
- 选
- 能
- 够
- 改
- 进
- 外
- 部
- 搜
- 索
- 控
- 制
- 器
- ；
- 内
- 存
- 保
- 留
- 尺
- 度
- 混
- 入
- 子
- 自
- Only declared population-search structural condition corrected; no claim that learned candidate rewrites top-level evolution, no improver gain theorem.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_automl_zero` · AutoML-Zero · v2
  - https://arxiv.org/html/2003.03384v2；阅读深度：`未单列`。
- `r4training_src_w_automl_zero` · 已存来源 · 2003.03384v2
  - https://arxiv.org/html/2003.03384v2；阅读深度：`selected_original_method_passages`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d66175f754509bdbdb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
