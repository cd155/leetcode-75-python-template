"""
Tests for LeetCode 1431: Kids With the Greatest Number of Candies
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.kids_with_the_greatest_number_of_candies import Solution


class TestKidsWithTheGreatestNumberOfCandies:
    """Test cases for LeetCode 1431: Kids With the Greatest Number of Candies"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]

    def test_example_2(self):
        assert self.solution.kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False]

    def test_example_3(self):
        assert self.solution.kidsWithCandies([12,1,12], 10) == [True,False,True]

