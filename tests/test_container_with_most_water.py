"""
Tests for LeetCode 11: Container With Most Water
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from two_pointers.container_with_most_water import Solution


class TestContainerWithMostWater:
    """Test cases for LeetCode 11: Container With Most Water"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49

    def test_example_2(self):
        assert self.solution.maxArea([1,1]) == 1

