"""
Tests for LeetCode 452: Minimum Number of Arrows to Burst Balloons
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from intervals.minimum_number_of_arrows_to_burst_balloons import Solution


class TestMinimumNumberOfArrowsToBurstBalloons:
    """Test cases for LeetCode 452: Minimum Number of Arrows to Burst Balloons"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2

    def test_example_2(self):
        assert self.solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4

    def test_example_3(self):
        assert self.solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2

