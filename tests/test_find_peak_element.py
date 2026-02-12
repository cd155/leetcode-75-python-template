"""
Tests for LeetCode 162: Find Peak Element
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_search.find_peak_element import Solution


class TestFindPeakElement:
    """Test cases for LeetCode 162: Find Peak Element"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.findPeakElement([1,2,3,1]) == 2

    def test_example_2(self):
        result = self.solution.findPeakElement([1,2,1,3,5,6,4])
        assert result in [1, 5]

