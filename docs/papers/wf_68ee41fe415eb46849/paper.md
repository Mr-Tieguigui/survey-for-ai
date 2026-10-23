# Model-based Utility Functions

> 概念/理论/立场 · 2011 · `wf_68ee41fe415eb46849`

**作者**：Bill Hibbard  
**原文**：https://arxiv.org/abs/1111.3934  
**研究分支**：安全、攻击与持续更新治理  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
For the argmax self-modifying policy, Proposition 4 gives a non-modification result under constant geometric discounting, no environmental read/write access to its program, and changes permitted only for strict value improvement. Direct theoretical context for goal stability and how tie-breaking and agent/environment boundaries affect self-modification arguments.

### 与 RSI 的具体关系

- Direct theoretical context for goal stability and how tie-breaking and agent/environment boundaries affect self-modification arguments.

## 2. 论文的核心内容与贡献

### role:b570_01_role_1111_3934
For the argmax self-modifying policy, Proposition 4 gives a non-modification result under constant geometric discounting, no environmental read/write access to its program, and changes permitted only for strict value improvement.

**适用版本**：1111.3934v2；**原文定位**：§5 self-modification, equations 13–15 and Proposition 4 tool L622–666；Assumptions / boundaries: §5 self-modification, equations 13–15 and Proposition 4 tool L673–688。
**引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`。

### 已存角色解释 · `s18ctx_role_review_wf_68ee41fe415eb46849`
以先学习环境模型再计算模型相关效用处理自欺骗，并在通常假设下论证代理不选择修改效用；摘要明确初始结构匹配先验使其不适用于任意环境，目标保持结论须保留这些条件。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 具体机制、研究对象与协议
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18ctx_role_ev_wf_68ee41fe415eb46849`**：以先学习环境模型再计算模型相关效用处理自欺骗，并在通常假设下论证代理不选择修改效用；摘要明确初始结构匹配先验使其不适用于任意环境，目标保持结论须保留这些条件。
  - 来源版本：1111.3934v2；定位：Atom entry http://arxiv.org/abs/1111.3934v2；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`b570_01_ev_1111_3934`**：For the argmax self-modifying policy, Proposition 4 gives a non-modification result under constant geometric discounting, no environmental read/write access to its program, and changes permitted only for strict value improvement.
  - 来源版本：1111.3934v2；定位：§5 self-modification, equations 13–15 and Proposition 4 tool L622–666；Assumptions / boundaries: §5 self-modification, equations 13–15 and Proposition 4 tool L673–688；深度：`selected_primary_theorem_assumptions_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Prediction-model learning is already implicit in interaction-history inference; physical implementation changes are outside the framework. This conditional rational-agent result is not an implemented safety guarantee.
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_01_src_1111_3934` · Model-based Utility Functions · 1111.3934v2
  - https://arxiv.org/pdf/1111.3934v2；阅读深度：`selected_primary_theorem_assumptions_and_limits`。
- `s18ctx_role_src_5f39b04b550b44a8` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=0708.4311%2C0812.4360%2C1008.2972%2C1111.1797%2C1111.3934%2C1112.2127%2C1112.5309%2C1202.6177%2C1204.2328%2C1205.3139%2C1206.6389%2C1207.6868%2C1208.3719%2C1304.7827%2C1312.5602%2C1312.6034%2C1312.6114%2C1312.6199%2C1403.3773%2C1406.1078%2C1408.5093%2C1409.0473%2C1409.1556%2C1409.3215%2C1410.5401%2C1411.1373%2C1412.5068%2C1412.6980%2C1503.02531%2C1503.03585%2C1504.04909%2C1506.02626%2C1506.06724%2C1509.09169%2C1511.03246%2C1511.05952%2C1511.06349%2C1511.07289%2C1511.09249%2C1601.03411%2C1602.03506%2C1603.02484%2C1603.06155%2C1604.00624%2C1604.00772%2C1604.07269%2C1606.01540%2C1606.03498%2C1606.04671%2C1606.05250%2C1606.06565%2C1607.01474%2C1608.01413%2C1609.03543%2C1609.07093%2C1609.07434%2C1609.07843%2C1609.08000%2C1609.08144%2C1609.09106%2C1610.01235%2C1611.00020%2C1611.00685%2C1611.01578%2C1611.02779%2C1611.04831%2C1611.05418%2C1611.05763%2C1611.06204%2C1611.07718%2C1611.09268%2C1612.03975%2C1702.08495%2C1702.08608%2C1703.03400%2C1703.06748%2C1704.00028%2C1704.03242%2C1704.04861%2C1705.03551%2C1705.04414%2C1705.07874%2C1705.08417%2C1706.01284%2C1706.02515%2C1706.03946%2C1706.05296%2C1706.09254%2C1706.09763%2C1707.06170%2C1707.06347%2C1707.08476%2C1707.08819%2C1708.04680%2C1708.06733%2C1708.07747%2C1709.04555%2C1709.09816%2C1710.09974%2C1711.01558&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_theorem_assumptions_and_limits。
**当前引用权限**：`selected_primary_role_definitions_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_68ee41fe415eb46849 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
