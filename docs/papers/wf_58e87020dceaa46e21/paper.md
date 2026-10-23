# Automated Design of Agentic Systems: A Survey of Algorithms for Searching, Optimizing, and Evolving LLM Agents, Workflows, and Prompts

> 综述/系统综述/谱系 · 2026 · `wf_58e87020dceaa46e21`

**作者**：Maksim Madžar, Igor Mekterović  
**原文**：https://doi.org/10.20944/preprints202606.0238.v1  
**研究分支**：综述与领域导航  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
把NAS的搜索空间/策略/估计拓展为优化目标、搜索策略、表示与反馈四轴，组织固定基础模型外围的prompt、workflow、模块和代码搜索。

## 2. 论文的核心内容与贡献

### role:r7nav_role_adas
把NAS的搜索空间/策略/估计拓展为优化目标、搜索策略、表示与反馈四轴，组织固定基础模型外围的prompt、workflow、模块和代码搜索。

**适用版本**：Preprints.org v1 posted2026-06-02; returned redirected page explicitly Version1；**原文定位**：§1 scope tool L100–105；§2 foundations tool L106–123；§3 framework tool L124–129。
**引用权限**：`selected_primary_role_framework_claims_only`。

## 3. 综述范围、分类框架与覆盖
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r7nav_role_adas_ev`**：把NAS的搜索空间/策略/估计拓展为优化目标、搜索策略、表示与反馈四轴，组织固定基础模型外围的prompt、workflow、模块和代码搜索。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- §1把主要范围限定于largely frozen模型的design-time scaffold优化，不能当所有训练期RSI的全景。
- 表达能力与可搜索性、反馈丰富度与credit assignment是组织张力；代码空间可表达不代表实际搜索可发现任意系统。
- 本次未核其所有33方法编码、性能数值或全文引用准确性，不能把综述描述当直接继承证据。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r7nav_src_adas` · 已存来源 · Preprints.org v1 posted2026-06-02; returned redirected page explicitly Version1
  - https://www.preprints.org/manuscript/202606.0238/v1；阅读深度：`selected_primary_framework_and_explicit_limits`。

**证据深度**：registry_abstract。
**当前引用权限**：`selected_primary_role_framework_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_58e87020dceaa46e21 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
