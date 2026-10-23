# MetaAgent: Toward Self-Evolving Agent via Tool Meta-Learning

> 方法论文 · 2025 · `wf_4bfe11db2c978c65f0`

**作者**：Hongjin Qian, Zheng Liu  
**原文**：https://arxiv.org/abs/2508.00271  
**研究分支**：工具、技能与经验复用  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：冻结LM及工具调用框架内的累积经验E和知识库C；具体更新过程为：E/C条件化后续工具规划/反思；任务内自反思和答题后verified反思分开；更新状态的保留与后继使用为：跨任务E/C保留；自反思也可在本任务内反馈。

## 2. 论文的核心内容与贡献

### configuration:cfg_metaagent
Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

**适用版本**：v2；**原文定位**：Section 2.2 Eqs.6-7。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_metaagent
`cfg_metaagent` · explicit_boundary_from_previous_primary_recheck

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LM及工具调用框架内的累积经验E和知识库C |
| 改进过程与下一轮参与 | E/C条件化后续工具规划/反思；任务内自反思和答题后verified反思分开 |
| 保留的状态及时间尺度 | 跨任务E/C保留；自反思也可在本任务内反馈 |
| 外部固定部分 | 基模型与工具路由，C可预构建 |

**配置判定**：Structural core within the explicitly stated boundary; not a claim of universal/full RSI, improver gain or autonomy.

来源：https://arxiv.org/abs/2508.00271v2；版本：v2；定位：Section 2.2 Eqs.6-7。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e_metaagent`**：经验E与知识库C保留；答题后verified reflection用于后续任务。
  - 来源版本：v2；定位：S2.SS2.p7；S2.SS2.SSS0.Px1.p3；S3.SS1.SSS0.Px3.p1；深度：`AI_rechecked_primary_text_author_report`。

- **`e_metaagent_split`**：自反思可回到当前任务；答题后验证反思的经验只用于后续任务。
  - 来源版本：v2；定位：S2.SS2.SSS0.Px1.p2；S2.SS2.SSS0.Px1.p3；深度：`AI_rechecked_primary_text_author_report`。

- **`accel_ev_metaagent_gt_boundary`**：验证反思使用答案反馈，其经验仅用于后续任务；工具路由和模型参数固定。
  - 来源版本：unknown；定位：§2.2 Self-Refinement following Eq.7；§2.2 Self-Expansion first paragraph；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 知识库可有预构建阶段；工具路由及模型固定
- 不能把两种保留边界混写
- 不能称无反馈、参数自训练或工具路由器递归改进。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_metaagent_v2` · 已存来源 · v2
  - https://arxiv.org/html/2508.00271v2；阅读深度：`未单列`。
- `recheck_src_w_metaagent` · 已存来源 · v2
  - https://arxiv.org/html/2508.00271v2；阅读深度：`未单列`。

**证据深度**：selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4bfe11db2c978c65f0 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
