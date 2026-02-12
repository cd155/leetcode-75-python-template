"""
Tests for LeetCode 643: Maximum Average Subarray I
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from sliding_window.maximum_average_subarray_i import Solution


class TestMaximumAverageSubarrayI:
    """Test cases for LeetCode 643: Maximum Average Subarray I"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75

    def test_example_2(self):
        assert self.solution.findMaxAverage([5], 1) == 5.0

