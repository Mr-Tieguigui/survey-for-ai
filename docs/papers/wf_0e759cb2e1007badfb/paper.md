# AI Safety Gridworlds

> Benchmark/数据集/任务套件 · 2017 · `wf_0e759cb2e1007badfb`

**作者**：Jan Leike, Miljan Martic, Victoria Krakovna, Pedro A. Ortega, Tom Everitt, Andrew Lefrancq, Laurent Orseau, Shane Legg  
**原文**：https://arxiv.org/abs/1711.09883  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
AI Safety Gridworlds把可见reward与隐藏安全performance R*区分，用小型RL环境测试规格错误和鲁棒性。self-modification任务是whisky触发探索率升至0.9的有限扰动，主要测代理避免有害自变的能力，不能解释为构造更强后继或RSI加速实验。

## 2. 论文的核心内容与贡献

### role:r11_role_safety_gridworlds
AI Safety Gridworlds把可见reward与隐藏安全performance R*区分，用小型RL环境测试规格错误和鲁棒性。self-modification任务是whisky触发探索率升至0.9的有限扰动，主要测代理避免有害自变的能力，不能解释为构造更强后继或RSI加速实验。

**适用版本**：1711.09883v1；**原文定位**：§2 environment formalization tool L98–109；§2.2.1 self-modification tool L169–180；§3.2 results tool L245–255；§4 discussion tool L256–259；§1 scope/limitations tool L57–62。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

### 已存角色解释 · `s18_role_review_wf_0e759cb2e1007badfb`
AI Safety Gridworlds 提供安全中断、副作用、奖励博弈及自修改稳健性等强化学习环境，以对代理隐藏的性能函数区分规范和稳健性问题；是安全评测基础，不自动等于递归改进 benchmark。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：提供RSI自变安全、reward gaming和目标保真的历史评测基础；实际self-modification只是行为探索参数被环境改动，不是自主代码/学习算子升级。
- **leakage and information boundary**：隐藏performance是实验设计约束；真正进步要求跨环境泛化。对特定ad hoc R*调参不能当解决整个安全问题类别。
- **metrics**：- 分别报告可见reward return与隐藏performance function return；规格问题二者不同，鲁棒性问题二者相同 - 图10对15种子均值、100episode平滑；不把安全performance分数当可见训练reward
- **selection and reuse**：作者为学好可见reward进行了hyperparameter tuning；隐藏performance供外部评价。讨论明确反对窥视performance再过拟合suite，若用human feedback评价环境不可再给反馈。
- **split and visibility**：每episode reset不等于统计留出；lava world专门从训练地图转至桥/熔岩边界偏移的测试地图，作者强调未在多地图变体训练。其他环境不统一宣称train/test split。
- **task or data unit**：不大于10×10的episodic gridworld；最多100步、四方向动作，环境特定安全目标；基线A2C与Rainbow，并用Sarsa更新变体对照self-modification。
- **unknowns**：- 现代LLM代理在这些环境的外部有效性unknown - 原实现commit及复现随机种子结果未核

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_0e759cb2e1007badfb`**：AI Safety Gridworlds 提供安全中断、副作用、奖励博弈及自修改稳健性等强化学习环境，以对代理隐藏的性能函数区分规范和稳健性问题；是安全评测基础，不自动等于递归改进 benchmark。
  - 来源版本：1711.09883v2；定位：Atom entry http://arxiv.org/abs/1711.09883v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r11_ev_safety_gridworlds`**：AI Safety Gridworlds把可见reward与隐藏安全performance R*区分，用小型RL环境测试规格错误和鲁棒性。self-modification任务是whisky触发探索率升至0.9的有限扰动，主要测代理避免有害自变的能力，不能解释为构造更强后继或RSI加速实验。
  - 来源版本：1711.09883v1；定位：§2 environment formalization tool L98–109；§2.2.1 self-modification tool L169–180；§3.2 results tool L245–255；§4 discussion tool L256–259；§1 scope/limitations tool L57–62；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 每R*为单环境定制，能否泛化到同类其他实例仍开放；省略interpretability、multi-agent、formal verification及scalable oversight等问题。
- 普通RL基线没有处理规格错误的专用机制，失败不构成所有安全学习方法的不可能性定理。
- 没有运行原实现；仅所选protocol/self-modification/limits段核查。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 每R*为单环境定制，能否泛化到同类其他实例仍开放；省略interpretability、multi-agent、formal verification及scalable oversight等问题。; 普通RL基线没有处理规格错误的专用机制，失败不构成所有安全学习方法的不可能性定理。; 没有运行原实现；仅所选protocol/self-modification/limits段核查。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_safety_gridworlds` · AI Safety Gridworlds · 1711.09883v1
  - https://arxiv.org/html/1711.09883v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。
- `s18_role_src_36dcd0fd301066b1` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=1711.03938%2C1711.03953%2C1711.04340%2C1711.05101%2C1711.07414%2C1711.09846%2C1711.09883%2C1712.01815%2C1712.06567%2C1712.07040%2C1801.02668%2C1801.10314%2C1802.06070%2C1802.07569%2C1803.02999%2C1803.03453%2C1803.04585%2C1803.05457%2C1803.10122%2C1804.03980%2C1804.06893%2C1805.00899%2C1805.01109%2C1805.09613%2C1805.11604%2C1805.11973%2C1805.12069%2C1805.12114%2C1806.00178%2C1806.01261%2C1806.07937%2C1806.08730%2C1806.09030%2C1807.00734%2C1807.05076%2C1808.08745%2C1808.09422%2C1808.09468%2C1809.02156%2C1809.07124%2C1809.09600%2C1809.11096%2C1810.00069%2C1810.00123%2C1810.04805%2C1810.07074%2C1810.08272%2C1810.10535%2C1810.10863%2C1811.00739%2C1811.01241%2C1811.07871%2C1811.08886%2C1812.01070%2C1812.01825%2C1812.08775%2C1812.10757%2C1901.02860%2C1901.09492%2C1901.10995%2C1902.03689%2C1902.04043%2C1902.06705%2C1902.07638%2C1902.09469%2C1903.00161%2C1903.06733%2C1903.08772%2C1903.09848%2C1903.10145%2C1903.12261%2C1904.07734%2C1904.09675%2C1904.09728%2C1904.10509%2C1904.12901%2C1905.01386%2C1905.07830%2C1905.09717%2C1905.10044%2C1905.10847%2C1905.10985%2C1905.13053%2C1906.02243%2C1906.05015%2C1906.08253%2C1906.08663%2C1906.11951%2C1907.00909%2C1907.03651%2C1907.09190%2C1907.11692%2C1907.12108%2C1908.04734%2C1908.10084%2C1909.01095%2C1909.02622%2C1909.03848%2C1909.06146%2C1909.06576&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_0e759cb2e1007badfb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
