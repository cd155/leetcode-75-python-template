"""
Tests for LeetCode 151: Reverse Words in a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.reverse_words_in_a_string import Solution


class TestReverseWordsInAString:
    """Test cases for LeetCode 151: Reverse Words in a String"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.reverseWords("the sky is blue") == "blue is sky the"

    def test_example_2(self):
        assert self.solution.reverseWords("  hello world  ") == "world hello"

    def test_example_3(self):
        assert self.solution.reverseWords("a good   example") == "example good a"

