---
description: generate changelog from commit history
allowed-tools: Bash(git:*), Read, Write
argument-hint: optional: version_tag
---

# Changelog

Generate changelog entry from recent commits.

## Arguments

- $SINCE — starting point (tag, commit, or date)
- $VERSION — version number for this release

## Steps

1. Get commits since reference:
   ```bash
   git log {since}..HEAD --oneline
   ```

2. Categorize by type:
   - Features (feat)
   - Bug Fixes (fix)
   - Refactoring (refactor)
   - Performance (perf)
   - Documentation (docs)
   - Other (chore, test)

3. Generate changelog entry:
   ```markdown
   ## [{version}] - {date}
   
   ### Added
   - {feat commits}
   
   ### Fixed
   - {fix commits}
   
   ### Changed
   - {refactor commits}
   
   ### Performance
   - {perf commits}
   ```

4. Output:
   ```
   [Changelog] Generated for {version}
   
   Commits analyzed: {count}
   
   Entry:
   {generated changelog}
   
   Add to CHANGELOG.md? (provide file path if different)
   ```
