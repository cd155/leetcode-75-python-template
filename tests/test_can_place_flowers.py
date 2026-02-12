"""
Tests for LeetCode 605: Can Place Flowers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.can_place_flowers import Solution


class TestCanPlaceFlowers:
    """Test cases for LeetCode 605: Can Place Flowers"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.canPlaceFlowers([1,0,0,0,1], 1) == True

    def test_example_2(self):
        assert self.solution.canPlaceFlowers([1,0,0,0,1], 2) == False

