"""
Tests for LeetCode 345: Reverse Vowels of a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.reverse_vowels_of_a_string import Solution


class TestReverseVowelsOfAString:
    """Test cases for LeetCode 345: Reverse Vowels of a String"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.reverseVowels("IcesCreAm") == "AcijsCreIm"

    def test_example_2(self):
        assert self.solution.reverseVowels("leetcode") == "leotcede"

