"""Check local Markdown link targets and skill metadata without dependencies."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
errors = []
for file in root.rglob("*.md"):
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        local = target.split("#", 1)[0]
        if local and not (file.parent / local).exists():
            errors.append(f"{file.relative_to(root)}: missing {target}")
for file in (root / "skills").glob("*/SKILL.md"):
    text = file.read_text()
    if not text.startswith("---\n") or not re.search(r"^name: .+", text, re.M) or not re.search(r"^description: .+", text, re.M):
        errors.append(f"{file.relative_to(root)}: missing skill metadata")
if errors:
    raise SystemExit("\n".join(errors))
print("Local Markdown links and skill metadata passed.")
