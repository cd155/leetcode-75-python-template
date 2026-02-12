"""
Tests for LeetCode 394: Decode String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from stack.decode_string import Solution


class TestDecodeString:
    """Test cases for LeetCode 394: Decode String"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.decodeString("3[a]2[bc]") == "aaabcbc"

    def test_example_2(self):
        assert self.solution.decodeString("3[a2[c]]") == "accaccacc"

    def test_example_3(self):
        assert self.solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"

