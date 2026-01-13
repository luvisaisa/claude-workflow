# claude workflow setup - installation guide

installation instructions for mac, windows, and linux.

---

## quick start

### download

download the appropriate version for your operating system:

- **macos**: `claude-workflow-setup-macos.zip`
- **windows**: `claude-workflow-setup-windows.zip`
- **linux**: `claude-workflow-setup-linux.tar.gz`

### install

**macos:**
1. extract `claude-workflow-setup-macos.zip`
2. drag `Claude Workflow Setup.app` to your applications folder (optional)
3. double-click to run
4. if macos blocks it: right-click → open → confirm

**windows:**
1. extract `claude-workflow-setup-windows.zip`
2. double-click `claude-workflow-setup.exe`
3. if windows smartscreen appears: click "more info" → "run anyway"

**linux:**
1. extract: `tar -xzf claude-workflow-setup-linux.tar.gz`
2. make executable: `chmod +x claude-workflow-setup`
3. run: `./claude-workflow-setup`
4. if qt errors occur, install dependencies (see troubleshooting below)

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

**antivirus blocking the executable**

solution:
- temporarily disable antivirus
- or add `claude-workflow-setup.exe` to whitelist
- this is a false positive - pyinstaller executables are often flagged

### linux

**"error while loading shared libraries: libxcb-xinerama.so.0"**

solution (ubuntu/debian):
```bash
sudo apt install libxcb-xinerama0 libxcb-cursor0
```

solution (fedora):
```bash
sudo dnf install xcb-util-wm xcb-util-cursor
```

solution (arch):
```bash
sudo pacman -S libxcb
```

**"qt.qpa.plugin: could not load the qt platform plugin"**

solution:
```bash
export QT_QPA_PLATFORM=xcb
./claude-workflow-setup
```

**permission denied**

solution:
```bash
chmod +x claude-workflow-setup
./claude-workflow-setup
```

---

## building from source

if you prefer to build the executable yourself:

### prerequisites

- python 3.9 or later
- git (optional)

### macos build

```bash
# clone or download source
git clone <repository-url>
cd scripts

# run build script
chmod +x build-mac.sh
./build-mac.sh

# output: dist/Claude Workflow Setup.app
```

### windows build

```cmd
REM clone or download source
git clone <repository-url>
cd scripts

REM run build script
build-windows.bat

REM output: dist\claude-workflow-setup.exe
```

### linux build

```bash
# clone or download source
git clone <repository-url>
cd scripts

# run build script
chmod +x build-linux.sh
./build-linux.sh

# output: dist/claude-workflow-setup
```

---

## running from source (no build)

if you don't want to create an executable:

```bash
# install dependencies
pip3 install -r requirements.txt

# run directly
python3 claude_setup.py
```

---

## system requirements

### macos
- macos 10.13 (high sierra) or later
- 100 mb disk space

### windows
- windows 7 or later (64-bit)
- 100 mb disk space

### linux
- 64-bit linux distribution
- qt6 libraries (usually pre-installed)
- 100 mb disk space

---

## uninstall

### macos
- delete `Claude Workflow Setup.app` from applications

### windows
- delete `claude-workflow-setup.exe`

### linux
- delete `claude-workflow-setup` executable

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
