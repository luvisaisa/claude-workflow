---
description: analyze refactoring scope, create execution plan
allowed-tools: Read, Grep, Glob
argument-hint: required: refactoring_goal
---

# Refactor Plan

Analyze and plan refactor without implementing.

## Arguments

- $TARGET — what to refactor (file, module, function)
- $GOAL — what improvement to achieve

## Steps

1. Read and understand current implementation

2. Map dependencies:
   - What uses this code
   - What this code uses
   - Test coverage

3. Analyze:
   - Current issues
   - Desired end state
   - Risk areas

4. Create plan:
   ```
   [Refactor Plan] {target}
   
   ## Current State
   {description of current implementation}
   
   ## Issues
   - {issue 1}
   - {issue 2}
   
   ## Proposed Changes
   1. {change 1}
      - Files affected: {files}
      - Risk: {low/medium/high}
   
   2. {change 2}
      - Files affected: {files}
      - Risk: {low/medium/high}
   
   ## Dependencies
   - {count} files import this
   - {count} tests cover this
   
   ## Suggested Order
   1. {first step}
   2. {second step}
   ...
   
   ## Estimated Scope
   - Files to modify: {count}
   - Tests to update: {count}
   - Risk level: {overall risk}
   
   Ready to proceed?
   ```

Do not implement — plan only.
