#!/usr/bin/env python3
"""Download the published Themis model files from Hugging Face."""
import argparse
import json
from pathlib import Path

REPO_ID = "lili55339/Themis-26B-A4B-V1"
DEFAULT_REVISION = "4dffa8ec99f3db6683f784b60c73846dc1f136b2"
METADATA_FILES = (
    "README.md", "README.zh-CN.md", "LICENSE", "NOTICE", "config.json",
    "model.safetensors.index.json", "tokenizer/tokenizer_config.json",
)
MODEL_FILES = METADATA_FILES + (
    "tokenizer/tokenizer.json", "tokenizer/chat_template.jinja",
) + tuple(f"weights/layer-{index:02d}.safetensors" for index in range(30)) + (
    "weights/shared.safetensors",
)


def positive_workers(value):
    workers = int(value)
    if not 1 <= workers <= 32:
        raise argparse.ArgumentTypeError("Use between 1 and 32 download workers.")
    return workers


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-dir", type=Path, default=Path("models/Themis-26B-A4B-V1"))
    parser.add_argument("--revision", default=DEFAULT_REVISION)
    parser.add_argument("--max-workers", type=positive_workers, default=8)
    parser.add_argument("--metadata-only", action="store_true", help="Download small metadata and license files.")
    parser.add_argument("--dry-run", action="store_true", help="Print a download plan without network requests.")
    args = parser.parse_args(argv)
    planned = METADATA_FILES if args.metadata_only else MODEL_FILES
    plan = {"repo_id": REPO_ID, "revision": args.revision,
            "local_dir": str(args.local_dir), "max_workers": args.max_workers,
            "file_count": len(planned), "files": list(planned)}
    print(json.dumps(plan, indent=2))
    if args.dry_run:
        return 0
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        parser.exit(1, "Install dependencies first: pip install -r requirements.txt\n")
    path = snapshot_download(repo_id=REPO_ID, repo_type="model", revision=args.revision,
                             local_dir=str(args.local_dir), allow_patterns=list(planned),
                             max_workers=args.max_workers)
    print("Download complete: " + str(path))
    print("Model inference requires a compatible Themis runtime supplied separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
