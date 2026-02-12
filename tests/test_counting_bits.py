"""
Tests for LeetCode 338: Counting Bits
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from bit_manipulation.counting_bits import Solution


class TestCountingBits:
    """Test cases for LeetCode 338: Counting Bits"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.countBits(2) == [0,1,1]

    def test_example_2(self):
        assert self.solution.countBits(5) == [0,1,1,2,1,2]

