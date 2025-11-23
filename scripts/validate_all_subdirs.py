#!/usr/bin/env python3
"""Validate all subdirectories in a parent directory."""

import subprocess
import sys
from pathlib import Path


def validate_all_subdirs(parent_dir: str):
    """Validate all subdirectories in the parent directory."""
    base_dir = Path(parent_dir)
    if not base_dir.exists():
        print(f"Error: Directory not found: {parent_dir}")
        return

    subdirs = [
        d for d in base_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    ]

    total_valid = 0
    total_invalid = 0
    invalid_dirs = []

    print(f"Found {len(subdirs)} subdirectories to validate...\n")

    for subdir in sorted(subdirs):
        result = subprocess.run(
            [sys.executable, "validate_directory.py", str(subdir)],
            capture_output=True,
            text=True,
        )

        # Check for validation results
        output_lines = result.stdout.split("\n")
        has_errors = False
        error_lines = []

        for line in output_lines:
            if "Invalid files:" in line:
                has_errors = True
            elif has_errors and ".yml:" in line:
                error_lines.append(line.strip())
            elif "Validation complete:" in line:
                try:
                    count_str = line.split(":")[1].strip().split()[0]
                    count = int(count_str.split("/")[0])
                    total_valid += count
                    # Check if there were errors
                    if "files valid" in line and count > 0:
                        # Check if total files > valid files
                        total_str = line.split("/")[1].split()[0]
                        total_count = int(total_str)
                        if total_count > count:
                            has_errors = True
                except (ValueError, IndexError):
                    pass

        if has_errors or result.returncode != 0:
            invalid_dirs.append(
                (subdir.name, "\n".join(error_lines) if error_lines else result.stdout)
            )
            total_invalid += 1

    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Subdirectories validated: {len(subdirs)}")
    print(f"  Total valid presets: {total_valid}")
    if invalid_dirs:
        print(f"  Directories with issues: {len(invalid_dirs)}")
        print("\nIssues found:")
        for dir_name, output in invalid_dirs:
            print(f"\n  {dir_name}:")
            # Extract just the error lines
            for line in output.split("\n"):
                if "Invalid files:" in line or ".yml:" in line:
                    print(f"    {line.strip()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 validate_all_subdirs.py <parent_directory>")
        sys.exit(1)

    validate_all_subdirs(sys.argv[1])
