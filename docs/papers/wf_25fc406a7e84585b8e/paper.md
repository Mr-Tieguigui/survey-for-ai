# AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

> 方法论文 · 2026 · `wf_25fc406a7e84585b8e`

**作者**：Yaxin Luo, Haobin Jiang, Jialv Zou, Xu Huang, Wenhao Yan, Haodong Li, Zhengrong Yue, Jing Li, Xiaofu Chen, Xiaohan Zhao, Jiacheng Liu, Jiacheng Cui, Zhiqiang Shen, Xiaotong Li  
**原文**：https://arxiv.org/abs/2608.13560  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定LM/optimization evaluator、design harness H、train/dev tasks与持久record L；具体更新过程为：当前H跑train，P读train轨迹/评分/L，每轮改一个component；train提高且dev不降才接受，否则旧H；失败记录供下轮；更新状态的保留与后继使用为：H checkpoint和L跨outer iterations与tasks保留并供下轮proposal。

## 2. 论文的核心内容与贡献

### configuration:cfg_autodesign_outer_harness_checkpoint_v1
outer loop保留H和优化记录进入后继修订，四条件在harness开发系统成立；固定H内层单poster修图不等同此配置。

**适用版本**：2608.13560v1；**原文定位**：§2 tool L100–138；§3.1–3.2 tool L139–172。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### AutoDesign: persistent outer meta-harness updates
`cfg_autodesign_outer_harness_checkpoint_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定LM/optimization evaluator、design harness H、train/dev tasks与持久record L。 |
| 改进过程与下一轮参与 | 当前H跑train，P读train轨迹/评分/L，每轮改一个component；train提高且dev不降才接受，否则旧H；失败记录供下轮。 |
| 保留的状态及时间尺度 | H checkpoint和L跨outer iterations与tasks保留并供下轮proposal。 |
| 外部固定部分 | - 基础theta - human annotated artifacts构建后冻结Rmeta - dev gate/单组件约束 |

**配置判定**：outer loop保留H和优化记录进入后继修订，四条件在harness开发系统成立；固定H内层单poster修图不等同此配置。

来源：https://arxiv.org/html/2608.13560v1；版本：2608.13560v1；定位：§2 tool L100–138；§3.1–3.2 tool L139–172。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8a_ev_cfg_autodesign_outer_harness_checkpoint_v1`**：outer loop保留H和优化记录进入后继修订，四条件在harness开发系统成立；固定H内层单poster修图不等同此配置。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- dev不向P暴露但反复用于gate；optimization Rmeta与最终PosterBench协议不同。
- L172是single active harness顺序迭代，不做tree search。
- 可选human guidance与外部参考artifact保留，不称无人工目标或基础权重训练。
- - dev不向P暴露但反复用于gate；optimization Rmeta与最终PosterBench协议不同。 - L172是single active harness顺序迭代，不做tree search。 - 可选human guidance与外部参考artifact保留，不称无人工目标或基础权重训练。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8a_src_w_autodesign_v1` · 已存来源 · 2608.13560v1
  - https://arxiv.org/html/2608.13560v1；阅读深度：`targeted_primary_method_state_feedback_limits`。

**证据深度**：original_abstract, targeted_primary_method_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_25fc406a7e84585b8e --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
