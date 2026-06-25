#!/usr/bin/env python3
"""
generate_agents.py — Game Studio OS
Rigenera i file .claude/agents/*.md da roles.json + TEMPLATE_AGENT.md.
Usa per propagare modifiche a regole universali o struttura template.

Uso:
    python3 scripts/generate_agents.py                  # rigenera tutti
    python3 scripts/generate_agents.py design-quest-designer  # uno specifico
"""

import json
import os
import sys
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
ROLES_JSON = ROOT / "roles.json"
TEMPLATE_FILE = ROOT / ".claude" / "TEMPLATE_AGENT.md"
AGENTS_DIR = ROOT / ".claude" / "agents"

TEMPLATE = """\
---
name: {name}
description: {description}
tools: {tools}
model: {model}
---

You are the **{display_name}** of Game Studio OS. Rispondi sempre in italiano salvo richiesta diversa.

## Ruolo
{role_desc}

## Macroarea
{macroarea} — orchestratore: `{parent}`

## Responsabilità
{responsibilities}

## Autorità — puoi modificare
{can_modify_str}

## Limiti — NON puoi modificare
{cannot_modify}

## Output richiesto
{output}

## Regole
Eredita `.claude/RULES_BASE.md`. Nessuna aggiunta specifica.
"""


def slug_to_display(slug: str) -> str:
    parts = slug.split("-")
    return " ".join(p.capitalize() for p in parts[1:]) if len(parts) > 1 else slug.capitalize()


def generate(role: dict) -> str:
    can_modify_lines = "\n".join(f"- {p}" for p in role.get("can_modify", [])) or "- (nessuna)"
    return TEMPLATE.format(
        name=role["name"],
        description=role.get("description", ""),
        tools=role.get("tools", "Read, Write, Edit, Grep, Glob"),
        model=role.get("model", "sonnet"),
        display_name=role.get("display_name", slug_to_display(role["name"])),
        role_desc=role.get("role_desc", "Da definire."),
        macroarea=role.get("macroarea", "Da definire"),
        parent=role.get("parent", "—"),
        responsibilities=role.get("responsibilities", "- Da definire."),
        can_modify_str=can_modify_lines,
        cannot_modify=role.get("cannot_modify", "- Tutto ciò che non è in Autorità"),
        output=role.get("output", "- Formato Markdown con frontmatter YAML"),
    )


def main():
    with open(ROLES_JSON) as f:
        roles = json.load(f)

    target = sys.argv[1] if len(sys.argv) > 1 else None
    count = 0

    for role in roles:
        if target and role["name"] != target:
            continue
        out_path = AGENTS_DIR / f"{role['name']}.md"
        # Only overwrite if role has extended fields (display_name, role_desc, etc.)
        # to avoid clobbering hand-written files that roles.json extracted partially.
        if not role.get("role_desc") and out_path.exists():
            print(f"  SKIP {role['name']} (no role_desc in roles.json — edit roles.json first)")
            continue
        content = generate(role)
        out_path.write_text(content)
        count += 1
        print(f"  OK   {out_path.name}")

    print(f"\nGenerati {count} file agente.")


if __name__ == "__main__":
    main()
