# POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding

> Benchmark/数据集/任务套件 · 2024 · `wf_560486ae5e917a24f7`

**作者**：Alexey Skrynnik, Anton Andreychuk, Anatolii Borzilov, Alexander Chernyavskiy, Konstantin Yakovlev, Aleksandr Panov  
**原文**：https://arxiv.org/abs/2407.14931  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
POGEMA是partial-observation多agent grid navigation平台，区分到达固定目标的MAPF和到目标即换新目标的LMAPF。评测路径成本、完成与吞吐、OOD地图和规模；lifelong目标更换不是改进规则/模型持续自更新。

## 2. 论文的核心内容与贡献

### role:r14_role_pogema
POGEMA是partial-observation多agent grid navigation平台，区分到达固定目标的MAPF和到目标即换新目标的LMAPF。评测路径成本、完成与吞吐、OOD地图和规模；lifelong目标更换不是改进规则/模型持续自更新。

**适用版本**：2407.14931v1；**原文定位**：§3.1 mechanics/observations/reward/indicators tool L198–227；§4.1 dataset coverage tool L253–256；§4.2 metrics/OOD/scalability tool L287–300；§5 limitations tool L327–329。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_560486ae5e917a24f7`
POGEMA 提供合作多代理寻路环境、实例生成、可视化和统一评价协议，以比较学习与搜索方法；摘要没有自改或递归更新任务，不能因多代理评测直接纳入 RSI 专用 benchmark。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：背景：为多agent/具身自改方法提供潜在外部test environment，平台本身不是RSI闭环实证。
- **metrics**：- MAPF success rate、sum-of-costs/makespan；LMAPF completed goals/episode length吞吐 - 高层Performance/OOD相对best求比；另考规模、cooperation/congestion/pathfinding，不把吞吐混作RSI增长率
- **selection and reuse**：提供MARL、hybrid、search solver比较；ego-centric observation/reward可由wrapper改，必须按同setting比较。
- **split and visibility**：ID地图相似于训练；OOD用训练未见、不同障碍结构的MovingAI-tiles。不是所有baseline都需训练，不能把环境reset称数据留出。
- **task or data unit**：agent同时在grid行动，collision shielding；MAPF支持stay/disappear-at-target，LMAPF不断重新分配目标到episode结束。
- **unknowns**：- 具体地图seed/训练数据重复的独立审计unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_560486ae5e917a24f7`**：POGEMA 提供合作多代理寻路环境、实例生成、可视化和统一评价协议，以比较学习与搜索方法；摘要没有自改或递归更新任务，不能因多代理评测直接纳入 RSI 专用 benchmark。
  - 来源版本：2407.14931v3；定位：Atom entry http://arxiv.org/abs/2407.14931v3；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r14_ev_pogema`**：POGEMA是partial-observation多agent grid navigation平台，区分到达固定目标的MAPF和到目标即换新目标的LMAPF。评测路径成本、完成与吞吐、OOD地图和规模；lifelong目标更换不是改进规则/模型持续自更新。
  - 来源版本：2407.14931v1；定位：§3.1 mechanics/observations/reward/indicators tool L198–227；§4.1 dataset coverage tool L253–256；§4.2 metrics/OOD/scalability tool L287–300；§5 limitations tool L327–329；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- communication目前未在environment中disentangle；当时缺JAX/GPU并行工具集成。
- minimal observation/碰撞shield和离散grid限制生态外推；源码或基线训练未复现。
- 官方精确v1题名为Cooperative Multi-Agent Navigation；保留原Pathfinding题名作为变体，不新增paper。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- communication目前未在environment中disentangle；当时缺JAX/GPU并行工具集成。; minimal observation/碰撞shield和离散grid限制生态外推；源码或基线训练未复现。; 官方精确v1题名为Cooperative Multi-Agent Navigation；保留原Pathfinding题名作为变体，不新增paper。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_pogema` · POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding · 2407.14931v1
  - https://arxiv.org/html/2407.14931v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。
- `s18_role_src_54a38080c1c5236e` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2406.17744%2C2406.17809%2C2406.17949%2C2406.18629%2C2406.18695%2C2406.18847%2C2406.18921%2C2406.19226%2C2406.19314%2C2406.20087%2C2407.00203%2C2407.00215%2C2407.00247%2C2407.00320%2C2407.00466%2C2407.00695%2C2407.00993%2C2407.01031%2C2407.01093%2C2407.01102%2C2407.01178%2C2407.01476%2C2407.01489%2C2407.01502%2C2407.01505%2C2407.01725%2C2407.01863%2C2407.02265%2C2407.02477%2C2407.02511%2C2407.02646%2C2407.02855%2C2407.03913%2C2407.03953%2C2407.04842%2C2407.04903%2C2407.05000%2C2407.05291%2C2407.05705%2C2407.06551%2C2407.06946%2C2407.06985%2C2407.07086%2C2407.07487%2C2407.08039%2C2407.08693%2C2407.08735%2C2407.08739%2C2407.08811%2C2407.08819%2C2407.08940%2C2407.09394%2C2407.09499%2C2407.09811%2C2407.10022%2C2407.10031%2C2407.10040%2C2407.10049%2C2407.10362%2C2407.10627%2C2407.10671%2C2407.10805%2C2407.11005%2C2407.11008%2C2407.11016%2C2407.11024%2C2407.11046%2C2407.11422%2C2407.11484%2C2407.12036%2C2407.12784%2C2407.12821%2C2407.12853%2C2407.12994%2C2407.13032%2C2407.13399%2C2407.13578%2C2407.13729%2C2407.14414%2C2407.14931%2C2407.15073%2C2407.15325%2C2407.15711%2C2407.16148%2C2407.16216%2C2407.16252%2C2407.16604%2C2407.16741%2C2407.16931%2C2407.17695%2C2407.18367%2C2407.18416%2C2407.18626%2C2407.18901%2C2407.18961%2C2407.19056%2C2407.20183%2C2407.20906%2C2407.21358%2C2407.21783&max_results=100；阅读深度：`未单列`。

**证据深度**：selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_560486ae5e917a24f7 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
