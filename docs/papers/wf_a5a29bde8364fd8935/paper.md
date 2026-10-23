# EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

> 方法论文 · 2026 · `wf_a5a29bde8364fd8935`

**作者**：Yikai Qin, Yifei Deng, Mingjian Liang, Wenxuan Song, Zepeng Lin, Zhiyi Jiang, Jiajun Fu, Qiao Sun, Huashuo Lei, Xicheng Gong, Jiayi Chen, Han Zhao, Shuanghao Bai, Pengxiang Ding, Pengwei Wang, Haoang Li  
**原文**：https://arxiv.org/abs/2610.07969  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：可验证物理资产库、候选场景、执行证据及改错循环组成仿真数据构建系统；不含下游学生回流；具体更新过程为：失败检查驱动资产修复/再生成或局部SceneEdit，重新验证和执行；通过检查的资产进入可复用池并参与后续场景构建；更新状态的保留与后继使用为：通过验证的资产跨场景复用；候选修订在后续验证/生成中继续使用。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_smith_asset_scene
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：2610.07969v1；**原文定位**：§3 tool L80–138; §4 selected evaluation protocol。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### EmbodiedSmith: persistent asset/scene correction and reuse boundary
`cfg_r8b_smith_asset_scene` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 可验证物理资产库、候选场景、执行证据及改错循环组成仿真数据构建系统；不含下游学生回流。 |
| 改进过程与下一轮参与 | 失败检查驱动资产修复/再生成或局部SceneEdit，重新验证和执行；通过检查的资产进入可复用池并参与后续场景构建。 |
| 保留的状态及时间尺度 | 通过验证的资产跨场景复用；候选修订在后续验证/生成中继续使用。 |
| 外部固定部分 | - 任务成功标准在执行前固定 - 几何/物理检查和仿真接口 - 外部生成/检查模型及技能接口 |
| 评价与选择设置 | - **persistent state**：validated reusable asset pool and revision drafts - **policy training feedback**：not_certified |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：资产池与生成—验证—执行边界明确。（状态：`supported`；定位：§3 tool L80–138; §4 selected evaluation protocol）。
- **更新由什么过程产生**：自身检查与任务执行失败触发局部修订。（状态：`supported`；定位：§3 tool L80–138; §4 selected evaluation protocol）。
- **状态怎样持久保留**：资产池和修订候选保留，不限于最终文本答案。（状态：`supported`；定位：§3 tool L80–138; §4 selected evaluation protocol）。
- **更新怎样进入后续改进**：保留资产参与后续场景生成；新场景失败再触发局部改错，反馈边界是生成器系统。（状态：`supported`；定位：§3 tool L80–138; §4 selected evaluation protocol）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2610.07969；版本：2610.07969v1；定位：§3 tool L80–138; §4 selected evaluation protocol。

## 4. 实验、评价协议与结果的可解释范围


- **persistent state**：validated reusable asset pool and revision drafts
- **policy training feedback**：not_certified

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_smith_asset_scene`**：可验证物理资产库、候选场景、执行证据及改错循环组成仿真数据构建系统；不含下游学生回流。 失败检查驱动资产修复/再生成或局部SceneEdit，重新验证和执行；通过检查的资产进入可复用池并参与后续场景构建。
  - 来源版本：2610.07969v1；定位：§3 tool L80–138; §4 selected evaluation protocol；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 资产技能直接整合进完整scene generator仍有下游工作表述，不把局部系统拼为全部已实现管线。
- 固定输入snapshot→生成→冻结candidate→执行→独立检查；改动在新draft中，不动态改成功判据。
- 下游policy训练主要单向使用合成数据，未认证学生更新反过来改善生成器。
- 几何可达不保证任务可执行；Top-5选择指标不等于全部尝试平均成功率；sim结果不等于现实部署。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_smith` · 已存来源 · 2610.07969v1
  - https://arxiv.org/html/2610.07969；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a5a29bde8364fd8935 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
