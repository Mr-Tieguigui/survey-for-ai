# DataFoundry: Evolving Data Preparators via Recursive Self-Improvement

> 方法论文 · 2026 · `wf_6d33f4edcb911adc60`

**作者**：Cehao Yang, Xiaojun Wu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Hui Xiong, Jian Guo  
**原文**：https://arxiv.org/abs/2608.29966  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定四接口数据preparator、可修改adapter、pilot运行与评估报告组成数据准备系统；具体更新过程为：每轮把基础preparator与当前adapter重新编译，pilot报告经Trace触发编码代理修订adapter，下一轮使用该adapter再次准备/评价数据；更新状态的保留与后继使用为：跨pilot轮保留adapter；不是把单条回答当成改进状态。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_datafoundry_adapter
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：2608.29966v1；**原文定位**：§3 tool L109–201; §4.2 L202–234。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### DataFoundry: persistent preparator adapter refinement
`cfg_r8b_datafoundry_adapter` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定四接口数据preparator、可修改adapter、pilot运行与评估报告组成数据准备系统。 |
| 改进过程与下一轮参与 | 每轮把基础preparator与当前adapter重新编译，pilot报告经Trace触发编码代理修订adapter，下一轮使用该adapter再次准备/评价数据。 |
| 保留的状态及时间尺度 | 跨pilot轮保留adapter；不是把单条回答当成改进状态。 |
| 外部固定部分 | - 基础preparator四接口 - 外部编码LLM及编译/运行约束 - 标准库中的评价维度和pilot预算 |
| 评价与选择设置 | - **adapter composition**：Adapt(base, current_adapter), not unbounded concatenation - **downstream model**：Qwen2.5-7B - **observed refinement rounds**：2 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：四接口、adapter和pilot边界明示。（状态：`supported`；定位：§3 tool L109–201; §4.2 L202–234）。
- **更新由什么过程产生**：自身pilot产出被评价并触发adapter修改。（状态：`supported`；定位：§3 tool L109–201; §4.2 L202–234）。
- **状态怎样持久保留**：新adapter跨轮保留。（状态：`supported`；定位：§3 tool L109–201; §4.2 L202–234）。
- **更新怎样进入后续改进**：改后preparator生成下一轮pilot数据并接受新评价。（状态：`supported`；定位：§3 tool L109–201; §4.2 L202–234）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2608.29966；版本：2608.29966v1；定位：§3 tool L109–201; §4.2 L202–234。

## 4. 实验、评价协议与结果的可解释范围


- **adapter composition**：Adapt(base, current_adapter), not unbounded concatenation
- **downstream model**：Qwen2.5-7B
- **observed refinement rounds**：2

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_datafoundry_adapter`**：固定四接口数据preparator、可修改adapter、pilot运行与评估报告组成数据准备系统。 每轮把基础preparator与当前adapter重新编译，pilot报告经Trace触发编码代理修订adapter，下一轮使用该adapter再次准备/评价数据。
  - 来源版本：2608.29966v1；定位：§3 tool L109–201; §4.2 L202–234；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 最终学生SFT是下游检验，没有证明学生反馈回到preparator。
- 评价与修改均由外部编码代理承担；选择标准不等于评价器自身学习。
- 实际主要2轮，正文指出更多轮可恶化；不认证持续单调提升。
- 若干对照采用已有报告；未认证所有端点重新同成本运行。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_data` · 已存来源 · 2608.29966v1
  - https://arxiv.org/html/2608.29966；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_6d33f4edcb911adc60 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
