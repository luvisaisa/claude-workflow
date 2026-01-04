# pydev-workflow: Step 07 — Implementation

> **Workflow**: pydev-workflow  
> **Step**: 07-implementation  
> **Previous**: 06-impl-plan  
> **Next**: 08-test-strategy  
> **Output**: Source code, updated `IMPLEMENTATION_PLAN.md`, `DEV_LOG.md` entries

---

## Pre-Flight

1. **Read CLAUDE.md** — project best practices
2. **Read IMPLEMENTATION_PLAN.md** — understand unit sequence
3. **Read ARCHITECTURE.md** — reference designs
4. **Check DEV_LOG.md** — verify step 06 complete

---

## Purpose

Execute the implementation plan by building each unit in sequence. This step triggers pydev-feature workflow for each unit.

---

## 80% Certainty Rule

**Above 80%**: Execute, document decisions  
**Below 80%**: Stop, ask specific questions

---

## Execution

```
[STEP 07] IMPLEMENTATION
```

### Process

For each unit in IMPLEMENTATION_PLAN.md:

1. **Load unit TODO** from implementation plan
2. **Run pydev-feature workflow** (01-task-analysis through 06-cleanup)
3. **Update progress** in IMPLEMENTATION_PLAN.md
4. **Add DEV_LOG entry** for significant units
5. **Commit and push** per pydev-feature rules
6. **Proceed to next unit**

---

### Progress Tracking

Update IMPLEMENTATION_PLAN.md after each unit:

```markdown
## Progress Tracking

| Unit | Status | Started | Completed | Notes |
|------|--------|---------|-----------|-------|
| 1.1 | Complete | 2024-01-01 | 2024-01-01 | |
| 1.2 | In Progress | 2024-01-02 | | Blocked by X |
| 2.1 | Not Started | | | |
```

---

### Unit Execution Format

For each unit, report:

```
========================================
UNIT [X.X]: [Unit Name]
========================================

Status: STARTING
Depends On: [Units] - [All Complete / Blocked by X]
TODO:
* Major Task: [goal]
   * Mid-level Task: [deliverable]
      * Minor task: [action]

----------------------------------------

[Run pydev-feature workflow]

----------------------------------------

Status: COMPLETE
Files Created:
  - [path/to/file.py]
Files Modified:
  - [path/to/other.py]
Tests: [X] passed
Commits:
  - [hash] feat: [message]
  - [hash] test: [message]

========================================
```

---

### Checkpoint Rules

| Checkpoint | When |
|------------|------|
| Phase complete | After all units in a phase finish |
| Blocked | When dependencies aren't met |
| Major decision | When implementation reveals design issue |
| Deviation | When deviating from plan |

---

### Handling Deviations

If implementation reveals issues with the plan:

1. **Stop** current unit
2. **Document** the issue discovered
3. **Assess** impact on other units
4. **Update** IMPLEMENTATION_PLAN.md if minor
5. **Checkpoint** if major change needed

```markdown
### Deviation Report

**Unit**: [X.X]
**Issue**: [What was discovered]
**Impact**: [What's affected]
**Proposed Change**: [How to handle]
**Requires Approval**: [Yes/No]
```

---

### DEV_LOG Entries

Add DEV_LOG entry for:
- Each phase completion
- Each major component completion
- Any significant decisions or deviations

```markdown
### [YYYY-MM-DD] [Phase/Component] Implementation Complete {#impl-phase-x}

**Summary**: Completed [phase/component] implementation

**Units Completed**:

| Unit | Description |
|------|-------------|
| [X.X] | [What was built] |

**Files Created**:

| File | Purpose |
|------|---------|
| [path] | [what it does] |

**Test Coverage**: [X]% for this phase

**Commits**:
- `[hash]` [message]

**Next Steps**:
- Continue with [next phase/unit]

---
```

---

### Git Discipline

| Event | Action |
|-------|--------|
| Mid-level task complete | Commit |
| Major task complete | Commit + Push |
| Unit complete | Commit + Push + Update progress |
| Phase complete | Commit + Push + DEV_LOG entry |

**Commit format**:
```bash
git commit -m "feat: [component] - [what was implemented]"
```

---

### Completion Criteria

Step 07 is complete when:
- [ ] All units in IMPLEMENTATION_PLAN.md marked Complete
- [ ] All acceptance criteria met
- [ ] All tests passing (at unit level)
- [ ] IMPLEMENTATION_PLAN.md progress fully updated
- [ ] DEV_LOG.md has entries for all phases

---

### Output

**Update IMPLEMENTATION_PLAN.md**:
- Progress tracking table fully updated
- All units marked Complete
- Any deviations documented

**Update DEV_LOG.md**:
- Entry for each phase completion
- Final implementation summary

**Update CLAUDE.md**:
- Current step: 08-test-strategy
- Active TODO: cleared or updated

---

## Commit

After all implementation:

```bash
git add .
git commit -m "feat: implementation complete - all units built"
git push origin main
```

---

## Output Summary

| Output | Action |
|--------|--------|
| Source code | All units implemented |
| IMPLEMENTATION_PLAN.md | Progress tracking complete |
| DEV_LOG.md | Phase completion entries |
| CLAUDE.md | Updated status |
| Git | Multiple commits throughout |
