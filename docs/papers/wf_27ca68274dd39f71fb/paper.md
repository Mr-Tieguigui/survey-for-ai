# Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation

> 方法论文 · 2023 · `wf_27ca68274dd39f71fb`

**作者**：Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai  
**原文**：https://arxiv.org/abs/2310.02304  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：后继改进程序 I_t；具体更新过程为：后继 I_t 用于生成下一轮 I_(t+1)；更新状态的保留与后继使用为：代码跨自改进轮保留；LM不更新。

## 2. 论文的核心内容与贡献

### configuration:cfg_stop
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：2310.02304v3；**原文定位**：PDF physical p2 Introduction；PDF physical p3 §2 Recursive Self-Improvement；PDF physical p4 §3 Algorithm 1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_stop
`cfg_stop` · method_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 后继改进程序 I_t。 |
| 改进过程与下一轮参与 | 后继 I_t 用于生成下一轮 I_(t+1)。 |
| 保留的状态及时间尺度 | 代码跨自改进轮保留；LM不更新。 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/pdf/2310.02304v3；版本：2310.02304v3；定位：PDF physical p2 Introduction；PDF physical p3 §2 Recursive Self-Improvement；PDF physical p4 §3 Algorithm 1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_stop`**：后继改进器由前代改进器生成，并进入后续递归轮。
  - 来源版本：v3；定位：PDF physical p.4, Algorithm 1；深度：`AI_rechecked_primary_text_author_report`。

- **`e_stop_theory`**：作者将工作置于RSI理论背景，但不证明脚手架修改最优。
  - 来源版本：v3；定位：PDF physical p.3, Related Work；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只更新代码scaffold/改进程序，不更新底层LM权重。
- meta-utility任务、评价程序和外层迭代驱动固定；未证明代码改进最优。
- LM与元效用固定；完整实验协议未重审
- 理论启发，不传播Gödel定理保证

## 7. 与其他论文的具体关系

### [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../r02_concept/wf_0e73b118b5b1559785.md)
关系：`conceptually_motivated_by` · `r_stop_godel` · 当前展示权限：`primary_supported`。
STOP在相关工作中明确将Gödel Machine列为递归自改进的严格形式化先驱；STOP实际以固定LM、固定meta-utility任务与外部驱动迭代更新改进程序I，未建立Gödel Machine的证明搜索与全局最优切换条件。

**关系边界**：概念动机边；不认证直接算法、代码继承或Gödel最优性保证。STOP原文明确没有证明scaffold改进最优，底层LM固定。Gödel保证依赖形式公理、证明搜索与所声明效用和环境假设。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/pdf/2310.02304v3；版本：2310.02304v3；定位：PDF physical p3 §2 Recursive Self-Improvement；PDF physical p4 §3 Algorithm 1。
- object：https://arxiv.org/html/cs/0309048v5；版本：cs/0309048v5；定位：S2.SS2.p1；S4.SS1.p1。

## 8. 来源清单、复查入口与解析缺口
- `oct15_root_src_w_stop` · 已存来源 · 2310.02304v3
  - https://arxiv.org/pdf/2310.02304v3；阅读深度：`selected_primary_method_and_limits_passages`。
- `recheck_src_w_stop` · 已存来源 · v3
  - https://arxiv.org/pdf/2310.02304v3；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_27ca68274dd39f71fb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
