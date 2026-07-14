"""
Command-line interface for OpsPilot.
"""

from __future__ import annotations

import argparse

from opspilot import __version__
from opspilot.commands.info import run as info_run


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="opspilot",
        description="A modern DevOps automation platform for Linux.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="<command>",
    )

    # Placeholder command until additional capabilities are implemented.
    subparsers.add_parser(
        "info",
        help="Display general system information.",
    )

    return parser


def run() -> int:
    """
    Parse command-line arguments and dispatch execution.

    Returns:
        Process exit status.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "info":
        return info_run()

    parser.error(f"Unknown command: {args.command}")
    return 2
