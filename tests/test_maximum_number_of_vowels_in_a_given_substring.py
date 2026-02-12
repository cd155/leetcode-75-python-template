"""
Tests for LeetCode 1456: Maximum Number of Vowels in a Given Substring
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from sliding_window.maximum_number_of_vowels_in_a_given_substring import Solution


class TestMaximumNumberOfVowelsInAGivenSubstring:
    """Test cases for LeetCode 1456: Maximum Number of Vowels in a Given Substring"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.maxVowels("abciiidef", 3) == 3

    def test_example_2(self):
        assert self.solution.maxVowels("aeiou", 2) == 2

    def test_example_3(self):
        assert self.solution.maxVowels("leetcode", 3) == 2

