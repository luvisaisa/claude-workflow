---
description: analyze bug, trace execution, propose minimal fix
allowed-tools: Read, Grep, Glob, Bash(pytest:*)
argument-hint: required: issue_description
---

# Debug

Structured debug workflow for issues.

## Arguments

- $ISSUE — description of the issue
- $LOCATION — where the issue occurs (file, endpoint, etc.) if known

## Steps

1. **Reproduce**
   - Understand reproduction steps
   - Identify relevant test or create minimal repro
   - Confirm the issue exists

2. **Investigate**
   ```
   [Reading] {files being examined}
   ```
   - Trace code path from entry point
   - Identify relevant functions and data flow
   - Check recent changes: `git log --oneline -10 -- {file}`

3. **Hypothesize**
   ```
   [Analyzing] Forming hypotheses:
   1. {hypothesis 1} — {likelihood}
   2. {hypothesis 2} — {likelihood}
   ```

4. **Narrow Down**
   - Add logging or use debugger
   - Test hypotheses systematically
   - Identify root cause

5. **Fix**
   - Implement minimal fix
   - Add test that catches the bug
   - Verify fix works

6. **Report**
   ```
   [Debug Complete]
   
   Root cause: {explanation}
   
   Fix: {what was changed}
   
   Files modified:
   - {file}: {change}
   
   Test added: {test_name}
   
   Prevention: {how to prevent similar issues}
   ```
