"""Tests for preset file discovery and CLI helpers (validate_directory module)."""

import pytest

# validate_directory is a top-level module (py-modules in pyproject.toml)
import validate_directory


class TestShouldIgnorePresetFile:
    """Tests for _should_ignore_preset_file."""

    def test_ignores_system_yml(self):
        assert validate_directory._should_ignore_preset_file("folderprefs.yml") is True
        assert validate_directory._should_ignore_preset_file("lastfolder.yml") is True
        assert validate_directory._should_ignore_preset_file("lastpreset.yml") is True

    def test_ignores_system_yaml(self):
        assert validate_directory._should_ignore_preset_file("folderprefs.yaml") is True
        assert validate_directory._should_ignore_preset_file("lastfolder.yaml") is True
        assert validate_directory._should_ignore_preset_file("lastpreset.yaml") is True

    def test_ignores_midi_files(self):
        assert validate_directory._should_ignore_preset_file("midi1.yml") is True
        assert validate_directory._should_ignore_preset_file("midi2.yaml") is True

    def test_ignores_hidden_files(self):
        assert validate_directory._should_ignore_preset_file("._prst001.yml") is True

    def test_does_not_ignore_valid_presets(self):
        assert validate_directory._should_ignore_preset_file("prst001.yml") is False
        assert validate_directory._should_ignore_preset_file("prst001.yaml") is False


class TestFindYmlFiles:
    """Tests for find_yml_files (discovers .yml and .yaml preset files)."""

    def test_finds_yml_and_yaml(self, tmp_path):
        (tmp_path / "prst001.yml").touch()
        (tmp_path / "prst002.yaml").touch()
        found = validate_directory.find_yml_files(str(tmp_path))
        assert len(found) == 2
        names = {f.name for f in found}
        assert names == {"prst001.yml", "prst002.yaml"}

    def test_excludes_system_files(self, tmp_path):
        (tmp_path / "prst001.yml").touch()
        (tmp_path / "folderprefs.yml").touch()
        (tmp_path / "lastfolder.yaml").touch()
        (tmp_path / "midi1.yml").touch()
        found = validate_directory.find_yml_files(str(tmp_path))
        assert len(found) == 1
        assert found[0].name == "prst001.yml"

    def test_returns_sorted(self, tmp_path):
        (tmp_path / "prst002.yml").touch()
        (tmp_path / "prst001.yaml").touch()
        found = validate_directory.find_yml_files(str(tmp_path))
        assert [f.name for f in found] == ["prst001.yaml", "prst002.yml"]

    def test_recursive_finds_in_subdirs(self, tmp_path):
        (tmp_path / "prst001.yml").touch()
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "prst002.yaml").touch()
        found = validate_directory.find_yml_files(str(tmp_path), recursive=True)
        assert len(found) == 2
        names = {f.name for f in found}
        assert names == {"prst001.yml", "prst002.yaml"}

    def test_non_recursive_does_not_find_subdirs(self, tmp_path):
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "prst001.yml").touch()
        found = validate_directory.find_yml_files(str(tmp_path), recursive=False)
        assert len(found) == 0

    def test_raises_for_nonexistent_directory(self):
        with pytest.raises(ValueError, match="Directory not found"):
            validate_directory.find_yml_files("/nonexistent/path/xyz")


class TestValidatePresetFileOptions:
    """Tests for validate_preset_file with run_crossref/run_samples options (issue #16)."""

    def test_schema_only_passes_without_samples_or_crossref(self, tmp_path):
        """With run_crossref=False and run_samples=False, only schema and filename are validated."""
        preset_yml = tmp_path / "prst001.yml"
        preset_yml.write_text(
            "Preset 1:\n"
            "  Name: Test\n"
            "  Channel 1:\n"
            "    Pitch: 0.00\n"
            "    Zone 1:\n"
            "      Sample: no_such_file.wav\n"
        )
        success, msg = validate_directory.validate_preset_file(
            preset_yml, sample_dir=None, run_crossref=False, run_samples=False
        )
        assert success is True
        assert msg == "Valid"

    def test_json_output_is_valid_and_has_expected_structure(self, tmp_path, capsys):
        """CLI --json emits valid JSON with results and summary (issue #16)."""
        (tmp_path / "prst001.yml").write_text(
            "Preset 1:\n  Name: A\n  Channel 1:\n    Pitch: 0.00\n    Zone 1:\n      Sample: x.wav\n"
        )
        (tmp_path / "prst002.yml").write_text("Preset 1:\n  Name: B\n  Channel 1:\n    Pitch: 0.00\n    Zone 1:\n")
        # prst002 is invalid (Zone 1 missing Sample)
        import sys

        old_argv = sys.argv
        sys.argv = ["a8-validate", str(tmp_path), "--json"]
        try:
            validate_directory.main()
        finally:
            sys.argv = old_argv
        out, err = capsys.readouterr()
        data = __import__("json").loads(out)
        assert "results" in data
        assert "summary" in data
        assert data["summary"]["total"] == 2
        assert len(data["results"]) == 2
        assert data["results"][0]["file"]
        assert "valid" in data["results"][0]
        assert "message" in data["results"][0]
        valid_count = sum(1 for r in data["results"] if r["valid"])
        assert data["summary"]["valid"] == valid_count
        assert data["summary"]["invalid"] == 2 - valid_count
