# ReSI: Recursive Safety Improvement toward Resistant and Resilient AI

> 方法论文 · 2026 · `wf_64b1f1bb5a5cbc6bc4`

**作者**：Jingnan Zheng, Dongcheng Zhang, Yi Zhang, Ming Zhang, Qiaosheng Zhang, Youbang Sun, An Zhang, Xiangnan He, Tat-Seng Chua, Xia Hu, Bowen Zhou, Chaochao Lu, Xiang Wang  
**原文**：https://arxiv.org/abs/2610.12233  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：target M_t、red-team methods和recipe search/execution framework构成bounded system；GPT-4o external auto-research proposer不等于target model，Pareto gate与refinement skills固定；具体更新过程为：当前target的成功攻击诱导attack dataset；auto-research根据pilot与Pareto反馈改data sources/method/mixture/hyperparameters，选择合格target LoRA checkpoint进入下一轮red teaming；更新状态的保留与后继使用为：accepted target weights、attack evidence、recipe/trial结果跨round保留；下一轮攻击面由已更新target决定。

## 2. 论文的核心内容与贡献

### configuration:cfg_resi_target_lora_pareto_recipe_loop_v1
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 当前target的成功攻击诱导attack dataset；auto-research根据pilot与Pareto反馈改data sources/method/mixture/hyperparameters，选择合格target LoRA checkpoint进入下一轮red teaming。

**适用版本**：2610.12233v1；**原文定位**：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### ReSI v1 target-model LoRA with fixed Pareto recipe search
`cfg_resi_target_lora_pareto_recipe_loop_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | target M_t、red-team methods和recipe search/execution framework构成bounded system；GPT-4o external auto-research proposer不等于target model，Pareto gate与refinement skills固定。 |
| 改进过程与下一轮参与 | 当前target的成功攻击诱导attack dataset；auto-research根据pilot与Pareto反馈改data sources/method/mixture/hyperparameters，选择合格target LoRA checkpoint进入下一轮red teaming。 |
| 保留的状态及时间尺度 | accepted target weights、attack evidence、recipe/trial结果跨round保留；下一轮攻击面由已更新target决定。 |
| 外部固定部分 | - GPT-4o temperature 0 proposer与S1–S4 refinement skills - Pareto safety gain/BC/IF阈值及M0 retention reference - red-teaming资源、训练backend和bounded trial controls |
| 评价与选择设置 | - **accepted rounds**：2, 2, 3, 1 respectively; all stop after no next-round gate-passing candidate - **adapter**：LoRA; model-specific recipes - **evaluation**：safety ASR plus benign compliance and instruction following; external fixed gate - **targets**：Qwen3.6-27B, Ministral-3-14B, DeepSeek-V4-Flash-0731, Safin-1 |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§2区分target、攻击、recipe与固定gate，§3给external GPT-4o角色。（状态：`supported`；定位：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318）。
- **更新由什么过程产生**：当前target的攻击证据和trial feedback改变recipe并训练target LoRA。（状态：`supported`；定位：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318）。
- **状态怎样持久保留**：Pareto-selected target checkpoint进入下一round，失败则保留旧target。（状态：`supported`；定位：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318）。
- **更新怎样进入后续改进**：已接受新target成为后续red-teaming和recipe selection对象；报告1–3轮accepted并再尝试终止轮。（状态：`supported`；定位：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 当前target的成功攻击诱导attack dataset；auto-research根据pilot与Pareto反馈改data sources/method/mixture/hyperparameters，选择合格target LoRA checkpoint进入下一轮red teaming。

来源：https://arxiv.org/html/2610.12233v1；版本：2610.12233v1；定位：§2.1–2.2 target-specific attack evidence tool L112–131；§2.3–2.4 feedback recipes, reset and retention gate tool L174–230；§3 actual proposer, models and accepted rounds tool L233–244；§5–6 fixed skills and bounded recursion tool L311–318。

## 4. 实验、评价协议与结果的可解释范围


- **accepted rounds**：2, 2, 3, 1 respectively; all stop after no next-round gate-passing candidate
- **adapter**：LoRA; model-specific recipes
- **evaluation**：safety ASR plus benign compliance and instruction following; external fixed gate
- **targets**：Qwen3.6-27B, Ministral-3-14B, DeepSeek-V4-Flash-0731, Safin-1

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_resi_target_lora_pareto_recipe_loop_v1`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 当前target的成功攻击诱导attack dataset；auto-research根据pilot与Pareto反馈改data sources/method/mixture/hyperparameters，选择合格target LoRA checkpoint进入下一轮red teaming。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 独立pilot/refinement通常从当前M_t重启；只有S4从合格SFT checkpoint续GRPO，不应画成每个trial连续累积权重。
- 同round共享validation panels/gate thresholds，用于自适应选择；正式test泛化仅限文中所列held-out/OOD攻击评价。
- 更新target而非GPT-4o或refinement技能；后者跨round保持固定，作者把技能自改列为未来工作。
- 独立pilot/refinement通常从当前M_t重启；只有S4从合格SFT checkpoint续GRPO，不应画成每个trial连续累积权重。; 同round共享validation panels/gate thresholds，用于自适应选择；正式test泛化仅限文中所列held-out/OOD攻击评价。; 更新target而非GPT-4o或refinement技能；后者跨round保持固定，作者把技能自改列为未来工作。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_resi` · ReSI: Recursive Safety Improvement toward Resistant and Resilient AI · 2610.12233v1
  - https://arxiv.org/html/2610.12233v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_64b1f1bb5a5cbc6bc4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
