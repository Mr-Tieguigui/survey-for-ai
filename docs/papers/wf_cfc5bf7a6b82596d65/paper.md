# AlphaEvolve: A coding agent for scientific and algorithmic discovery

> 方法论文 · 2025 · `wf_cfc5bf7a6b82596d65`

**作者**：Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog  
**原文**：https://arxiv.org/abs/2506.13131  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定LM/评价器与可演化程序数据库、prompt sampler和后继程序提案；具体更新过程为：Prompt sampler读取已有程序和分数，LM提出diff，执行评价后候选回写数据库供后继提案；更新状态的保留与后继使用为：程序与评价信息跨演化代保留；不等于LM权重自训练。

## 2. 论文的核心内容与贡献

### configuration:cfg_alphaevolve
在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。

**适用版本**：2506.13131v1；**原文定位**：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_alphaevolve_meta_prompt_option
LLM提案指令/上下文在独立数据库共演化，更新指令支配后续程序提案；不声称主实验全部启用

**适用版本**：v1；**原文定位**：S2.SS2.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_alphaevolve
`cfg_alphaevolve` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定LM/评价器与可演化程序数据库、prompt sampler和后继程序提案。 |
| 改进过程与下一轮参与 | Prompt sampler读取已有程序和分数，LM提出diff，执行评价后候选回写数据库供后继提案。 |
| 保留的状态及时间尺度 | 程序与评价信息跨演化代保留；不等于LM权重自训练。 |
| 外部固定部分 | Gemini模型、evaluator、数据库管理 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。（状态：`supported`；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312）。
- **更新由什么过程产生**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。（状态：`supported`；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312）。
- **状态怎样持久保留**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。（状态：`supported`；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312）。
- **更新怎样进入后续改进**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。（状态：`supported`；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312）。

**配置判定**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。

来源：https://arxiv.org/html/2506.13131v1；版本：2506.13131v1；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312。

### cfg_alphaevolve_meta_prompt_option
`cfg_alphaevolve_meta_prompt_option` · optional_method_description_not_all_experiments

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 可选meta prompt evolution方法配置 |

**配置判定**：LLM提案指令/上下文在独立数据库共演化，更新指令支配后续程序提案；不声称主实验全部启用

来源：https://arxiv.org/html/2506.13131v1；版本：v1；定位：S2.SS2.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_alphaevolve`**：在明确的程序数据库—候选提案—自动评价—保留边界中，已评分程序进入后继prompt并改变下一代程序提案，满足有界结构反馈；不要求可选meta-prompt开关或基础LM权重更新。
  - 来源版本：2506.13131v1；定位：§2 Figure 2 tool L107–110；§2.2 tool L259–275；§2.5 tool L310–312；深度：`未单列`。

- **`e3_w_alphaevolve`**：主提示可读取历史程序/评分；原文还描述可选meta prompt evolution，但不是所有实验共同启用项
  - 来源版本：v1；定位：S2.SS2.p1；S2.SS3.SSS0.Px2.p1；S2.SS5.p1；深度：`未单列`。

- **`e4_cfg_alphaevolve`**：主提示包含历史解决方案与固定提案指令；执行结果渲染和meta-prompt共演化列为可定制选项，数据库积累程序及结果并重取历史方案。
  - 来源版本：v1；定位：S2.SS2.p1；S2.SS3.SSS0.Px2.p1；S2.SS5.p1；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 仅标准方法边界；不同主实验的独立超参与可选meta-prompt启用状态仍不能一概推定。
- 自动评价只保证相应测试范围；不认证外层演化规则自行改写或收益持续加速。
- 主
- 配
- 置
- 的
- 可
- 写
- 机
- 制
- /
- 各
- 实
- 验
- 启
- 用
- 项
- 未
- 对
- 齐
- ；
- 新
- 增
- 选
- m
- e
- t
- a
- -
- p
- r
- o
- 单
- 列
- ，
- 不
- 能
- 整
- 篇
- 或
- 全
- 部
- 升
- 核
- 心
- 已
- 有
- 独
- 立
- c
- 方
- 法
- 记
- 录
- 但
- 与
- 具
- 体
- 改
- 进
- 参
- 证
- 据
- 。
- 本
- 轮
- 因
- 通
- 历
- 史
- 候
- 池
- 自
- 动
- 级

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r7root_src_alpha_program_archive` · 已存来源 · 2506.13131v1
  - https://arxiv.org/html/2506.13131v1；阅读深度：`未单列`。
- `src_20261013_w_alphaevolve` · 已存来源 · v1
  - https://arxiv.org/html/2506.13131v1；阅读深度：`未单列`。
- `stage1_src_w_alphaevolve` · 已存来源 · v1
  - https://arxiv.org/html/2506.13131v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_cfc5bf7a6b82596d65 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
