"""
Tests for LeetCode 1657: Determine if Two Strings Are Close
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from hash_map.determine_if_two_strings_are_close import Solution


class TestDetermineIfTwoStringsAreClose:
    """Test cases for LeetCode 1657: Determine if Two Strings Are Close"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.closeStrings("abc", "bca") == True

    def test_example_2(self):
        assert self.solution.closeStrings("a", "aa") == False

    def test_example_3(self):
        assert self.solution.closeStrings("cabbba", "abbccc") == True

