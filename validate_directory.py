#!/usr/bin/env python3
"""
Assimil8or Preset Directory Validator

This script validates all Assimil8or preset files (.yml) in a specified directory.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

from a8_validate.yaml_parser import parse_yaml_file, YAMLSyntaxError, InvalidPresetError, PresetParseError
from a8_validate.schema_validator import validate_preset, SchemaValidationError
from a8_validate.cross_reference_validator import validate_relationships, CrossReferenceError
from a8_validate.file_system_validator import validate_sample_files, FileSystemValidationError


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
        f for f in all_yml_files 
        if (f.name not in ignore_patterns and 
            not f.name.startswith("midi") and 
            not f.name.startswith("._"))
    ]


def validate_preset_file(file_path: Path, sample_dir: Path) -> Tuple[bool, str]:
    """
    Validate a preset file.
    
    Returns:
        Tuple of (success, message)
    """
    try:
        # Parse the YAML file with line number preservation
        preset_data, line_map = parse_yaml_file(str(file_path), return_line_map=True)
        
        # Validate schema
        try:
            validate_preset(preset_data)
        except SchemaValidationError as e:
            # Attempt to extract parameter and preset name from error message
            param_name = None
            preset_key = None
            msg = str(e)
            import re
            param_match = re.search(r'Parameter (\w+)', msg)
            preset_match = re.search(r'in (Preset \d+)', msg)
            if param_match:
                param_name = param_match.group(1)
            if preset_match:
                preset_key = preset_match.group(1)
            # Build path tuple
            path = None
            if preset_key and param_name:
                path = (preset_key, param_name)
            elif param_name:
                path = (param_name,)
            # Get line number from line_map if available
            line_number = None
            if path and path in line_map:
                line_number = line_map[path]
            else:
                # Try to find line number by partial matching keys in line_map
                for key_path in line_map.keys():
                    if path and all(p == k for p, k in zip(path, key_path)):
                        line_number = line_map[key_path]
                        break
            
            if line_number:
                raise SchemaValidationError(f"{e} (line {line_number})") from e
            else:
                raise
        
        # Validate cross-references
        validate_relationships(preset_data)
        
        # Validate sample files
        if sample_dir:
            validate_sample_files(preset_data, str(sample_dir))
        
        return True, "Valid"
    
    except (YAMLSyntaxError, InvalidPresetError, PresetParseError) as e:
        return False, f"YAML parsing error: {e}"
    except SchemaValidationError as e:
        return False, f"Schema validation error: {e}"
    except CrossReferenceError as e:
        return False, f"Cross-reference error: {e}"
    except FileSystemValidationError as e:
        return False, f"Sample file error: {e}"
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
        output_file = open(args.output, 'w')
        def output_print(*args, **kwargs):
            # Handle end and flush separately to avoid issues
            end_char = kwargs.pop('end', '\n')
            flush_flag = kwargs.pop('flush', False)
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
        traceback.print_exc(file=output_file if output_file else sys.stderr)
        return 1
    finally:
        if output_file:
            output_file.close()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
