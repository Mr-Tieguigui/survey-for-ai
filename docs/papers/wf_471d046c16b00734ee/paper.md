# SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment

> Benchmark/数据集/任务套件 · 2026 · `wf_471d046c16b00734ee`

**作者**：Sihang Jiang, Lipeng Ma, Zhonghua Hong, Keyi Wang, Zhiyu Lu, Tengfei Wang, Shisong Chen, Jinghao Zhang, Tianjun Pan, Weijia Li, Jiaqing Liang, Yanghua Xiao  
**原文**：https://arxiv.org/abs/2604.08988  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
adjacent纵向评价协议；作者的SEA定义和flywheel论证不自动成为本项目递归性判据或一般收敛保证。

## 2. 论文的核心内容与贡献

### configuration:cfg_sea_eval_longitudinal_protocol_v1
adjacent纵向评价协议；作者的SEA定义和flywheel论证不自动成为本项目递归性判据或一般收敛保证。

**适用版本**：v1；**原文定位**：§4.1–4.2 tool L212–281；§4.3 tool L282–313；§5.1–5.2 tool L315–328。
**引用权限**：`listed_configuration_scope_only`。

## 3. 任务、数据与评价设计

### cfg_sea_eval_longitudinal_protocol_v1
`cfg_sea_eval_longitudinal_protocol_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定任务流评价协议；受测OpenClaw和GenericAgent以Claude Opus4.6实例化，隔离沙箱。 |
| 改进过程与下一轮参与 | 联合观察任务成功率、token及时间序列斜率；相关/正交任务流、环境阶跃和模拟Undo反馈分别探测积累、稳定及偏好适应。 |
| 保留的状态及时间尺度 | 纵向任务流保留代理跨任务状态供测量；评测指标与任务生成/评分规则不在运行中自改。 |
| 外部固定部分 | - 任务与变体、环境变化 - 成功/资源/干预指标及模拟偏好 - harness、基础模型和沙箱 |

**配置判定**：adjacent纵向评价协议；作者的SEA定义和flywheel论证不自动成为本项目递归性判据或一般收敛保证。

来源：https://arxiv.org/html/2604.08988v1；版本：v1；定位：§4.1–4.2 tool L212–281；§4.3 tool L282–313；§5.1–5.2 tool L315–328。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r4bench_ev_cfg_sea_eval_longitudinal_protocol_v1`**：联合观察任务成功率、token及时间序列斜率；相关/正交任务流、环境阶跃和模拟Undo反馈分别探测积累、稳定及偏好适应。
  - 来源版本：v1；定位：§4.1–4.2 tool L212–281；§4.3 tool L282–313；§5.1–5.2 tool L315–328；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- v1样本量有未解冲突：L302写30原始+90变体=120；L312写30原始+60变体=90，不统一为一个数。
- L328静态实验报告12原子任务，不能用设计章节声明30任务冒充已实测全量。
- 作者实际列OpenClaw/GenericAgent，未证明测试其它本库算法。
- token下降/成功不变是诊断信号，不能单凭曲线确认因果记忆利用、用户对齐或一般安全。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r4bench_src_sea_eval` · 已存来源 · v1
  - https://arxiv.org/html/2604.08988v1；阅读深度：`selected_original_benchmark_protocol_and_limits`。

**证据深度**：unknown。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_471d046c16b00734ee --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
