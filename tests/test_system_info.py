"""
Tests for the system information service.
"""

from __future__ import annotations

from opspilot.core.system_info import get_system_info


def test_get_system_info_returns_system_info() -> None:
    """The system information service should return populated data."""

    info = get_system_info()

    assert info.operating_system
    assert info.release
    assert info.version
    assert info.machine
    assert info.processor is not None
    assert info.python_version
    assert info.hostname

