# AFlow: Automating Agentic Workflow Generation

> 方法论文 · 2024 · `wf_aa4728a57c94677a3d`

**作者**：Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, Chenglin Wu  
**原文**：https://arxiv.org/html/2410.10762v1  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Configuration-specific structural and empirical boundary review; no universal RSI, autonomous researcher, or independent replication certification.

## 2. 论文的核心内容与贡献

### configuration:cfg_aflow_code_workflow_mcts_v1
在工作流与搜索经验边界内持续改进；实际实验搜索空间是声明完整形式空间的受约束子集。

**适用版本**：2410.10762v1；**原文定位**：§3.2 tool L147–167；§4 Algorithm1 and detail tool L168–213；§5.1 tool L215–221。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### aflow code workflow mcts v1
`cfg_aflow_code_workflow_mcts_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 工作流代码、提示、候选搜索树和父节点修改经验；优化LLM与executor权重固定。 |
| 改进过程与下一轮参与 | 软混合选择父工作流，LLM编辑提示与连接代码，执行验证集多次评分并回传修改/成败经验，供下一轮搜索。 |
| 保留的状态及时间尺度 | 候选代码与树经验跨搜索步骤保留，选定工作流应用到测试例。 |
| 外部固定部分 | - 模型/温度/输出格式固定的实际搜索设定、operator集、外部评价函数、数据划分、树选择与停止规则 |

**配置判定**：在工作流与搜索经验边界内持续改进；实际实验搜索空间是声明完整形式空间的受约束子集。

来源：https://arxiv.org/html/2410.10762v1；版本：2410.10762v1；定位：§3.2 tool L147–167；§4 Algorithm1 and detail tool L168–213；§5.1 tool L215–221。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`found4_ev_cfg_aflow_code_workflow_mcts_v1`**：在工作流与搜索经验边界内持续改进；实际实验搜索空间是声明完整形式空间的受约束子集。
  - 来源版本：unknown；定位：§3.2 tool L147–167；§4 Algorithm1 and detail tool L168–213；§5.1 tool L215–221；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 节点模型M、温度、输出格式在实做中固定；不将形式上完整搜索空间当实际穷尽。
- 5次验证评分/20搜索轮/固定operator由研究者配置，优化器和MCTS控制不自改。
- 报告的不同基线预算与模型绑定不能外推普遍性能排序。
- 节点模型M、温度、输出格式在实做中固定；不将形式上完整搜索空间当实际穷尽。; 5次验证评分/20搜索轮/固定operator由研究者配置，优化器和MCTS控制不自改。; 报告的不同基线预算与模型绑定不能外推普遍性能排序。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `found4_src_aflow` · 已存来源 · 2410.10762v1
  - https://arxiv.org/html/2410.10762v1；阅读深度：`selected_official_fulltext_method_passages`。

**证据深度**：selected_official_fulltext_method_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_aa4728a57c94677a3d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
