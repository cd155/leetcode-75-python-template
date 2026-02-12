"""
Tests for LeetCode 1318: Minimum Flips to Make a OR b Equal to c
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from bit_manipulation.minimum_flips_to_make_a_or_b_equal_to_c import Solution


class TestMinimumFlipsToMakeAOrBEqualToC:
    """Test cases for LeetCode 1318: Minimum Flips to Make a OR b Equal to c"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.minFlips(2, 6, 5) == 3

    def test_example_2(self):
        assert self.solution.minFlips(4, 2, 7) == 1

    def test_example_3(self):
        assert self.solution.minFlips(1, 2, 3) == 0

