# Rename Safe

Rename symbol across codebase with verification.

## Arguments

- $OLD_NAME — current name
- $NEW_NAME — new name
- $SCOPE — scope of rename (file, module, or "all")

## Steps

1. Find all occurrences:
   ```bash
   grep -rn "{old_name}" --include="*.py" --include="*.ts" --include="*.tsx" .
   ```

2. Categorize:
   - Definition
   - Usages
   - Imports
   - Strings/comments (may need manual review)
   - Tests

3. Perform rename:
   - Update definition
   - Update all usages
   - Update imports
   - Update tests
   - Skip strings/comments (flag for manual review)

4. Run verification:
   ```bash
   pytest
   mypy .
   ruff check .
   npm run lint
   npm run typecheck
   ```

5. Report:
   ```
   [Rename] {old_name} → {new_name}
   
   Updated: {count} occurrences in {count} files
   
   Files modified:
   - {file}: {count} changes
   
   Manual review needed:
   - {file}:{line} — {reason}
   
   Verification: {results}
   ```
