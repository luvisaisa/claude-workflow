# claude workflow scripts

collection of development workflow automation tools for claude code.

## contents

### .claude/ - workflow automation

complete claude code setup with:
- **31 slash commands** - organized development tasks
- **3 skills** - pydev-workflow (12-step project), pydev-feature (6-step feature), project-audit (codebase analysis)
- **automation hooks** - auto-formatting, git config
- **project settings** - pre-configured for python projects

### claude_setup.py - setup tool

gui application to copy .claude/ folder to new projects.

**macos:** download pre-built app from releases (see [INSTALL.md](INSTALL.md))

**windows/linux:** run from source:

```bash
pip3 install -r requirements.txt
python3 claude_setup.py
```

**features:**
- select existing project folder or create new one
- validates target directory and permissions
- detects existing .claude/ and prompts for overwrite
- opens folder after successful copy
- cross-platform path handling

**note:** .claude is a hidden folder (starts with .). on mac, press `cmd+shift+.` in finder to show hidden files.

## building macos app

create standalone app for macos:

```bash
./scripts/build-mac.sh
# output: dist/Claude Workflow Setup.app

# create distributable zip
cd dist && zip -r claude-workflow-setup-macos.zip "Claude Workflow Setup.app"
```

**windows/linux:** no build needed - users run the python script directly.

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
├── .claude/                      # workflow automation (distributed)
│   ├── commands/                 # 31 slash commands
│   ├── skills/                   # pydev-workflow, pydev-feature
│   ├── hooks/                    # automation scripts
│   └── settings.json             # project settings
├── assets/                       # source assets
│   ├── DEV-WF-ICON.png          # source icon
│   └── icons/                    # generated platform icons
├── docs/                         # source documentation
│   ├── claude-commands/          # slash command sources
│   └── pydev-workflow/           # workflow documentation
├── scripts/                      # build and utility scripts
│   ├── build-mac.sh             # macos build script
│   ├── build-windows.bat        # windows build script
│   ├── build-linux.sh           # linux build script
│   └── convert-icon.py          # icon converter
├── tests/                        # test suite
│   └── test-claude-setup.py
├── claude_setup.py               # gui setup tool
├── claude-setup.spec             # pyinstaller spec file
├── requirements.txt              # python dependencies
├── version.txt                   # version number
├── README.md                     # this file
├── INSTALL.md                    # installation guide
└── CLAUDE.md                     # operating instructions
```

## workflows

see `.claude/skills/` for detailed workflow documentation:
- **pydev-workflow** - 12-step project development (init → deployment)
- **pydev-feature** - 6-step feature implementation (analysis → cleanup)
- **project-audit** - comprehensive codebase analysis and health assessment

## license

created for use with claude code cli tool.
