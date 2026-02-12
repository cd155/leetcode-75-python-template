"""
Tests for LeetCode 72: Edit Distance
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_multidimensional.edit_distance import Solution


class TestEditDistance:
    """Test cases for LeetCode 72: Edit Distance"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.minDistance("horse", "ros") == 3

    def test_example_2(self):
        assert self.solution.minDistance("intention", "execution") == 5

