# Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity

> 方法论文 · 2020 · `wf_0d0470f1accb7d9b1a`

**作者**：Thomas Miconi, Aditya Rawal, Jeff Clune, Kenneth O. Stanley  
**原文**：https://arxiv.org/abs/2002.10585  
**研究分支**：自指权重、优化器与元学习  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定meta训练参数下的200步cue-reward episode与可塑recurrent layer；具体更新过程为：网络输出M(t)调节Hebbian写入，更新后的有效递归权重影响后续活动和M(t)；更新状态的保留与后继使用为：同一episode的多次独立动作/反馈；episode开始Hebb=0。

## 2. 论文的核心内容与贡献

### configuration:cfg_backpropamine_retroactive_cue_rl
在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

**适用版本**：2002.10585v1；**原文定位**：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_backpropamine_simple_cue_rl
在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

**适用版本**：2002.10585v1；**原文定位**：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Backpropamine simple neuromodulation: cue-reward RL
`cfg_backpropamine_simple_cue_rl` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定meta训练参数下的200步cue-reward episode与可塑recurrent layer |
| 改进过程与下一轮参与 | 网络输出M(t)调节Hebbian写入，更新后的有效递归权重影响后续活动和M(t) |
| 保留的状态及时间尺度 | 同一episode的多次独立动作/反馈；episode开始Hebb=0 |
| 外部固定部分 | - 基线w与plasticity系数α - Hebbian公式及clip - 外部A2C与奖励任务 |
| 评价与选择设置 | - **episode steps**：200 - **hidden recurrent neurons**：200 - **meta training**：A2C - **previous reward as input**：True - **task**：cue-reward association |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：方法定义固定/可塑分量（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107）。
- **更新由什么过程产生**：M(t)由网络自身计算（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107）。
- **状态怎样持久保留**：Hebb(t+1)进入后续有效权重（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107）。
- **更新怎样进入后续改进**：后续网络活动再生成M(t)调节下一次更新（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107）。

**配置判定**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

来源：https://arxiv.org/html/2002.10585v1；版本：2002.10585v1；定位：§3.1 Eq1–2; web lines70–79；§3.2.1 Eq3; web lines81–87；§4.1; web lines100–107。

### Backpropamine retroactive neuromodulation: cue-reward RL
`cfg_backpropamine_retroactive_cue_rl` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定meta训练参数下的200步cue-reward episode与可塑recurrent layer |
| 改进过程与下一轮参与 | 网络M(t)门控eligibility trace写入Hebbian分量，修改后网络继续产生后续调制 |
| 保留的状态及时间尺度 | 同一episode的多次独立动作/反馈；episode开始Hebb=0 |
| 外部固定部分 | - 基线w与plasticity系数α - Hebbian公式及clip - 外部A2C与奖励任务 - eligibility trace公式 |
| 评价与选择设置 | - **episode steps**：200 - **hidden recurrent neurons**：200 - **meta training**：A2C - **previous reward as input**：True - **task**：cue-reward association |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：方法显式分离eligibility与Hebbian状态（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107）。
- **更新由什么过程产生**：网络计算正负M(t)控制实际塑性（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107）。
- **状态怎样持久保留**：Hebb与E在episode内跨时间步（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107）。
- **更新怎样进入后续改进**：被修改网络继续计算调制信号（状态：`supported`；定位：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107）。

**配置判定**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。

来源：https://arxiv.org/html/2002.10585v1；版本：2002.10585v1；定位：§3.1 Eq1–2; web lines70–79；§3.2.2 Eq4–5; web lines88–98；§4.1; web lines100–107。

## 4. 实验、评价协议与结果的可解释范围


- **episode steps**：200
- **hidden recurrent neurons**：200
- **meta training**：A2C
- **previous reward as input**：True
- **task**：cue-reward association

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4_root_ev_cfg_backpropamine_simple_cue_rl`**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`r4_root_ev_cfg_backpropamine_retroactive_cue_rl`**：在指定episode/任务适应边界内满足结构四条件；不是跨任务永久学习、元优化器自主改写或开放式能力递增的认证。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Hebbian trace在每个episode/lifetime开始时归零（§3.1）；不声称跨episode保留。
- 结构权重、可塑性系数和外部A2C训练方案固定于内层适应；core仅指有界结构闭环。
- 不把PTB的监督语言建模设置或其性能移植到本RL配置。
- 原文方法与实验设置选段核查；不提供独立实验复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4_root_src_backpropamine` · 已存来源 · 2002.10585v1
  - https://arxiv.org/html/2002.10585v1；阅读深度：`selected_primary_methods_and_experiment_settings`。
- `r4_root_src_backpropamine_modulation` · 已存来源 · 2002.10585v1
  - https://arxiv.org/html/2002.10585v1；阅读深度：`selected_primary_methods_and_experiment_settings`。

**证据深度**：original_abstract, selected_primary_method_and_experiment_settings_20261016。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0d0470f1accb7d9b1a --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
