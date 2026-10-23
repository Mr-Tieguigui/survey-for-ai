# Active Retrieval Augmented Generation

> 背景/相邻基础 · 2023 · `wf_f6446cf96f9c362b99`

**作者**：Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, Graham Neubig  
**原文**：https://aclanthology.org/2023.emnlp-main.495/  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
主动决定检索时机和内容的相邻基础；原方法没有跨独立输出提交持久改进状态。

## 2. 论文的核心内容与贡献

### configuration:cfg_flare_active_retrieval
主动检索背景配置；未提交供后续独立任务使用的改进状态。 Confident-token trigger is specific to FLARE_direct; FLARE_instruct is a separate variant.

**适用版本**：EMNLP-2023-version-of-record；**原文定位**：§2；§3；Fig.1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 具体机制、研究对象与协议

### FLARE_direct confidence-triggered retrieval
`cfg_flare_active_retrieval` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结LM、文档库、检索器和句子级置信触发 |
| 改进过程与下一轮参与 | 预测下一句，低置信触发检索并重生成该句 |
| 保留的状态及时间尺度 | 当前长文本生成内的前缀和检索上下文 |
| 外部固定部分 | LM、文档库、触发阈值和检索算法 |

**配置判定**：主动检索背景配置；未提交供后续独立任务使用的改进状态。 Confident-token trigger is specific to FLARE_direct; FLARE_instruct is a separate variant.

来源：https://aclanthology.org/2023.emnlp-main.495.pdf；版本：EMNLP-2023-version-of-record；定位：§2；§3；Fig.1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `registered_cfg_src_c3331df991408294` · 已存来源 · EMNLP-2023-version-of-record
  - https://aclanthology.org/2023.emnlp-main.495.pdf；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_f6446cf96f9c362b99 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
