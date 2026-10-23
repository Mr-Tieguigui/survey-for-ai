# RIWANav: Recursive World-Action Models with Self-Improvement for Urban Navigation

> 方法论文 · 2026 · `wf_2f458fc3ad8fb4b47c`

**作者**：Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Haitao Yang, Songchang Jin, Dianxi Shi  
**原文**：https://arxiv.org/abs/2610.08640  
**研究分支**：自生成数据、课程与参数训练  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

**实际来源题名（已存版本）**：RIWANav: Recursive World–Action Models with Self-Improvement for Urban Navigation。工作家族题名与具体来源题名分别保留。

## 1. 这项工作研究什么
在当前已核配置中，系统边界为：学习policy pi_theta与action-conditioned Cosmos f_phi交替更新；offline UrbanNav提供state、expert action和录制future；f_phi在每个policy phase内冻结而非全程固定；具体更新过程为：world model想象action结果供GRPO；改进policy输出expert-consistent action-video pairs，以相对初始policy的novelty和当前prediction error重排replay并更新world model；更新状态的保留与后继使用为：theta/phi checkpoints与新旧replay池跨阶段保留；下一版phi生成下次policy改进反馈，更新policy继续改变replay/curriculum。

## 2. 论文的核心内容与贡献

### configuration:cfg_riwanav_policy_worldmodel_replay_v1
四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 world model想象action结果供GRPO；改进policy输出expert-consistent action-video pairs，以相对初始policy的novelty和当前prediction error重排replay并更新world model。

**适用版本**：2610.08640v1；**原文定位**：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249。
**引用权限**：`listed_configuration_scope_only`。

## 3. 方法机制与实现细节

### RIWANav v1 alternating policy/world-model adaptation
`cfg_riwanav_policy_worldmodel_replay_v1` · empirical_method

| 方法要素 | 当前记录的具体内容 |
|---|---|
| 系统边界 | 学习policy pi_theta与action-conditioned Cosmos f_phi交替更新；offline UrbanNav提供state、expert action和录制future；f_phi在每个policy phase内冻结而非全程固定。 |
| 改进过程与下一轮参与 | world model想象action结果供GRPO；改进policy输出expert-consistent action-video pairs，以相对初始policy的novelty和当前prediction error重排replay并更新world model。 |
| 保留的状态及时间尺度 | theta/phi checkpoints与新旧replay池跨阶段保留；下一版phi生成下次policy改进反馈，更新policy继续改变replay/curriculum。 |
| 外部固定部分 | - offline expert recorded futures与expert-consistency admission - 初始policy pi_theta0作为KL/novelty reference - DINOv2/CLIP特征、navigation score和更新规则 |
| 评价与选择设置 | - **candidates per state**：4 - **evaluation**：UrbanNav official train/test-seen/test-unseen; three seeds; 128 held-out pairs per WM evaluation set - **world model final round**：19 - **world model update**：every 500 policy steps; at most 500 replay examples |

**反馈闭环如何成立（按配置核查）**：
- **明确的系统边界**：§III-A policy/world model及offline监督边界明确。（状态：`supported`；定位：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249）。
- **更新由什么过程产生**：GRPO改变theta；policy诱导数据和curriculum改变phi。（状态：`supported`；定位：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249）。
- **状态怎样持久保留**：模型checkpoint和新旧replay跨round保留。（状态：`supported`；定位：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249）。
- **更新怎样进入后续改进**：新版phi评价后续policy候选，后续policy再诱导world-model训练样本。（状态：`supported`；定位：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249）。

**配置判定**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 world model想象action结果供GRPO；改进policy输出expert-consistent action-video pairs，以相对初始policy的novelty和当前prediction error重排replay并更新world model。

来源：https://arxiv.org/html/2610.08640v1；版本：2610.08640v1；定位：§III-A coupled policy/world-model state tool L91–104；§III-B–C learned feedback and replay update tool L109–139；§IV-A fixed settings and evaluator tool L167–175；§IV-D 19-round feedback evidence tool L221–238；§IV-F offline-data limits tool L247–249。

## 4. 实验、评价协议与结果的可解释范围


- **candidates per state**：4
- **evaluation**：UrbanNav official train/test-seen/test-unseen; three seeds; 128 held-out pairs per WM evaluation set
- **world model final round**：19
- **world model update**：every 500 policy steps; at most 500 replay examples

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r15_ev_cfg_riwanav_policy_worldmodel_replay_v1`**：四条件在声明的有限状态/权重反馈边界上支持core；不据此推断强RSI、无界加速或独立复现。 world model想象action结果供GRPO；改进policy输出expert-consistent action-video pairs，以相对初始policy的novelty和当前prediction error重排replay并更新world model。
  - 来源版本：unknown；定位：参见来源索引；深度：`targeted_primary_method_state_feedback_limits_20261019`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 固定offline dataset仅能监督接近expert motion的policy动作；不是通过自由现实探索生成新ground truth。
- K=19有限任务特定递归；个别round有波动，非单调或无界加速。
- 现实机器人部署是可行性示例，不能替代跨城市/embodiment控制评价。
- 固定offline dataset仅能监督接近expert motion的policy动作；不是通过自由现实探索生成新ground truth。; K=19有限任务特定递归；个别round有波动，非单调或无界加速。; 现实机器人部署是可行性示例，不能替代跨城市/embodiment控制评价。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r15_src_riwanav` · RIWANav: Recursive World–Action Models with Self-Improvement for Urban Navigation · 2610.08640v1
  - https://arxiv.org/html/2610.08640v1；阅读深度：`未单列`。

**证据深度**：original_abstract, targeted_primary_method_state_feedback_limits_20261019。
**当前引用权限**：`configuration_bounded_claims_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_2f458fc3ad8fb4b47c --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
