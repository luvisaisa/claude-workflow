---
description: generate or update documentation for code, api, or architecture
allowed-tools: Read, Grep, Glob, Write, Edit
argument-hint: required: documentation_target
---

# Document

Generate/update docstrings and README for module.

## Arguments

- $TARGET — module or directory to document

## Steps

1. Read the code and understand:
   - Module purpose
   - Public API
   - Usage patterns
   - Dependencies

2. Update docstrings:
   - Module-level docstring
   - Class docstrings
   - Public function docstrings (Google style)
   - Skip obvious private helpers

3. Create/update README if directory:
   ```markdown
   # {Module Name}
   
   {Brief description}
   
   ## Overview
   {What this module does}
   
   ## Usage
   {Code examples}
   
   ## API Reference
   {Key classes and functions}
   
   ## Dependencies
   {What this module requires}
   ```

4. Run verification:
   ```bash
   ruff check {target}
   ```

5. Report:
   ```
   [Document] {target}
   
   Updated:
   - {count} docstrings added/updated
   - README: {created/updated/unchanged}
   
   Files modified:
   - {file}
   ```
