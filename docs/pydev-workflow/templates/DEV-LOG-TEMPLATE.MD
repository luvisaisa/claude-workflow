# Development Log Template

> Copy this template when initializing a new project's DEV_LOG.md

---

```markdown
# Development Log

> Project: [Project Name]  
> Started: [YYYY-MM-DD]  
> Workflow: pydev-workflow

---

## Table of Contents

| Date | Entry | Link |
|------|-------|------|
| [YYYY-MM-DD] | [Entry title] | [#entry-id](#entry-id) |

---

## Entries

### [YYYY-MM-DD] [Entry Title] {#entry-id}

**Summary**: [One paragraph describing what was accomplished]

**Changes**:

| Component | Change |
|-----------|--------|
| [component name] | [what changed] |

**Files Added/Modified**:

| File | Action | Purpose |
|------|--------|---------|
| [path/to/file] | CREATE/MODIFY/DELETE | [why] |

**Decisions Made**:

| Decision | Rationale |
|----------|-----------|
| [what was decided] | [why] |

**Diagrams** (if applicable):

```mermaid
flowchart LR
    [relevant diagram]
```

**Test Results** (if applicable):

| Metric | Value |
|--------|-------|
| Tests passed | [X] |
| Tests failed | [Y] |
| Coverage | [Z]% |

**Next Steps**:
- [What comes next]
- [Follow-up tasks]

**Refs**:
- [Link to relevant doc section]
- [Related commit hash]

---
```

---

## Entry Types

Use these templates for different entry types:

### Project Initialization
```markdown
### [YYYY-MM-DD] Project Initialized {#init}

**Summary**: Established project foundation for [Project Name]

**Documents Created**:

| Document | Purpose |
|----------|---------|
| PROJECT_FOUNDATION.md | Project definition and scope |
| CLAUDE.md | Best practices and agent context |
| DEV_LOG.md | Development timeline |

**Decisions Made**:

| Decision | Rationale |
|----------|-----------|
| [Tech stack] | [Why chosen] |
| [Architecture approach] | [Why chosen] |

**Next Steps**:
- Proceed to system architecture design (02-system-architecture)

---
```

### Architecture Update
```markdown
### [YYYY-MM-DD] [Component/System] Architecture Defined {#arch-component}

**Summary**: Designed [component/system] architecture

**Components Defined**:

| Component | Responsibility |
|-----------|----------------|
| [name] | [what it does] |

**Architecture Diagram**:

```mermaid
flowchart TD
    [diagram]
```

**Decisions Made**:

| Decision | Rationale |
|----------|-----------|
| [pattern choice] | [why] |

**Next Steps**:
- [Next architecture task or implementation]

---
```

### Feature Implementation
```markdown
### [YYYY-MM-DD] [Feature Name] Implemented {#feat-name}

**Summary**: Implemented [feature description]

**Changes**:

| Component | Change |
|-----------|--------|
| [component] | [what changed] |

**Files Added/Modified**:

| File | Action | Purpose |
|------|--------|---------|
| [path] | CREATE | [why] |
| [path] | MODIFY | [why] |

**Test Coverage**:

| Metric | Value |
|--------|-------|
| Tests added | [X] |
| Coverage | [Y]% |

**Commits**:
- `[hash]` feat: [message]
- `[hash]` test: [message]

**Next Steps**:
- [Follow-up tasks]

---
```

### Bug Fix
```markdown
### [YYYY-MM-DD] Fixed: [Bug Description] {#fix-name}

**Summary**: Fixed [bug description]

**Root Cause**: [What caused the bug]

**Solution**: [How it was fixed]

**Files Modified**:

| File | Change |
|------|--------|
| [path] | [what was fixed] |

**Tests Added**:

| Test | Purpose |
|------|---------|
| [test name] | [prevents regression] |

**Commits**:
- `[hash]` fix: [message]

---
```

### Refactoring
```markdown
### [YYYY-MM-DD] Refactored: [Component/Area] {#refactor-name}

**Summary**: Refactored [what] for [why]

**Before/After**:

| Aspect | Before | After |
|--------|--------|-------|
| [metric] | [old] | [new] |

**Changes**:

| File | Change |
|------|--------|
| [path] | [what changed] |

**Rationale**: [Why this refactoring was needed]

**Tests**: All existing tests pass

**Commits**:
- `[hash]` refactor: [message]

---
```

### Documentation Update
```markdown
### [YYYY-MM-DD] Documentation: [What was documented] {#docs-name}

**Summary**: Updated documentation for [what]

**Documents Updated**:

| Document | Section | Change |
|----------|---------|--------|
| [doc name] | [section] | [what was added/changed] |

**Diagrams Added**:

```mermaid
[new diagram]
```

**Commits**:
- `[hash]` docs: [message]

---
```

---

## Best Practices

1. **Add entry for every meaningful change** — not just code, also architecture decisions, documentation updates, bug fixes

2. **Keep table of contents current** — add link for every new entry

3. **Use consistent entry IDs** — format: `#type-name` (e.g., `#feat-auth`, `#fix-login`, `#docs-api`)

4. **Include mermaid diagrams** for architecture changes

5. **Reference commits** when applicable

6. **Timestamp everything** — use YYYY-MM-DD format

7. **Link to related docs** — reference ARCHITECTURE.md sections, IMPLEMENTATION_PLAN.md items

8. **Be concise but complete** — someone should be able to understand the project history from the dev log alone
