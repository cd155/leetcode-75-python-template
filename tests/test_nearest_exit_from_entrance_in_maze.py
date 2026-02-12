"""
Tests for LeetCode 1926: Nearest Exit from Entrance in Maze
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph_bfs.nearest_exit_from_entrance_in_maze import Solution


class TestNearestExitFromEntranceInMaze:
    """Test cases for LeetCode 1926: Nearest Exit from Entrance in Maze"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]) == 1

    def test_example_2(self):
        assert self.solution.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]) == 2

    def test_example_3(self):
        assert self.solution.nearestExit([[".","+"]],[0,0]) == -1

