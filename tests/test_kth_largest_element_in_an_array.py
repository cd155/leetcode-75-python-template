"""
Tests for LeetCode 215: Kth Largest Element in an Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.kth_largest_element_in_an_array import Solution


class TestKthLargestElementInAnArray:
    """Test cases for LeetCode 215: Kth Largest Element in an Array"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.findKthLargest([3,2,1,5,6,4], 2) == 5

    def test_example_2(self):
        assert self.solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

