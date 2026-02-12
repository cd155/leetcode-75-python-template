"""
Tests for LeetCode 2352: Equal Row and Column Pairs
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from hash_map.equal_row_and_column_pairs import Solution


class TestEqualRowAndColumnPairs:
    """Test cases for LeetCode 2352: Equal Row and Column Pairs"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1

    def test_example_2(self):
        assert self.solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3

