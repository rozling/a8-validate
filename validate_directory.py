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
    """Find all .yml files in the specified directory."""
    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        raise ValueError(f"Directory not found: {directory}")
    
    return list(dir_path.glob("*.yml"))


def validate_preset_file(file_path: Path, sample_dir: Path) -> Tuple[bool, str]:
    """
    Validate a preset file.
    
    Returns:
        Tuple of (success, message)
    """
    try:
        # Parse the YAML file
        preset_data = parse_yaml_file(str(file_path))
        
        # Validate schema
        validate_preset(preset_data)
        
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
    args = parser.parse_args()
    
    try:
        yml_files = find_yml_files(args.directory)
        sample_dir = Path(args.directory)
        
        if not yml_files:
            print("No .yml files found in {}".format(args.directory))
            return
        
        print("Found {} preset files. Starting validation...".format(len(yml_files)))
        
        results = []
        for file_path in yml_files:
            if args.verbose:
                print("Validating {}... ".format(file_path.name), end="", flush=True)
            
            success, message = validate_preset_file(file_path, sample_dir)
            results.append((file_path, success, message))
            
            if args.verbose:
                status = "✓ VALID" if success else "✗ INVALID"
                print(status)
        
        # Print summary
        valid_count = sum(1 for _, success, _ in results if success)
        print("\nValidation complete: {}/{}  files valid".format(valid_count, len(results)))
        
        # Print details for invalid files
        invalid_files = [(path, msg) for path, success, msg in results if not success]
        if invalid_files:
            print("\nInvalid files:")
            for path, message in invalid_files:
                print("  {}: {}".format(path.name, message))
    
    except Exception as e:
        print("Error: {}".format(e))
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
