#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path
import sys

try:
    import yaml  # PyYAML
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "globalchurch.yaml"
DOCS_DIR = ROOT / "docs"
INDEX_MD = DOCS_DIR / "index.md"

def run_linkml_docs():
    DOCS_DIR.mkdir(exist_ok=True)
    cmd = ["linkml", "generate", "doc", str(SCHEMA), "--directory", str(DOCS_DIR)]
    subprocess.check_call(cmd)

def load_subsets():
    data = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    subsets = data.get("subsets", {}) or {}
    # ensure deterministic ordering by key
    rows = []
    for name in sorted(subsets.keys()):
        desc = (subsets[name] or {}).get("description", "").strip()
        rows.append((name, desc))
    return rows

def replace_subsets_section(index_text: str, table_md: str) -> str:
    # Normalize line endings
    text = index_text.replace('\r\n', '\n').replace('\r', '\n')
    lines = text.split('\n')

    # Find '## Subsets' header
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('## subsets'):
            start = i
            break

    # If not present, append a new section at end
    if start is None:
        if not text.endswith('\n'):
            text += '\n'
        return text + '\n## Subsets\n\n' + table_md

    # Find next section header starting with '## '
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('## '):
            end = j
            break

    head = '\n'.join(lines[:start])
    tail = '\n'.join(lines[end:])

    new_section = '## Subsets\n\n' + table_md.rstrip() + '\n'

    if head and not head.endswith('\n'):
        head += '\n'
    if tail and not tail.startswith('\n'):
        tail = '\n' + tail

    return head + new_section + tail

def build_table(rows):
    if not rows:
        return "| Subset | Description |\n| --- | --- |\n| _None defined_ | |\n\n"
    lines = ["| Subset | Description |", "| --- | --- |"]
    for name, desc in rows:
        desc = (desc or '').replace('|', r'\|')
        lines.append(f"| {name} | {desc} |")
    return "\n".join(lines) + "\n\n"

def write_subsets_page(rows):
    """Create/overwrite docs/Subsets.md with a dedicated table so it can be linked directly."""
    DOCS_DIR.mkdir(exist_ok=True)
    page = [
        "# Subsets", "",
        build_table(rows)
    ]
    (DOCS_DIR / "Subsets.md").write_text("\n".join(page), encoding="utf-8")


def ensure_index_link_to_subsets():
    """Ensure index.md contains a link to the Subsets page near the top."""
    if not INDEX_MD.exists():
        return
    text = INDEX_MD.read_text(encoding='utf-8')
    # If a link already exists, do nothing
    if "[Subsets](Subsets.md)" in text or "(Subsets.md)" in text:
        return
    # Insert after the first H1 or at top
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith('# '):
            insert_at = i + 1
            break
    lines.insert(insert_at, "")
    lines.insert(insert_at + 1, "- See **[Subsets](Subsets.md)** for a full list of subset tags.")
    INDEX_MD.write_text('\n'.join(lines), encoding='utf-8')

def main():
    if not SCHEMA.exists():
        print(f"Schema not found: {SCHEMA}")
        sys.exit(1)

    print("• Generating docs with LinkML…")
    run_linkml_docs()

    print("• Loading subsets from YAML…")
    rows = load_subsets()
    table_md = build_table(rows)

    if not INDEX_MD.exists():
        print(f"index.md not found at {INDEX_MD} (did doc generation succeed?)")
        sys.exit(1)

    print("• Updating Subsets section in docs/index.md…")
    original = INDEX_MD.read_text(encoding="utf-8")
    updated = replace_subsets_section(original, table_md)

    if updated != original:
        INDEX_MD.write_text(updated, encoding="utf-8")
        print(f"✓ Updated Subsets table with {len(rows)} row(s).")
    else:
        print("i No changes made (section already up to date).")

    # Always write a dedicated Subsets page and ensure index links to it
    write_subsets_page(rows)
    ensure_index_link_to_subsets()

if __name__ == "__main__":
    main()