"""
Tests for LeetCode 1137: N-th Tribonacci Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_1d.nth_tribonacci_number import Solution


class TestNthTribonacciNumber:
    """Test cases for LeetCode 1137: N-th Tribonacci Number"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.tribonacci(4) == 4

    def test_example_2(self):
        assert self.solution.tribonacci(25) == 1389537

    def test_example_3(self):
        assert self.solution.tribonacci(0) == 0

