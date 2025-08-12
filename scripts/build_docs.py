# This script generates documentation for the Global.Church schema using LinkML,
# extracts subset information, and updates the main index.md file with a table of subsets.
# It also creates a dedicated Subsets.md page and ensures the index links to it.

#!/usr/bin/env python3
import re
import subprocess
import argparse
from pathlib import Path
import sys

# --- LinkML doc generator overrides ---
from linkml.generators.docgen import DocGenerator
from linkml_runtime.linkml_model.meta import SubsetDefinition
from linkml_runtime.utils.formatutils import underscore

try:
    import yaml  # PyYAML
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "globalchurch.yaml"
DOCS_DIR = ROOT / "docs"
INDEX_MD = DOCS_DIR / "index.md"


# --- Custom DocGenerator to force subset pages to snake_case ---
class SnakeCaseSubsetDocGen(DocGenerator):
    """
    Override DocGenerator.name() so SubsetDefinition pages/links are snake_case
    (e.g., 'church_core.html' instead of 'ChurchCore.html').
    """
    def name(self, element):
        if isinstance(element, SubsetDefinition):
            return underscore(element.name)
        return super().name(element)

def run_linkml_docs():
    """
    Generate docs with a custom DocGenerator so that subset pages are snake_case.
    This replaces the 'linkml generate doc' subprocess call.
    """
    DOCS_DIR.mkdir(exist_ok=True)
    # Some LinkML versions don't accept 'yamlfile='; pass schema path positionally.
    try:
        gen = SnakeCaseSubsetDocGen(
            str(SCHEMA),                 # positional path to schema file
            directory=str(DOCS_DIR),
            index_name="index",
        )
    except TypeError:
        # Fallback for older/newer API variants that lack 'index_name' or differ slightly
        gen = SnakeCaseSubsetDocGen(
            str(SCHEMA),
            directory=str(DOCS_DIR),
        )
    gen.serialize()

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
    """
    Replace the entire '## Subsets' section body with a fresh GFM table.
    We do NOT reuse any existing header/separator lines to avoid carrying
    forward malformed Markdown.
    """
    # Normalize line endings
    text = index_text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    # Find '## Subsets' header line
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## subsets"):
            start = i
            break

    # If there is no Subsets section, append one at the end
    if start is None:
        if not text.endswith("\n"):
            text += "\n"
        # Write header + blank line + table
        return text + "\n## Subsets\n\n" + table_md

    # Find the next header after Subsets (or EOF)
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break

    # Keep everything before '## Subsets', then write a clean section, then the tail
    head = "\n".join(lines[:start])  # up to but not including the header
    tail = "\n".join(lines[end:])    # from the next header (or EOF)

    # Compose a clean section: header + blank + our table
    section = "## Subsets\n\n" + table_md.rstrip() + "\n"

    # Ensure correct spacing between chunks
    if head and not head.endswith("\n"):
        head += "\n"
    if tail and not tail.startswith("\n"):
        tail = "\n" + tail

    return head + section + tail

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


# --- Remove Mermaid diagrams from generated docs ---
def strip_mermaid_diagrams(text: str) -> str:
    """
    Remove Mermaid class diagrams from generated Markdown.
    We strip any fenced code block that starts with ```mermaid and contains 'classDiagram'.
    This is idempotent and safe to run multiple times.
    """
    # Normalize newlines
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    # Pattern for fenced mermaid blocks (non-greedy)
    import re as _re
    pattern = _re.compile(r"```mermaid\s+.*?classDiagram.*?```", _re.DOTALL | _re.IGNORECASE)
    t = pattern.sub("", t)
    return t


def remove_diagrams_from_docs():
    """
    Iterate over generated Markdown files and remove Mermaid class diagrams.
    We target class pages primarily (e.g., 'User.md', 'Church.md'), but it's safe
    to process all .md files.
    """
    for md_path in DOCS_DIR.glob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        new_text = strip_mermaid_diagrams(text)
        if new_text != text:
            md_path.write_text(new_text, encoding="utf-8")

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
    print("• Removing Mermaid class diagrams from generated pages…")
    remove_diagrams_from_docs()

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