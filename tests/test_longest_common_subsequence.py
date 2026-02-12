"""
Tests for LeetCode 1143: Longest Common Subsequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_multidimensional.longest_common_subsequence import Solution


class TestLongestCommonSubsequence:
    """Test cases for LeetCode 1143: Longest Common Subsequence"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.longestCommonSubsequence("abcde", "ace") == 3

    def test_example_2(self):
        assert self.solution.longestCommonSubsequence("abc", "abc") == 3

    def test_example_3(self):
        assert self.solution.longestCommonSubsequence("abc", "def") == 0

