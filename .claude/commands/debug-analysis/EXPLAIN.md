---
description: explain code functionality, architecture, and patterns
allowed-tools: Read, Grep, Glob
argument-hint: required: code_path
---

# Explain

Explain how a module/function works without changing anything.

## Arguments

- $TARGET — path to module or function

## Steps

1. Read the target code thoroughly

2. Identify:
   - Purpose and responsibility
   - Inputs and outputs
   - Dependencies
   - Side effects
   - Error conditions

3. Output:
   ```
   [Explain] {target}
   
   ## Purpose
   {what it does and why}
   
   ## Interface
   - Input: {parameters with types}
   - Output: {return value}
   - Side effects: {any side effects}
   
   ## How It Works
   {step-by-step explanation of logic}
   
   ## Dependencies
   - {dependency}: {how it's used}
   
   ## Usage Example
   {code example}
   
   ## Notes
   - {edge cases, gotchas, or important details}
   ```

Do not modify any code.
