"""
Tests for LeetCode 547: Number of Provinces
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph_dfs.number_of_provinces import Solution


class TestNumberOfProvinces:
    """Test cases for LeetCode 547: Number of Provinces"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2

    def test_example_2(self):
        assert self.solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

