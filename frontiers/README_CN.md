# 前沿 Survey · 开放方向目录

[English](README.md) · [简体中文](README_CN.md) · [Registry](registry.json)

这些是待认领的研究提案，不是已完成的 Survey。RSI 仍为现有实例，且独立管理其固定语料。提案中的链接仅有发现导航权限；候选目录不增加 RSI 的收录量。

| 编号 | 候选方向 | 核心研究问题 | 状态 | 文件夹 |
|---|---|---|---|---|
| F01 | 智能体记忆与持续学习 | 外部记忆如何影响后续任务，怎样评估真实迁移？ | ○ 待启动 | [agent-memory](agent-memory/) |
| F02 | 测试时计算、推理与适配 | 额外推理预算和测试时更新分别带来什么变化？ | ○ 待启动 | [test-time-adaptation](test-time-adaptation/) |
| F03 | 科学发现与研究智能体 | 从研究问题到候选结果，哪些环节有可复核证据？ | ○ 待启动 | [scientific-discovery](scientific-discovery/) |
| F04 | 世界模型与具身交互 | 可生成、可预测和可交互的环境模型分别支持什么？ | ○ 待启动 | [world-models](world-models/) |
| F05 | 智能体评测与可靠性 | 怎样区分模型、环境、harness 与评价协议的贡献？ | ○ 待启动 | [agent-evaluation](agent-evaluation/) |
| F06 | 多智能体协作与组织 | 协作结构怎样影响任务分解、通信和执行结果？ | ○ 待启动 | [multi-agent-systems](multi-agent-systems/) |
| ＋ | **你的领域** | 提出范围与读者问题 | 开放补充 | [_template](_template/) |

## 如何补充

1. 选择候选方向；或复制 `_template/` 到新 ID 的目录。
2. 编辑该目录的 `scope.json`：名称、问题、比较轴、一手发现入口及责任人。
3. 在 `registry.json` 的 `directions` 中登记 ID 和相对范围文件路径。
4. 执行下方构建与检查命令，自动同步本目录及项目主 README 的中英文表格。
5. 按[主 README 的步骤](../README_CN.md#为其他领域构建-survey)，将实际研究初始化到该方向的 `survey/` 子目录。
6. 完成相应阶段后再修改状态；`ready` 仅指声明范围的验收，并保留证据深度与例外。

```bash
python scripts/build_frontier_index.py
python scripts/build_frontier_index.py --check
```

命令在仓库根目录执行，无需模型或网络。`registry.json` 只登记目录，各方向的 `scope.json` 是提案内容的维护源；README 为生成视图。不要在提案中计入未做的正文审查。
