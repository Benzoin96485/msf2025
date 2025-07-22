"""
Unit and regression test for the msf2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import msf2025


def test_msf2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "msf2025" in sys.modules
