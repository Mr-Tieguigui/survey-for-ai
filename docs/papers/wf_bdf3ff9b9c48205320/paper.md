# FreeEvolve: Learning to Evolve Beyond Fixed Loops

> 方法论文 · 2026 · `wf_bdf3ff9b9c48205320`

**作者**：Lecheng Kong, Like Hui, Nikos Kanakaris, Prithwish Jana, Sahika Genc, Narayanan Sadagopan  
**原文**：https://arxiv.org/abs/2610.09197  
**研究分支**：工作流与执行控制  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定环境与外部agent、候选markdown skill、worker完整搜索campaign和独立meta-controller组成两层系统；具体更新过程为：外层根据worker任务分数及traces修改candidate skill，再由新worker完整campaign测验；选出skill供后续campaign/迁移；更新状态的保留与后继使用为：候选skill跨meta试验保留；worker在campaign内保留harness修订和运行轨迹。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_free_skill_meta
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：unversioned_observed；**原文定位**：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### FreeEvolve: editable evolution skill selected through worker campaigns
`cfg_r8b_free_skill_meta` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定环境与外部agent、候选markdown skill、worker完整搜索campaign和独立meta-controller组成两层系统。 |
| 改进过程与下一轮参与 | 外层根据worker任务分数及traces修改candidate skill，再由新worker完整campaign测验；选出skill供后续campaign/迁移。 |
| 保留的状态及时间尺度 | 候选skill跨meta试验保留；worker在campaign内保留harness修订和运行轨迹。 |
| 外部固定部分 | - meta-controller与candidate是独立拷贝 - 任务环境和评价资源约束 - 两层嵌套的上层meta环境不继续递归 |
| 评价与选择设置 | - **candidate controller separation**：True - **meta environment**：excluded from further nesting - **nesting depth**：two levels |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：外层skill与内层worker边界明确。（状态：`supported`；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260）。
- **更新由什么过程产生**：worker执行反馈驱动候选skill修改。（状态：`supported`；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260）。
- **状态怎样持久保留**：skill跨worker试验/任务保留。（状态：`supported`；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260）。
- **更新怎样进入后续改进**：更新skill组织后续worker campaign，所得反馈继续指导skill搜索。（状态：`supported`；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2610.09197；版本：unversioned_observed；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260。

## 4. 实验、评价协议与结果的可解释范围


- **candidate controller separation**：True
- **meta environment**：excluded from further nesting
- **nesting depth**：two levels

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_free_skill_meta`**：固定环境与外部agent、候选markdown skill、worker完整搜索campaign和独立meta-controller组成两层系统。 外层根据worker任务分数及traces修改candidate skill，再由新worker完整campaign测验；选出skill供后续campaign/迁移。
  - 来源版本：unversioned_observed；定位：§3 tool L110–165; §4.1 L170–171; §5 tool L246–260；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 修改candidate不修改当前meta-controller；不是无界自我重写。
- worker可选择eval子集、重复/seed/并发与停止，比较须匹配实际资源口径。
- held-out分区用于最终检验；不同小模型并非都有held-out增益。
- ARC单campaign qualitative case不是分布性保证；不认证能力越弱也能自举。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_free` · 已存来源 · unversioned_observed
  - https://arxiv.org/html/2610.09197；阅读深度：`selected_primary_method_protocol_and_limits`。
- `r9_src_cfg_r8b_free_skill_meta` · 已存来源 · unversioned_observed
  - https://arxiv.org/html/2610.09197；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_bdf3ff9b9c48205320 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
