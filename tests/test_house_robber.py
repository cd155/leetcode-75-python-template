"""
Tests for LeetCode 198: House Robber
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_1d.house_robber import Solution


class TestHouseRobber:
    """Test cases for LeetCode 198: House Robber"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.rob([1,2,3,1]) == 4

    def test_example_2(self):
        assert self.solution.rob([2,7,9,3,1]) == 12

