#!/usr/bin/env python3
"""
Assimil8or Preset Directory Validator

This script validates Assimil8or preset files (.yml and .yaml) in a specified directory.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from a8_validate.cross_reference_validator import CrossReferenceError, validate_relationships
from a8_validate.file_system_validator import (
    FileSystemValidationError,
    InvalidPresetFilenameError,
    validate_preset_filename,
    validate_sample_files,
)
from a8_validate.schema_validator import SchemaValidationError, validate_preset
from a8_validate.yaml_parser import InvalidPresetError, PresetParseError, YAMLSyntaxError, parse_yaml_file


def _line_for_path(
    path: Optional[Tuple[str, ...]],
    line_map: Dict[Tuple[str, ...], int],
) -> Optional[int]:
    """Resolve a validation path to a line number using the YAML line_map. Returns None if not found."""
    if not path or not line_map:
        return None
    if path in line_map:
        return line_map[path]
    # Fallback: prefix match (path may be longer than stored keys)
    for key_path in line_map.keys():
        if len(key_path) <= len(path) and path[: len(key_path)] == key_path:
            return line_map[key_path]
    return None


def _should_ignore_preset_file(name: str) -> bool:
    """Return True if this preset filename should be ignored (system files)."""
    ignore_names = {
        "folderprefs.yml",
        "lastfolder.yml",
        "lastpreset.yml",
        "folderprefs.yaml",
        "lastfolder.yaml",
        "lastpreset.yaml",
    }
    if name in ignore_names:
        return True
    if name.startswith("midi") and (name.endswith(".yml") or name.endswith(".yaml")):
        return True
    if name.startswith("._"):
        return True
    return False


def find_yml_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Find all preset files (.yml and .yaml) in the specified directory, excluding system files.

    Ignores:
    - folderprefs.yml / folderprefs.yaml
    - lastfolder.yml / lastfolder.yaml
    - lastpreset.yml / lastpreset.yaml
    - midi*.yml / midi*.yaml
    - ._* (hidden files)

    Args:
        directory: Directory to search.
        recursive: If True, search subdirectories as well; each preset is validated
            with its containing directory as the sample root.

    Returns:
        Sorted list of paths to preset files.
    """
    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        raise ValueError(f"Directory not found: {directory}")

    if recursive:
        all_files = list(dir_path.rglob("*.yml")) + list(dir_path.rglob("*.yaml"))
    else:
        all_files = list(dir_path.glob("*.yml")) + list(dir_path.glob("*.yaml"))

    filtered = [f for f in all_files if not _should_ignore_preset_file(f.name)]
    return sorted(filtered)


def validate_preset_file(
    file_path: Path,
    sample_dir: Optional[Path],
    run_crossref: bool = True,
    run_samples: bool = True,
) -> Tuple[bool, str]:
    """
    Validate a preset file.

    Args:
        file_path: Path to the preset YAML file.
        sample_dir: Directory used to resolve sample paths; can be None if run_samples is False.
        run_crossref: If True, run cross-reference validation.
        run_samples: If True and sample_dir is set, validate sample files and memory.

    Returns:
        Tuple of (success, message)
    """
    try:
        # Validate filename format first
        validate_preset_filename(file_path.name)

        # Parse the YAML file with line number preservation
        preset_data, line_map = parse_yaml_file(str(file_path), return_line_map=True)

        # Validate schema (mutate=False so we do not modify the parsed data)
        try:
            preset_data = validate_preset(preset_data, mutate=False)
        except SchemaValidationError as e:
            line_number = _line_for_path(getattr(e, "path", None), line_map)
            if line_number is not None:
                raise SchemaValidationError(f"{e} (line {line_number})", path=getattr(e, "path", None)) from e
            raise

        if run_crossref:
            validate_relationships(preset_data)

        if run_samples and sample_dir:
            validate_sample_files(preset_data, str(sample_dir))

        return True, "Valid"

    except InvalidPresetFilenameError as e:
        return False, f"Filename error: {e}"
    except (YAMLSyntaxError, InvalidPresetError, PresetParseError) as e:
        return False, f"YAML parsing error: {e}"
    except SchemaValidationError as e:
        return False, f"Schema validation error: {e}"
    except CrossReferenceError as e:
        line_number = _line_for_path(getattr(e, "path", None), line_map)
        msg = str(e)
        if line_number is not None:
            msg = f"{msg} (line {line_number})"
        return False, f"Cross-reference error: {msg}"
    except FileSystemValidationError as e:
        line_number = _line_for_path(getattr(e, "path", None), line_map)
        msg = str(e)
        if line_number is not None:
            msg = f"{msg} (line {line_number})"
        return False, f"Sample file error: {msg}"
    except Exception as e:
        return False, f"Unexpected error: {e}"


