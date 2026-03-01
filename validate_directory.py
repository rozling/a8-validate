#!/usr/bin/env python3
"""
Assimil8or Preset Directory Validator

This script validates all Assimil8or preset files (.yml) in a specified directory.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

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


def find_yml_files(directory: str) -> List[Path]:
    """
    Find all .yml files in the specified directory, excluding system files.

    Ignores:
    - folderprefs.yml
    - lastfolder.yml
    - lastpreset.yml
    - midi*.yml
    - ._* (hidden files)
    """
    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        raise ValueError(f"Directory not found: {directory}")

    # Get all .yml files
    all_yml_files = list(dir_path.glob("*.yml"))

    # Define files to ignore
    ignore_patterns = [
        "folderprefs.yml",
        "lastfolder.yml",
        "lastpreset.yml",
    ]

    # Filter out ignored files
    return [
        f
        for f in all_yml_files
        if (f.name not in ignore_patterns and not f.name.startswith("midi") and not f.name.startswith("._"))
    ]


def validate_preset_file(file_path: Path, sample_dir: Path) -> Tuple[bool, str]:
    """
    Validate a preset file.

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

        # Validate cross-references
        validate_relationships(preset_data)

        # Validate sample files
        if sample_dir:
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
    parser.add_argument("directory", help="Directory containing preset .yml files and samples")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--output", "-o", help="Output file for results (optional)")
    args = parser.parse_args()

    output_file = None
    if args.output:
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
        yml_files = find_yml_files(args.directory)
        sample_dir = Path(args.directory)

        if not yml_files:
            output_print("No .yml files found in {}".format(args.directory))
            return

        output_print("Found {} preset files. Starting validation...".format(len(yml_files)))

        results = []
        for file_path in yml_files:
            if args.verbose:
                output_print("Validating {}... ".format(file_path.name), end="", flush=True)

            success, message = validate_preset_file(file_path, sample_dir)
            results.append((file_path, success, message))

            if args.verbose:
                status = "✓ VALID" if success else "✗ INVALID"
                output_print(status)
                if not success:
                    output_print("  Error: {}".format(message))

        # Print summary
        valid_count = sum(1 for _, success, _ in results if success)
        output_print("\nValidation complete: {}/{}  files valid".format(valid_count, len(results)))

        # Print details for invalid files
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
