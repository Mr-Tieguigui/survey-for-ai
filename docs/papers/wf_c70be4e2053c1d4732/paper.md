# Meta-Reinforcement Learning with Self-Modifying Networks

> 方法论文 · 2022 · `wf_c70be4e2053c1d4732`

**作者**：Mathieu Chalvidal, Thomas Serre, Rufin VanRullen  
**原文**：https://arxiv.org/abs/2202.02363  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Harlow任务适应期的一层动态W及观察/上一动作/奖励输入；具体更新过程为：当前W参与read/write递归并形成W_t，作为下一步初始状态参与后续更新；更新状态的保留与后继使用为：任务适应轨迹内跨决策步保留W；不据此声称跨新任务永久继承。

## 2. 论文的核心内容与贡献

### configuration:cfg_metods_harlow_synaptic_adaptation
在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

**适用版本**：2202.02363v3；**原文定位**：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### MetODS Harlow: recursive synaptic policy adaptation
`cfg_metods_harlow_synaptic_adaptation` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Harlow任务适应期的一层动态W及观察/上一动作/奖励输入 |
| 改进过程与下一轮参与 | 当前W参与read/write递归并形成W_t，作为下一步初始状态参与后续更新 |
| 保留的状态及时间尺度 | 任务适应轨迹内跨决策步保留W；不据此声称跨新任务永久继承 |
| 外部固定部分 | - meta参数f/g/α/κ/β - read/write及递归次数结构 - 外部A2C训练与任务分布 |
| 评价与选择设置 | - **dynamic layer size**：20 - **initial W0**：normal(0,1e-3) - **meta training**：A2C - **settings source id**：r4_root_src_metods_settings - **task**：Harlow |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Algorithm1给出θ和W0（状态：`supported`；定位：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354）。
- **更新由什么过程产生**：当前W参与下一次read和write（状态：`supported`；定位：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354）。
- **状态怎样持久保留**：W_t传递到下一步W^(0)（状态：`supported`；定位：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354）。
- **更新怎样进入后续改进**：W改变后续输入编码所经read及下一次权重更新（状态：`supported`；定位：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354）。

**配置判定**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

来源：https://arxiv.org/html/2202.02363v3；版本：2202.02363v3；定位：§3.1 Eq3–6 and Algorithm1; web lines91–140；§5.1 Harlow; web lines156–165；§10 Table1 and §10.1; settings snapshot web lines338–354。

## 4. 实验、评价协议与结果的可解释范围


- **dynamic layer size**：20
- **initial W0**：normal(0,1e-3)
- **meta training**：A2C
- **settings source id**：r4_root_src_metods_settings
- **task**：Harlow

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_root_ev_cfg_metods_harlow_synaptic_adaptation`**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只测试单动态层；扩展至整网为未来工作（§3.1）。
- Table1列Harlow W0随机初始化；不泛化为所有任务配置均重置或随机初始化。
- 原文不同benchmark预算与比较条件各异；本卡不作统一性能排名。
- 任务内自指权重演化与外层meta参数优化分开。
- 原文方法与实验设置选段核查；不提供独立实验复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_root_src_metods` · 已存来源 · 2202.02363v3
  - https://arxiv.org/html/2202.02363v3；阅读深度：`selected_primary_methods_and_experiment_settings`。
- `r4_root_src_metods_settings` · 已存来源 · 2202.02363v3
  - https://arxiv.org/html/2202.02363v3；阅读深度：`selected_primary_methods_and_experiment_settings`。

**证据深度**：original_abstract, selected_primary_method_and_experiment_settings_20261016。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_c70be4e2053c1d4732 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
