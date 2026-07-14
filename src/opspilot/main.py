"""
Application entry point for OpsPilot.
"""

from __future__ import annotations
from opspilot.cli import run


def main() -> int:
    """Start the OpsPilot command-line application."""
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
