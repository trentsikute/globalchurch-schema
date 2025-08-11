# This script generates documentation for the Global.Church schema using LinkML,
# extracts subset information, and updates the main index.md file with a table of subsets.
# It also creates a dedicated Subsets.md page and ensures the index links to it.

#!/usr/bin/env python3
import re
import subprocess
import argparse
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

    # Find '## Subsets' header line
    subsets_h = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('## subsets'):
            subsets_h = i
            break

    # If no Subsets header exists, append a new section with header + table
    if subsets_h is None:
        if not text.endswith('\n'):
            text += '\n'
        return text + '\n## Subsets\n\n' + table_md

    # Within the Subsets section, locate the markdown table header
    table_header_idx = None
    for j in range(subsets_h + 1, len(lines)):
        if lines[j].strip().startswith('| Subset |'):
            table_header_idx = j
            break
        # stop if we hit the next header before finding a table
        if lines[j].startswith('## '):
            table_header_idx = None
            break

    # Find the end of the Subsets section (next header or EOF)
    next_header_idx = len(lines)
    for k in range(subsets_h + 1, len(lines)):
        if lines[k].startswith('## '):
            next_header_idx = k
            break

    # Build the new section body
    new_section_body = []
    if table_header_idx is None:
        # No table existed – construct full section body
        new_section_body.append('')  # ensure blank line after header
        new_section_body.append(table_md.rstrip())
        new_section_body.append('')
    else:
        # Keep the header line and the separator line, then replace the rest with our rows
        sep_idx = table_header_idx + 1 if table_header_idx + 1 < len(lines) else table_header_idx
        # Copy header + separator exactly as they are in the original file
        header_line = lines[table_header_idx]
        sep_line = lines[sep_idx]
        new_section_body.extend([header_line, sep_line])
        # Append our generated rows (without re-adding header/separator)
        # Extract only the body rows from table_md by skipping the first two lines
        gen_lines = table_md.strip('\n').split('\n')
        body_rows = gen_lines[2:] if len(gen_lines) > 2 else []
        new_section_body.extend(body_rows)
        new_section_body.append('')

    # Reassemble the document
    head = '\n'.join(lines[:subsets_h + 1])  # include '## Subsets' line
    tail = '\n'.join(lines[next_header_idx:])

    # Ensure proper newlines around the section
    if head and not head.endswith('\n'):
        head += '\n'
    if tail and not tail.startswith('\n'):
        tail = '\n' + tail

    return head + '\n'.join(new_section_body) + tail

def fix_enum_links(index_text: str, to_html: bool) -> str:
    """
    Convert enum links between .md <-> .html depending on target.
    - For local preview in VS Code: keep .md (to_html=False)
    - For GitHub Pages: use .html (to_html=True)
    """
    if to_html:
        # BeliefTypeEnum.md -> BeliefTypeEnum.html
        pattern = re.compile(r"\]\(([A-Z][A-Za-z0-9]*Enum)\.md\)")
        return pattern.sub(r"](\1.html)", index_text)
    else:
        # BeliefTypeEnum.html -> BeliefTypeEnum.md (if previously rewritten)
        pattern = re.compile(r"\]\(([A-Z][A-Za-z0-9]*Enum)\.html\)")
        return pattern.sub(r"](\1.md)", index_text)

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


# --- New helper functions for slot examples ---
def load_examples_by_slot():
    """Return a dict: slot_name -> list of {value, description} from the YAML schema."""
    data = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    slots = (data or {}).get("slots", {}) or {}
    examples_by_slot = {}
    for slot_name, slot_body in slots.items():
        ex_list = (slot_body or {}).get("examples", []) or []
        norm = []
        for ex in ex_list:
            if isinstance(ex, dict):
                val = ex.get("value", "")
                desc = ex.get("description", "")
                # Ensure strings (generator expects strings in docs)
                val = "" if val is None else str(val)
                desc = "" if desc is None else str(desc)
                norm.append({"value": val, "description": desc})
            else:
                # If example is a bare string, keep it, empty description
                norm.append({"value": str(ex), "description": ""})
        if norm:
            examples_by_slot[slot_name] = norm
    return examples_by_slot


def build_examples_table(rows):
    """Make a two-column Markdown table (Value | Description) from example rows."""
    if not rows:
        return ""
    out = ["| Value | Description |", "| --- | --- |"]
    for r in rows:
        v = (r.get("value") or "").replace("|", r"\|")
        d = (r.get("description") or "").replace("|", r"\|")
        # Keep rows even if description is empty
        out.append(f"| {v} | {d} |")
    return "\n".join(out) + "\n\n"


def rewrite_slot_examples_sections(examples_by_slot):
    """For each docs/slot.*.md page, replace the Examples section body with a
    two-column table built from YAML examples (Value | Description).
    The function preserves the existing '## Examples' header and replaces only
    the content until the next '## ' header (or EOF).
    """
    for md_path in DOCS_DIR.glob("slot.*.md"):
        text = md_path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
        # slot.<name>.md -> <name>
        slot_name = md_path.stem.split(".", 1)[-1]
        rows = examples_by_slot.get(slot_name)
        if not rows:
            # nothing to rewrite for this slot
            continue
        table = build_examples_table(rows)
        if not table.strip():
            continue
        lines = text.split("\n")
        # Find '## Examples' header
        start = None
        for i, ln in enumerate(lines):
            if ln.strip().lower().startswith("## examples"):
                start = i
                break
        if start is None:
            # If no Examples header exists, append one at the end
            if not text.endswith("\n"):
                text += "\n"
            text += "\n## Examples\n\n" + table
            md_path.write_text(text, encoding="utf-8")
            continue
        # Find next section header after start
        end = len(lines)
        for j in range(start + 1, len(lines)):
            if lines[j].startswith("## "):
                end = j
                break
        # Rebuild: keep up to the header line, then header + blank + our table, then tail
        head = "\n".join(lines[: start + 1])
        tail = "\n".join(lines[end:])
        if head and not head.endswith("\n"):
            head += "\n"
        if tail and not tail.startswith("\n"):
            tail = "\n" + tail
        new_text = head + "\n" + table + tail
        if new_text != text:
            md_path.write_text(new_text, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", action="store_true",
                    help="Generate index links for GitHub Pages (.html) instead of local .md")
    args = ap.parse_args()
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
    updated = fix_enum_links(updated, to_html=args.pages)

    if updated != original:
        INDEX_MD.write_text(updated, encoding="utf-8")
        print(f"✓ Updated Subsets table with {len(rows)} row(s).")
    else:
        print("i No changes made (section already up to date).")

    print("• Rewriting slot Examples sections with two-column tables…")
    examples_by_slot = load_examples_by_slot()
    rewrite_slot_examples_sections(examples_by_slot)

    # Always write a dedicated Subsets page and ensure index links to it
    write_subsets_page(rows)

if __name__ == "__main__":
    main()