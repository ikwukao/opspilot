"""
Core functionality for collecting basic system information.
"""

from __future__ import annotations

import platform
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemInfo:
    """Represents basic information about the host system."""

    operating_system: str
    release: str
    machine: str
    processor: str
    python_version: str


def get_system_info() -> SystemInfo:
    """Collect basic information about the current system."""

    return SystemInfo(
        operating_system=platform.system(),
        release=platform.release(),
        machine=platform.machine(),
        processor=platform.processor(),
        python_version=platform.python_version(),
    )
