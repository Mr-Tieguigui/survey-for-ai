# Reflexion: Language Agents with Verbal Reinforcement Learning

> 方法论文 · 2023 · `wf_3fb5d6b0a837235b64`

**作者**：Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao  
**原文**：https://arxiv.org/abs/2303.11366  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：Actor/Evaluator/反思器及反思记忆；具体更新过程为：反思器读取已有mem和轨迹并写入新反思；Actor在下次试次读取mem；更新状态的保留与后继使用为：同一任务的多次完整试次，通常保留1–3项。

## 2. 论文的核心内容与贡献

### configuration:cfg_reflexion
跨完整试次符合本项目保留条件；不能外推为跨任务、跨会话永久记忆

**适用版本**：v4；**原文定位**：S3.p1；S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_reflexion
`cfg_reflexion` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | Actor/Evaluator/反思器及反思记忆 |
| 改进过程与下一轮参与 | 反思器读取已有mem和轨迹并写入新反思；Actor在下次试次读取mem |
| 保留的状态及时间尺度 | 同一任务的多次完整试次，通常保留1–3项 |
| 外部固定部分 | LM参数、评价器和上下文上限 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：Actor/Evaluator/反思器及反思记忆（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px4.p1；S3.SS0.SSS0.Px5.p1）。
- **更新由什么过程产生**：反思器读取已有mem和轨迹并写入新反思；Actor在下次试次读取mem（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px4.p1；S3.SS0.SSS0.Px5.p1）。
- **状态怎样持久保留**：同一任务的多次完整试次，通常保留1–3项（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px4.p1；S3.SS0.SSS0.Px5.p1）。
- **更新怎样进入后续改进**：反思器读取已有mem和轨迹并写入新反思；Actor在下次试次读取mem（状态：`supported`；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px4.p1；S3.SS0.SSS0.Px5.p1）。

**配置判定**：跨完整试次符合本项目保留条件；不能外推为跨任务、跨会话永久记忆

来源：https://arxiv.org/html/2303.11366v4；版本：v4；定位：S3.p1；S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_reflexion`**：反思器读取已有mem和轨迹并写入新反思；Actor在下次试次读取mem
  - 来源版本：v4；定位：S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px4.p1；S3.SS0.SSS0.Px5.p1；深度：`AI_primary_method_passage_recheck`。

- **`oct15_agents_ev_r2_voyager_reflexion_5`**：Voyager将环境状态成功判断与失败批评组合为自验证，并在成功后把可执行程序加入跨任务技能库；Reflexion原配置已有独立Evaluator，反思器读取奖励、轨迹和既有记忆，为后续完整试次生成反思记忆。两者应按反馈组合与保留对象对照，不能称Reflexion没有成功评价。
  - 来源版本：unknown；定位：参见来源索引；深度：`author_local_comparison_plus_curator_two_endpoint_boundary_correction`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Reflexion包含独立Evaluator角色，评价可由EM、手写启发式或LLM实现。
- 反思记忆通常保留1–3项，原配置不能外推跨任务永久记忆。
- 跨
- 完
- 整
- 试
- 次
- 符
- 合
- 本
- 项
- 目
- 保
- 留
- 条
- 件
- ；
- 不
- 能
- 外
- 推
- 为
- 任
- 务
- 、
- 会
- 话
- 永
- 久
- 记
- 忆
- Voyager§2.3将其自验证称为比自反思更全面是作者局部表述，不表示原Reflexion框架缺Evaluator。Voyager§3.2明确为其Minecraft Reflexion基线添加执行错误与Voyager自验证；该适配基线不能等同原Reflexion完整配置。技能库与反思记忆的机制比较不认证代码继承、统一性能优势或跨任务永久记忆。

## 7. 与其他论文的具体关系

### [ExpeL: LLM Agents Are Experiential Learners](../r03_method/wf_984256074226b209d4.md)
关系：`adapts_design_of` · `r2_expel_reflexion_4` · 当前展示权限：`primary_supported`。
ExpeL明确在训练经验收集阶段采用Reflexion的失败轨迹反思与同任务重试：失败后累积反思文本并输入下一次ReAct试次；随后把跨任务经验用于insights提取。Reflexion原方法确认Actor、Evaluator、反思器及跨试次反思记忆循环。

**关系边界**：适配关系仅覆盖训练经验收集组件；ExpeL主部署配置单次作答，§5.5另有测试重试变体，不能把两个配置混合。Reflexion原文反思记忆通常只保留1–3条，不认证跨任务永久记忆；未检查代码复用。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S5.SS5.p1；A4.SS5.p1。
- object：https://arxiv.org/html/2303.11366v4；版本：v4；定位：S3.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。
- expand_src_w_expel：https://arxiv.org/html/2308.10144v3；版本：v3；定位：S4.SS1.p1；S4.SS2.SSSx2.p1；S4.SS2.SSSx2.p2；S4.SS3.p1。

### [Voyager: An Open-Ended Embodied Agent with Large Language Models](../r03_method/wf_b71b1297191d522793.md)
关系：`contrasts_system_boundary_with` · `r2_voyager_reflexion_5` · 当前展示权限：`primary_supported`。
Voyager将环境状态成功判断与失败批评组合为自验证，并在成功后把可执行程序加入跨任务技能库；Reflexion原配置已有独立Evaluator，反思器读取奖励、轨迹和既有记忆，为后续完整试次生成反思记忆。两者应按反馈组合与保留对象对照，不能称Reflexion没有成功评价。

**关系边界**：Voyager§2.3将其自验证称为比自反思更全面是作者局部表述，不表示原Reflexion框架缺Evaluator。Voyager§3.2明确为其Minecraft Reflexion基线添加执行错误与Voyager自验证；该适配基线不能等同原Reflexion完整配置。技能库与反思记忆的机制比较不认证代码继承、统一性能优势或跨任务永久记忆。

**已存关系来源与定位（保留原记录端点语义）**：
- subject：https://arxiv.org/html/2305.16291v2；版本：v2；定位：S2.SS2.p2；S2.SS2.p3；S2.SS3.p1；S2.SS3.p2；S3.SS2.p1；S3.SS2.p3。
- object：https://arxiv.org/html/2303.11366v4；版本：v4；定位：S3.p1；S3.SS0.SSS0.Px2.p1；S3.SS0.SSS0.Px3.p1；S3.SS0.SSS0.Px5.p1。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_reflexion` · Reflexion · v4
  - https://arxiv.org/html/2303.11366v4；阅读深度：`未单列`。
- `oct15_agents_src_w_reflexion` · 已存来源 · v4
  - https://arxiv.org/html/2303.11366v4；阅读深度：`selected_two_endpoint_primary_method_passages`。
- `oct15_agents_src_w_voyager` · 已存来源 · v2
  - https://arxiv.org/html/2305.16291v2；阅读深度：`selected_two_endpoint_primary_method_passages`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_3fb5d6b0a837235b64 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
