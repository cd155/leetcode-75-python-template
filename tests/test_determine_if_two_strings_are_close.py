"""
Tests for LeetCode 1657: Determine if Two Strings Are Close
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("determine_if_two_strings_are_close", src_path / "hash_map_set" / "determine_if_two_strings_are_close.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestDetermineIfTwoStringsAreClose:
    """Test cases for Determine if Two Strings Are Close problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.closeStrings("abc", "bca") == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.closeStrings("a", "aa") == False

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.closeStrings("cabbba", "abbccc") == True
