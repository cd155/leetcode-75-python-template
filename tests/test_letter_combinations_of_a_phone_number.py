"""
Tests for LeetCode 17: Letter Combinations of a Phone Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from backtracking.letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber:
    """Test cases for LeetCode 17: Letter Combinations of a Phone Number"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert sorted(self.solution.letterCombinations("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])

    def test_example_2(self):
        assert self.solution.letterCombinations("") == []

    def test_example_3(self):
        assert sorted(self.solution.letterCombinations("2")) == sorted(["a","b","c"])

