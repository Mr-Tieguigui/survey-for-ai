# EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation

> 方法论文 · 2026 · `wf_aa8eef11bee8a542e2`

**作者**：Haoran Lang, Haotao Lu, Shiyu Sang, Haoyang Luo, Guo Chen, Qun Li, Jingyi Yu, Ye Shi, Jingya Wang  
**原文**：https://arxiv.org/abs/2609.38905  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：当前机器人policy、累积数据、训练期恢复代理与reset分布组成训练闭环；具体更新过程为：当前policy rollout失败时暂停仿真并规划恢复；保留有效rollout/纠正示范，按失败归因更新reset混合分布，RECAP更新policy后再次收集；更新状态的保留与后继使用为：policy、数据集与reset分布跨训练轮保留。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_embodi_training
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：unversioned_observed；**原文定位**：§3.3 tool L147–214; §5 tool L249–262。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### EmbodiRSI: recovery-data and failure-reset adaptive robot training
`cfg_r8b_embodi_training` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前机器人policy、累积数据、训练期恢复代理与reset分布组成训练闭环。 |
| 改进过程与下一轮参与 | 当前policy rollout失败时暂停仿真并规划恢复；保留有效rollout/纠正示范，按失败归因更新reset混合分布，RECAP更新policy后再次收集。 |
| 保留的状态及时间尺度 | policy、数据集与reset分布跨训练轮保留。 |
| 外部固定部分 | - 视觉/几何monitor与规划器 - reset网格及基准初始分布 - RECAP学习规则 - 最终测试没有恢复代理 |
| 评价与选择设置 | - **collection mixture**：(1-alpha)p0+alpha*p_hard - **deployment learning**：not_certified - **updates**：R0 to R2, two policy updates |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：训练系统状态与最终部署评价分开。（状态：`supported`；定位：§3.3 tool L147–214; §5 tool L249–262）。
- **更新由什么过程产生**：自身失败、恢复轨迹和归因触发数据与policy更新。（状态：`supported`；定位：§3.3 tool L147–214; §5 tool L249–262）。
- **状态怎样持久保留**：数据累积和policy跨轮保留。（状态：`supported`；定位：§3.3 tool L147–214; §5 tool L249–262）。
- **更新怎样进入后续改进**：更新policy在下一轮新的混合reset分布上收集，新的失败继续驱动改进。（状态：`supported`；定位：§3.3 tool L147–214; §5 tool L249–262）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2609.38905；版本：unversioned_observed；定位：§3.3 tool L147–214; §5 tool L249–262。

## 4. 实验、评价协议与结果的可解释范围


- **collection mixture**：(1-alpha)p0+alpha*p_hard
- **deployment learning**：not_certified
- **updates**：R0 to R2, two policy updates

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_embodi_training`**：当前机器人policy、累积数据、训练期恢复代理与reset分布组成训练闭环。 当前policy rollout失败时暂停仿真并规划恢复；保留有效rollout/纠正示范，按失败归因更新reset混合分布，RECAP更新policy后再次收集。
  - 来源版本：unversioned_observed；定位：§3.3 tool L147–214; §5 tool L249–262；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 失败归因是规则性启发，不是严格因果识别；成功恢复episode不计失败归因分子。
- reset混合权重不规定保留轨迹的比例；最终测试reset不随训练重采样。
- 固定两次更新，不认证无限递归；场景重建和workspace泛化仍有限。
- 最终测试移除恢复、人类干预与规划器，不能称部署期在线学习。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_embodi` · 已存来源 · unversioned_observed
  - https://arxiv.org/html/2609.38905；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_aa8eef11bee8a542e2 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
