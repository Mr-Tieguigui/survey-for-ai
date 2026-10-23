# TestPrism: Rethinking Test Evaluation Beyond a Single Reference

> Benchmark/数据集/任务套件 · 2026 · `wf_7311a375d2a69a8780`

**作者**：Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu  
**原文**：https://arxiv.org/abs/2610.12289  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
TestPrism对每任务以reference+4valid alternatives+5invalid implementations构成隐藏panel，测生成测试能否同时接纳多种正确实现并拒错误。Joint Success Function与单reference acceptance分开；论文另有TestHelix RSI方法，本批只认证benchmark/评测protocol，不能据方法名新增core配置。

## 2. 论文的核心内容与贡献

### role:r14_role_testprism
TestPrism对每任务以reference+4valid alternatives+5invalid implementations构成隐藏panel，测生成测试能否同时接纳多种正确实现并拒错误。Joint Success Function与单reference acceptance分开；论文另有TestHelix RSI方法，本批只认证benchmark/评测protocol，不能据方法名新增core配置。

**适用版本**：2610.12289v1；**原文定位**：§2.1–2.4 construction/labels/panels tool L143–159；§2.5–2.6 split/metrics tool L160–176；§3 TestHelix method role separated tool L177–188；AppendixE limitations tool L739–748。
**引用权限**：`selected_primary_role_protocol_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：直接关联生成测试/RSI feedback verifiers及候选选择有效性；TestHelix方法需要独立配置后才能作方法结构结论。
- **metrics**：- Reference Acceptance、Valid Acceptance、Invalid Rejection和harmonic mean - JSF要求initialfail且所有选中valid通过/invalid拒绝；有限panel共同成功非全部实现空间正确性 - change/entry coverage与collection counts另报，不把missing/errors统一当正确
- **selection and reuse**：source quota/solution size/test density筛任务；排无法运行env、未决expert concerns；候选生成去重/inapplicable并用failedcheck/AST distance过滤多样性。
- **split and visibility**：1700/300disjoint；candidate panel在test generation时隐藏；标签固定来自validated source verifier；每实现reset干净环境。
- **task or data unit**：17来源共2000任务，1700training供TestHelix strategy development、300test；test共3000 labeled implementations。每任务panel10实现，包含reference。
- **unknowns**：- 所有upstream gold的独立正确性与真实deployment错误比例unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r14_ev_testprism`**：TestPrism对每任务以reference+4valid alternatives+5invalid implementations构成隐藏panel，测生成测试能否同时接纳多种正确实现并拒错误。Joint Success Function与单reference acceptance分开；论文另有TestHelix RSI方法，本批只认证benchmark/评测protocol，不能据方法名新增core配置。
  - 来源版本：2610.12289v1；定位：§2.1–2.4 construction/labels/panels tool L143–159；§2.5–2.6 split/metrics tool L160–176；§3 TestHelix method role separated tool L177–188；AppendixE limitations tool L739–748；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只评finite panels、固定task contracts，不证明exhaustive semantic coverage。
- upstream gold correctness未逐项重新证明；AST Jaccard非semantic distance，balanced valid/invalid不是实际错误率。
- equal inference limits不代表equal consumed compute；strategy开发与inference费用分开。
- 只评finite panels、固定task contracts，不证明exhaustive semantic coverage。; upstream gold correctness未逐项重新证明；AST Jaccard非semantic distance，balanced valid/invalid不是实际错误率。; equal inference limits不代表equal consumed compute；strategy开发与inference费用分开。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r14_src_testprism` · TestPrism: Rethinking Test Evaluation Beyond a Single Reference · 2610.12289v1
  - https://arxiv.org/html/2610.12289v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_role_protocol_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7311a375d2a69a8780 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
