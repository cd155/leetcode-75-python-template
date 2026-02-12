"""
Tests for LeetCode 994: Rotting Oranges
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph_bfs.rotting_oranges import Solution


class TestRottingOranges:
    """Test cases for LeetCode 994: Rotting Oranges"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

    def test_example_2(self):
        assert self.solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

    def test_example_3(self):
        assert self.solution.orangesRotting([[0,2]]) == 0

