# Fix Imports

Sort and clean imports across specified files.

## Arguments

- $TARGET — file, directory, or "all"

## Steps

1. Run ruff import sorting:
   ```bash
   ruff check {target} --select I --fix
   ```

2. Run ruff to remove unused imports:
   ```bash
   ruff check {target} --select F401 --fix
   ```

3. For frontend:
   ```bash
   npm run lint -- --fix --rule 'import/order: error'
   ```

4. Run verification:
   ```bash
   mypy {target}
   pytest --tb=short
   ```

5. Report:
   ```
   [Fix Imports] Complete
   
   Files processed: {count}
   Imports sorted: {count}
   Unused imports removed: {count}
   
   Changes:
   - {file}: {changes}
   
   Verification: {types clean} / {tests pass}
   ```
