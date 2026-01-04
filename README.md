# claude workflow scripts

collection of development workflow automation tools for claude code.

## contents

### .claude/ - workflow automation

complete claude code setup with:
- **31 slash commands** - organized development tasks
- **2 skills** - pydev-workflow (12-step project) and pydev-feature (6-step feature)
- **automation hooks** - auto-formatting, git config
- **project settings** - pre-configured for python projects

### claude_setup.py - setup tool

gui application to copy .claude/ folder to new projects.

**usage:**

```bash
# install dependencies
pip3 install -r requirements.txt

# run setup tool
python3 claude_setup.py
```

**features:**
- select existing project folder or create new one
- validates target directory and permissions
- detects existing .claude/ and prompts for overwrite
- opens folder after successful copy
- cross-platform path handling

**note:** .claude is a hidden folder (starts with .). on mac, press `cmd+shift+.` in finder to show hidden files.

## development

**run tests:**
```bash
pytest tests/ -v
```

**verify code:**
```bash
mypy claude_setup.py --ignore-missing-imports
python3 -m pytest tests/
```

## structure

```
.
├── .claude/                      # workflow automation
│   ├── commands/                 # 31 slash commands
│   ├── skills/                   # pydev-workflow, pydev-feature
│   ├── hooks/                    # automation scripts
│   └── settings.json             # project settings
├── claude_setup.py               # gui setup tool
├── requirements.txt              # python dependencies
├── tests/                        # test suite
│   └── test-claude-setup.py
└── README.md                     # this file
```

## workflows

see `.claude/skills/` for detailed workflow documentation:
- **pydev-workflow** - 12-step project development (init → deployment)
- **pydev-feature** - 6-step feature implementation (analysis → cleanup)

## license

created for use with claude code cli tool.
