# Generating on Generated: An Approach Towards Self-Evolving Diffusion Models

> 方法论文 · 2026 · `wf_title_4a14408077463396`

**作者**：Association for Artificial Intelligence 2026  
**原文**：https://doi.org/10.48448/51mw-6a25  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
RSIDiff iteratively generates diffusion-model synthetic data, selects preference-favored samples, weights them against base-model distribution shift and fine-tunes the next model. Prompt filtering, automated preference sampling and distribution weighting jointly structure the feedback-data loop. Direct bounded self-training bridge: the current generator's outputs become selected/weighted data for persistent weights used in the next generation. Self-training rounds are not acceptance-gated code revisions or evidence of accelerating improvement.

### 与 RSI 的具体关系

- Direct bounded self-training bridge: the current generator's outputs become selected/weighted data for persistent weights used in the next generation. Self-training rounds are not acceptance-gated code revisions or evidence of accelerating improvement.

## 2. 论文的核心内容与贡献

### role:b570_09_role_wf_title_4a14408077463396
RSIDiff iteratively generates diffusion-model synthetic data, selects preference-favored samples, weights them against base-model distribution shift and fine-tunes the next model. Prompt filtering, automated preference sampling and distribution weighting jointly structure the feedback-data loop.

**适用版本**：arXiv:2502.09963v1 author preprint；**原文定位**：iterative weighted synthetic-data fine-tuning; PDF physical page 4, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)；base-distribution weighting reference; PDF physical page 5, derived page-text lines 47-55 (one-based local extraction, not web-tool lines)；distance threshold and decay hyperparameter dependence; PDF physical page 5, derived page-text lines 74-78 (one-based local extraction, not web-tool lines)。
**引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`。

## 3. 方法机制与实现细节
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围

Image preference/quality metrics and human-preference assessments on held-out prompt sets; fixed round count and distribution shift are distinct from cost-to-target or accepted-revision counts.

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`b570_09_ev_wf_title_4a14408077463396`**：RSIDiff iteratively generates diffusion-model synthetic data, selects preference-favored samples, weights them against base-model distribution shift and fine-tunes the next model. Prompt filtering, automated preference sampling and distribution weighting jointly structure the feedback-data loop.
  - 来源版本：arXiv:2502.09963v1 author preprint；定位：iterative weighted synthetic-data fine-tuning; PDF physical page 4, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)；base-distribution weighting reference; PDF physical page 5, derived page-text lines 47-55 (one-based local extraction, not web-tool lines)；distance threshold and decay hyperparameter dependence; PDF physical page 5, derived page-text lines 74-78 (one-based local extraction, not web-tool lines)；深度：`selected_primary_role_definition_protocol_scope_and_limits`。

## 5. 原文选段：把方法与实验细节展开

### 选段 1 · 机制 / 定义 · iterative weighted synthetic-data fine-tuning
**来源**：https://arxiv.org/pdf/2502.09963v1  
**实际版本**：arXiv:2502.09963v1 author preprint  
**精确定位**：PDF physical page 4, derived page-text lines 1-14 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_title_4a14408077463396`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 2 · 机制 / 定义 · base-distribution weighting reference
**来源**：https://arxiv.org/pdf/2502.09963v1  
**实际版本**：arXiv:2502.09963v1 author preprint  
**精确定位**：PDF physical page 5, derived page-text lines 47-55 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_title_4a14408077463396`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

### 选段 3 · 限制 · distance threshold and decay hyperparameter dependence
**来源**：https://arxiv.org/pdf/2502.09963v1  
**实际版本**：arXiv:2502.09963v1 author preprint  
**精确定位**：PDF physical page 5, derived page-text lines 74-78 (one-based local extraction, not web-tool lines)  
**关联证据**：`b570_09_ev_wf_title_4a14408077463396`

逐字选段保留在有访问控制的完整信息包；公开阅读视图保留上方版本与定位。

以上仅为已存选段的转录；行号是该记录声明的派生文本行号，不改写为出版商页码。缺失数学符号不据上下文重构。

## 6. 局限、冲突与不能推出的结论

- The loop uses fixed filtering/scoring/weighting machinery and a predefined round count; it does not establish recursive redesign of that machinery. Weighting is relative to a base-generated reference distribution, and preference proxies do not prove universal visual correctness or indefinite collapse-free improvement.

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `b570_09_src_wf_title_4a14408077463396` · Generating on Generated: An Approach Towards Self-Evolving Diffusion Models · arXiv:2502.09963v1 author preprint
  - https://arxiv.org/pdf/2502.09963v1；阅读深度：`selected_primary_role_definition_protocol_scope_and_limits`。

**仍未核准的内容**：

- Reviewed author arXiv2502.09963v1 preprint for Underline presentation DOI cohort; final/presentation text identity not assumed.
- Empirical claims are author reports, not independently replicated by this review.
- Detailed configurations, numeric magnitudes and inheritance relations are not certified by this role review.

**证据深度**：original_abstract, registry_abstract, selected_primary_role_definition_protocol_scope_and_limits。
**当前引用权限**：`selected_primary_role_definitions_protocol_assumptions_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_title_4a14408077463396 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
