# STaR: Bootstrapping Reasoning With Reasoning

> 方法论文 · 2022 · `wf_9c3c6d83941546cacd`

**作者**：Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman  
**原文**：https://arxiv.org/abs/2203.14465  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：模型生成rationale及筛选训练集；具体更新过程为：新微调模型生成下一轮rationale；每轮训练从原始预训练模型重启；更新状态的保留与后继使用为：跨rationale生成轮次。

## 2. 论文的核心内容与贡献

### configuration:cfg_star
参数不是逐轮累加；保留的递归依赖是新模型成为下一轮生成器

**适用版本**：v2；**原文定位**：S3.SS1.p1.1；S3.SS1.p2.2；S3.SS2.p1.1；alg1。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### cfg_star
`cfg_star` · declared_specific_configuration

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 模型生成rationale及筛选训练集 |
| 改进过程与下一轮参与 | 新微调模型生成下一轮rationale；每轮训练从原始预训练模型重启 |
| 保留的状态及时间尺度 | 跨rationale生成轮次 |
| 外部固定部分 | 正确答案、种子rationale示例、筛选与微调程序 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：模型生成rationale及筛选训练集（状态：`supported`；定位：S3.SS1.p1）。
- **更新由什么过程产生**：新微调模型生成下一轮rationale；每轮训练从原始预训练模型重启（状态：`supported`；定位：S3.SS1.p1）。
- **状态怎样持久保留**：跨rationale生成轮次（状态：`supported`；定位：S3.SS1.p1）。
- **更新怎样进入后续改进**：新微调模型生成下一轮rationale；每轮训练从原始预训练模型重启（状态：`supported`；定位：S3.SS1.p1）。

**配置判定**：参数不是逐轮累加；保留的递归依赖是新模型成为下一轮生成器

来源：https://arxiv.org/html/2203.14465v2；版本：v2；定位：S3.SS1.p1.1；S3.SS1.p2.2；S3.SS2.p1.1；alg1。

## 4. 实验、评价协议与结果的可解释范围
当前保存的解析未完整登记实验数据、基线、预算、误差条与统计检验。不能据此填入具体性能数字，或进行跨论文分数排序。理论、综述和背景工作也不因此被强造实验。

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`e2_w_star`**：新微调模型生成下一轮rationale；每轮训练从原始预训练模型重启
  - 来源版本：v2；定位：S3.SS1.p1；深度：`AI_primary_method_passage_recheck`。

- **`e3_training_p2c_restem_star_sampling_boundary`**：ReST-EM原文明确比较STaR的单次贪心生成与自身温度多样本生成；STaR还用正确答案提示对失败题进行rationalization，再按最终答案正确性过滤。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- base重置训练而非持续累加参数。
- 正确答案提示仅用作rationalization，训练输入删去提示。
- 最终答案正确不证实rationale忠实性。
- 参
- 数
- 不
- 是
- 逐
- 轮
- 累
- 加
- ；
- 保
- 留
- 的
- 递
- 归
- 依
- 赖
- 新
- 模
- 型
- 成
- 为
- 下
- 一
- 生
- 器
- 这是作者明确的采样与失败题处理机制比较，不证明ReST-EM完整继承STaR。ReST-EM关于rationalization错误推理/正确答案的观察限定其初步实验，不是跨数据集复现STaR或证明全部rationalization不忠实；两者都从base重训生成新策略。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `expand_src_w_restem` · ReST-EM · v4
  - https://arxiv.org/html/2312.06585v4；阅读深度：`未单列`。
- `expand_src_w_star` · STaR · v2
  - https://arxiv.org/html/2203.14465v2；阅读深度：`未单列`。

**证据深度**：original_abstract, selected_method_passages_with_abstract_baseline。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_9c3c6d83941546cacd --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
