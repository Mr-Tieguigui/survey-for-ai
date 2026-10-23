# AIDE: AI-Driven Exploration in the Space of Code

> 方法论文 · 2025 · `wf_bc4a082767b6da7c5d`

**作者**：Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, Yuxiang Wu  
**原文**：https://arxiv.org/abs/2502.13138  
**研究分支**：科研代理、实验与发现  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：代码解树T与摘要Sigma(T)作为改进者的持久上下文；具体更新过程为：执行记录/指标/调参/报错被摘要，实际输入后续coding operator；搜索策略固定；更新状态的保留与后继使用为：跨完整代码实验提案。

## 2. 论文的核心内容与贡献

### configuration:cfg_aide
本项目宽操作性定义下的历史上下文反馈核心；不是coding/search operator代码自改或研究者能力收益认证

**适用版本**：v1；**原文定位**：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_aide
`cfg_aide` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 代码解树T与摘要Sigma(T)作为改进者的持久上下文 |
| 改进过程与下一轮参与 | 执行记录/指标/调参/报错被摘要，实际输入后续coding operator；搜索策略固定 |
| 保留的状态及时间尺度 | 跨完整代码实验提案 |
| 外部固定部分 | 固定search policy、LLM及专用coding prompts |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：代码解树T与摘要Sigma(T)作为改进者的持久上下文（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1）。
- **更新由什么过程产生**：执行记录/指标/调参/报错被摘要，实际输入后续coding operator；搜索策略固定（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1）。
- **状态怎样持久保留**：跨完整代码实验提案（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1）。
- **更新怎样进入后续改进**：执行记录/指标/调参/报错被摘要，实际输入后续coding operator；搜索策略固定（状态：`supported`；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1）。

**配置判定**：本项目宽操作性定义下的历史上下文反馈核心；不是coding/search operator代码自改或研究者能力收益认证

来源：https://arxiv.org/html/2502.13138v1；版本：v1；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_aide`**：AIDE用树搜索优化机器学习工程代码的验证指标。
  - 来源版本：v1；定位：S3.p1；深度：`AI_rechecked_primary_text_author_report`。

- **`e3_w_aide`**：执行记录/指标/调参/报错被摘要，实际输入后续coding operator；搜索策略固定
  - 来源版本：v1；定位：S3.SS1.p1；S3.SS2.SSS0.Px1.p1；S3.SS2.SSS0.Px2.p1；S3.SS2.SSS0.Px3.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 不是由该段证明研究代理自身更新
- 本
- 项
- 目
- 宽
- 操
- 作
- 性
- 定
- 义
- 下
- 的
- 历
- 史
- 上
- 文
- 反
- 馈
- 核
- 心
- ；
- 不
- 是
- c
- o
- d
- i
- n
- g
- /
- s
- e
- a
- r
- h
- 
- p
- t
- 代
- 码
- 自
- 改
- 或
- 研
- 究
- 者
- 能
- 力
- 收
- 益
- 认
- 证

## 7. 与其他论文的具体关系

### [Recursive self-improvement of AI research agents](../r03_method/wf_59d41d27ae673fd141.md)
关系：`refactors_implementation_of` · `r_aide2_aide` · 当前展示权限：`primary_supported`。
AIDE²作者明确称初始内环代理AIDE0是AIDE的精简重构：移除ML专用机制但保留树搜索与draft/debug/improve操作，外环重写内环代理。AIDE原文的方案树、搜索策略、代码与摘要算子提供被保留组件的双端依据。

**关系边界**：重构关系具体属于AIDE²初始内环AIDE0；AIDE_human是另一个人为研发基线/外环代理，不与原始AIDE混同；主运行固定每环模型且外环更强，不能声称两个循环均无人工固定组件。

**关系主语端 / 宾语端依据**：https://arxiv.org/html/2609.26457v1（v1；S2.SS2.p1.1；S2.SS2.p2.1）；https://arxiv.org/html/2502.13138v1（v1；S3.SS1.p1.1；S3.SS2.SSS0.Px1.p1.1）。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_aide` · 已存来源 · v1
  - https://arxiv.org/html/2502.13138v1；阅读深度：`未单列`。
- `stage1_src_w_aide` · 已存来源 · v1
  - https://arxiv.org/html/2502.13138v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bc4a082767b6da7c5d --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
