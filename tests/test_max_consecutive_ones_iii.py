"""
Tests for LeetCode 1004: Max Consecutive Ones III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from sliding_window.max_consecutive_ones_iii import Solution


class TestMaxConsecutiveOnesIii:
    """Test cases for LeetCode 1004: Max Consecutive Ones III"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6

    def test_example_2(self):
        assert self.solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10

