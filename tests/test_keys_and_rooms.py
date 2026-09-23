"""
Tests for LeetCode 841: Keys and Rooms
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("keys_and_rooms", src_path / "graphs_dfs" / "keys_and_rooms.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestKeysAndRooms:
    """Test cases for Keys and Rooms problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canVisitAllRooms([[1], [2], [3], []]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) == False
