# Recursive self-improvement of AI research agents

> 方法论文 · 2026 · `wf_59d41d27ae673fd141`

**作者**：Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zhengyao Jiang  
**原文**：https://arxiv.org/abs/2609.26457  
**研究分支**：科研代理、实验与发现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：接受的incumbent代码；具体更新过程为：内层候选选择可编辑；主发现轨迹外层未换成后继代理；更新状态的保留与后继使用为：固定外层继续修改内层incumbent。

## 2. 论文的核心内容与贡献

### configuration:cfg_aide2
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v1；**原文定位**：Section 2.1 outer loop。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_aide2_ignition
Ignition comparison probes second-order behavior; do not replace the main outer-loop configuration with this probe.

**适用版本**：v1；**原文定位**：Section 3.6。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_aide2
`cfg_aide2` · main_experiment

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 接受的incumbent代码。 |
| 改进过程与下一轮参与 | 内层候选选择可编辑；主发现轨迹外层未换成后继代理。 |
| 保留的状态及时间尺度 | 固定外层继续修改内层incumbent。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/html/2609.26457v1；版本：v1；定位：Section 2.1 outer loop。

### cfg_aide2_ignition
`cfg_aide2_ignition` · evaluation_probe

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 各arm自己的候选与incumbent。 |
| 改进过程与下一轮参与 | 比较AIDE_47与AIDE_human作外层；不是持续自动晋升。 |
| 保留的状态及时间尺度 | 每个arm的外层代理保持指定身份。 |

**配置判定**：Ignition comparison probes second-order behavior; do not replace the main outer-loop configuration with this probe.

来源：https://arxiv.org/html/2609.26457v1；版本：v1；定位：Section 3.6。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_aide2`**：内层代码与候选选择可编辑，主轨迹外层AIDE_human及argmax固定。
  - 来源版本：v1；定位：S2.SS1.p3；S2.SS1.p4；S2.SS2.p2；深度：`AI_rechecked_primary_text_author_report`。

- **`e_aide2_lineage`**：AIDE₀从AIDE重构，去掉ML专用组件并保留树搜索。
  - 来源版本：v1；定位：S2.SS2.p1；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 点火探测不能混作主轨迹持续晋升
- 来源为作者明确说明，不证明完整代码相同

## 7. 与其他论文的具体关系

### [AIDE: AI-Driven Exploration in the Space of Code](../r03_method/wf_bc4a082767b6da7c5d.md)
关系：`refactors_implementation_of` · `r_aide2_aide` · 当前展示权限：`primary_supported`。
AIDE²作者明确称初始内环代理AIDE0是AIDE的精简重构：移除ML专用机制但保留树搜索与draft/debug/improve操作，外环重写内环代理。AIDE原文的方案树、搜索策略、代码与摘要算子提供被保留组件的双端依据。

**关系边界**：重构关系具体属于AIDE²初始内环AIDE0；AIDE_human是另一个人为研发基线/外环代理，不与原始AIDE混同；主运行固定每环模型且外环更强，不能声称两个循环均无人工固定组件。

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2609.26457v1（v1；S2.SS2.p1.1；S2.SS2.p2.1）；https://arxiv.org/html/2502.13138v1（v1；S3.SS1.p1.1；S3.SS2.SSS0.Px1.p1.1）。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_aide2` · 已存来源 · v1
  - https://arxiv.org/html/2609.26457v1；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_59d41d27ae673fd141 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
