#!/usr/bin/env python3
"""Convert claude-commands to .claude/commands with frontmatter."""

import os
from pathlib import Path

# Command metadata: description and allowed tools
COMMAND_METADATA = {
    # core-workflow
    "VERIFY": {
        "desc": "run full verification suite (tests, types, lint) and report results",
        "tools": "Bash(pytest:*), Bash(mypy:*), Bash(ruff:*), Bash(npm:*)",
        "args": "none"
    },
    "CHECKPOINT": {
        "desc": "pause and summarize progress, await user confirmation before continuing",
        "tools": "*",
        "args": "none"
    },
    "COMPACT": {
        "desc": "create session handoff summary with files changed, decisions, and next steps",
        "tools": "*",
        "args": "none"
    },
    "HELP": {
        "desc": "show all available commands organized by category",
        "tools": "Read, Grep, Glob",
        "args": "none"
    },

    # scaffolding
    "NEW-MODEL": {
        "desc": "create sqlalchemy model with migration and tests",
        "tools": "Read, Glob, Grep, Write, Bash(alembic:*), Bash(pytest:*)",
        "args": "required: model_name table_name fields"
    },
    "NEW-ENDPOINT": {
        "desc": "create fastapi endpoint with validation, tests, and documentation",
        "tools": "Read, Glob, Grep, Write, Edit, Bash(pytest:*)",
        "args": "required: route_path method description"
    },
    "NEW-SERVICE": {
        "desc": "create service module with business logic, tests, and type hints",
        "tools": "Read, Glob, Write, Bash(pytest:*), Bash(mypy:*)",
        "args": "required: service_name description"
    },
    "NEW-ADAPTER": {
        "desc": "create data adapter following existing adapter pattern with registry",
        "tools": "Read, Glob, Grep, Write, Bash(pytest:*)",
        "args": "required: adapter_name source_type"
    },
    "NEW-COMPONENT": {
        "desc": "create react/next.js component with types, styles, and tests",
        "tools": "Read, Glob, Write, Bash(npm:*)",
        "args": "required: component_name component_type"
    },

    # database
    "MIGRATION": {
        "desc": "create alembic migration, review changes, and apply if approved",
        "tools": "Bash(alembic:*), Read, Grep",
        "args": "required: migration_message"
    },
    "MIGRATE-CHECK": {
        "desc": "verify migration status, check for pending migrations",
        "tools": "Bash(alembic:*), Read",
        "args": "none"
    },
    "SEED": {
        "desc": "run database seeding scripts with validation",
        "tools": "Bash(python3:*), Read, Grep",
        "args": "optional: seed_script"
    },

    # testing
    "TEST": {
        "desc": "run pytest with coverage for specified target",
        "tools": "Bash(pytest:*), Read, Grep, Glob",
        "args": "required: target_path"
    },
    "TEST-GENERATE": {
        "desc": "generate comprehensive test suite for specified module or function",
        "tools": "Read, Glob, Grep, Write, Bash(pytest:*)",
        "args": "required: source_path"
    },
    "TEST-EDGE-CASES": {
        "desc": "analyze code and generate edge case tests",
        "tools": "Read, Glob, Grep, Write, Bash(pytest:*)",
        "args": "required: source_path"
    },

    # debug-analysis
    "DEBUG": {
        "desc": "analyze bug, trace execution, propose minimal fix",
        "tools": "Read, Grep, Glob, Bash(pytest:*)",
        "args": "required: issue_description"
    },
    "EXPLAIN": {
        "desc": "explain code functionality, architecture, and patterns",
        "tools": "Read, Grep, Glob",
        "args": "required: code_path"
    },
    "FIND-USAGES": {
        "desc": "find all usages of function, class, or variable across codebase",
        "tools": "Grep, Glob, Read",
        "args": "required: symbol_name"
    },
    "TRACE": {
        "desc": "trace code execution path through multiple files",
        "tools": "Read, Grep, Glob",
        "args": "required: entry_point"
    },

    # refactoring
    "EXTRACT": {
        "desc": "extract code into reusable function/class, update all usages",
        "tools": "Read, Grep, Glob, Edit, Write, Bash(pytest:*), Bash(mypy:*)",
        "args": "required: source_path extraction_target"
    },
    "RENAME-SAFE": {
        "desc": "safely rename symbol across codebase with verification",
        "tools": "Grep, Glob, Edit, Bash(pytest:*), Bash(mypy:*)",
        "args": "required: old_name new_name"
    },
    "REFACTOR-PLAN": {
        "desc": "analyze refactoring scope, create execution plan",
        "tools": "Read, Grep, Glob",
        "args": "required: refactoring_goal"
    },

    # documentation
    "DOCUMENT": {
        "desc": "generate or update documentation for code, api, or architecture",
        "tools": "Read, Grep, Glob, Write, Edit",
        "args": "required: documentation_target"
    },
    "API-DOCS": {
        "desc": "generate api documentation from code with examples",
        "tools": "Read, Grep, Glob, Write",
        "args": "optional: api_path"
    },
    "ARCHITECTURE-SYNC": {
        "desc": "sync architecture.md with current codebase state",
        "tools": "Read, Grep, Glob, Edit",
        "args": "none"
    },

    # git-pr
    "COMMIT": {
        "desc": "create conventional commit with proper message format",
        "tools": "Bash(git:*)",
        "args": "optional: commit_message"
    },
    "CHANGELOG": {
        "desc": "generate changelog from commit history",
        "tools": "Bash(git:*), Read, Write",
        "args": "optional: version_tag"
    },
    "PR-PREP": {
        "desc": "prepare pull request with summary, test plan, and checklist",
        "tools": "Bash(git:*), Read, Write",
        "args": "optional: pr_title"
    },

    # quick-fixes
    "FIX-LINT": {
        "desc": "auto-fix linting issues with ruff and eslint",
        "tools": "Bash(ruff:*), Bash(npm:*)",
        "args": "optional: file_path"
    },
    "FIX-IMPORTS": {
        "desc": "organize and fix import statements",
        "tools": "Read, Edit, Bash(ruff:*)",
        "args": "optional: file_path"
    },
    "FIX-TYPES": {
        "desc": "fix type errors reported by mypy or typescript",
        "tools": "Read, Edit, Bash(mypy:*), Bash(npm:*)",
        "args": "optional: file_path"
    }
}

