# Help

List all available commands with descriptions.

## Output Format

```
[Help] Available Commands

## Core Workflow
  /checkpoint    — Force progress checkpoint, summarize state
  /compact       — Compress context by summarizing completed work
  /verify        — Run full verification suite and report
  /help          — Show this help message

## Scaffolding
  /new-adapter   — Create adapter for external service
  /new-component — Create frontend component with tests
  /new-endpoint  — Create API endpoint with validation
  /new-model     — Create data model with migrations
  /new-service   — Create service with dependency injection

## Database
  /migration     — Create database migration
  /migrate-check — Verify migration safety
  /seed          — Generate seed data

## Testing
  /test          — Run pytest with coverage for target
  /test-generate — Generate test file for code
  /test-edge-cases — Generate edge case tests

## Debug & Analysis
  /debug         — Structured debug workflow
  /explain       — Explain code step by step
  /find-usages   — Find all usages of symbol
  /trace         — Trace execution path

## Refactoring
  /extract       — Extract into function/class/module
  /refactor-plan — Plan refactoring with impact analysis
  /rename-safe   — Rename symbol across codebase

## Documentation
  /document      — Generate/update documentation
  /api-docs      — Generate API documentation
  /architecture-sync — Sync ARCHITECTURE.md with code

## Git & PR
  /commit        — Verify and generate commit message
  /changelog     — Generate changelog from commits
  /pr-prep       — Prepare pull request

## Quick Fixes
  /fix-imports   — Auto-fix import issues
  /fix-lint      — Auto-fix linting errors
  /fix-types     — Fix type annotations

---

Tip: Use `/command-name` or describe what you need.
See: claude-commands/README.md for full documentation.
```

## Usage Examples

Show contextual examples based on current work:

```
Common workflows:

  Before committing:
    /verify → /commit

  Adding a feature:
    /new-service MyService → /test-generate → /verify

  Debugging:
    /debug "description" file.py → /test-edge-cases

  Refactoring:
    /refactor-plan → /rename-safe or /extract → /verify
```
