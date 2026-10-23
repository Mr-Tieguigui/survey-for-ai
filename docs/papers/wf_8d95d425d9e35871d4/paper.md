# Evolution Transformer: In-Context Evolutionary Optimization

> 方法论文 · 2024 · `wf_8d95d425d9e35871d4`

**作者**：Robert Tjarko Lange, Yingtao Tian, Yujin Tang  
**原文**：https://arxiv.org/abs/2403.02985  
**研究分支**：程序、算法与演化搜索  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
Evolution Transformer 从评估轨迹与搜索分布统计输出分布更新，先以教师算法轨迹蒸馏，并提出从随机初始化自指训练自举；教师蒸馏和自训练应拆作不同配置核实。

## 2. 论文的核心内容与贡献

### configuration:cfg_evotf_self_referential_ead
自己当前checkpoint生成扰动轨迹并筛选蒸馏形成下一轮checkpoint，四结构条件成立；未认证固定蒸馏/扰动元规则自改或单调收益。

**适用版本**：2403.02985v1；**原文定位**：v1 §7 tool L166–175；v1 §8 tool L176–183。
**引用权限**：`listed_configuration_scope_only`。

### configuration:cfg_evotf_teacher_distillation
固定teacher的EAD训练中，学生更新不参与下一批teacher轨迹生成，因此本训练边界C4不成立；这是监督算法蒸馏相邻配置，不能记作自己生成数据的SR-EAD。

**适用版本**：2403.02985v1；**原文定位**：v1 §§3–4 tool L101–131；v1 §8 limits tool L176–183。
**引用权限**：`listed_configuration_scope_only`。

### 已存角色解释 · `s18_role_review_wf_8d95d425d9e35871d4`
Evolution Transformer 从评估轨迹与搜索分布统计输出分布更新，先以教师算法轨迹蒸馏，并提出从随机初始化自指训练自举；教师蒸馏和自训练应拆作不同配置核实。

研究类型：未单列；权限：`role_and_relevance_boundary_only_not_technical_answer_evidence`。

## 3. 方法机制与实现细节

### Evolution Transformer: fixed-teacher EAD training
`cfg_evotf_teacher_distillation` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 本卡仅固定teacher的EAD训练阶段：teacher算法生成轨迹，EvoTF参数theta由KL蒸馏训练；不纳入训练后优化任务的部署搜索过程。 |
| 改进过程与下一轮参与 | theta仅预测teacher分布更新，训练期不主动作用任务；梯度学习到的theta不决定下一批teacher轨迹的提案分布。 |
| 保留的状态及时间尺度 | theta跨监督训练步保留；固定teacher目标生成机制不因学生theta更新而刷新。 |
| 外部固定部分 | - teacher算法与轨迹生成方式 - KL蒸馏目标与Adam |
| 评价与选择设置 | - **generations**：32 - **population**：10 - **teacher families**：- OpenAI-ES - Sep-CMA-ES - Gaussian hillclimb - SNES - **training boundary only**：True - **training dims**：5 |

**配置判定**：固定teacher的EAD训练中，学生更新不参与下一批teacher轨迹生成，因此本训练边界C4不成立；这是监督算法蒸馏相邻配置，不能记作自己生成数据的SR-EAD。

来源：https://arxiv.org/html/2403.02985v1；版本：2403.02985v1；定位：v1 §§3–4 tool L101–131；v1 §8 limits tool L176–183。

### Evolution Transformer: SR-EAD self-generated trajectory loop
`cfg_evotf_self_referential_ead` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 当前EvoTF checkpoint及其扰动子代，固定BBO任务与轨迹筛选、蒸馏操作；不依赖外部teacher算法。 |
| 改进过程与下一轮参与 | 扰动当前theta得64offspring；各offspring跑相同采样任务，按表现保留最好轨迹，做单次梯度蒸馏更新theta再重复。 |
| 保留的状态及时间尺度 | 更新checkpoint跨轮保存，其扰动offspring决定下一轮生成的优化轨迹和训练数据。 |
| 外部固定部分 | - 任务集与fitness - Gaussian perturbation及衰减日程 - performance filter - distillation gradient rule |
| 评价与选择设置 | - **hardware**：4 A100 - **negative result**：Pendulum unstable - **offspring**：64 - **per iteration**：one gradient distillation update - **perturbations**：- 0.004 - 0.005 - **runs**：3 - **tasks**：5 BBOB subset, same sampled tasks for offspring |

**配置判定**：自己当前checkpoint生成扰动轨迹并筛选蒸馏形成下一轮checkpoint，四结构条件成立；未认证固定蒸馏/扰动元规则自改或单调收益。

来源：https://arxiv.org/html/2403.02985v1；版本：2403.02985v1；定位：v1 §7 tool L166–175；v1 §8 tool L176–183。

## 4. 实验、评价协议与结果的可解释范围


