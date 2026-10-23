# Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

> 方法论文 · 2025 · `wf_title_1935c85b092513ff`

**作者**：Wenyi Wang, Piotr Piękos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jürgen Schmidhuber  
**原文**：https://arxiv.org/abs/2510.21614  
**研究分支**：代理架构、harness与代码  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：agent tree and accepted child code; fixed: HGM expansion/evaluation scheduler, benchmark and scoring, backbone weights；具体更新过程为：被选择的代理运行自身代码生成修改，保留的后代可再作父代；更新状态的保留与后继使用为：within archived development run。

## 2. 论文的核心内容与贡献

### configuration:cfg_hgm_swe500
所列原文支持声明边界内四条件；不升级为改进器收益或全面自主性。

**适用版本**：v3；**原文定位**：Section 2; Section 3.3; Section 4.3.1; Appendix C.1。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_hgm_swe60
所列原文支持声明边界内四条件；不升级为改进器收益或全面自主性。

**适用版本**：v3；**原文定位**：Section 2 (actions m_a); Section 3.3; Section 4.2; Appendix C.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_hgm_swe60
`cfg_hgm_swe60` · HGM SWE-Verified-60 comparison

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | agent tree and accepted child code; fixed: HGM expansion/evaluation scheduler, benchmark and scoring, backbone weights |
| 改进过程与下一轮参与 | 被选择的代理运行自身代码生成修改，保留的后代可再作父代。 |
| 保留的状态及时间尺度 | within archived development run |

**配置判定**：所列原文支持声明边界内四条件；不升级为改进器收益或全面自主性。

来源：https://arxiv.org/html/2510.21614v3；版本：v3；定位：Section 2 (actions m_a); Section 3.3; Section 4.2; Appendix C.1。

### cfg_hgm_swe500
`cfg_hgm_swe500` · HGM full SWE-Bench Verified optimization

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | agent tree and accepted child code; fixed: HGM scheduler, benchmark and scoring, backbone weights |
| 改进过程与下一轮参与 | 同一自修改树机制；保留子代理可继续生成后代。 |
| 保留的状态及时间尺度 | within full-500 development run |

**配置判定**：所列原文支持声明边界内四条件；不升级为改进器收益或全面自主性。

来源：https://arxiv.org/html/2510.21614v3；版本：v3；定位：Section 2; Section 3.3; Section 4.3.1; Appendix C.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_hgm`**：HGM把DGM/SICA视为树搜索实例，分析任务成绩与后代生产力的错配。
  - 来源版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1；深度：`AI_rechecked_primary_text_author_report`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 有限基准内分析，非无条件全局最优证明

## 7. 与其他论文的具体关系

### [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../r03_method/wf_c29f716871f8031486.md)
关系：`evaluates_configuration` · `r_hgm_dgm` · 当前展示权限：`primary_supported`。
HGM在SWE-Verified-60/Polyglot运行树上分析DGM选择指标与后代clade实证生产力的关系。

**关系边界**：配置限于该研究的算法实例和离线树分析，原DGM完整任务集/预算不等同；经验后代最大值是有界估计，不是内在改进能力的普遍测量。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- object：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p2；S3.p3。
- recheck_src_w_hgm：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- recheck_src_w_dgm：https://arxiv.org/html/2505.22954v3；版本：v3；定位：S3.p2；S3.p3。

### [A Self-Improving Coding Agent](../r03_method/wf_f5d4d370636d9b3832.md)
关系：`evaluates_configuration` · `r_hgm_sica` · 当前展示权限：`primary_supported`。
HGM在其SWE-Verified-60/Polyglot算法比较中分析SICA的任务得分选择准则与后代clade实证生产力。

**关系边界**：只认证HGM研究中的SICA式算法实例与选择分析，不把结果推广到全部SICA版本或任务；相关性不是因果能力保证。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- object：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。
- recheck_src_w_hgm：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p1；S2.p3；S4.SS1.p1。
- recheck_src_w_sica：https://arxiv.org/html/2504.15228v2；版本：v2；定位：S3.p1；S3.p3。

### [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](../r04_system/wf_616c2bdc62bb176053.md)
关系：`adapts_design_of` · `r3_red_queen_adapts_hgm_search` · 当前展示权限：`primary_supported`。
RQGM v3 §3.1与Appendix B.2明确沿用HGM的CMP/Thompson父节点采样、节点自身计数评价采样及UCB-Air扩展门控；HGM v3 §3.3原方法确认这三个组成。

**关系边界**：谱系只落在搜索调度组件；不代表完整SWE60实验配置、代码逐行复用或理论保证无条件继承。RQGM只在epoch内满足剩余假设时讨论HGM分析；跨epoch额外要求受控替换与依赖记录擦除。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/pdf/2606.26294v3；版本：v3；定位：PDF p.3 §3.1；PDF p.18 Appendix B.2。
- object：https://arxiv.org/html/2510.21614v3；版本：v3；定位：S2.p3.1；S3.SS3.SSS0.Px1.p2.1；S3.SS3.SSS0.Px1.p5.1；S3.SS3.SSS0.Px2.p1.1；S3.SS3.SSS0.Px3.p2.1。

## 8. 来源清单、复查入口与解析缺口
- `recheck_src_w_hgm` · 已存来源 · v3
  - https://arxiv.org/html/2510.21614v3；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_1935c85b092513ff --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
