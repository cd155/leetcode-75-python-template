"""
Tests for LeetCode 1732: Find the Highest Altitude
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from prefix_sum.find_the_highest_altitude import Solution


class TestFindTheHighestAltitude:
    """Test cases for LeetCode 1732: Find the Highest Altitude"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.largestAltitude([-5,1,5,0,-7]) == 1

    def test_example_2(self):
        assert self.solution.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0