def main():
    parser = argparse.ArgumentParser(description="Validate Assimil8or preset files in a directory")
    parser.add_argument(
        "directory",
        help="Directory containing preset .yml/.yaml files and samples",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--output", "-o", help="Output file for results (optional)")
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Scan subdirectories recursively; each preset is validated with its folder as the sample root",
    )
    parser.add_argument(
        "--samples-dir",
        metavar="PATH",
        default=None,
        help="Resolve sample files from this directory instead of the preset directory",
    )
    parser.add_argument(
        "--schema-only",
        "--no-samples",
        dest="schema_only",
        action="store_true",
        help="Skip sample file existence/format and memory checks (schema and filename only)",
    )
    parser.add_argument(
        "--no-crossref",
        action="store_true",
        help="Skip cross-reference validation (e.g. for quick schema-only checks)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON (results + summary) for CI or batch tooling",
    )
    args = parser.parse_args()

    if args.samples_dir is not None:
        sd = Path(args.samples_dir)
        if not sd.exists() or not sd.is_dir():
            print("Error: --samples-dir must be an existing directory: {}".format(args.samples_dir), file=sys.stderr)
            return 1

    output_file = None
    if args.output:
        # UTF-8 for preset names/paths with non-ASCII (issue #17)
        output_file = open(args.output, "w", encoding="utf-8")

        def output_print(*args, **kwargs):
            # Handle end and flush separately to avoid issues
            end_char = kwargs.pop("end", "\n")
            flush_flag = kwargs.pop("flush", False)
            # Print to file
            print(*args, **kwargs, file=output_file, end=end_char)
            # Print to stdout
            print(*args, **kwargs, end=end_char, flush=flush_flag)
            if flush_flag:
                output_file.flush()

    else:
        output_print = print

    try:
        preset_files = find_yml_files(args.directory, recursive=args.recursive)
        base_dir = Path(args.directory)
        samples_base = Path(args.samples_dir) if args.samples_dir else None

        if not preset_files:
            output_print("No preset files (.yml or .yaml) found in {}".format(args.directory))
            return

        run_crossref = not args.no_crossref
        run_samples = not args.schema_only

        if not args.json:
            output_print("Found {} preset files. Starting validation...".format(len(preset_files)))

        results = []
        for file_path in preset_files:
            if samples_base is not None:
                sample_dir = samples_base
            else:
                sample_dir = file_path.parent if args.recursive else base_dir
            if args.verbose and not args.json:
                display_path = file_path.relative_to(base_dir) if args.recursive else file_path.name
                output_print("Validating {}... ".format(display_path), end="", flush=True)

            success, message = validate_preset_file(
                file_path, sample_dir, run_crossref=run_crossref, run_samples=run_samples
            )
            results.append((file_path, success, message))

            if args.verbose and not args.json:
                status = "✓ VALID" if success else "✗ INVALID"
                output_print(status)
                if not success:
                    output_print("  Error: {}".format(message))

        valid_count = sum(1 for _, success, _ in results if success)
        invalid_count = len(results) - valid_count

        if args.json:
            json_results: List[Dict[str, Any]] = [
                {"file": str(fp), "valid": ok, "message": msg} for fp, ok, msg in results
            ]
            payload = {
                "results": json_results,
                "summary": {"total": len(results), "valid": valid_count, "invalid": invalid_count},
            }
            out = json.dumps(payload, indent=2)
            output_print(out)
        else:
            output_print("\nValidation complete: {}/{} files valid".format(valid_count, len(results)))
            invalid_files = [(path, msg) for path, success, msg in results if not success]
            if invalid_files:
                output_print("\nInvalid files:")
                invalid_files.sort(key=lambda x: x[0].name)
                for path, message in invalid_files:
                    output_print("  {}: {}".format(path.name, message))

    except Exception as e:
        output_print("Error: {}".format(e))
        import traceback

        # Always write traceback to stderr, not output file
        traceback.print_exc(file=sys.stderr)
        return 1
    finally:
        if output_file:
            output_file.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
