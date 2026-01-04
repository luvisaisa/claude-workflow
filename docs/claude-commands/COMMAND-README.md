# Claude Commands

> Custom slash commands for Claude Code  
> Use with: `/command-name` or reference in conversation

---

## Command Categories

| Category | Purpose |
|----------|---------|
| core-workflow | Workflow control, checkpoints, verification |
| scaffolding | Generate new code structures |
| database | Database migrations and seeding |
| testing | Test generation and execution |
| debug-analysis | Debugging, tracing, code analysis |
| refactoring | Safe code restructuring |
| documentation | Doc generation and sync |
| git-pr | Git workflow and releases |
| quick-fixes | Automated lint/type/import fixes |

---

## All Commands

### core-workflow/

| Command | Description |
|---------|-------------|
| `CHECKPOINT` | Force progress checkpoint — summarize state and await confirmation |
| `COMPACT` | Compress context by summarizing completed work |
| `VERIFY` | Run full verification suite (tests, types, lint) and report |

### scaffolding/

| Command | Description |
|---------|-------------|
| `NEW-ADAPTER` | Create adapter class for external service integration |
| `NEW-COMPONENT` | Create frontend component with props and tests |
| `NEW-ENDPOINT` | Create API endpoint with validation and tests |
| `NEW-MODEL` | Create data model with validation and migrations |
| `NEW-SERVICE` | Create service class with dependency injection |

### database/

| Command | Description |
|---------|-------------|
| `MIGRATION` | Create database migration for schema changes |
| `MIGRATE-CHECK` | Verify migration safety and reversibility |
| `SEED` | Generate seed data for development/testing |

### testing/

| Command | Description |
|---------|-------------|
| `TEST` | Run pytest with coverage for specified target |
| `TEST-GENERATE` | Generate test file for existing code |
| `TEST-EDGE-CASES` | Identify and generate edge case tests |

### debug-analysis/

| Command | Description |
|---------|-------------|
| `DEBUG` | Structured debug workflow for issues |
| `EXPLAIN` | Explain how code works step by step |
| `FIND-USAGES` | Find all usages of function/class/variable |
| `TRACE` | Trace execution path through codebase |

### refactoring/

| Command | Description |
|---------|-------------|
| `EXTRACT` | Extract code into new function/class/module |
| `REFACTOR-PLAN` | Plan refactoring with impact analysis |
| `RENAME-SAFE` | Rename symbol across entire codebase |

### documentation/

| Command | Description |
|---------|-------------|
| `DOCUMENT` | Generate/update documentation for code |
| `API-DOCS` | Generate API documentation from endpoints |
| `ARCHITECTURE-SYNC` | Sync ARCHITECTURE.md with current codebase |

### git-pr/

| Command | Description |
|---------|-------------|
| `COMMIT` | Verify, format, and generate commit message |
| `CHANGELOG` | Generate changelog from recent commits |
| `PR-PREP` | Prepare pull request with description and checklist |

### quick-fixes/

| Command | Description |
|---------|-------------|
| `FIX-IMPORTS` | Auto-fix import issues |
| `FIX-LINT` | Auto-fix linting errors |
| `FIX-TYPES` | Fix type annotation issues |

---

## Usage Examples

```bash
# run verification before committing
/verify

# generate tests for a service
/test-generate src/services/parser_service.py

# debug an issue
/debug "API returns 500 on large uploads" src/api/upload.py

# safe rename across codebase
/rename-safe old_function_name new_function_name

# prepare a commit
/commit
```

---

## Integration with pydev-workflow

These commands complement the pydev-workflow system:

| Workflow Step | Relevant Commands |
|---------------|-------------------|
| 03-data-models | `NEW-MODEL`, `MIGRATION` |
| 05-interfaces | `NEW-ENDPOINT`, `NEW-ADAPTER` |
| 07-implementation | `NEW-SERVICE`, `NEW-COMPONENT` |
| 08-test-strategy | `TEST-GENERATE`, `TEST-EDGE-CASES` |
| 09-test-impl | `TEST`, `VERIFY` |
| 11-documentation | `DOCUMENT`, `API-DOCS`, `ARCHITECTURE-SYNC` |

---

## Adding New Commands

1. Create `.md` file in appropriate category folder
2. Follow existing command format:
   - Title and description
   - Arguments section (if any)
   - Steps section with clear actions
   - Output format specification
3. Update this README with new command
