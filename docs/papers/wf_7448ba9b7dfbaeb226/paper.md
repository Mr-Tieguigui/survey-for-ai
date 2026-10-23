# DataSense-Bench: The First Step Toward an AI Scientist

> Benchmark/数据集/任务套件 · 2026 · `wf_7448ba9b7dfbaeb226`

**作者**：Yudi Zhang, Mingyu Cao, Lu Yin, Mykola Pechenizkiy, Shiwei Liu  
**原文**：https://arxiv.org/abs/2610.12190  
**研究分支**：Benchmark、数据集与任务  
**解析依据**：已保存的角色审查、配置核查、原文定位与选段；不是重新全文精读。

## 1. 这项工作研究什么
DataSense-Bench测量训练前数据价值判断：代理提交五个互不重叠的轨迹子集及效用排序，随后外部固定SFT分别从新基模副本训练并评测。首选数据收益与排序预测是两个独立指标，训练结果不回传用于修改本次选择。

## 2. 论文的核心内容与贡献

### role:r11_role_datasense
DataSense-Bench测量训练前数据价值判断：代理提交五个互不重叠的轨迹子集及效用排序，随后外部固定SFT分别从新基模副本训练并评测。首选数据收益与排序预测是两个独立指标，训练结果不回传用于修改本次选择。

**适用版本**：2610.12190v1；**原文定位**：§3.1 data units tool L88–94；§3.1–3.2 submission/freeze tool L106–116；§3.3–4.1 metrics/downstream evaluation tool L118–133；§5 conclusion/limitations/impact tool L197–206。
**引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`。

## 3. 任务、数据与评价设计
该工作按研究角色解析，不强行构造方法配置。具体定义、协议或论证见以下证据片段及其来源定位。

## 4. 实验、评价协议与结果的可解释范围


- **actual RSI relation**：作者直接关联RSI中训练资源分配的数据判断能力；该协议隔离的是训练前预测，不是有训练收益回传的递归选择循环。
- **leakage and information boundary**：评测访问限制与排除validation是协议约束；未独立审计源池和所有测试任务的语义去重或预训练污染。
- **metrics**：- 首组s1及相同规模/recipe随机选择的差值Δrandom - best-group accuracy与五组预测/真实效用Spearman相关分开 - TBLite 100任务×3尝试平均reward；BFCL V3四类别各200case、每checkpoint三评测种子
- **selection and reuse**：同一4小时选择预算内首次交付无效可重试一次；提交索引CSV及method report。训练/评测不计入该预算，且结果仅事后验证。
- **split and visibility**：EnvScaler的validation轨迹排除；代理只能推理访问基模，不能训练或看BFCL/TBLite评测实例。提交顺序冻结后才从五个独立基模副本SFT并评分。
- **task or data unit**：选择单元是完整轨迹；BFCL每组50条、TBLite每组1000条，均选五组；固定Qwen3-4B和任务内相同训练recipe。每代理任务三次独立选择run。
- **unknowns**：- 源池与测试集全量重叠审计unknown - RL和自生成数据扩展unknown

### 原文证据记录中的具体观察
这些是已存证据记录的有界解释。历史记录或未准入记录的存在，不覆盖上方当前准入权限。

- **`r11_ev_datasense`**：DataSense-Bench测量训练前数据价值判断：代理提交五个互不重叠的轨迹子集及效用排序，随后外部固定SFT分别从新基模副本训练并评测。首选数据收益与排序预测是两个独立指标，训练结果不回传用于修改本次选择。
  - 来源版本：2610.12190v1；定位：§3.1 data units tool L88–94；§3.1–3.2 submission/freeze tool L106–116；§3.3–4.1 metrics/downstream evaluation tool L118–133；§5 conclusion/limitations/impact tool L197–206；深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

## 5. 原文选段：把方法与实验细节展开
目前没有可移植的逐字正文选段可纳入本卡。上面仍提供已存方法、结论和定位；不把概括重新包装成原文引文。若研究问题超出这些内容，需要针对对应版本补读。

## 6. 局限、冲突与不能推出的结论

- 只测已有数据SFT选择与排序，RL后训练及生成新数据为未来工作。
- 收益有限且跨任务排序不稳定；挑中有用子集不代表可靠地比较所有子集。
- 未独立复现训练recipe、随机基线或全部失败惩罚。
- 只测已有数据SFT选择与排序，RL后训练及生成新数据为未来工作。; 收益有限且跨任务排序不稳定；挑中有用子集不代表可靠地比较所有子集。; 未独立复现训练recipe、随机基线或全部失败惩罚。

## 7. 与其他论文的具体关系
当前没有准入的双端关系。可以通过研究分支进行主题连读，但不能把共同分支、引用或年代相邻理解为继承。

## 8. 来源清单、复查入口与解析缺口
- `r11_src_datasense` · DataSense-Bench: The First Step Toward an AI Scientist · 2610.12190v1
  - https://arxiv.org/html/2610.12190v1；阅读深度：`selected_primary_benchmark_or_evaluation_protocol_and_limits`。

**证据深度**：original_abstract, selected_primary_benchmark_or_evaluation_protocol_and_limits。
**当前引用权限**：`selected_primary_evaluation_protocol_claims_and_limits_only`；人工签核：`False`。

**AI 联合读取**：`python scripts/dossier.py wf_7448ba9b7dfbaeb226 --excerpts`。解析卡编排本身不新增主张、原文核查或独立复现。
