"""
Tests for LeetCode 1493: Longest Subarray of 1's After Deleting One Element
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_subarray_of_1s_after_deleting_one_element", src_path / "sliding_window" / "longest_subarray_of_1s_after_deleting_one_element.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLongestSubarrayOf1sAfterDeletingOneElement:
    """Test cases for Longest Subarray of 1's After Deleting One Element problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.longestSubarray([1, 1, 0, 1]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.longestSubarray([1, 1, 1]) == 2
