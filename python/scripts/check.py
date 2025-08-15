#!/usr/bin/env python3
"""Run all checks for the magic-case project."""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"Running {description}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False


def main() -> int:
    """Run all checks."""
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    checks = [
        (["uv", "run", "ruff", "check", "."], "Linting"),
        (["uv", "run", "ruff", "format", "--check", "."], "Formatting"),
        (["uv", "run", "pytest", "-q"], "Tests"),
    ]

    all_passed = True
    for cmd, description in checks:
        if not run_command(cmd, description):
            all_passed = False

    if all_passed:
        print("\n🎉 All checks passed!")
        return 0
    else:
        print("\n💥 Some checks failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
