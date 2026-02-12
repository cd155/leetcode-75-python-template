"""
Tests for LeetCode 1071: Greatest Common Divisor of Strings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.greatest_common_divisor_of_strings import Solution


class TestGreatestCommonDivisorOfStrings:
    """Test cases for LeetCode 1071: Greatest Common Divisor of Strings"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.gcdOfStrings("ABCABC", "ABC") == "ABC"

    def test_example_2(self):
        assert self.solution.gcdOfStrings("ABABAB", "ABAB") == "AB"

    def test_example_3(self):
        assert self.solution.gcdOfStrings("LEET", "CODE") == ""

