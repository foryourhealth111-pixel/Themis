# Download guide

[Project overview](../README.md) | [简体中文](download.zh-CN.md)

## Requirements

Use Python 3.10 or later and install `huggingface_hub`:

```bash
pip install -r requirements.txt
```

The public model is [lili55339/Themis-26B-A4B-V1](https://huggingface.co/lili55339/Themis-26B-A4B-V1). Downloads default to the verified revision `d72b3f8d2ed16f20e9270c29d012e820b93fb31a`. The download helper uses the public Hub; no token is required for a publicly accessible model.

## Preview and download

```bash
python examples/download_model.py --dry-run
python examples/download_model.py --local-dir ./models/Themis-26B-A4B-V1
```

`--dry-run` prints the intended files without downloading or contacting the Hub. The full plan contains 40 model and license files: 31 weight shards, five configuration/tokenizer files, two model cards, LICENSE and NOTICE. Model-card demonstration assets are left on the Hub.

For a small download containing configuration, the weight index, tokenizer configuration and license notices:

```bash
python examples/download_model.py --metadata-only --local-dir ./model-metadata
```

This subset is useful for inspecting packaging. Full model use requires the weight shards and tokenizer vocabulary as well.

Change concurrency or select an explicit revision:

```bash
python examples/download_model.py --max-workers 8 --local-dir ./models/Themis-26B-A4B-V1
python examples/download_model.py --revision d72b3f8d2ed16f20e9270c29d012e820b93fb31a --dry-run
```

The full weight payload is 27,694,122,564 bytes. Reserve at least 30 GB of free space for the model files and extra space for local cache behavior. Re-running the same download reuses files through Hugging Face's download metadata.

## Hugging Face CLI

The official CLI provides a direct alternative:

```bash
hf download lili55339/Themis-26B-A4B-V1 --revision d72b3f8d2ed16f20e9270c29d012e820b93fb31a --local-dir ./models/Themis-26B-A4B-V1
```

This CLI command downloads the model repository, including presentation assets. See the [official download documentation](https://huggingface.co/docs/huggingface_hub/guides/download).

## Running the model

A compatible Themis inference runtime is required separately. This GitHub repository provides documentation and a model-download example. The release does not bundle a runtime or hosted API endpoint. Direct `AutoModelForCausalLM.from_pretrained()` compatibility has not been validated.

For download issues, include your Python version, operating system, selected model revision and the error message in a GitHub issue. Keep credentials and private inputs out of public reports.
