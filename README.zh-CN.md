# Themis

**面向工具选择、分类和 Agent 动作决策的开放权重结构化决策模型。**

[English](README.md) | **简体中文**

[模型权重](https://huggingface.co/lili55339/Themis-26B-A4B-V1) · [完整评测](docs/benchmarks.zh-CN.md) · [下载指南](docs/download.zh-CN.md) · [Apache 2.0](LICENSE)

![Themis：面向 Agent 的结构化决策](assets/themis-cover.png)

Themis 根据场景、问题或候选动作输出结构化决策及相应概率，适用于工具选择、请求分类、业务规则判断和 Agent 下一步动作选择。

当前模型版本为 **Themis-26B-A4B-V1**，基于 **Google DeepMind 的 Gemma 4 26B-A4B-it**，INT8 模型权重已发布到 Hugging Face。

## 评测摘要

以下结果来自项目已完成的评测，记录日期为 **2026 年 10 月 14 日**。各项评测保留其原生统计口径。

| 评测 | 结果 | 本次对照中的位置 | 范围 |
| --- | ---: | --- | --- |
| Heaven | **93.07%** | **所选 12 个模型中第 1** | 同一组公开题，答对 215 / 231 道 |
| Decision Index 0.3 | **70.46** | **复现对照的 12 个模型中第 1** | 公开校正指数；37 个题集，覆盖五个领域 |
| QUB / jevbench-240 | **82.15 / 100** | **已保存快照的 22 个模型中第 2** | 240 个案例的完整套件一致性分数 |

[完整评测说明](docs/benchmarks.zh-CN.md)包含对照表，以及 Themis 低于所列 Jev 基线的工作流结果。QUB 结果来自项目自行运行的评测，尚未登记为官方榜单提交。

## 基准测试排名

以下图片采用 **2026 年 10 月 14 日**的评测快照，排名适用于图中列出的模型和基准版本。Themis 成绩来自项目本地评测，尚未登记为官方榜单条目。既往训练与实验记录中存在公开评测数据重合情况，请结合这一背景阅读结果。

### 三项基准总览

![Themis 在 Heaven、Decision Index 0.3 和 QUB 中的得分与对照位置](assets/benchmarks/00-benchmark-overview.png)

### Heaven：所选 12 个模型，同一组 231 道题

准确率为 **93.07%**，答对 215 道题。采用 v1.3.0 参考结果，与 Jev 1.13.0 相比高 **6.49 个百分点**，与 OpenJev thinking 相比高 **4.33 个百分点**。

![Heaven 所选 12 个决策模型的准确率排名](assets/benchmarks/01-heaven.png)

### Decision Index 0.3：公开复现文件中的全部 11 个模型加 Themis

公开指数为 **70.46**，比 Torchcast Decision 27B 高 **5.36 分**，比 Jev 高 **12.50 分**。对照采用公开评测部分；维护者的 Full score 还包含私有评测。

![Decision Index 0.3 公开指数的 12 模型排名](assets/benchmarks/02-decision-index-0.3.png)

### QUB / jevbench-240：快照中的全部 21 个参考模型加 Themis

完整套件得分为 **82.15 / 100**，在这组 22 模型快照中位列第 2。Open-Jev-9B 得分为 **83.90**，图中所有模型均采用完整 240 案例套件的统计口径。

![QUB 完整套件一致性得分的 22 模型排名](assets/benchmarks/03-qub-full.png)

### Decision Index 0.3：五大领域对比

Themis 在五个领域的得分均高于已保存的 Jev 基线，其中工具与自动化得分为 **85.86**。领域分数采用基准原生权重计算。

![Themis 与 Jev 在 Decision Index 五大领域的得分对比](assets/benchmarks/04-decision-index-domains.png)

[完整分数表与测量说明](docs/benchmarks.zh-CN.md)提供图中全部模型的具体分数、领域表现、一致性维度及补充工作流结果。

## 应用演示

### 文件整理

查找指定海报，重命名并归档，最后检查目标目录。

![Themis 网页文件整理演示](assets/files-agent.gif)

### 商品海报编辑

在 Photopea 中替换产品图片、调整版式、更新标题和价格，并导出海报。

![Themis 商品海报编辑演示](assets/poster-agent.gif)

### 电脑选配

选择规格，核对预算与报价，并保存配置供审核。

![Themis 电脑选配演示](assets/computer-agent.gif)

### 国际象棋：中局对弈

![Themis 国际象棋中局对弈演示](assets/chess.gif)

从复杂中局展开对弈，围绕子力交换、进攻与防守推进棋局。

### 超级马里奥：奔跑与跳跃

![Themis 超级马里奥演示](assets/mario.gif)

在经典马里奥关卡中奔跑、跳跃和跨越障碍，沿关卡向前推进。

### DOOM：正面防守

![Themis DOOM 正面防守演示](assets/doom.gif)

在正面防守场景中瞄准来袭敌人并持续开火，应对连续进攻。

### 五人制足球：进攻配合

![Themis 五人制足球进攻演示](assets/football.gif)

通过传球、带球与射门完成一次进攻配合，并取得进球。

以上七个演示展示项目评测环境中的效果。[Hugging Face 模型介绍](https://huggingface.co/lili55339/Themis-26B-A4B-V1#3-application-demos)同样包含完整演示；本仓库提供介绍文档和下载工具。

## 下载模型

使用 Python 3.10 或更新版本。先查看下载计划，再下载固定版本的模型：

```bash
pip install -r requirements.txt
python examples/download_model.py --dry-run
python examples/download_model.py --local-dir ./models/Themis-26B-A4B-V1
```

默认固定版本为 `4dffa8ec99f3db6683f784b60c73846dc1f136b2`。31 份权重分片约占 **27.69 GB**（十进制单位），请额外预留分词器和下载元数据空间。脚本使用明确的文件清单，并通过 `huggingface_hub` 支持恢复下载。

小体积的元数据下载、命令行方式及其他选项见[下载指南](docs/download.zh-CN.md)。

### 推理运行条件

运行这些权重需要另行配套兼容的 Themis 推理运行时。本次 GitHub 发布包含下载工具；推理服务器和托管 API 位于当前发布范围之外。尚未验证直接通过 `AutoModelForCausalLM.from_pretrained()` 加载此发布包。

## 仓库内容

- **GitHub：**中英介绍、评测摘要、精选演示录像和模型下载工具。
- **Hugging Face：**模型权重、必要配置及分词器文件。
- **公开范围：**训练流程、训练数据集和内部架构实现单独维护，保留在本次公开范围之外。

## 反馈与贡献

欢迎通过 [Issues](https://github.com/foryourhealth111-pixel/Themis/issues)反馈下载问题、文档修正和使用场景。请附上模型版本及相关环境信息，并确认公开示例的使用权限。贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证与署名

本仓库的原创文档、下载工具和发布检查工具采用 **Apache License 2.0**。链接到的 Themis 模型文件同样采用 Apache 2.0。完整条款和署名见 [LICENSE](LICENSE) 与 [NOTICE](NOTICE)。

演示素材中的第三方内容仍受各自权利人的权利约束。模型和项目许可证不授予第三方内容及商标的额外使用权。
