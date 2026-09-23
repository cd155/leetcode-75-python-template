"""
Tests for LeetCode 1768: Merge Strings Alternately
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_strings_alternately", src_path / "array_string" / "merge_strings_alternately.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMergeStringsAlternately:
    """Test cases for Merge Strings Alternately problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.mergeAlternately("abc", "pqr") == "apbqcr"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.mergeAlternately("ab", "pqrs") == "apbqrs"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.mergeAlternately("abcd", "pq") == "apbqcd"

    def test_empty_word1(self):
        """Test with empty first string"""
        assert self.solution.mergeAlternately("", "abc") == "abc"

    def test_empty_word2(self):
        """Test with empty second string"""
        assert self.solution.mergeAlternately("abc", "") == "abc"

    def test_both_empty(self):
        """Test with both strings empty"""
        assert self.solution.mergeAlternately("", "") == ""

    def test_single_character_each(self):
        """Test with single character strings"""
        assert self.solution.mergeAlternately("a", "b") == "ab"
