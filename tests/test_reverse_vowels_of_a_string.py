"""
Tests for LeetCode 345: Reverse Vowels of a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reverse_vowels_of_a_string", src_path / "array_string" / "reverse_vowels_of_a_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReverseVowelsOfAString:
    """Test cases for Reverse Vowels of a String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.reverseVowels("IceCreAm") == "AceCreIm"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.reverseVowels("leetcode") == "leotcede"
