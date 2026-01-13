#!/usr/bin/env python3
"""
claude workflow setup tool.

gui application to copy .claude/ folder (commands, skills, hooks, settings)
to new or existing project directories.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def get_source_claude_dir() -> Path:
    """
    locate .claude/ folder relative to this script.

    returns:
        path to .claude/ directory

    raises:
        FileNotFoundError: if .claude/ folder not found
    """
    # when running as pyinstaller bundle, use the extracted temp directory
    if getattr(sys, 'frozen', False):
        # running as bundled executable
        bundle_dir = Path(sys._MEIPASS)
        claude_dir = bundle_dir / ".claude"
    else:
        # running as normal python script
        script_dir = Path(__file__).parent
        claude_dir = script_dir / ".claude"

    if not claude_dir.exists():
        raise FileNotFoundError(
            f".claude/ folder not found at {claude_dir}\n"
            "ensure this script is in the same directory as .claude/"
        )

    return claude_dir


def validate_target_dir(target: Path) -> tuple[bool, str]:
    """
    check if target directory is valid for copying.

    args:
        target: path to target directory

    returns:
        (is_valid, message) - validation result and descriptive message
    """
    # check if parent exists (for new folder creation)
    if not target.exists():
        parent = target.parent
        if not parent.exists():
            return False, f"parent directory does not exist: {parent}"
        if not parent.is_dir():
            return False, f"parent path is not a directory: {parent}"

    # check if target exists and is a directory
    if target.exists() and not target.is_dir():
        return False, f"target path exists but is not a directory: {target}"

    # check write permissions on target or parent
    check_path = target if target.exists() else target.parent
    if not check_path.exists():
        return False, f"cannot access directory: {check_path}"

    # attempt to verify write permissions
    try:
        test_file = check_path / ".write_test"
        test_file.touch()
        test_file.unlink()
    except (OSError, PermissionError) as e:
        return False, f"no write permission: {e}"

    return True, "valid target directory"


def copy_claude_folder(source: Path, target: Path, overwrite: bool = False) -> bool:
    """
    copy .claude/ folder to target directory.

    args:
        source: source .claude/ directory
        target: target project directory
        overwrite: if true, overwrite existing .claude/ folder

    returns:
        true if copy successful, false otherwise

    raises:
        FileExistsError: if target/.claude/ exists and overwrite=False
    """
    target_claude = target / ".claude"

    # check if .claude/ already exists in target
    if target_claude.exists():
        if not overwrite:
            raise FileExistsError(
                f".claude/ already exists in {target}\n"
                "use overwrite=True to replace it"
            )
        # remove existing .claude/ folder
        shutil.rmtree(target_claude)

    # copy .claude/ folder to target
    shutil.copytree(source, target_claude)

    # verify copy succeeded
    if not target_claude.exists():
        return False

    # verify key files exist
    required_files = [
        target_claude / "settings.json",
        target_claude / "commands",
        target_claude / "skills",
        target_claude / "hooks",
    ]

    for required in required_files:
        if not required.exists():
            return False

    return True


class ClaudeSetupWindow(QMainWindow):
    """main window for claude workflow setup tool."""

    def __init__(self) -> None:
        """initialize the setup window."""
        super().__init__()

        self.source_claude_dir: Path | None = None

        # attempt to locate source .claude/ folder
        try:
            self.source_claude_dir = get_source_claude_dir()
        except FileNotFoundError as e:
            QMessageBox.critical(
                self,
                "Error",
                f"failed to locate .claude/ folder:\n\n{e}",
            )
            sys.exit(1)

        self.init_ui()

    def init_ui(self) -> None:
        """initialize user interface components."""
        self.setWindowTitle("claude workflow setup")
        self.setMinimumWidth(500)

        # create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # title label
        title = QLabel("claude workflow setup")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        layout.addWidget(title)

        # description label
        description = QLabel(
            "copy .claude/ folder (commands, skills, hooks, settings)\n"
            "to a new or existing project directory.\n\n"
            "the .claude/ folder contains:\n"
            "• 31 slash commands for development tasks\n"
            "• 3 ai skills (pydev-workflow, pydev-feature, project-audit)\n"
            "• automation hooks for formatting and git setup\n"
            "• project settings"
        )
        description.setWordWrap(True)
        description.setStyleSheet("margin: 10px; color: #666;")
        layout.addWidget(description)

        # source folder info
        source_info = QLabel(f"source: {self.source_claude_dir}")
        source_info.setStyleSheet("margin: 10px; font-family: monospace; color: #333;")
        layout.addWidget(source_info)

        # button: select existing folder
        select_btn = QPushButton("select existing project folder")
        select_btn.clicked.connect(self.select_existing_folder)
        select_btn.setMinimumHeight(40)
        layout.addWidget(select_btn)

        # button: create new folder
        create_btn = QPushButton("create new project folder")
        create_btn.clicked.connect(self.create_new_folder)
        create_btn.setMinimumHeight(40)
        layout.addWidget(create_btn)

        # status label
        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("margin: 10px; padding: 10px;")
        layout.addWidget(self.status_label)

        layout.addStretch()

    def select_existing_folder(self) -> None:
        """handle select existing folder button click."""
        folder = QFileDialog.getExistingDirectory(
            self,
            "select project folder",
            str(Path.home()),
            QFileDialog.Option.ShowDirsOnly,
        )

        if folder:
            self.copy_to_target(Path(folder))

    def create_new_folder(self) -> None:
        """handle create new folder button click."""
        folder = QFileDialog.getExistingDirectory(
            self,
            "select parent directory for new project",
            str(Path.home()),
            QFileDialog.Option.ShowDirsOnly,
        )

        if not folder:
            return

        # prompt for new folder name
        from PySide6.QtWidgets import QInputDialog

        name, ok = QInputDialog.getText(
            self,
            "new project folder",
            "enter project folder name:",
        )

        if ok and name:
            new_folder = Path(folder) / name
            try:
                new_folder.mkdir(parents=True, exist_ok=False)
                self.copy_to_target(new_folder)
            except FileExistsError:
                QMessageBox.warning(
                    self,
                    "folder exists",
                    f"folder already exists: {new_folder}\n\n"
                    "use 'select existing folder' instead.",
                )
            except (OSError, PermissionError) as e:
                QMessageBox.critical(
                    self,
                    "error",
                    f"failed to create folder:\n\n{e}",
                )

    def copy_to_target(self, target: Path) -> None:
        """
        copy .claude/ folder to target directory.

        args:
            target: target project directory
        """
        # validate target directory
        is_valid, message = validate_target_dir(target)
        if not is_valid:
            self.status_label.setText(f"❌ error: {message}")
            self.status_label.setStyleSheet(
                "margin: 10px; padding: 10px; background-color: #ffebee; color: #c62828;"
            )
            QMessageBox.critical(self, "invalid target", message)
            return

        # check if .claude/ already exists
        target_claude = target / ".claude"
        overwrite = False

        if target_claude.exists():
            reply = QMessageBox.question(
                self,
                "folder exists",
                f".claude/ folder already exists in:\n{target}\n\n"
                "do you want to overwrite it?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.No:
                self.status_label.setText("❌ cancelled - .claude/ folder already exists")
                self.status_label.setStyleSheet(
                    "margin: 10px; padding: 10px; background-color: #fff3e0; color: #e65100;"
                )
                return

            overwrite = True

        # copy .claude/ folder
        try:
            print(f"\n[DEBUG] copying from: {self.source_claude_dir}")
            print(f"[DEBUG] copying to: {target}")
            print(f"[DEBUG] target .claude/ will be at: {target_claude}")

            success = copy_claude_folder(
                self.source_claude_dir,  # type: ignore
                target,
                overwrite=overwrite,
            )

            print(f"[DEBUG] copy success: {success}")
            if success:
                print(f"[DEBUG] verifying .claude/ exists at: {target_claude}")
                print(f"[DEBUG] exists: {target_claude.exists()}")
                if target_claude.exists():
                    files = list(target_claude.rglob("*"))
                    print(f"[DEBUG] total items in .claude/: {len(files)}")
                    print(f"[DEBUG] first 10 items:")
                    for f in files[:10]:
                        print(f"[DEBUG]   - {f.relative_to(target_claude)}")

            if success:
                # build detailed success message with file list
                target_claude = target / ".claude"
                file_count = sum(1 for _ in target_claude.rglob("*") if _.is_file())

                self.status_label.setText(
                    f"✅ success!\n\n"
                    f".claude/ folder copied to:\n{target}/.claude\n\n"
                    f"copied {file_count} files\n\n"
                    f"your project now has:\n"
                    f"• 31 slash commands\n"
                    f"• 3 ai skills (pydev-workflow, pydev-feature, project-audit)\n"
                    f"• automation hooks for formatting and git setup\n\n"
                    f"note: .claude is a hidden folder\n"
                    f"press cmd+shift+. in finder to view hidden files"
                )
                self.status_label.setStyleSheet(
                    "margin: 10px; padding: 10px; background-color: #e8f5e9; color: #2e7d32;"
                )

                # show success dialog with option to open folder
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle("success")
                msg.setText(
                    f"claude workflow setup complete!\n\n"
                    f".claude/ folder copied to:\n{target}\n\n"
                    f"copied {file_count} files\n\n"
                    f"includes: 31 commands, 3 skills, automation hooks\n\n"
                    f"note: .claude is a HIDDEN folder (starts with .)\n"
                    f"in finder: press cmd+shift+. to show hidden files"
                )
                msg.setStandardButtons(
                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Open
                )
                msg.button(QMessageBox.StandardButton.Open).setText("open folder")

                reply = msg.exec()

                # open folder in finder if requested
                if reply == QMessageBox.StandardButton.Open:
                    import subprocess
                    subprocess.run(["open", str(target)])
            else:
                raise RuntimeError("copy verification failed")

        except Exception as e:
            self.status_label.setText(f"❌ error during copy:\n{e}")
            self.status_label.setStyleSheet(
                "margin: 10px; padding: 10px; background-color: #ffebee; color: #c62828;"
            )
            QMessageBox.critical(
                self,
                "copy failed",
                f"failed to copy .claude/ folder:\n\n{e}",
            )


def main() -> None:
    """main entry point for claude setup tool."""
    app = QApplication(sys.argv)

    # set application metadata
    app.setApplicationName("claude workflow setup")
    app.setOrganizationName("claude-code")

    # create and show main window
    window = ClaudeSetupWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
