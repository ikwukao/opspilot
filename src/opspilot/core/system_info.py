"""
Collect system information.
"""

from __future__ import annotations

import platform
import socket

from opspilot.models.system import SystemInfo


def get_system_info() -> SystemInfo:
    """Collect information about the current host."""

    return SystemInfo(
        operating_system=platform.system(),
        release=platform.release(),
        version=platform.version(),
        machine=platform.machine(),
        processor=platform.processor() or "Unknown",
        python_version=platform.python_version(),
        hostname=socket.gethostname(),
    )
