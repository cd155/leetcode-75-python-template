"""
Tests for LeetCode 841: Keys and Rooms
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph_dfs.keys_and_rooms import Solution


class TestKeysAndRooms:
    """Test cases for LeetCode 841: Keys and Rooms"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.canVisitAllRooms([[1],[2],[3],[]]) == True

    def test_example_2(self):
        assert self.solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False

