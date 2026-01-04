---
description: sync architecture.md with current codebase state
allowed-tools: Read, Grep, Glob, Edit
argument-hint: none
---

# Architecture Sync

Compare implementation against architecture docs, report drift.

## Arguments

- $ARCH_DOC — path to architecture document
- $IMPL_PATH — path to implementation (default: src/)

## Steps

1. Read architecture document and extract:
   - Component definitions
   - Interface contracts
   - Data flow expectations
   - Directory structure
   - Naming conventions

2. Scan implementation:
   - Actual directory structure
   - Actual component organization
   - Actual interfaces
   - Actual data flow

3. Compare and identify drift:
   - Missing components
   - Extra components (not in spec)
   - Interface mismatches
   - Naming inconsistencies
   - Structural deviations

4. Report:
   ```
   [Architecture Sync] {arch_doc} vs {impl_path}
   
   ## Aligned ✅
   - {component}: matches spec
   - {component}: matches spec
   
   ## Drift Detected ⚠️
   - {component}: {expected} vs {actual}
   - {missing}: specified but not implemented
   - {extra}: implemented but not in spec
   
   ## Recommendations
   1. {recommendation}
   2. {recommendation}
   
   Overall alignment: {percentage}%
   ```

Do not modify any code.
