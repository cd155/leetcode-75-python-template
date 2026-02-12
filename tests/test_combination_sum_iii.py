"""
Tests for LeetCode 216: Combination Sum III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from backtracking.combination_sum_iii import Solution


class TestCombinationSumIii:
    """Test cases for LeetCode 216: Combination Sum III"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.combinationSum3(3, 7) == [[1,2,4]]

    def test_example_2(self):
        assert sorted(self.solution.combinationSum3(3, 9)) == sorted([[1,2,6],[1,3,5],[2,3,4]])

    def test_example_3(self):
        assert self.solution.combinationSum3(4, 1) == []

