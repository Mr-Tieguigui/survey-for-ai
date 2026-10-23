# Self-Evolving Coding Rules for AI Coding Agents

> 方法论文 · 2026 · `wf_8015bdf396efb2c662`

**作者**：Zhengyuan Jiang, Reachal Wang, Yuepeng Hu, Yupu Wang, Yuqi Jia, Neil Zhenqiang Gong  
**原文**：https://arxiv.org/abs/2610.00650  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：AGENTS.md规则池与分配统计；具体更新过程为：固定mutator将规则作为被改对象，judge执行任务代码；历史统计调整变异份额；更新状态的保留与后继使用为：跨规则池迭代。

## 2. 论文的核心内容与贡献

### configuration:cfg_ruleevolve
当前证据是外部规则优化；被改规则是否支配mutator/judge而非仅目标编码代理未建立；保持原adjacent，不因题名升核心

**适用版本**：v1；**原文定位**：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_ruleevolve
`cfg_ruleevolve` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | AGENTS.md规则池与分配统计 |
| 改进过程与下一轮参与 | 固定mutator将规则作为被改对象，judge执行任务代码；历史统计调整变异份额 |
| 保留的状态及时间尺度 | 跨规则池迭代 |
| 外部固定部分 | 模型参数、变异指令、judge与分配公式 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：AGENTS.md规则池与分配统计（状态：`supported`；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3）。
- **更新由什么过程产生**：固定mutator将规则作为被改对象，judge执行任务代码；历史统计调整变异份额（状态：`supported`；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3）。
- **状态怎样持久保留**：跨规则池迭代（状态：`supported`；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3）。
- **更新怎样进入后续改进**：当前证据是外部规则优化；被改规则是否支配mutator/judge而非仅目标编码代理未建立；保持原adjacent，不因题名升核心（状态：`unknown`；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3）。

**配置判定**：当前证据是外部规则优化；被改规则是否支配mutator/judge而非仅目标编码代理未建立；保持原adjacent，不因题名升核心

来源：https://arxiv.org/html/2610.00650v1；版本：v1；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_ruleevolve`**：固定mutator将规则作为被改对象，judge执行任务代码；历史统计调整变异份额
  - 来源版本：v1；定位：S3.SS1.p1；S4.SS1.p1；S4.SS2.p1；S4.SS2.p5；S4.SS3.p2；S4.SS3.p3；深度：`AI_primary_method_passage_recheck`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 当
- 前
- 证
- 据
- 是
- 外
- 部
- 规
- 则
- 优
- 化
- ；
- 被
- 改
- 否
- 支
- 配
- m
- u
- t
- a
- o
- r
- /
- j
- d
- g
- e
- 而
- 非
- 仅
- 目
- 标
- 编
- 码
- 代
- 理
- 未
- 建
- 立
- 保
- 持
- 原
- c
- n
- ，
- 不
- 因
- 题
- 名
- 升
- 核
- 心

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_ruleevolve` · RuleEvolve · v1
  - https://arxiv.org/html/2610.00650v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8015bdf396efb2c662 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
