# Themis

**面向工具选择、分类和 Agent 动作决策的开放权重结构化决策模型。**

[English](README.md) | **简体中文**

[模型权重](https://huggingface.co/lili55339/Themis-26B-A4B-V1) · [完整评测](docs/benchmarks.zh-CN.md) · [下载指南](docs/download.zh-CN.md) · [Apache 2.0](LICENSE)

![Themis：面向 Agent 的结构化决策](assets/themis-cover.png)

Themis 根据场景、问题或候选动作输出结构化决策及相应概率，适用于工具选择、请求分类、业务规则判断和 Agent 下一步动作选择。

当前模型版本为 **Themis-26B-A4B-V1**，基于 **Google DeepMind 的 Gemma 4 26B-A4B-it**，INT8 模型权重已发布到 Hugging Face。

## 评测摘要

以下结果来自项目已完成的评测，记录日期为 **2026 年 10 月 14 日**。各项评测保留其原生统计口径。

| 评测 | 结果 | 范围 |
| --- | ---: | --- |
| Heaven | **93.07%** | 同一组公开题，答对 215 / 231 道 |
| Decision Index 0.3 | **70.46** | 公开校正指数；37 个题集，覆盖五个领域 |
| QUB / jevbench-240 | **82.15 / 100** | 240 个案例的完整套件一致性分数 |
| Heaven 串行延迟 | **P50 43.54 ms · P95 131.78 ms** | 单张 RTX PRO 6000 Blackwell Server Edition，231 次单问题请求 |

延迟从同机 HTTP 请求提交开始，计算到完整响应接收完成；模型加载和服务预热在计时前完成，首个正式请求纳入统计。这组 Heaven 输入为 91–3,869 tokens。硬件、输入长度和服务条件会影响延迟。

[完整评测说明](docs/benchmarks.zh-CN.md)包含对照表、长输入测试，以及 Themis 低于所列 Jev 基线的工作流结果。QUB 结果来自项目自行运行的评测，尚未登记为官方榜单提交。

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

以上七个演示展示项目评测环境中的效果。[Hugging Face 模型介绍](https://huggingface.co/lili55339/Themis-26B-A4B-V1#4-application-demos)同样包含完整演示；本仓库提供介绍文档和下载工具。

## 下载模型

使用 Python 3.10 或更新版本。先查看下载计划，再下载固定版本的模型：

```bash
pip install -r requirements.txt
python examples/download_model.py --dry-run
python examples/download_model.py --local-dir ./models/Themis-26B-A4B-V1
```

默认固定版本为 `d72b3f8d2ed16f20e9270c29d012e820b93fb31a`。31 份权重分片约占 **27.69 GB**（十进制单位），请额外预留分词器和下载元数据空间。脚本使用明确的文件清单，并通过 `huggingface_hub` 支持恢复下载。

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
