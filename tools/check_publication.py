#!/usr/bin/env python3
"""Validate the public release allowlist, links, and accidental secret patterns."""
import ast
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = frozenset(['.gitattributes', '.github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/config.yml', '.github/ISSUE_TEMPLATE/feedback.yml', '.github/workflows/publication-check.yml', '.gitignore', 'CONTRIBUTING.md', 'LICENSE', 'NOTICE', 'README.md', 'README.zh-CN.md', 'assets/computer-agent.gif', 'assets/files-agent.gif', 'assets/poster-agent.gif', 'assets/serial-token-latency.en.png', 'assets/serial-token-latency.zh-CN.png', 'assets/themis-cover.png', 'docs/benchmarks.md', 'docs/benchmarks.zh-CN.md', 'docs/download.md', 'docs/download.zh-CN.md', 'examples/download_model.py', 'requirements.txt', 'tools/check_publication.py'])


def main():
    if (ROOT / ".git").exists():
        result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                                cwd=ROOT, capture_output=True, check=True)
        paths = {name.decode("utf-8") for name in result.stdout.split(b"\0") if name}
    else:
        paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                 if p.is_file() and "__pycache__" not in p.parts}
    errors = []
    for name in sorted(paths - ALLOWED):
        errors.append("File outside publication allowlist: " + name)
    for name in sorted(ALLOWED - paths):
        errors.append("Missing required public file: " + name)
    secret = re.compile(r"(?:hf_[A-Za-z0-9]{25,}|gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{25,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
    for name in sorted(paths & ALLOWED):
        path = ROOT / name
        if path.is_symlink():
            errors.append("Symlinks are not allowed: " + name)
        if path.stat().st_size > 12 * 1024 * 1024:
            errors.append("Public file exceeds 12 MiB: " + name)
        if path.suffix not in {".md", ".py", ".txt", ".yml", ""} and not name.startswith(".git"):
            continue
        text = path.read_text(encoding="utf-8")
        if secret.search(text):
            errors.append("Credential-like content found in: " + name)
        if path.suffix == ".py":
            ast.parse(text, filename=name)
        if path.suffix == ".md":
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                if "://" in link or link.startswith("#"):
                    continue
                target = (path.parent / link.split("#", 1)[0]).resolve()
                if not target.is_relative_to(ROOT) or not target.is_file():
                    errors.append("Broken local link in " + name + ": " + link)
            if re.search(r"(?:不是|并非|并不是)[^。\n]{0,100}(?:而是|而要|而应)", text):
                errors.append("Chinese framing rule violation in " + name)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(paths)} public files, local document links, and secret patterns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
