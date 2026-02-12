"""
Tests for LeetCode 2462: Total Cost to Hire K Workers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.total_cost_to_hire_k_workers import Solution


class TestTotalCostToHireKWorkers:
    """Test cases for LeetCode 2462: Total Cost to Hire K Workers"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.totalCost([17,12,10,2,7,2,11,20,8], 3, 4) == 11

    def test_example_2(self):
        assert self.solution.totalCost([1,2,4,1], 3, 3) == 4

