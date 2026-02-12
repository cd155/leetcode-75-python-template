"""
Tests for LeetCode 933: Number of Recent Calls
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from queue.number_of_recent_calls import Solution


class TestNumberOfRecentCalls:
    """Test cases for LeetCode 933: Number of Recent Calls"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        rc = Solution()
        assert rc.ping(1) == 1
        assert rc.ping(100) == 2
        assert rc.ping(3001) == 3
        assert rc.ping(3002) == 3

