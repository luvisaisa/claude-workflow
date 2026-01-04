# Extract

Extract function/class/module from existing code.

## Arguments

- $SOURCE — source file
- $TARGET — what to extract (lines, function name, or description)
- $DESTINATION — where to put it (new file or existing file)

## Steps

1. Read source and identify extraction boundaries

2. Identify:
   - Dependencies of extracted code
   - Usages of extracted code
   - Required imports

3. Create extraction:
   - Move code to destination
   - Add necessary imports
   - Export from destination
   - Update source to import from destination
   - Update all other usages

4. Run verification:
   ```bash
   pytest
   mypy .
   ruff check .
   ```

5. Report:
   ```
   [Extract] Complete
   
   Extracted: {what}
   From: {source}
   To: {destination}
   
   Files modified:
   - {file}: {change}
   
   Usages updated: {count}
   
   Verification: {results}
   ```
