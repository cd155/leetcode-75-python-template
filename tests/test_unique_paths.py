"""
Tests for LeetCode 62: Unique Paths
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_multidimensional.unique_paths import Solution


class TestUniquePaths:
    """Test cases for LeetCode 62: Unique Paths"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.uniquePaths(3, 7) == 28

    def test_example_2(self):
        assert self.solution.uniquePaths(3, 2) == 3

