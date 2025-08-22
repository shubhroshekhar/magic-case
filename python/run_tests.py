#!/usr/bin/env python3
"""
Test runner script for magic-case library.

This script provides easy access to different test categories and options.
"""

import argparse
import subprocess
import sys


def run_command(cmd: list[str]) -> int:
    """Run a command and return the exit code."""
    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode
    except FileNotFoundError:
        print("Error: pytest not found. Please install pytest first.")
        return 1


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(
        description="Run magic-case tests with various options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py                    # Run all tests
  python run_tests.py --fast            # Run only fast tests
  python run_tests.py --unit            # Run only unit tests
  python run_tests.py --integration     # Run only integration tests
  python run_tests.py --coverage        # Run with coverage report
  python run_tests.py --verbose         # Run with verbose output
  python run_tests.py --parallel        # Run tests in parallel
        """,
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Run only fast tests (exclude slow and performance tests)",
    )

    parser.add_argument("--unit", action="store_true", help="Run only unit tests")

    parser.add_argument(
        "--integration", action="store_true", help="Run only integration tests"
    )

    parser.add_argument(
        "--performance", action="store_true", help="Run only performance tests"
    )

    parser.add_argument(
        "--edge-case", action="store_true", help="Run only edge case tests"
    )

    parser.add_argument(
        "--error-handling", action="store_true", help="Run only error handling tests"
    )

    parser.add_argument(
        "--coverage", action="store_true", help="Run tests with coverage report"
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Run tests with verbose output"
    )

    parser.add_argument(
        "--parallel",
        "-n",
        type=int,
        metavar="NUM",
        help="Run tests in parallel with specified number of workers",
    )

    parser.add_argument(
        "--stop", "-x", action="store_true", help="Stop after first failure"
    )

    parser.add_argument(
        "--tb",
        choices=["short", "long", "line", "no"],
        default="short",
        help="Traceback style (default: short)",
    )

    parser.add_argument(
        "--durations",
        type=int,
        default=10,
        help="Show N slowest test durations (default: 10)",
    )

    parser.add_argument(
        "--k", type=str, help="Only run tests matching the substring expression"
    )

    parser.add_argument(
        "--m", type=str, help="Only run tests matching given mark expression"
    )

    args = parser.parse_args()

    # Build pytest command
    cmd = ["python", "-m", "pytest"]

    # Add test path
    cmd.append("tests/")

    # Add options based on arguments
    if args.fast:
        cmd.extend(["-m", "not slow and not performance"])
    elif args.unit:
        cmd.extend(["-m", "not integration and not performance"])
    elif args.integration:
        cmd.extend(["-m", "integration"])
    elif args.performance:
        cmd.extend(["-m", "performance"])
    elif args.edge_case:
        cmd.extend(["-m", "edge_case"])
    elif args.error_handling:
        cmd.extend(["-m", "error_handling"])

    if args.coverage:
        cmd.extend(["--cov=magic_case", "--cov-report=html", "--cov-report=term"])

    if args.verbose:
        cmd.append("-v")

    if args.parallel:
        cmd.extend(["-n", str(args.parallel)])

    if args.stop:
        cmd.append("-x")

    cmd.extend(["--tb", args.tb])
    cmd.extend(["--durations", str(args.durations)])

    if args.k:
        cmd.extend(["-k", args.k])

    if args.m:
        cmd.extend(["-m", args.m])

    # Print the command being run
    print(f"Running: {' '.join(cmd)}")
    print("-" * 80)

    # Run the tests
    exit_code = run_command(cmd)

    if exit_code == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit code {exit_code}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
