"""
Tests for LeetCode 1926: Nearest Exit from Entrance in Maze
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("nearest_exit_from_entrance_in_maze", src_path / "graphs_bfs" / "nearest_exit_from_entrance_in_maze.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNearestExitFromEntranceInMaze:
    """Test cases for Nearest Exit from Entrance in Maze problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]) == 2

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.nearestExit([[".", "+"]], [0, 0]) == -1
