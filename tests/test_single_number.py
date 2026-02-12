"""
Tests for LeetCode 136: Single Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from bit_manipulation.single_number import Solution


class TestSingleNumber:
    """Test cases for LeetCode 136: Single Number"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.singleNumber([2,2,1]) == 1

    def test_example_2(self):
        assert self.solution.singleNumber([4,1,2,1,2]) == 4

    def test_example_3(self):
        assert self.solution.singleNumber([1]) == 1

