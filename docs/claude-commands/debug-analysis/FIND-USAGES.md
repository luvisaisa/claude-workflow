# Find Usages

Find all usages of a function/class/variable across codebase.

## Arguments

- $SYMBOL — the symbol to find (e.g., "parse_content", "BaseAdapter", "CONFIG")

## Steps

1. Search for usages:
   ```bash
   grep -rn "{symbol}" --include="*.py" --include="*.ts" --include="*.tsx" src/ tests/
   ```

2. Categorize findings:
   - Definition location
   - Direct calls/references
   - Imports
   - Subclasses/implementations
   - Tests

3. Output:
   ```
   [Find Usages] {symbol}
   
   Definition: {file}:{line}
   
   Usages: {count} total
   
   By type:
   - Calls: {count}
     - {file}:{line} — {context}
   - Imports: {count}
     - {file}:{line}
   - Subclasses: {count}
     - {file}:{line} — {class name}
   - Tests: {count}
     - {file}:{line}
   
   Safe to modify: {yes/no with reasoning}
   ```

Do not modify any code.
