# Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

> 方法论文 · 2026 · `wf_fb639e0da250efca5c`

**作者**：Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu  
**原文**：https://arxiv.org/abs/2610.12369  
**研究分支**：具身、机器人与交互环境  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：episode state variables with fixed source code; fixed: policy source code, no runtime coding agent；具体更新过程为：代码仅执行状态转移和机器人动作；运行配置中未执行离线代码开发；更新状态的保留与后继使用为：episode state; library frozen at execution。

## 2. 论文的核心内容与贡献

### configuration:cfg_coap_coding_agent_library_validation_loop_v1
显式声明开发agent+库+评价器边界后支持有界程序反馈；不从机器人theta-only边界偷换得到。

**适用版本**：2610.12369v1；**原文定位**：§3.3–3.4 tool L204–250。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_coap_development
原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。

**适用版本**：2610.12369v1；**原文定位**：§3.3–3.4 tool L204–250。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_coap_execution
运行时代码固定；状态转移不能替代自修改和后续改进过程。

**适用版本**：v1；**原文定位**：Section 3 Eq.1; Section 3.4; Section 5.4。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_coap_execution
`cfg_coap_execution` · COAP frozen runtime robot policy

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | episode state variables with fixed source code; fixed: policy source code, no runtime coding agent |
| 改进过程与下一轮参与 | 代码仅执行状态转移和机器人动作；运行配置中未执行离线代码开发。 |
| 保留的状态及时间尺度 | episode state; library frozen at execution |

**配置判定**：运行时代码固定；状态转移不能替代自修改和后续改进过程。

来源：https://arxiv.org/html/2610.12369v1；版本：v1；定位：Section 3 Eq.1; Section 3.4; Section 5.4。

### cfg_coap_development
`cfg_coap_development` · code_library_boundary_view

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 保留机器人库代码theta，外部编码代理参与离线开发 |
| 改进过程与下一轮参与 | coding agent读失败开发记录提出diff；接受库为后续分支基底 |
| 保留的状态及时间尺度 | 跨离线开发轮次 |
| 外部固定部分 | 外部编码代理、接受程序与开发验证划分 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。
- **更新由什么过程产生**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。（状态：`contradicted`；定位：§3.3–3.4 tool L204–250）。
- **状态怎样持久保留**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。
- **更新怎样进入后续改进**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。

**配置判定**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。

来源：https://arxiv.org/html/2610.12369v1；版本：2610.12369v1；定位：§3.3–3.4 tool L204–250。

### COAP: explicit coding-agent + retained code + validation development system
`cfg_coap_coding_agent_library_validation_loop_v1` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 外部Claude Opus 5.5开发agent、当前可运行代码theta、开发失败记录、CPU检查与固定validation接受规则共同组成显式开发系统。 |
| 改进过程与下一轮参与 | agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。 |
| 保留的状态及时间尺度 | 接受代码跨开发轮和任务保留，执行阶段代码固定；开发集/validation/test各用途分列。 |
| 外部固定部分 | - 基础coding LM - CPU检查与validation接受规则 - 仿真平台及给定任务 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。
- **更新由什么过程产生**：agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。
- **状态怎样持久保留**：agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。
- **更新怎样进入后续改进**：agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。（状态：`supported`；定位：§3.3–3.4 tool L204–250）。

**配置判定**：显式声明开发agent+库+评价器边界后支持有界程序反馈；不从机器人theta-only边界偷换得到。

来源：https://arxiv.org/html/2610.12369v1；版本：2610.12369v1；定位：§3.3–3.4 tool L204–250。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7root_ev_cfg_coap_development`**：原记录仅把机器人代码库theta作为边界，C2不成立：编辑由外部coding agent完成；但更新后的theta成为后继开发分支基础，C4有原文支持。显式开发系统配置另列。
  - 来源版本：2610.12369v1；定位：§3.3–3.4 tool L204–250；深度：`未单列`。

- **`r7root_ev_cfg_coap_coding_agent_library_validation_loop_v1`**：显式声明开发agent+库+评价器边界后支持有界程序反馈；不从机器人theta-only边界偷换得到。 agent读取当前代码及失败状态，提议并行worktree diff；通过检查后在validation比较，接受theta(k+1)成为所有后继分支的基础。
  - 来源版本：2610.12369v1；定位：§3.3–3.4 tool L204–250；深度：`未单列`。

