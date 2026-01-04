---
description: run full verification suite (tests, types, lint) and report results
allowed-tools: Bash(pytest:*), Bash(mypy:*), Bash(ruff:*), Bash(npm:*)
argument-hint: none
---

# Verify

Run full verification suite and report results.

## Steps

1. Run Python verification:
   ```bash
   pytest --tb=short
   mypy .
   ruff check .
   ruff format . --check
   ```

2. Run frontend verification:
   ```bash
   npm run lint
   npm run typecheck
   npm test
   ```

3. Report results in this format:
   ```
   [Verify] Results:
   
   Python:
   - Tests: X passed, Y failed
   - Types: clean / X errors
   - Lint: clean / X warnings
   
   Frontend:
   - Lint: clean / X errors
   - Types: clean / X errors
   - Tests: X passed, Y failed
   
   Status: ✅ All clear / 🔴 Issues found
   ```

4. If issues found, list them with file:line references.

Do not fix anything — report only.
