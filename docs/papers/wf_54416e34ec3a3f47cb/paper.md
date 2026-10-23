# Self-Discover: Large Language Models Self-Compose Reasoning Structures

> 方法论文 · 2024 · `wf_54416e34ec3a3f47cb`

**作者**：Pei Zhou, Jay Pujara, Xiang Ren, Xinyun Chen, Heng-Tze Cheng, Quoc V. Le, Ed H. Chi, Denny Zhou, Swaroop Mishra, Huaixiu Steven Zheng  
**原文**：https://arxiv.org/abs/2402.03620  
**研究分支**：推理与输出修订  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：任务专用SELECT/ADAPT/IMPLEMENT推理结构；具体更新过程为：产生一次任务结构后附到各任务实例用于回答；所述Stage2没有继续更新结构的回路；更新状态的保留与后继使用为：同一任务的多个实例。

## 2. 论文的核心内容与贡献

### configuration:cfg_self_discover
结构跨实例保留已支持；后续结构改进回路在该配置中未执行，不能由任务泛化或跨模型复用推出RSI

**适用版本**：v1；**原文定位**：S2.SS1.p1；S2.SS2.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_self_discover
`cfg_self_discover` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 任务专用SELECT/ADAPT/IMPLEMENT推理结构 |
| 改进过程与下一轮参与 | 产生一次任务结构后附到各任务实例用于回答；所述Stage2没有继续更新结构的回路 |
| 保留的状态及时间尺度 | 同一任务的多个实例 |
| 外部固定部分 | 基础LM、三动作及固定模块集合 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：任务专用SELECT/ADAPT/IMPLEMENT推理结构（状态：`supported`；定位：S2.SS1.p1；S2.SS2.p1）。
- **更新由什么过程产生**：产生一次任务结构后附到各任务实例用于回答；所述Stage2没有继续更新结构的回路（状态：`supported`；定位：S2.SS1.p1；S2.SS2.p1）。
- **状态怎样持久保留**：同一任务的多个实例（状态：`supported`；定位：S2.SS1.p1；S2.SS2.p1）。
- **更新怎样进入后续改进**：结构跨实例保留已支持；后续结构改进回路在该配置中未执行，不能由任务泛化或跨模型复用推出RSI（状态：`contradicted`；定位：S2.SS1.p1；S2.SS2.p1）。

**配置判定**：结构跨实例保留已支持；后续结构改进回路在该配置中未执行，不能由任务泛化或跨模型复用推出RSI

来源：https://arxiv.org/html/2402.03620v1；版本：v1；定位：S2.SS1.p1；S2.SS2.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e3_w_self_discover`**：产生一次任务结构后附到各任务实例用于回答；所述Stage2没有继续更新结构的回路
  - 来源版本：v1；定位：S2.SS1.p1；S2.SS2.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 结
- 构
- 跨
- 实
- 例
- 保
- 留
- 已
- 支
- 持
- ；
- 后
- 续
- 改
- 进
- 回
- 路
- 在
- 该
- 配
- 置
- 中
- 未
- 执
- 行
- ，
- 不
- 能
- 由
- 任
- 务
- 泛
- 化
- 或
- 模
- 型
- 复
- 用
- 推
- 出
- R
- S
- I

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `stage1_src_w_self_discover` · 已存来源 · v1
  - https://arxiv.org/html/2402.03620v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_54416e34ec3a3f47cb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