- **`e2_w_coap`**：接受代码成为后续分支基础；原文未建立它执行或改变外部编码代理的改进程序
  - 来源版本：v1；定位：S3.SS3.p1；S3.SS4.p1；S3.SS4.p2；S5.SS4.p1；S5.SS4.p2；深度：`AI_primary_method_passage_recheck`。

- **`e3_w_coap`**：coding agent读失败开发记录提出diff；接受库为后续分支基底
  - 来源版本：v1；定位：S3.SS4.p1；S3.SS4.p2；S5.SS4.p2；深度：`未单列`。

- **`e4_cfg_coap_development`**：外部coding agent读取失败开发记录，接受后的机器人库代码成为未来分支基底。
  - 来源版本：v1；定位：S3.SS4.p1；S3.SS4.p2；S5.SS4.p2；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只覆盖仿真中的离线开发；不认证部署在线自改、现实机器人泛化或固定LM权重更新。
- validation上的接受阈值不是对所有未见布局的单调改进保证；开发debug与validation选优不同，test另行评估。
- 机器人执行时读取状态不等于theta自行修改；外部开发循环另见显式新配置。
- 代
- 码
- 保
- 留
- 和
- 机
- 器
- 人
- 任
- 务
- 收
- 益
- 有
- 报
- 告
- ；
- 条
- 件
- 4
- 继
- 续
- 未
- 知
- 固
- 定
- 运
- 行
- 时
- c
- f
- g
- _
- o
- a
- p
- e
- x
- u
- t
- i
- n
- 仍
- 为
- d
- j
- 原
- 边
- 界
- ：
- 库
- 不
- 等
- 于
- 编
- 理
- 改
- 进
- 程
- 序
- 额
- 外
- 日
- 志
- 或
- 调
- 用
- 链
- 取
- 得
- ，
- 能
- 仅
- 靠
- 分
- 支
- 基
- 底
- 升
- 级
- 持
- h
- 把
- 部
- 
- 其
- 上
- 下
- 文
- 无
- 痕
- 纳
- 入
- 。
- 足
- 以
- 作
- 开
- 发
- 制
- 导
- 航
- 新
- 配
- 置
- 解
- 释
- 尚
- 完
- 成

## 7. 与其他论文的具体关系

### [Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision](../r03_method/wf_a7c55e2196d2e1c9dc.md)
关系：`contrasts_system_boundary_with` · `r2_visuomotor_rsi_coap_16` · 当前展示权限：`primary_supported`。
Visuomotor RSI的方法框架以当前学生失败轨迹及修复后的续跑能力决定下一轮恢复监督，经PostTrain保留学生参数，教师参数跨轮固定；COAP离线开发由编码代理根据失败记录提出机器人库代码diff，经CPU检查、验证集成功数与兼容性约束选择分支，接受代码作为后续分支基底。其可变资产分别为学生策略参数与机器人库源代码。

**关系边界**：左端是所提多轮方法框架，原文将关键多轮对照列为评价协议，不能认证已有实证递归收益；右端只用离线开发配置，不能混入冻结的在线执行配置。COAP现有窄边界条件4仍待定；比较关系本身不升级核心归属。COAP所查结果仅模拟，未取得共同基准、直接继承或参数/代码收益等价证据。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2610.05151v1；版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。
- object：https://arxiv.org/html/2610.12369v1；版本：v1；定位：S3.SS3.p1；S3.SS4.p1；S3.SS4.p2；S5.SS4.p1；S5.SS4.p2。
- expand_src_w_visuomotor_rsi：https://arxiv.org/html/2610.05151v1；版本：v1；定位：S3.SS1.p1；S3.SS8.p1；S5.SS0.SSS0.Px2.p1；S6.p1。
- expand_src_w_coap：https://arxiv.org/html/2610.12369v1；版本：v1；定位：S3.SS3.p1；S3.SS4.p1；S3.SS4.p2；S5.SS4.p1；S5.SS4.p2。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_coap` · Code-Only-as-Policy (COAP) · v1
  - https://arxiv.org/html/2610.12369v1；阅读深度：`未单列`。
- `r7root_src_coap_development` · 已存来源 · 2610.12369v1
  - https://arxiv.org/html/2610.12369v1；阅读深度：`未单列`。
- `src_20261013_w_coap` · 已存来源 · v1
  - https://arxiv.org/html/2610.12369v1；阅读深度：`未单列`。
- `stage1_src_w_coap` · 已存来源 · v1
  - https://arxiv.org/html/2610.12369v1；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_fb639e0da250efca5c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
