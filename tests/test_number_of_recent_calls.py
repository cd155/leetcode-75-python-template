"""
Tests for LeetCode 933: Number of Recent Calls
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("number_of_recent_calls", src_path / "queue" / "number_of_recent_calls.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
RecentCounter = module.RecentCounter


class TestNumberOfRecentCalls:
    """Test cases for Number of Recent Calls problem"""

    def test_example_1(self):
        """Test case from example 1"""
        recentCounter = RecentCounter()
        assert recentCounter.ping(1) == 1
        assert recentCounter.ping(100) == 2
        assert recentCounter.ping(3001) == 3
        assert recentCounter.ping(3002) == 3
