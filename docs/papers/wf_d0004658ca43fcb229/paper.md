# TextGrad: Automatic "Differentiation" via Text

> 方法论文 · 2024 · `wf_d0004658ca43fcb229`

**作者**：Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou  
**原文**：https://arxiv.org/abs/2406.07496  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：原混合实例/提示优化记录；具体更新过程为：实例解和跨查询提示是不同优化变量；momentum是可选读取旧变量机制；更新状态的保留与后继使用为：实例内或跨查询，必须拆分。

## 2. 论文的核心内容与贡献

### configuration:cfg_textgrad_instance
只优化给定实例的代码/答案/分子；不认证跨输出系统自改

**适用版本**：v1；**原文定位**：S2.SSx4.p2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_textgrad_prompt
更正条件4：保留提示通过真实执行影响下一轮诊断，不要求固定TGD指令改写。实例优化仍是另一个adjacent子配置；gpt-4o反馈与gpt-3.5前向模型不可写成同模型自主闭环。

**适用版本**：v1；**原文定位**：S2.SSx1.SSS0.Px2.pic1.p2；S2.SSx1.SSS0.Px3.pic2.p1；S2.SSx4.p3；S3.SS3.p2；S3.SS3.p5；S3.SS3.p7。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_textgrad
`cfg_textgrad` · scope_index

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 原混合实例/提示优化记录 |
| 改进过程与下一轮参与 | 实例解和跨查询提示是不同优化变量；momentum是可选读取旧变量机制 |
| 保留的状态及时间尺度 | 实例内或跨查询，必须拆分 |
| 外部固定部分 | TGD、图反馈程序、LM及约束 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。（状态：`unknown`；定位：§2 Instance vs Prompt Optimization tool L146–170）。
- **更新由什么过程产生**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。（状态：`unknown`；定位：§2 Instance vs Prompt Optimization tool L146–170）。
- **状态怎样持久保留**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。（状态：`unknown`；定位：§2 Instance vs Prompt Optimization tool L146–170）。
- **更新怎样进入后续改进**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。（状态：`unknown`；定位：§2 Instance vs Prompt Optimization tool L146–170）。

**配置判定**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。

来源：https://arxiv.org/html/2406.07496v1；版本：2406.07496v1；定位：§2 Instance vs Prompt Optimization tool L146–170。

### cfg_textgrad_instance
`cfg_textgrad_instance` · split_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 单个解变量优化 |

**配置判定**：只优化给定实例的代码/答案/分子；不认证跨输出系统自改

来源：https://arxiv.org/html/2406.07496v1；版本：v1；定位：S2.SSx4.p2。

### cfg_textgrad_prompt
`cfg_textgrad_prompt` · split_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 跨查询任务提示优化 |

**反馈闭环如何成立（按配置核查）**：
- **更新怎样进入后续改进**：跨查询持久Prompt进入当前小批量forward，答案与评价产生反馈，TGD结合当前变量和反馈更新Prompt，验证后的提示参与后续小批量forward和反馈生成。（状态：`supported`；定位：S2.SSx1.SSS0.Px2.pic1.p2；S2.SSx1.SSS0.Px3.pic2.p1；S2.SSx4.p3；S3.SS3.p2；S3.SS3.p5；S3.SS3.p7）。

**配置判定**：更正条件4：保留提示通过真实执行影响下一轮诊断，不要求固定TGD指令改写。实例优化仍是另一个adjacent子配置；gpt-4o反馈与gpt-3.5前向模型不可写成同模型自主闭环。

来源：https://arxiv.org/html/2406.07496v1；版本：v1；定位：S2.SSx1.SSS0.Px2.pic1.p2；S2.SSx1.SSS0.Px3.pic2.p1；S2.SSx4.p3；S3.SS3.p2；S3.SS3.p5；S3.SS3.p7。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_textgrad`**：原文明确分实例优化与跨查询提示优化；混合父记录仅作为索引，四条件分别读取已建子配置。
  - 来源版本：2406.07496v1；定位：§2 Instance vs Prompt Optimization tool L146–170；深度：`未单列`。

- **`e2_w_textgrad`**：实例优化只修改当前解；提示优化跨查询学习；可选momentum读取旧变量
  - 来源版本：v1；定位：S2.SSx4.p2；S2.SSx4.p3；S2.SSx5.p2；S2.SSx5.p4；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_textgrad`**：实例解和跨查询提示是不同优化变量；momentum是可选读取旧变量机制
  - 来源版本：v1；定位：S2.SSx2.p1；S2.SSx2.p2；S2.SSx4.p2；S2.SSx4.p3；S2.SSx5.p4；深度：`未单列`。

- **`e4_cfg_textgrad_prompt`**：跨查询持久Prompt进入当前小批量forward，答案与评价产生反馈，TGD结合当前变量和反馈更新Prompt，验证后的提示参与后续小批量forward和反馈生成。
  - 来源版本：v1；定位：S2.SSx1.SSS0.Px2.pic1.p2；S2.SSx1.SSS0.Px3.pic2.p1；S2.SSx4.p3；S3.SS3.p2；S3.SS3.p5；S3.SS3.p7；深度：`未单列`。

- **`e4_cfg_textgrad`**：实例优化和跨查询Prompt优化具有不同保留尺度；本轮Prompt子配置已闭合反馈，实例子配置维持adjacent。
  - 来源版本：v1；定位：S2.SSx4.p3；S3.SS3.p5；S3.SS3.p7；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 本索引不是一个额外实验臂，不给混合单位强加单一C4。
- 原
- 配
- 置
- 必
- 须
- 拆
- 分
- ，
- 实
- 例
- 路
- 线
- a
- d
- j
- c
- e
- n
- t
- ；
- 提
- 示
- 的
- 改
- 进
- 机
- 制
- 参
- 与
- 仍
- 待
- 核
- 不
- 能
- 整
- 篇
- 统
- 一
- 升
- 心
- 优
- 化
- 子
- 可
- 判
- p
- r
- o
- m
- 执
- 行
- 者
- 未
- 知
- 混
- 在
- 父
- 记
- 录
- 中
- 强
- 定
- 案
- 更
- 正
- 条
- 件
- 4
- ：
- 保
- 留
- 通
- 过
- 真
- 影
- 响
- 下
- 轮
- 诊
- 断
- 要
- 求
- 固
- T
- G
- D
- 指
- 令
- 写
- 。
- 是
- 另
- 个
- g
- -
- 反
- 馈
- 3
- .
- 5
- 前
- 向
- 模
- 型
- 成
- 同
- 自
- 主
- 闭
- 环
- 作
- 为
- 合
- 入
- 口
- i
- 剩
- 余
- 问
- 题
- 单
- 位
- 而
- 非
- P
- 方
- 法
- 读
- 把
- 范
- 围
- 传
- 播
- 至
- 所
- 有

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_textgrad` · TextGrad · v1
  - https://arxiv.org/html/2406.07496v1；阅读深度：`未单列`。
- `r7root_src_textgrad_scope` · 已存来源 · 2406.07496v1
  - https://arxiv.org/html/2406.07496v1；阅读深度：`未单列`。
- `src_20261013_w_textgrad` · 已存来源 · v1
  - https://arxiv.org/html/2406.07496v1；阅读深度：`未单列`。
- `stage1_src_w_textgrad` · 已存来源 · v1
  - https://arxiv.org/html/2406.07496v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_d0004658ca43fcb229 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
