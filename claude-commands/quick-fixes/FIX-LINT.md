# Fix Lint

Run ruff and fix linting issues.

## Steps

1. Run ruff with auto-fix:
   ```bash
   ruff check . --fix
   ruff format .
   ```

2. Check for remaining issues:
   ```bash
   ruff check .
   ```

3. For remaining issues:
   - Analyze each
   - Fix manually if safe
   - Flag if fix changes logic

4. Run frontend lint:
   ```bash
   npm run lint -- --fix
   ```

5. Run tests:
   ```bash
   pytest --tb=short
   ```

6. Report:
   ```
   [Fix Lint] Complete
   
   Auto-fixed: {count}
   Manually fixed: {count}
   
   Changes:
   - {file}: {fixes applied}
   
   Needs manual attention:
   - {file}:{line} — {issue} — {why it needs human review}
   
   Verification: {lint clean} / {tests pass}
   ```
