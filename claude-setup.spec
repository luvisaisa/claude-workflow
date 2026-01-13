# -*- mode: python ; coding: utf-8 -*-
"""
pyinstaller spec file for claude workflow setup tool.

builds standalone executable for mac, windows, linux.
"""

import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# determine icon path based on platform
if sys.platform == 'darwin':
    # macos
    icon_path = 'assets/icons/DEV-WF-ICON.icns'
elif sys.platform == 'win32':
    # windows (not built)
    icon_path = None
else:
    # linux (not built)
    icon_path = None

# verify icon exists
if icon_path and not Path(icon_path).exists():
    print(f"warning: icon file not found: {icon_path}")
    print("run: python3 scripts/convert-icon.py")
    icon_path = None

# collect pyside6 data files
pyside6_datas = collect_data_files('PySide6')

a = Analysis(
    ['claude_setup.py'],
    pathex=[],
    binaries=[],
    datas=pyside6_datas,
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='claude-workflow-setup',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # no console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,  # platform-specific icon
)

# macos app bundle
app = BUNDLE(
    exe,
    name='Claude Workflow Setup.app',
    icon=icon_path if sys.platform == 'darwin' else None,
    bundle_identifier='com.claude-code.workflow-setup',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSMinimumSystemVersion': '10.13.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
    },
)
