# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

> 方法论文 · 2025 · `wf_c1ef72d96fa3292590`

**作者**：Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab  
**原文**：https://arxiv.org/abs/2507.19457  
**研究分支**：提示与程序化优化  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：复合系统任务提示与固定reflection meta-prompt；具体更新过程为：AppendixC确认改写的是任务assistant instruction，当前指令/任务轨迹/反馈作为固定reflection提示输入；更新状态的保留与后继使用为：跨候选优化轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_gepa
更正条件4：原待定理由额外要求改进执行者本身改变，强于既有协议。固定reflection meta-prompt和LM不自改；本结论为完整优化回路边界内的执行反馈参与，不认证改进器能力增长。

**适用版本**：v2；**原文定位**：A3.p1；S3.p1；S3.p2；S3.p3；S3.p4。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_gepa
`cfg_gepa` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 复合系统任务提示与固定reflection meta-prompt |
| 改进过程与下一轮参与 | AppendixC确认改写的是任务assistant instruction，当前指令/任务轨迹/反馈作为固定reflection提示输入 |
| 保留的状态及时间尺度 | 跨候选优化轮次 |
| 外部固定部分 | reflection meta-prompt、模型权重、Pareto规则 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：复合系统任务提示与固定reflection meta-prompt（状态：`supported`；定位：S3.p1；S3.p4；A3.p1）。
- **更新由什么过程产生**：AppendixC确认改写的是任务assistant instruction，当前指令/任务轨迹/反馈作为固定reflection提示输入（状态：`supported`；定位：S3.p1；S3.p4；A3.p1）。
- **状态怎样持久保留**：跨候选优化轮次（状态：`supported`；定位：S3.p1；S3.p4；A3.p1）。
- **更新怎样进入后续改进**：保留的候选提示实际执行生成模块输入/输出、推理和诊断反馈；这些信号与当前提示一起进入固定反思LM，提案获接受后进入候选池并可参与下一轮。（状态：`supported`；定位：S3.p1；S3.p2；S3.p3；S3.p4；A3.p1）。

**配置判定**：更正条件4：原待定理由额外要求改进执行者本身改变，强于既有协议。固定reflection meta-prompt和LM不自改；本结论为完整优化回路边界内的执行反馈参与，不认证改进器能力增长。

来源：https://arxiv.org/html/2507.19457v2；版本：v2；定位：A3.p1；S3.p1；S3.p2；S3.p3；S3.p4。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_gepa`**：候选运行轨迹和反馈用于修订提示，池和父选择保留；reflection meta-prompt是否被更新未建立
  - 来源版本：v2；定位：S3.p1；S3.p2；S3.p3；S3.p4；S3.SS1.p1；S6.p1；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_gepa`**：AppendixC确认改写的是任务assistant instruction，当前指令/任务轨迹/反馈作为固定reflection提示输入
  - 来源版本：v2；定位：S3.p1；S3.p4；A3.p1；深度：`未单列`。

- **`e4_cfg_gepa`**：保留的候选提示实际执行生成模块输入/输出、推理和诊断反馈；这些信号与当前提示一起进入固定反思LM，提案获接受后进入候选池并可参与下一轮。
  - 来源版本：v2；定位：S3.p1；S3.p2；S3.p3；S3.p4；A3.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 提
- 示
- 收
- 益
- 和
- 诊
- 断
- 轨
- 迹
- 有
- 报
- 告
- ；
- 更
- 新
- 的
- 目
- 标
- 是
- 否
- 支
- 配
- 改
- 进
- 算
- 子
- 尚
- 未
- 闭
- 合
- ，
- 条
- 件
- 4
- 保
- 留
- 知
- 实
- 际
- 执
- 行
- 及
- 反
- 馈
- 已
- 核
- 固
- 定
- 思
- 器
- 满
- 足
- 项
- 所
- 需
- 者
- 参
- 与
- 仍
- 界
- 不
- 仅
- 因
- 迭
- 代
- 或
- 题
- 升
- 心
- 正
- ：
- 原
- 待
- 理
- 由
- 额
- 外
- 要
- 求
- 本
- 身
- 变
- 强
- 于
- 既
- 协
- 议
- 。
- r
- e
- f
- l
- c
- t
- i
- o
- n
- 
- m
- a
- -
- p
- L
- M
- 自
- 结
- 论
- 为
- 完
- 整
- 优
- 化
- 回
- 路
- 边
- 内
- 认
- 证
- 能
- 力
- 增
- 长

## 7. 与其他论文的具体关系

### [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](../r03_method/wf_title_85954f3817cf3610.md)
关系：`contrasts_system_boundary_with` · `r2_gepa_promptbreeder_6` · 当前展示权限：`primary_supported`。
GEPA用固定反思模板处理候选执行轨迹/文字反馈并改写模块指令；Promptbreeder共同演化任务提示及其变异提示。

**关系边界**：GEPA确有相关工作引用，机制对照由整理者双端核查得出；引用不证明派生、共用代码或等预算优越。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2507.19457v2；版本：v2；定位：S3.p4；S6.p1。
- object：https://arxiv.org/html/2309.16797v1；版本：v1；定位：S3.p3；S3.p4；S3.p5；S3.SS2.SSS3.p3。
- expand_src_w_gepa：https://arxiv.org/html/2507.19457v2；版本：v2；定位：S3.p1；S3.p2；S3.p3；S3.p4；S3.SS1.p1；S6.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_gepa` · GEPA · v2
  - https://arxiv.org/html/2507.19457v2；阅读深度：`未单列`。
- `src_20261013_w_gepa` · 已存来源 · v2
  - https://arxiv.org/html/2507.19457v2；阅读深度：`未单列`。
- `stage1_src_w_gepa` · 已存来源 · v2
  - https://arxiv.org/html/2507.19457v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c1ef72d96fa3292590 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
