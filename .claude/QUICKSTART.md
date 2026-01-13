# CLAUDE QUICKSTART

> fast reference for claude workflow commands and skills

---

## first time setup

1. **configure git credentials** (optional):
   ```bash
   cp .claude/git-config.example .claude/git-config
   # edit .claude/git-config with your email and username
   ```

2. **verify setup**:
   ```bash
   ls .claude/commands  # should show 9 categories
   ls .claude/skills    # should show pydev-workflow, pydev-feature
   ```

---

## most common commands

| command | use case |
|---------|----------|
| `/help` | show all available commands |
| `/verify` | run tests + types + lint before committing |
| `/commit` | create conventional commit with proper message |
| `/test-generate path/to/file.py` | generate test file for module |
| `/debug "description" file.py` | structured debugging workflow |
| `/session-handoff` | create handoff summary for next session |

---

## workflow cheat sheet

### starting a new project
```
1. run pydev-workflow skill: "start pydev-workflow"
2. follow 12-step process from initialization → deployment
3. checkpoint at each step for approval
```

### adding a feature
```
1. run pydev-feature skill: "implement [feature name]"
2. follow 6-step process: analyze → design → implement → test → integrate → cleanup
3. or use individual commands: /new-service, /test-generate, /verify
```

### before committing
```
1. /verify          # run all checks
2. fix any issues
3. /commit          # generate commit message
4. git commit -m "message from /commit"
```

### debugging issues
```
1. /debug "issue description" file.py
2. /trace            # trace execution path
3. /find-usages      # find all usages of symbol
4. /test-edge-cases  # generate edge case tests
```

### refactoring code
```
1. /refactor-plan                    # plan refactoring with impact analysis
2. /rename-safe old_name new_name    # safe rename across codebase
3. /extract                          # extract into function/class/module
4. /verify                           # ensure nothing broke
```

---

## command categories

**core-workflow** - /checkpoint, /session-handoff, /verify, /help
**scaffolding** - /new-adapter, /new-component, /new-endpoint, /new-model, /new-service
**database** - /migration, /migrate-check, /seed
**testing** - /test, /test-generate, /test-edge-cases
**debug-analysis** - /debug, /explain, /find-usages, /trace
**refactoring** - /extract, /refactor-plan, /rename-safe
**documentation** - /document, /api-docs, /architecture-sync
**git-pr** - /commit, /changelog, /pr-prep
**quick-fixes** - /fix-imports, /fix-lint, /fix-types

---

## skills

**pydev-workflow**
- 12-step project development: initialization → deployment
- triggers: "start pydev-workflow", "continue workflow", "step 05"

**pydev-feature**
- 6-step feature implementation: analysis → cleanup
- triggers: "implement [feature]", "add [feature]"

---

## automation hooks

**format-python.sh**
- auto-formats python files after write/edit with ruff
- runs automatically, no action needed

**session-setup.sh**
- auto-configures git user from .claude/git-config
- runs at session start

---

## common workflows

**daily development**
```
1. work on feature
2. /verify regularly
3. /commit when done
4. /session-handoff at end of day
```

**code review prep**
```
1. /verify
2. /test-generate for untested code
3. /document for undocumented code
4. /pr-prep
```

**inheriting a project**
```
1. /explain main_file.py            # understand key components
2. /trace function_name file.py     # trace execution paths
3. /architecture-sync               # update architecture docs
```

---

## troubleshooting

**command not working?**
- check command exists: `/help`
- verify syntax: see `/commands/[category]/[COMMAND].md`

**hooks not running?**
- check `.claude/settings.json` has hooks configured
- verify hook scripts are executable: `chmod +x .claude/hooks/*.sh`

**git not auto-configuring?**
- create `.claude/git-config` from `.claude/git-config.example`
- set `GIT_USER_EMAIL` and `GIT_USER_NAME`

---

## documentation

- full command reference: `.claude/commands/COMMAND-README.md`
- pydev-workflow details: `.claude/skills/pydev-workflow/WORKFLOW-REFERENCE.md`
- pydev-feature details: `.claude/skills/pydev-feature/WORKFLOW-REFERENCE.md`
- operating instructions: `CLAUDE.md` (project root)

---

version 1.0.0
