# ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents

> 方法论文 · 2026 · `wf_4c466e96bed2a78fbb`

**作者**：Elzo Brito dos Santos Filho  
**原文**：https://arxiv.org/abs/2606.23752  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
ESAA-Conversational 用可见对话事件日志及确定性投影维护异构编码代理交接，LLM 只参与显式整理；摘要的 self-referential 指开发案例，持久日志本身不证明改进器能力递归提升。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_esaa_memory_layer
保留所读边界；不由标题、持久日志或摘要自我表述认证core。

**适用版本**：unversioned_observed；**原文定位**：§3–4 tool L100–111, L130–304; §6 case L380–459。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_4c466e96bed2a78fbb`
ESAA-Conversational 用可见对话事件日志及确定性投影维护异构编码代理交接，LLM 只参与显式整理；摘要的 self-referential 指开发案例，持久日志本身不证明改进器能力递归提升。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### ESAA-Conversational: event-sourced memory infrastructure view
`cfg_r8b_esaa_memory_layer` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 确定性日志采集、投影、交接与显式curation组成可见对话记忆层；所判配置限定于该记忆基础设施。 |
| 改进过程与下一轮参与 | 采集可见事件形成append-only日志，投影为后续上下文，LLM仅在显式整理阶段参与。 |
| 保留的状态及时间尺度 | 持久事件日志和派生读模型跨会话保留。 |
| 外部固定部分 | - 确定性采集/投影逻辑 - 工作区过滤、lock与adapter接口 - 外部代理与人工开发编排 |
| 评价与选择设置 | - **selected view**：memory_layer_only_not_whole_private_development_workflow |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：记忆层与代理边界可定位。（状态：`supported`；定位：§3–4 tool L100–111, L130–304; §6 case L380–459）。
- **更新由什么过程产生**：机械capture及显式整理本身未定位可评价的自诱发能力更新；私有开发案例另有人工编排。（状态：`unknown`；定位：§3–4 tool L100–111, L130–304; §6 case L380–459）。
- **状态怎样持久保留**：日志及读模型可持久。（状态：`supported`；定位：§3–4 tool L100–111, L130–304; §6 case L380–459）。
- **更新怎样进入后续改进**：未来代理可读取记忆，但所读配置未闭合可评价的改进—后继改进链；不否认更宽开发系统可能闭合。（状态：`unknown`；定位：§3–4 tool L100–111, L130–304; §6 case L380–459）。

**配置判定**：保留所读边界；不由标题、持久日志或摘要自我表述认证core。

来源：https://arxiv.org/html/2606.23752；版本：unversioned_observed；定位：§3–4 tool L100–111, L130–304; §6 case L380–459。

## 4. 实验、评价协议与结果的可解释范围


- **selected view**：memory_layer_only_not_whole_private_development_workflow

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_4c466e96bed2a78fbb`**：ESAA-Conversational 用可见对话事件日志及确定性投影维护异构编码代理交接，LLM 只参与显式整理；摘要的 self-referential 指开发案例，持久日志本身不证明改进器能力递归提升。
  - 来源版本：2606.23752v1；定位：Atom entry http://arxiv.org/abs/2606.23752v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`r8b_ev_esaa_memory_layer`**：确定性日志采集、投影、交接与显式curation组成可见对话记忆层；所判配置限定于该记忆基础设施。 采集可见事件形成append-only日志，投影为后续上下文，LLM仅在显式整理阶段参与。
  - 来源版本：unversioned_observed；定位：§3–4 tool L100–111, L130–304; §6 case L380–459；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 私有self-development事件案例不是受控因果实验或全自主meta闭环。
- 公开greenfield测试不等于公开完整私有历史；redaction、cold replay与hash-chain属于后续工作。
- 零LLM-token仅指机械capture，不涵盖curation。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_esaa` · 已存来源 · unversioned_observed
  - https://arxiv.org/html/2606.23752；阅读深度：`selected_primary_method_protocol_and_limits`。
- `s18_role_src_c39c3f10395bfa2a` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2606.21005%2C2606.21037%2C2606.21124%2C2606.21262%2C2606.21339%2C2606.21401%2C2606.21445%2C2606.21559%2C2606.21597%2C2606.21627%2C2606.21710%2C2606.21811%2C2606.21856%2C2606.21930%2C2606.22263%2C2606.22329%2C2606.22330%2C2606.22417%2C2606.22495%2C2606.22528%2C2606.22678%2C2606.22723%2C2606.22783%2C2606.22844%2C2606.22877%2C2606.22913%2C2606.22918%2C2606.22950%2C2606.22961%2C2606.23032%2C2606.23038%2C2606.23104%2C2606.23130%2C2606.23255%2C2606.23387%2C2606.23449%2C2606.23629%2C2606.23752%2C2606.23835%2C2606.23927%2C2606.23991%2C2606.24051%2C2606.24064%2C2606.24155%2C2606.24177%2C2606.24292%2C2606.24311%2C2606.24370%2C2606.24496%2C2606.24530%2C2606.24595%2C2606.24773%2C2606.24775%2C2606.24786%2C2606.24937%2C2606.24965%2C2606.25039%2C2606.25057%2C2606.25139%2C2606.25189%2C2606.25207%2C2606.25358%2C2606.25407%2C2606.25447%2C2606.25996%2C2606.26057%2C2606.26080%2C2606.26300%2C2606.26429%2C2606.26614%2C2606.26669%2C2606.26722%2C2606.26728%2C2606.26806%2C2606.26859%2C2606.26935%2C2606.27136%2C2606.27146%2C2606.27180%2C2606.27188%2C2606.27316%2C2606.27330%2C2606.27350%2C2606.27359%2C2606.27446%2C2606.27593%2C2606.27619%2C2606.27666%2C2606.27780%2C2606.27922%2C2606.28050%2C2606.28249%2C2606.28270%2C2606.28347%2C2606.28349%2C2606.28370%2C2606.28406%2C2606.28409%2C2606.28413%2C2606.28570&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_4c466e96bed2a78fbb --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
