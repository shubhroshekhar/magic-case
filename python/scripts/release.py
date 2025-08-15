#!/usr/bin/env python3
"""Release management script for magic-case."""

import argparse
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


def get_current_version() -> str:
    """Get current version from pyproject.toml."""
    import tomllib

    project_root = Path(__file__).parent.parent
    pyproject_path = project_root / "pyproject.toml"

    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)

    return data["project"]["version"]


def update_version(version: str) -> None:
    """Update version in pyproject.toml."""

    project_root = Path(__file__).parent.parent
    pyproject_path = project_root / "pyproject.toml"

    # Read current content
    with open(pyproject_path) as f:
        content = f.read()

    # Replace version - target only the project version field
    import re

    content = re.sub(
        r'(\[project\]\s*\n(?:[^\[]*\n)*?version = )"[^"]*"', rf'\1"{version}"', content
    )

    # Write back
    with open(pyproject_path, "w") as f:
        f.write(content)

    print(f"✅ Updated version to {version}")


def main() -> int:
    """Main function."""
    parser = argparse.ArgumentParser(description="Release management for magic-case")
    parser.add_argument(
        "action", choices=["check", "bump", "release"], help="Action to perform"
    )
    parser.add_argument("--version", help="New version (for bump action)")
    parser.add_argument(
        "--type",
        choices=["patch", "minor", "major"],
        help="Version bump type (for bump action)",
    )

    args = parser.parse_args()

    if args.action == "check":
        version = get_current_version()
        print(f"Current version: {version}")
        return 0

    elif args.action == "bump":
        if not args.version and not args.type:
            print("Error: Must specify either --version or --type")
            return 1

        current_version = get_current_version()

        if args.version:
            new_version = args.version
        else:
            # Auto-bump based on type
            parts = current_version.split(".")
            if len(parts) != 3:
                print("Error: Version must be in format X.Y.Z")
                return 1

            major, minor, patch = map(int, parts)

            if args.type == "patch":
                patch += 1
            elif args.type == "minor":
                minor += 1
                patch = 0
            elif args.type == "major":
                major += 1
                minor = 0
                patch = 0

            new_version = f"{major}.{minor}.{patch}"

        print(f"Bumping version from {current_version} to {new_version}")
        update_version(new_version)
        return 0

    elif args.action == "release":
        version = get_current_version()
        print(f"Creating release for version {version}")

        # Run all checks
        checks = [
            (["uv", "run", "ruff", "check", "."], "Linting"),
            (["uv", "run", "ruff", "format", "--check", "."], "Formatting"),
            (["uv", "run", "pytest", "-q"], "Tests"),
        ]

        all_passed = True
        for cmd, description in checks:
            if not run_command(cmd, description):
                all_passed = False

        if not all_passed:
            print("❌ Some checks failed, cannot create release")
            return 1

        # Create tag
        tag_name = f"v{version}"
        print(f"Creating tag: {tag_name}")

        if not run_command(
            ["git", "tag", "-a", tag_name, "-m", f"Release {tag_name}"], "Create tag"
        ):
            return 1

        if not run_command(["git", "push", "origin", tag_name], "Push tag"):
            return 1

        print(f"🎉 Release {tag_name} created successfully!")
        print(
            "GitHub Actions will automatically create a release when the tag is pushed."
        )
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
