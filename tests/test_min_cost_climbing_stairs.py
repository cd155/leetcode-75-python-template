"""
Tests for LeetCode 746: Min Cost Climbing Stairs
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_1d.min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs:
    """Test cases for LeetCode 746: Min Cost Climbing Stairs"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.minCostClimbingStairs([10,15,20]) == 15

    def test_example_2(self):
        assert self.solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6

