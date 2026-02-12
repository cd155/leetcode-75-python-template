"""
Tests for LeetCode 724: Find Pivot Index
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from prefix_sum.find_pivot_index import Solution


class TestFindPivotIndex:
    """Test cases for LeetCode 724: Find Pivot Index"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.pivotIndex([1,7,3,6,5,6]) == 3

    def test_example_2(self):
        assert self.solution.pivotIndex([1,2,3]) == -1

    def test_example_3(self):
        assert self.solution.pivotIndex([2,1,-1]) == 0

