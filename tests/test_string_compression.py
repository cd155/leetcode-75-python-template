"""
Tests for LeetCode 443: String Compression
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.string_compression import Solution


class TestStringCompression:
    """Test cases for LeetCode 443: String Compression"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        chars = ["a","a","b","b","c","c","c"]
        assert self.solution.compress(chars) == 6

    def test_example_2(self):
        chars = ["a"]
        assert self.solution.compress(chars) == 1

    def test_example_3(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        assert self.solution.compress(chars) == 4

