# claude workflow setup - installation guide

installation instructions for mac, windows, and linux.

---

## quick start

### download and install

**macos (pre-built app):**
1. download `claude-workflow-setup-macos.zip` from releases
2. extract the zip file
3. drag `Claude Workflow Setup.app` to your applications folder (optional)
4. double-click to run
5. if macos blocks it: right-click → open → confirm

**windows and linux (run from source):**
1. download or clone the repository
2. install python 3.9+ if not already installed
3. install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
4. run the setup tool:
   ```bash
   python3 claude_setup.py
   ```

---

## what this tool does

copies the `.claude/` folder to your project directories.

the `.claude/` folder contains:
- **31 slash commands** - organized development tasks
- **3 ai skills** - pydev-workflow (12-step project), pydev-feature (6-step feature), project-audit (codebase analysis)
- **automation hooks** - auto-formatting python code, git config
- **project settings** - pre-configured for python projects

---

## usage

1. launch the application
2. choose one of two options:
   - **select existing project folder** - add .claude/ to an existing project
   - **create new project folder** - create a new folder and add .claude/
3. select or create the folder
4. if .claude/ already exists, confirm overwrite
5. click "open folder" to view the copied files

**important:** `.claude` is a hidden folder (starts with a dot)

**to view hidden folders:**
- **macos**: press `cmd + shift + .` in finder
- **windows**: view tab → show → hidden items
- **linux**: press `ctrl + h` in file manager

---

## post-installation setup

### configure git credentials (recommended)

the workflow includes automatic git configuration. to set your credentials:

1. **navigate to the .claude folder** in your project
2. **copy the example config**:
   ```bash
   cd your-project/.claude
   cp git-config.example git-config
   ```
3. **edit git-config** with your information:
   ```bash
   # open in your editor
   nano git-config
   # or
   code git-config
   ```
4. **set your credentials**:
   ```bash
   GIT_USER_EMAIL="your.email@example.com"
   GIT_USER_NAME="your-username"
   ```
5. **save the file**

the `session-setup.sh` hook will automatically configure git in your project using these credentials.

**note**: `git-config` is gitignored by default, so your credentials stay private.

### verify setup

check that everything is working:

```bash
# view the .claude folder contents
ls -la your-project/.claude

# should see:
# - commands/ (31 command files)
# - skills/ (3 skills: pydev-workflow, pydev-feature, project-audit)
# - hooks/ (format-python.sh, session-setup.sh)
# - settings.json
# - git-config.example
# - QUICKSTART.md
```

---

## troubleshooting

### macos

**"claude workflow setup cannot be opened because it is from an unidentified developer"**

solution:
1. right-click the app → select "open"
2. click "open" in the dialog
3. future launches will work normally

or:
1. system preferences → security & privacy
2. click "open anyway" for claude workflow setup

**"the application is damaged"**

solution:
```bash
xattr -cr "/Applications/Claude Workflow Setup.app"
```

### windows

**"windows protected your pc" smartscreen warning**

solution:
1. click "more info"
2. click "run anyway"

**python not found (windows/linux)**

solution:
- install python 3.9+ from https://www.python.org/downloads/
- on windows, check "add python to PATH" during installation
- verify: `python3 --version` or `python --version`

**pip not found (windows/linux)**

solution:
- usually installed with python
- on linux: `sudo apt install python3-pip` (ubuntu/debian)
- verify: `pip3 --version`

**pyside6 installation fails (windows/linux)**

solution:
- ensure you have latest pip: `pip3 install --upgrade pip`
- on linux, you may need: `sudo apt install python3-dev`
- retry: `pip3 install -r requirements.txt`

---

## building macos app from source

if you want to build the macos app yourself:

### prerequisites

- macos 10.13+
- python 3.9+
- git (optional)

### build steps

```bash
# clone or download source
git clone https://github.com/luvisaisa/claude-workflow.git
cd claude-workflow

# run build script
chmod +x scripts/build-mac.sh
./scripts/build-mac.sh

# output: dist/Claude Workflow Setup.app

# create distributable zip
cd dist
zip -r claude-workflow-setup-macos.zip "Claude Workflow Setup.app"
```

---

## system requirements

### macos (pre-built app)
- macos 10.13 (high sierra) or later
- 100 mb disk space

### windows and linux (python script)
- python 3.9 or later
- pip (python package installer)
- 50 mb disk space for dependencies

---

## uninstall

### macos
- delete `Claude Workflow Setup.app` from applications

### windows and linux
- delete the cloned repository folder
- optionally uninstall dependencies: `pip3 uninstall PySide6`

**note:** this does not affect any .claude/ folders you've copied to projects.

---

## support

for issues or questions:
1. check troubleshooting section above
2. verify .claude/ folder exists in source directory
3. try running from source (see "running from source" above)
4. check that you have python 3.9+ installed

---

## what gets copied

when you use this tool, these files are copied to your project:

```
your-project/
└── .claude/
    ├── commands/              # 31 slash commands
    │   ├── core-workflow/
    │   ├── scaffolding/
    │   ├── database/
    │   ├── testing/
    │   ├── debug-analysis/
    │   ├── refactoring/
    │   ├── documentation/
    │   ├── git-pr/
    │   └── quick-fixes/
    ├── skills/                # ai workflow skills
    │   ├── pydev-workflow/    # 12-step project development
    │   ├── pydev-feature/     # 6-step feature implementation
    │   └── project-audit/     # codebase analysis and health assessment
    ├── hooks/                 # automation scripts
    │   ├── format-python.sh   # auto-format python files
    │   └── session-setup.sh   # auto-configure git
    └── settings.json          # project settings
```

---

## license

created for use with claude code cli tool.

no warranty provided. use at your own risk.