- **generations**：32
- **population**：10
- **teacher families**：- OpenAI-ES - Sep-CMA-ES - Gaussian hillclimb - SNES
- **training boundary only**：True
- **training dims**：5


- **hardware**：4 A100
- **negative result**：Pendulum unstable
- **offspring**：64
- **per iteration**：one gradient distillation update
- **perturbations**：- 0.004 - 0.005
- **runs**：3
- **tasks**：5 BBOB subset, same sampled tasks for offspring

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`s18_role_ev_wf_8d95d425d9e35871d4`**：Evolution Transformer 从评估轨迹与搜索分布统计输出分布更新，先以教师算法轨迹蒸馏，并提出从随机初始化自指训练自举；教师蒸馏和自训练应拆作不同配置核实。
  - 来源版本：2403.02985v1；定位：Atom entry http://arxiv.org/abs/2403.02985v1；Atom summary element；深度：`official_primary_abstract_role_and_relevance_only`。

- **`h6_ev_cfg_evotf_teacher_distillation`**：固定teacher的EAD训练中，学生更新不参与下一批teacher轨迹生成，因此本训练边界C4不成立；这是监督算法蒸馏相邻配置，不能记作自己生成数据的SR-EAD。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

- **`h6_ev_cfg_evotf_self_referential_ead`**：自己当前checkpoint生成扰动轨迹并筛选蒸馏形成下一轮checkpoint，四结构条件成立；未认证固定蒸馏/扰动元规则自改或单调收益。
  - 来源版本：unknown；定位：参见来源索引；深度：`未单列`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- Pendulum在初始提升后表现下降且对两种perturbation强度均可见；不能只列成功CartPole/MNIST。
- meta-evolution和SR-EAD是不同配置，前者过拟合结果不当作后者同一实验。
- 只有5类BBOB训练任务、显存/短窗限制，open-ended discovery仅future方向。
- 训练后冻结EvoTF部署的mu/sigma/history可形成另一个bounded search-state闭环，但该部署过程不在本配置中，需独立判读，不能因theta冻结直接否定其C4。
- context sliding window受显存约束，未核任意长历史与大维度性能。
- 仅实读已缓存的官方 Atom 摘要作范围和角色判读；不是 2026-10-18 的最新版本检索，未核全文配置、定理、性能数值或继承关系，不支持技术性读者回答。
- 原文关键选段与指定状态反馈边界；非穷尽全文、所有证明认证或独立复现。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `h6_src_w_evolution_transformer` · 已存来源 · 2403.02985v1
  - https://arxiv.org/html/2403.02985v1；阅读深度：`targeted_primary_method_state_feedback_and_limits`。
- `s18_role_src_20fe003e28646d5b` · 已存来源 · Atom snapshot 2026-10-11; exact entry versions stored on review
  - https://export.arxiv.org/api/query?id_list=2402.08957%2C2402.09015%2C2402.09269%2C2402.09283%2C2402.09727%2C2402.09742%2C2402.09748%2C2402.10110%2C2402.10176%2C2402.10196%2C2402.10200%2C2402.10663%2C2402.10770%2C2402.10890%2C2402.10963%2C2402.10980%2C2402.10987%2C2402.11190%2C2402.11218%2C2402.11359%2C2402.11411%2C2402.11451%2C2402.11550%2C2402.11633%2C2402.11827%2C2402.11975%2C2402.12048%2C2402.12185%2C2402.12255%2C2402.12317%2C2402.12348%2C2402.12391%2C2402.12431%2C2402.12451%2C2402.12545%2C2402.12914%2C2402.12959%2C2402.13210%2C2402.13212%2C2402.13296%2C2402.13426%2C2402.13542%2C2402.13598%2C2402.13669%2C2402.13717%2C2402.14034%2C2402.14083%2C2402.14207%2C2402.14268%2C2402.14382%2C2402.15057%2C2402.15116%2C2402.15391%2C2402.15538%2C2402.15589%2C2402.15809%2C2402.15810%2C2402.16288%2C2402.16313%2C2402.16499%2C2402.16696%2C2402.16767%2C2402.16823%2C2402.16837%2C2402.16906%2C2402.16965%2C2402.17168%2C2402.17453%2C2402.17505%2C2402.17574%2C2402.17613%2C2402.17753%2C2402.18005%2C2402.18060%2C2402.18361%2C2402.18381%2C2402.18485%2C2402.19085%2C2402.19173%2C2402.19446%2C2402.19473%2C2403.00198%2C2403.00690%2C2403.00833%2C2403.00839%2C2403.01197%2C2403.01244%2C2403.01248%2C2403.01528%2C2403.02164%2C2403.02502%2C2403.02691%2C2403.02817%2C2403.02985%2C2403.03101%2C2403.03129%2C2403.03186%2C2403.03218%2C2403.03768%2C2403.03883&max_results=100；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261018。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_8d95d425d9e35871d4 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
