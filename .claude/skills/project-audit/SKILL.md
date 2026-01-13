---
name: project-audit
description: comprehensive project analysis identifying issues, missing documentation, and improvement opportunities. use when reviewing codebase health, onboarding to existing project, or conducting code quality assessment.
allowed-tools: Read, Glob, Grep, Bash(git:*), Bash(pytest:*), Bash(mypy:*), Bash(ruff:*)
---

# project-audit: Comprehensive Project Review

analyze project structure, code quality, documentation, and identify improvement opportunities.

## when to apply this skill

- user says "audit project", "review codebase", "analyze project health"
- user asks "what's wrong with this project", "how can i improve this"
- onboarding to new/existing project and need overview
- before major refactoring or feature work
- periodic health checks for long-running projects

## audit scope

### 1. project structure
- directory organization and clarity
- file naming conventions
- separation of concerns
- configuration management

### 2. code quality
- test coverage
- type checking status
- linting issues
- code duplication
- complexity metrics

### 3. documentation
- README completeness
- missing CLAUDE.md or project instructions
- API documentation
- architecture documentation
- inline code documentation

### 4. git hygiene
- commit message quality
- branch structure
- .gitignore completeness

### 5. dependencies
- outdated packages
- security vulnerabilities
- unused dependencies

### 6. development workflow
- missing automation (ci/cd, pre-commit hooks)
- test infrastructure
- build/deployment scripts

## audit process

### phase 1: discovery (read-only)

1. **identify project type**
   ```bash
   # check for framework indicators
   ls package.json pyproject.toml requirements.txt setup.py Cargo.toml go.mod
   ```

2. **analyze structure**
   ```bash
   find . -type f -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" | head -50
   tree -L 3 -I 'node_modules|venv|dist|build|__pycache__'
   ```

3. **check documentation**
   - README.md exists and complete?
   - CLAUDE.md or project instructions?
   - ARCHITECTURE.md or design docs?
   - API documentation?

4. **review git status**
   ```bash
   git log --oneline --no-merges -20
   git branch -a
   git status
   ```

### phase 2: quality analysis

5. **run verification tools**
   ```bash
   # python projects
   pytest --collect-only  # check test discovery
   mypy . --ignore-missing-imports
   ruff check .

   # javascript/typescript projects
   npm run lint
   npm run typecheck
   npm test -- --listTests
   ```

6. **analyze test coverage**
   ```bash
   # python
   pytest --cov --cov-report=term-missing

   # javascript
   npm test -- --coverage
   ```

7. **identify code smells**
   - large files (>500 lines)
   - high complexity functions
   - missing error handling
   - hardcoded values
   - commented-out code

### phase 3: dependency audit

8. **check dependencies**
   ```bash
   # python
   pip list --outdated

   # javascript
   npm outdated
   ```

9. **security scan** (if tools available)
   ```bash
   # python
   pip-audit

   # javascript
   npm audit
   ```

### phase 4: synthesis

10. **categorize findings**
    - critical: blocks development, security issues
    - high: significant technical debt, missing core docs
    - medium: code quality, partial test coverage
    - low: style issues, nice-to-haves

11. **prioritize recommendations**
    - quick wins: high impact, low effort
    - foundational: required for future work
    - incremental: gradual improvements

## output format

```markdown
# project audit report

> generated: [date]
> project: [name]
> type: [python/javascript/go/etc]

---

## executive summary

[2-3 sentences: overall health, key strengths, critical issues]

**health score**: [score/10]
- code quality: [score/10]
- documentation: [score/10]
- test coverage: [score/10]
- maintainability: [score/10]

---

## findings by priority

### critical issues

**[issue title]**
- location: [file:line]
- impact: [description]
- recommendation: [action]

### high priority

**[issue title]**
- location: [file:line or area]
- impact: [description]
- recommendation: [action]

### medium priority

[list medium priority items]

### low priority

[list low priority items]

---

## strengths

- [strength 1]
- [strength 2]
- [strength 3]

---

## metrics

**code metrics**
- total files: [count]
- lines of code: [count]
- test files: [count]
- test coverage: [percentage]

**quality metrics**
- type checking: [pass/fail - errors count]
- linting: [pass/fail - warnings count]
- tests passing: [count passed/total]

**documentation**
- README: [yes/no - completeness score]
- CLAUDE.md: [yes/no]
- architecture docs: [yes/no]
- inline docs: [coverage estimate]

---

## recommendations

### immediate actions (do now)

1. [action with specific steps]
2. [action with specific steps]
3. [action with specific steps]

### short-term improvements (this week)

1. [action]
2. [action]
3. [action]

### long-term enhancements (this month+)

1. [action]
2. [action]
3. [action]

---

## next steps

**to address critical issues:**
```bash
# specific commands to run
```

**to improve code quality:**
- use /fix-lint, /fix-types for quick fixes
- use /test-generate for missing tests
- use /document for missing documentation

**to improve structure:**
- use /refactor-plan for major restructuring
- use /extract for code organization
```

---

## autonomy guidelines

**proceed autonomously when:**
- running read-only analysis commands
- collecting metrics and statistics
- identifying obvious issues (linting errors, missing files)

**checkpoint when:**
- findings suggest major architectural issues
- recommendations require significant time investment
- priorities need user input (what matters most?)
- uncertain about project-specific conventions

---

## integration with other workflows

**after audit, use:**
- `/verify` - fix immediate quality issues
- `/test-generate` - improve test coverage
- `/document` - add missing documentation
- `/refactor-plan` - plan structural improvements
- `pydev-workflow` - establish development process

---

## audit frequency

**recommended schedule:**
- new project: immediately after setup
- active development: monthly
- maintenance mode: quarterly
- before major changes: always
- after onboarding: first week

---

version 1.0.0
