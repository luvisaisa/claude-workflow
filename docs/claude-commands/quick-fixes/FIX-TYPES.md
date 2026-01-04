# Fix Types

Run mypy and fix all type errors.

## Steps

1. Run mypy:
   ```bash
   mypy . --show-error-codes
   ```

2. For each error:
   - Analyze the error
   - Determine correct fix
   - Apply fix
   - Track what was changed

3. Common fixes:
   - Add missing type hints
   - Fix incorrect types
   - Add `# type: ignore` with comment for unfixable
   - Add null checks for Optional types
   - Fix import issues

4. Re-run mypy to confirm clean

5. Run tests to ensure no regressions:
   ```bash
   pytest --tb=short
   ```

6. Report:
   ```
   [Fix Types] Complete
   
   Errors fixed: {count}
   
   Changes:
   - {file}:{line} — {fix applied}
   
   Ignored (with reason):
   - {file}:{line} — {reason}
   
   Verification: {mypy clean} / {tests pass}
   ```
