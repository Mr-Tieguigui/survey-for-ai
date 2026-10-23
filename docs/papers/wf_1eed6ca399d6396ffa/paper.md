# RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

> Benchmark/数据集/任务套件 · 2026 · `wf_1eed6ca399d6396ffa`

**作者**：Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, Michael Qizhe Shieh  
**原文**：https://arxiv.org/abs/2607.25886  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
已核官方全文评测对象、任务协议和限制；测量协议与被测研究方法分开。

## 2. 论文的核心内容与贡献

### configuration:cfg_rsibench_data_checkpoint_research_protocol_v1
adjacent评测协议：测量跨模型数据中心研究和checkpoint选择；不把受测研究策略的反馈循环自动记成benchmark自身的RSI能力。

**适用版本**：2607.25886v1；**原文定位**：PDF physical p4 §3.1 Eqs1–2 (tool L170–191)；PDF physical pp5–6 §§3.2–4.1 (tool L240–308)；PDF physical p7 §4.2–4.3 (tool L311–333)；PDF physical pp12–13 §§5.5–6 (tool L642–672)。
**引用权限**：`listed_configuration_scope_only`。

## 3. 任务、数据与评价设计

### RSIBench-Data v1 main controlled checkpoint research protocol
`cfg_rsibench_data_checkpoint_research_protocol_v1` · evaluation_protocol

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定基模、共享LoRA-SFT/serving/Harbor–E2B评价服务、whitelist配置接口和有限资源预算组成评测协议；研究代理和其搜索历史为被测对象。 |
| 改进过程与下一轮参与 | 被测代理提出D_t与whitelist c_t，后端从同一M0训练候选；selection证据回给代理作下一数据策略/停止/checkpoint选择；官方输出评分度量所选checkpoint。协议本身不更新评价器或训练后端。 |
| 保留的状态及时间尺度 | 研究历史、数据候选和checkpoint在单次预算运行内保存；非研究代理权重自改，且每个候选从M0训练。 |
| 外部固定部分 | - 固定基模、外部rollout模型、SFT实现、服务/沙箱/验证器/评分规则、允许训练配置的白名单、预算及任务子集 |
| 评价与选择设置 | - **external rollout model**：Claude Opus 4.8 - **main budget**：nominal 16h wall clock and $500 Tinker per run - **main matrix**：4 researcher systems × 6 benchmark settings - **primary outcome**：selected checkpoint official benchmark-native score - **selection and official**：same task subset; fresh environments, not statistically held-out tasks - **target model**：Qwen/Qwen3.5-35B-A3B-Base - **training**：Tinker LoRA SFT from fixed M0 each attempt |

**配置判定**：adjacent评测协议：测量跨模型数据中心研究和checkpoint选择；不把受测研究策略的反馈循环自动记成benchmark自身的RSI能力。

来源：https://arxiv.org/pdf/2607.25886v1；版本：2607.25886v1；定位：PDF physical p4 §3.1 Eqs1–2 (tool L170–191)；PDF physical pp5–6 §§3.2–4.1 (tool L240–308)；PDF physical p7 §4.2–4.3 (tool L311–333)；PDF physical pp12–13 §§5.5–6 (tool L642–672)。

## 4. 实验、评价协议与结果的可解释范围


- **external rollout model**：Claude Opus 4.8
- **main budget**：nominal 16h wall clock and $500 Tinker per run
- **main matrix**：4 researcher systems × 6 benchmark settings
- **primary outcome**：selected checkpoint official benchmark-native score
- **selection and official**：same task subset; fresh environments, not statistically held-out tasks
- **target model**：Qwen/Qwen3.5-35B-A3B-Base
- **training**：Tinker LoRA SFT from fixed M0 each attempt

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`db4_ev_cfg_rsibench_data_checkpoint_research_protocol_v1`**：adjacent评测协议：测量跨模型数据中心研究和checkpoint选择；不把受测研究策略的反馈循环自动记成benchmark自身的RSI能力。
  - 来源版本：unknown；定位：PDF physical p4 §3.1 Eqs1–2 (tool L170–191)；PDF physical pp5–6 §§3.2–4.1 (tool L240–308)；PDF physical p7 §4.2–4.3 (tool L311–333)；PDF physical pp12–13 §§5.5–6 (tool L642–672)；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 方法§3.2固定训练基础设施，但数据及白名单内训练配置均可变；不能称纯数据单变量实验。
- selection与official用同任务子集；§6明确尚不能证明adaptive generalization。
- 每设置代表性单次运行，研究者LLM、harness和reasoning effort绑定，不能分离单组件效应。
- §5.5同family探索与主矩阵分开：所有适配checkpoint仍低于未适配基线，不认证RSI有效能力增益。
- 原文HTML v1不可得，已读的是官方v1 PDF工具文本，hash不是PDF原始字节。
- 方法§3.2固定训练基础设施，但数据及白名单内训练配置均可变；不能称纯数据单变量实验。; selection与official用同任务子集；§6明确尚不能证明adaptive generalization。; 每设置代表性单次运行，研究者LLM、harness和reasoning effort绑定，不能分离单组件效应。; §5.5同family探索与主矩阵分开：所有适配checkpoint仍低于未适配基线，不认证RSI有效能力增益。; 原文HTML v1不可得，已读的是官方v1 PDF工具文本，hash不是PDF原始字节。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `db4_src_rsibench_data` · 已存来源 · 2607.25886v1
  - https://arxiv.org/pdf/2607.25886v1；阅读深度：`selected_official_fulltext_protocol_and_limits`。

**证据深度**：original_abstract。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_1eed6ca399d6396ffa --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
