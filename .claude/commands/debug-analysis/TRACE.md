---
description: trace code execution path through multiple files
allowed-tools: Read, Grep, Glob
argument-hint: required: entry_point
---

# Trace

Trace code path from entry point through system.

## Arguments

- $ENTRY_POINT — starting point (e.g., "POST /api/annotations", "parse_document()")

## Steps

1. Identify entry point location in codebase

2. Trace execution path:
   ```
   [Trace] {entry_point}
   
   1. {file}:{line} — {function/method}
      → {what happens here}
   
   2. {file}:{line} — {function/method}
      → {what happens here}
   
   ...continues until exit
   ```

3. Note:
   - Database queries made
   - External service calls
   - Async boundaries
   - Error handling points
   - Data transformations

4. Output:
   ```
   [Trace Complete] {entry_point}
   
   Path: {count} steps
   
   Key operations:
   - DB: {queries}
   - External: {calls}
   - Transforms: {transforms}
   
   Potential issues:
   - {any concerns noted}
   ```

Do not modify any code.
