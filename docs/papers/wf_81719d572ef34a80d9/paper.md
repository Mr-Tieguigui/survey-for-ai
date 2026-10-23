# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

> 方法论文 · 2025 · `wf_81719d572ef34a80d9`

**作者**：Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, Tomas Pfister  
**原文**：https://arxiv.org/abs/2509.25140  
**研究分支**：持久记忆、反思与上下文  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
自评轨迹的策略记忆提取、检索与写入跨任务循环；基础配置单列，不将MaTTS或v2评测借入v1。

## 2. 论文的核心内容与贡献

### configuration:cfg_reasoningbank_base_v1
只核基础v1记忆配置；MaTTS平行/顺序扩展需分开核查。

**适用版本**：2509.25140v1；**原文定位**：§3.2；Appendix A.1–A.2。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_reasoningbank_faithfulness_audit
审计实现与原v1的gemini-embedding-001/default top-1不同；不能表示为原始配置逐项复现。

**适用版本**：2601.22436v1；**原文定位**：§2；§3.1；§4.2 and Figure 4；Appendix C ReasoningBank。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_reasoningbank_base_v1
`cfg_reasoningbank_base_v1` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 冻结代理、成功/失败自判定、抽取器、外部策略记忆 |
| 改进过程与下一轮参与 | 新任务检索策略；结束后从轨迹提取记忆并加入池 |
| 保留的状态及时间尺度 | 跨查询持久记忆池 |
| 外部固定部分 | 检索/抽取/追加程序、模型与判断协议 |

**配置判定**：只核基础v1记忆配置；MaTTS平行/顺序扩展需分开核查。

来源：https://arxiv.org/html/2509.25140v1；版本：2509.25140v1；定位：§3.2；Appendix A.1–A.2。

### cfg_reasoningbank_faithfulness_audit
`cfg_reasoningbank_faithfulness_audit` · 已存配置视图

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 忠实性研究的ReasoningBank在线代理与凝练策略记忆 |
| 改进过程与下一轮参与 | 检索凝练记忆辅助WebArena决策，任务后提取新记忆 |
| 保留的状态及时间尺度 | 跨查询记忆池 |
| 外部固定部分 | top-3、text-embedding-ada-002、30交互步上限、judge/extractor temperature 0 |

**配置判定**：审计实现与原v1的gemini-embedding-001/default top-1不同；不能表示为原始配置逐项复现。

来源：https://arxiv.org/html/2601.22436v1；版本：2601.22436v1；定位：§2；§3.1；§4.2 and Figure 4；Appendix C ReasoningBank。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论
当前未单列具体局限；这不表示没有局限。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `accel_src_faithfulness_v1` · 已存来源 · v1
  - https://arxiv.org/html/2601.22436v1；阅读深度：`未单列`。
- `intake_src_w_reasoningbank` · 已存来源 · 2509.25140v1
  - https://arxiv.org/html/2509.25140v1；阅读深度：`未单列`。

**证据深度**：targeted_primary_full_text_method_pass。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_81719d572ef34a80d9 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
