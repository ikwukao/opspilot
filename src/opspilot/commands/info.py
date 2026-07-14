"""
Implementation of the info capability.
"""

from __future__ import annotations

from opspilot.core.system_info import get_system_info
from cpuinfo import get_cpu_info


def run() -> int:
    """Execute the info capability."""

    info = get_system_info()
    cpu_info = get_cpu_info()

    print("OpsPilot System Information")
    print("=" * 50)
    print(f"Hostname            : {info.hostname}")
    print(f"Operating System    : {info.operating_system}")
    print(f"Release             : {info.release}")
    print(f"Kernel Version      : {info.version}")
    print(f"Architecture        : {info.machine}")
    print(f"Processor           : {cpu_info.get('brand_raw','Unknown Processor')}")
    print(f"Pyhon Version       : {info.python_version}")

    return 0
