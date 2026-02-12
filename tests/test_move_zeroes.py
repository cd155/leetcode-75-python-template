"""
Tests for LeetCode 283: Move Zeroes
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from two_pointers.move_zeroes import Solution


class TestMoveZeroes:
    """Test cases for LeetCode 283: Move Zeroes"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0,1,0,3,12]
        self.solution.moveZeroes(nums)
        assert nums == [1,3,12,0,0]

    def test_example_2(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        assert nums == [0]

