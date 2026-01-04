---
description: create conventional commit with proper message format
allowed-tools: Bash(git:*)
argument-hint: optional: commit_message
---

# Commit

Verify, format, and generate conventional commit message.

## Steps

1. Run verification:
   ```bash
   pytest --tb=short
   mypy .
   ruff check .
   ruff format .
   npm run lint --fix
   ```

2. Check for issues:
   - If tests fail: stop and report
   - If types fail: stop and report
   - Fix auto-fixable lint issues
   - Report unfixable issues

3. Analyze changes:
   ```bash
   git diff --staged --stat
   git diff --staged
   ```

4. Generate commit message:
   - Determine type: feat, fix, refactor, test, docs, chore, perf
   - Determine scope from changed files
   - Write concise description
   - Add body if changes are complex

5. Output:
   ```
   [Commit] Ready
   
   Verification: ✅ All passed
   
   Staged changes:
   - {file}: {summary}
   
   Suggested commit message:
   
   {type}({scope}): {description}
   
   {optional body}
   
   Run: git commit -m "{message}"
   ```

Do not execute git commit — provide message only.
