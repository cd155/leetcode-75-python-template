"""
Tests for LeetCode 151: Reverse Words in a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reverse_words_in_a_string", src_path / "array_string" / "reverse_words_in_a_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReverseWordsInAString:
    """Test cases for Reverse Words in a String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.reverseWords("the sky is blue") == "blue is sky the"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.reverseWords("  hello world  ") == "world hello"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.reverseWords("a good   example") == "example good a"
