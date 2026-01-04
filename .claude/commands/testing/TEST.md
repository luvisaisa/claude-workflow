---
description: run pytest with coverage for specified target
allowed-tools: Bash(pytest:*), Read, Grep, Glob
argument-hint: required: target_path
---

# Test

Run pytest with coverage for specified target.

## Arguments

- $TARGET — file, module, or test path (e.g., "src/services/parser.py", "tests/api/")

## Steps

1. Determine test path:
   - If source file: find corresponding test file
   - If test path: use directly
   - If module: find all related tests

2. Run tests with coverage:
   ```bash
   pytest {test_path} -v --tb=short --cov={source_path} --cov-report=term-missing
   ```

3. Report:
   ```
   [Test] Results for {target}
   
   Tests: {passed} passed, {failed} failed, {skipped} skipped
   Coverage: {percentage}%
   
   Uncovered lines:
   - {file}:{lines}
   
   Failed tests:
   - {test_name}: {reason}
   ```
