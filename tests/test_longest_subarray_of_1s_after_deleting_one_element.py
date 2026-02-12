"""
Tests for LeetCode 1493: Longest Subarray of 1s After Deleting One Element
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from sliding_window.longest_subarray_of_1s_after_deleting_one_element import Solution


class TestLongestSubarrayOf1SAfterDeletingOneElement:
    """Test cases for LeetCode 1493: Longest Subarray of 1s After Deleting One Element"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.longestSubarray([1,1,0,1]) == 3

    def test_example_2(self):
        assert self.solution.longestSubarray([0,1,1,1,0,1,1,0,1]) == 5

    def test_example_3(self):
        assert self.solution.longestSubarray([1,1,1]) == 2

