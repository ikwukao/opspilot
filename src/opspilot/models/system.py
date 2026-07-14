"""
Data models for system information.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SystemInfo:
    """Represents information about the host system."""

    operating_system: str
    release: str
    version: str
    machine: str
    processor: str
    python_version: str
    hostname: str
