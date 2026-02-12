"""
Tests for LeetCode 238: Product of Array Except Self
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf:
    """Test cases for LeetCode 238: Product of Array Except Self"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]

    def test_example_2(self):
        assert self.solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