def add_frontmatter(content: str, metadata: dict) -> str:
    """Add frontmatter to command file."""
    frontmatter = f"""---
description: {metadata['desc']}
allowed-tools: {metadata['tools']}
argument-hint: {metadata['args']}
---

"""
    return frontmatter + content

def process_command(src_path: Path, dest_path: Path):
    """Process a single command file."""
    # Get command name from filename
    cmd_name = src_path.stem

    if cmd_name not in COMMAND_METADATA:
        print(f"Warning: No metadata for {cmd_name}, skipping")
        return

    # Read original content
    content = src_path.read_text()

    # Add frontmatter
    new_content = add_frontmatter(content, COMMAND_METADATA[cmd_name])

    # Write to destination
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(new_content)
    print(f"✓ Converted {cmd_name}")

def main():
    base_dir = Path("/Users/isa/Desktop/python-projects/scripts")
    src_dir = base_dir / "claude-commands"
    dest_dir = base_dir / ".claude" / "commands"

    # Process all markdown files
    for md_file in src_dir.rglob("*.md"):
        if md_file.name == "COMMAND-README.md":
            # Copy README as-is
            dest_file = dest_dir / md_file.name
            dest_file.write_text(md_file.read_text())
            print(f"✓ Copied {md_file.name}")
            continue

        # Get relative path to preserve directory structure
        rel_path = md_file.relative_to(src_dir)
        dest_file = dest_dir / rel_path

        process_command(md_file, dest_file)

    print(f"\n✅ Converted {len(COMMAND_METADATA)} commands to .claude/commands/")

if __name__ == "__main__":
    main()
