"""
Tests for LeetCode 2215: Find the Difference of Two Arrays
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from hash_map.find_the_difference_of_two_arrays import Solution


class TestFindTheDifferenceOfTwoArrays:
    """Test cases for LeetCode 2215: Find the Difference of Two Arrays"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.findDifference([1,2,3], [2,4,6])
        assert [sorted(result[0]), sorted(result[1])] == [[1,3],[4,6]]

    def test_example_2(self):
        result = self.solution.findDifference([1,2,3,3], [1,1,2,2])
        assert [sorted(result[0]), sorted(result[1])] == [[3],[]]

