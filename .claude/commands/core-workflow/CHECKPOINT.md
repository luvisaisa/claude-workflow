---
description: pause and summarize progress, await user confirmation before continuing
allowed-tools: *
argument-hint: none
---

# Checkpoint

Force a progress checkpoint — summarize current state and await confirmation.

## Output Format

```
[Checkpoint] Pausing for confirmation.

## Done So Far
- [Completed item 1]
- [Completed item 2]

## Current State
[What's working, what's in progress, any issues encountered]

## Plan for Next Chunk
1. [Next step 1]
2. [Next step 2]
3. [Next step 3]

## Questions / Concerns
- [Any uncertainties or decisions needed]

Continue with this plan, or redirect?
```

## When to Use

- Automatically trigger when complexity increases
- When requested by user
- After completing a logical chunk of complex work
- Before making architectural decisions
