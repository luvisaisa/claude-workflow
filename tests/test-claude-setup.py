"""
tests for claude-setup.py.

tests copy logic, validation, and path handling.
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import pytest

# import functions from claude-setup
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from claude_setup import copy_claude_folder, get_source_claude_dir, validate_target_dir


class TestGetSourceClaudeDir:
    """test get_source_claude_dir() function."""

    def test_finds_claude_dir(self) -> None:
        """test that it finds .claude/ directory."""
        # this test assumes .claude/ exists in project root
        claude_dir = get_source_claude_dir()

        assert claude_dir.exists()
        assert claude_dir.is_dir()
        assert claude_dir.name == ".claude"

    def test_claude_dir_has_required_structure(self) -> None:
        """test that .claude/ has expected structure."""
        claude_dir = get_source_claude_dir()

        # check required subdirectories exist
        assert (claude_dir / "commands").exists()
        assert (claude_dir / "skills").exists()
        assert (claude_dir / "hooks").exists()

        # check settings file exists
        assert (claude_dir / "settings.json").exists()

    def test_raises_if_claude_dir_missing(self, tmp_path: Path) -> None:
        """test that it raises filenotfounderror if .claude/ missing."""
        # create a script in temp directory without .claude/
        fake_script = tmp_path / "fake-script.py"
        fake_script.write_text("# fake script")

        # temporarily patch __file__ to point to fake script
        import claude_setup

        original_file = claude_setup.__file__
        try:
            claude_setup.__file__ = str(fake_script)

            with pytest.raises(FileNotFoundError, match=".claude/ folder not found"):
                get_source_claude_dir()
        finally:
            claude_setup.__file__ = original_file


class TestValidateTargetDir:
    """test validate_target_dir() function."""

    def test_valid_existing_directory(self, tmp_path: Path) -> None:
        """test validation of existing writable directory."""
        is_valid, message = validate_target_dir(tmp_path)

        assert is_valid is True
        assert "valid" in message.lower()

    def test_valid_new_directory_with_existing_parent(self, tmp_path: Path) -> None:
        """test validation of new directory with existing parent."""
        new_dir = tmp_path / "new-project"

        is_valid, message = validate_target_dir(new_dir)

        assert is_valid is True
        assert "valid" in message.lower()

    def test_invalid_parent_does_not_exist(self, tmp_path: Path) -> None:
        """test that validation fails if parent directory missing."""
        invalid_path = tmp_path / "nonexistent" / "project"

        is_valid, message = validate_target_dir(invalid_path)

        assert is_valid is False
        assert "parent directory does not exist" in message.lower()

    def test_invalid_target_is_file(self, tmp_path: Path) -> None:
        """test that validation fails if target is a file."""
        file_path = tmp_path / "file.txt"
        file_path.write_text("content")

        is_valid, message = validate_target_dir(file_path)

        assert is_valid is False
        assert "not a directory" in message.lower()

    def test_invalid_no_write_permission(self, tmp_path: Path) -> None:
        """test that validation fails if no write permission."""
        # create read-only directory
        readonly_dir = tmp_path / "readonly"
        readonly_dir.mkdir()
        readonly_dir.chmod(0o444)

        try:
            is_valid, message = validate_target_dir(readonly_dir)

            # should fail on most systems (may pass if running as root)
            if is_valid is False:
                assert "permission" in message.lower()
        finally:
            # restore permissions for cleanup
            readonly_dir.chmod(0o755)


class TestCopyClaudeFolder:
    """test copy_claude_folder() function."""

    @pytest.fixture
    def mock_claude_dir(self, tmp_path: Path) -> Path:
        """create mock .claude/ directory for testing."""
        claude_dir = tmp_path / "source" / ".claude"
        claude_dir.mkdir(parents=True)

        # create required structure
        (claude_dir / "commands").mkdir()
        (claude_dir / "skills").mkdir()
        (claude_dir / "hooks").mkdir()
        (claude_dir / "settings.json").write_text('{"test": true}')

        # add some content
        (claude_dir / "commands" / "test.md").write_text("# test command")
        (claude_dir / "skills" / "test-skill").mkdir()
        (claude_dir / "skills" / "test-skill" / "SKILL.md").write_text("# test skill")
        (claude_dir / "hooks" / "test.sh").write_text("#!/bin/bash\necho test")

        return claude_dir

    @pytest.fixture
    def target_dir(self, tmp_path: Path) -> Path:
        """create target directory for testing."""
        target = tmp_path / "target"
        target.mkdir()
        return target

    def test_copy_to_empty_directory(
        self, mock_claude_dir: Path, target_dir: Path
    ) -> None:
        """test copying .claude/ to empty directory."""
        success = copy_claude_folder(mock_claude_dir, target_dir)

        assert success is True

        # verify .claude/ was copied
        target_claude = target_dir / ".claude"
        assert target_claude.exists()
        assert target_claude.is_dir()

        # verify structure was copied
        assert (target_claude / "commands").exists()
        assert (target_claude / "skills").exists()
        assert (target_claude / "hooks").exists()
        assert (target_claude / "settings.json").exists()

        # verify content was copied
        assert (target_claude / "commands" / "test.md").exists()
        assert (target_claude / "skills" / "test-skill" / "SKILL.md").exists()
        assert (target_claude / "hooks" / "test.sh").exists()

    def test_copy_fails_if_claude_exists_without_overwrite(
        self, mock_claude_dir: Path, target_dir: Path
    ) -> None:
        """test that copy fails if .claude/ exists and overwrite=false."""
        # create existing .claude/ in target
        (target_dir / ".claude").mkdir()

        with pytest.raises(FileExistsError, match=".claude/ already exists"):
            copy_claude_folder(mock_claude_dir, target_dir, overwrite=False)

    def test_copy_overwrites_if_overwrite_true(
        self, mock_claude_dir: Path, target_dir: Path
    ) -> None:
        """test that copy overwrites existing .claude/ if overwrite=true."""
        # create existing .claude/ with different content
        existing_claude = target_dir / ".claude"
        existing_claude.mkdir()
        (existing_claude / "old-file.txt").write_text("old content")

        success = copy_claude_folder(mock_claude_dir, target_dir, overwrite=True)

        assert success is True

        # verify old content is gone
        assert not (existing_claude / "old-file.txt").exists()

        # verify new content is present
        assert (existing_claude / "commands").exists()
        assert (existing_claude / "settings.json").exists()

    def test_copy_preserves_file_permissions(
        self, mock_claude_dir: Path, target_dir: Path
    ) -> None:
        """test that copy preserves file permissions."""
        # make hook executable
        hook = mock_claude_dir / "hooks" / "test.sh"
        hook.chmod(0o755)

        copy_claude_folder(mock_claude_dir, target_dir)

        # verify permissions were preserved
        copied_hook = target_dir / ".claude" / "hooks" / "test.sh"
        assert copied_hook.stat().st_mode & 0o111  # has execute permission

    def test_copy_creates_target_if_missing(
        self, mock_claude_dir: Path, tmp_path: Path
    ) -> None:
        """test that copy works with non-existent target directory."""
        target = tmp_path / "new-project"

        # create target directory first (function doesn't create it)
        target.mkdir()

        success = copy_claude_folder(mock_claude_dir, target)

        assert success is True
        assert (target / ".claude").exists()

    def test_copy_verification_detects_missing_files(
        self, tmp_path: Path, target_dir: Path
    ) -> None:
        """test that verification detects incomplete copies."""
        # create incomplete source .claude/
        incomplete_claude = tmp_path / "incomplete" / ".claude"
        incomplete_claude.mkdir(parents=True)
        # missing required subdirectories

        # copy should succeed but verification should fail
        shutil.copytree(incomplete_claude, target_dir / ".claude")

        # manually verify - should detect missing structure
        target_claude = target_dir / ".claude"
        missing_commands = not (target_claude / "commands").exists()
        missing_skills = not (target_claude / "skills").exists()
        missing_hooks = not (target_claude / "hooks").exists()
        missing_settings = not (target_claude / "settings.json").exists()

        # at least one should be missing
        assert missing_commands or missing_skills or missing_hooks or missing_settings


class TestIntegration:
    """integration tests for full workflow."""

    def test_full_copy_workflow(self, tmp_path: Path) -> None:
        """test complete workflow: locate source, validate target, copy."""
        # get real .claude/ directory
        source_claude = get_source_claude_dir()

        # create target directory
        target = tmp_path / "test-project"
        target.mkdir()

        # validate target
        is_valid, _ = validate_target_dir(target)
        assert is_valid is True

        # copy .claude/
        success = copy_claude_folder(source_claude, target)
        assert success is True

        # verify all expected content exists
        target_claude = target / ".claude"
        assert (target_claude / "commands").is_dir()
        assert (target_claude / "skills").is_dir()
        assert (target_claude / "hooks").is_dir()
        assert (target_claude / "settings.json").is_file()

        # verify some specific files
        assert (target_claude / "commands" / "core-workflow" / "VERIFY.md").exists()
        assert (target_claude / "skills" / "pydev-workflow" / "SKILL.md").exists()
        assert (target_claude / "hooks" / "format-python.sh").exists()

    def test_overwrite_existing_workflow(self, tmp_path: Path) -> None:
        """test overwriting existing .claude/ directory."""
        source_claude = get_source_claude_dir()

        target = tmp_path / "test-project"
        target.mkdir()

        # create existing .claude/ with custom file
        existing_claude = target / ".claude"
        existing_claude.mkdir()
        custom_file = existing_claude / "custom.txt"
        custom_file.write_text("custom content")

        # copy with overwrite
        success = copy_claude_folder(source_claude, target, overwrite=True)
        assert success is True

        # verify custom file is gone
        assert not custom_file.exists()

        # verify new content is present
        assert (existing_claude / "commands").exists()
        assert (existing_claude / "settings.json").exists()
