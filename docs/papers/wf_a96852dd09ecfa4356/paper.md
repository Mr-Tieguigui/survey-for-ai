# Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement

> 方法论文 · 2026 · `wf_a96852dd09ecfa4356`

**作者**：Ziqi Zhao, Fanqing Meng, Haocheng Lu, Lingxiao Du, Qiguang Chen, Mengkang Hu, Xiao-Ming Wu  
**原文**：https://arxiv.org/abs/2609.36675  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：固定外部LLM、并行私有数据程序树/ledger、共享经验黑板与重启学生训练组成data-search系统；具体更新过程为：根据自身训练/eval失败诊断修订数据生成及训练recipe；每候选从同一theta0 LoRA训练，经诊断gate后用同checkpoint完成剩余任务；ledger与共享lesson影响下一候选；更新状态的保留与后继使用为：保留程序树、失败记录、leaderboard与lessons；学生不继承上一候选参数。

## 2. 论文的核心内容与贡献

### configuration:cfg_r8b_forest_data_search
只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

**适用版本**：2609.36675v1；**原文定位**：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### Gödel Forest: persistent evidence-ledger data-program search with reset students
`cfg_r8b_forest_data_search` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 固定外部LLM、并行私有数据程序树/ledger、共享经验黑板与重启学生训练组成data-search系统。 |
| 改进过程与下一轮参与 | 根据自身训练/eval失败诊断修订数据生成及训练recipe；每候选从同一theta0 LoRA训练，经诊断gate后用同checkpoint完成剩余任务；ledger与共享lesson影响下一候选。 |
| 保留的状态及时间尺度 | 保留程序树、失败记录、leaderboard与lessons；学生不继承上一候选参数。 |
| 外部固定部分 | - 基础theta0和外部rollout模型 - 训练/评价接口、预算及gate框架 - 任务身份与官方评测接口 |
| 评价与选择设置 | - **cumulative Tinker budget USD**：500 - **selection vs official**：same task identities, isolated canonical post-selection run - **student initialization**：same base theta0 for each candidate - **wall clock limit hours**：16 - **workers**：3 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：search state和每次reset学生边界明确。（状态：`supported`；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229）。
- **更新由什么过程产生**：候选学生的失败诊断驱动后继数据程序修订。（状态：`supported`；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229）。
- **状态怎样持久保留**：档案、ledger、共享lesson跨候选保留。（状态：`supported`；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229）。
- **更新怎样进入后续改进**：更新经验/程序参与下一轮Generate/Train/Review；重启学生不消除此反馈。（状态：`supported`；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229）。

**配置判定**：只判定已声明配置的状态反馈闭合；结构core与实测收益、优化器自改、部署学习分别判断。

来源：https://arxiv.org/html/2609.36675v1；版本：2609.36675v1；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229。

## 4. 实验、评价协议与结果的可解释范围


- **cumulative Tinker budget USD**：500
- **selection vs official**：same task identities, isolated canonical post-selection run
- **student initialization**：same base theta0 for each candidate
- **wall clock limit hours**：16
- **workers**：3

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r8b_ev_forest_data_search`**：固定外部LLM、并行私有数据程序树/ledger、共享经验黑板与重启学生训练组成data-search系统。 根据自身训练/eval失败诊断修订数据生成及训练recipe；每候选从同一theta0 LoRA训练，经诊断gate后用同checkpoint完成剩余任务；ledger与共享lesson影响下一候选。
  - 来源版本：2609.36675v1；定位：r8b_versioned_methods Gödel Forest tool L98–123；r8b_finaldetail Gödel Forest v1 tool L112–229；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- selection与official阶段共享任务身份；official是冻结后隔离规范复核，不是held-out任务泛化。
- 诊断子集由worker选，gate通过后同一checkpoint评剩余任务，不重新训练。
- 总16h/$500约束覆盖全forest，不是每个worker独享。
- lesson中的Attribution是作者诊断，不等于独立干预证明；不凭Gödel名称认证形式效用证明。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r8b_src_forest` · 已存来源 · 2609.36675v1
  - https://arxiv.org/html/2609.36675v1；阅读深度：`selected_primary_method_protocol_and_limits`。
- `r9_src_cfg_r8b_forest_data_search` · 已存来源 · 2609.36675v1
  - https://arxiv.org/html/2609.36675v1；阅读深度：`selected_primary_method_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_method_protocol_and_limits。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_a96852dd09ecfa4356 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
