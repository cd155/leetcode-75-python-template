"""
Tests for LeetCode 1768: Merge Strings Alternately
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.merge_strings_alternately import Solution


class TestMergeStringsAlternately:
    """Test cases for merge strings alternately problem"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with equal length strings"""
        assert self.solution.mergeAlternately("abc", "pqr") == "apbqcr"
    
    def test_example_2(self):
        """Test with word2 longer than word1"""
        assert self.solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    
    def test_example_3(self):
        """Test with word1 longer than word2"""
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
