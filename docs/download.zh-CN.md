# 下载指南

[项目首页](../README.zh-CN.md) | [English](download.md)

## 环境

使用 Python 3.10 或更新版本，安装 `huggingface_hub`：

```bash
pip install -r requirements.txt
```

公开模型地址为 [lili55339/Themis-26B-A4B-V1](https://huggingface.co/lili55339/Themis-26B-A4B-V1)。脚本默认下载已核验的固定版本 `d72b3f8d2ed16f20e9270c29d012e820b93fb31a`。公开可访问的模型可直接通过 Hub 下载。

## 查看计划与下载

```bash
python examples/download_model.py --dry-run
python examples/download_model.py --local-dir ./models/Themis-26B-A4B-V1
```

`--dry-run` 仅打印计划文件清单，执行期间不访问 Hub。完整计划包含 40 个模型和许可证文件：31 份权重、5 个配置与分词器文件、2 份模型介绍，以及 LICENSE 和 NOTICE。模型介绍中的演示素材保留在 Hub。

可先下载小体积的配置、权重索引、分词器配置和许可声明：

```bash
python examples/download_model.py --metadata-only --local-dir ./model-metadata
```

该子集可用于检查发布格式。完整使用模型还需要权重分片及分词器词表。

可调整并发数或显式指定版本：

```bash
python examples/download_model.py --max-workers 8 --local-dir ./models/Themis-26B-A4B-V1
python examples/download_model.py --revision d72b3f8d2ed16f20e9270c29d012e820b93fb31a --dry-run
```

权重总大小为 27,694,122,564 字节。建议为模型文件至少预留 30 GB，并为本地缓存额外预留空间。重复执行相同下载会通过 Hugging Face 下载元数据复用已有文件。

## Hugging Face 命令行

也可以使用官方 CLI：

```bash
hf download lili55339/Themis-26B-A4B-V1 --revision d72b3f8d2ed16f20e9270c29d012e820b93fb31a --local-dir ./models/Themis-26B-A4B-V1
```

该命令下载模型仓库及其中的展示素材。详细行为见 [Hugging Face 下载文档](https://huggingface.co/docs/huggingface_hub/guides/download)。

## 推理运行条件

推理需要另行准备兼容的 Themis 运行时。本仓库提供介绍文档和下载示例；运行时与托管 API 位于本次发布范围之外。尚未验证直接通过 `AutoModelForCausalLM.from_pretrained()` 加载。

反馈下载问题时，请提供 Python 版本、操作系统、模型版本和错误信息。凭据及私有输入请保留在本地。
