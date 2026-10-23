# ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces

> Benchmark/数据集/任务套件 · 2026 · `wf_0d7c44713fe9e287e3`

**作者**：Xiangyi Li, Kyoung Whan Choe, Yimin Liu, Xiaokun Chen, Chujun Tao, Bingran You, Wenbo Chen, Zonglin Di, Jiankai Sun, Shenghan Zheng, Jiajun Bao, Yuanli Wang, Weixiang Yan, Yiyuan Li, Han-chung Lee  
**原文**：https://arxiv.org/abs/2604.05172  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ClawsBench以五个有状态mock服务上的44项任务测量代理完成能力和危险操作，数据库前后状态提供确定性部分得分。TSR、UAR、SCR分开；技能与meta prompt是实验因素。当前评测为single-shot，闭环技能精炼列为未来方向。

## 2. 论文的核心内容与贡献

### role:r11_role_clawsbench
ClawsBench以五个有状态mock服务上的44项任务测量代理完成能力和危险操作，数据库前后状态提供确定性部分得分。TSR、UAR、SCR分开；技能与meta prompt是实验因素。当前评测为single-shot，闭环技能精炼列为未来方向。

**适用版本**：2604.05172v1；**原文定位**：§3.3–4.1 state/scoring tool L189–202；§4.5–5.1 pilot/conditions tool L239–257；§5.1 metrics tool L281–285；§6 limitations/future tool L370–375。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：为自改代理外壳/技能提供能力与安全分离的评测模块；已报告实验未执行在线闭环技能自更新。
- **leakage and information boundary**：代理不能读取任务答案/种子文件的沙箱权限隔离是防绕过设计，作者也观察到逃逸尝试；pilot与main共享任务，因此不能声称独立任务泛化。
- **metrics**：- TSR=非安全任务得分≥0.8的比例 - UAR=安全任务得分<0的比例；SCR=安全任务得分≥0.8的比例 - task-level cluster bootstrap置信区间；5次重复下单任务估计仍嘈杂
- **selection and reuse**：固定领域技能与pilot归纳meta prompt按on/off条件比较；11个model–harness组合只有5个完整2×2，其余为不完整factorial。
- **split and visibility**：运行前从种子数据恢复隔离数据库快照；这属于执行复位，不能称统计留出任务集。meta prompt由40任务×30重复的pilot失败分析得到；main测44任务。
- **task or data unit**：单元为任务×model–harness×scaffolding条件×重复；20项非安全任务、24项安全任务，33条件每任务5次重复；五服务含14项跨服务任务。
- **unknowns**：- 代码级权限隔离是否不可绕过unknown - 同任务pilot调prompt后的独立任务效果unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r11_ev_clawsbench`**：ClawsBench以五个有状态mock服务上的44项任务测量代理完成能力和危险操作，数据库前后状态提供确定性部分得分。TSR、UAR、SCR分开；技能与meta prompt是实验因素。当前评测为single-shot，闭环技能精炼列为未来方向。
  - 来源版本：2604.05172v1；定位：§3.3–4.1 state/scoring tool L189–202；§4.5–5.1 pilot/conditions tool L239–257；§5.1 metrics tool L281–285；§6 limitations/future tool L370–375；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- mock省略rate limiting、latency和concurrent access，五服务44任务且无human baseline。
- single-shot；不计推理质量或成本，不完整factorial限制交互结论。
- 跨服务更危险与任务复杂度混杂；结构安全约束主要来自harness比较并未系统变更。
- mock省略rate limiting、latency和concurrent access，五服务44任务且无human baseline。; single-shot；不计推理质量或成本，不完整factorial限制交互结论。; 跨服务更危险与任务复杂度混杂；结构安全约束主要来自harness比较并未系统变更。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_clawsbench` · ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces · 2604.05172v1
  - https://arxiv.org/html/2604.05172v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0d7c44713fe9e287e3 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
