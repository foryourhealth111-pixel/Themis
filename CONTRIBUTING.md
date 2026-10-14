# Contributing

Thank you for helping improve Themis documentation and model access.

This repository accepts documentation corrections, improvements to the download utility, and reproducible evaluation feedback. Training pipelines, datasets and internal runtime implementations are maintained separately.

Before opening a pull request:

1. Keep changes within the public file allowlist in `tools/check_publication.py`.
2. Run `python tools/check_publication.py` and `python examples/download_model.py --dry-run`.
3. Keep credentials, server connection information, private inputs and downloaded model files out of Git.
4. Include the model revision and measurement conditions when reporting results.

Original contributions are provided under the repository's Apache 2.0 license. Identify any third-party materials and their applicable licenses.

Use [GitHub Issues](https://github.com/foryourhealth111-pixel/Themis/issues) for download problems and feedback. The [Hugging Face model card](https://huggingface.co/lili55339/Themis-26B-A4B-V1) describes the model release and its evaluation snapshot.
