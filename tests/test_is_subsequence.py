"""
Tests for LeetCode 392: Is Subsequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from two_pointers.is_subsequence import Solution


class TestIsSubsequence:
    """Test cases for LeetCode 392: Is Subsequence"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.isSubsequence("abc", "ahbgdc") == True

    def test_example_2(self):
        assert self.solution.isSubsequence("axc", "ahbgdc") == False

