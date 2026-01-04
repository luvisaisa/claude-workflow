---
description: create session handoff summary with files changed, decisions, and next steps
allowed-tools: *
argument-hint: none
---

# Compact

Trigger session compact summary for handoff.

## Output Format

```
[Compact] Ready for session handoff.

## Summary
[2-3 sentences: what was accomplished this session]

## Files Changed
- path/to/file.py — what changed
- path/to/other.ts — what changed

## Decisions Made
- [Decision]: [rationale]

## Current State
[What works, what's pending, any failing tests or known issues]

## Next Steps
- [ ] Immediate next task
- [ ] Follow-up items

## Context for Next Session
[Gotchas, in-progress thinking, unresolved questions, things that almost worked but didn't]
```

## Instructions

- Be thorough but concise
- Include any non-obvious context the next session needs
- List specific files, not general areas
- If tests are failing, note which ones and likely causes
- If architecture decisions were made, explain the reasoning
