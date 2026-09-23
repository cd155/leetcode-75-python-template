"""
Tests for LeetCode 2352: Equal Row and Column Pairs
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("equal_row_and_column_pairs", src_path / "hash_map_set" / "equal_row_and_column_pairs.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestEqualRowAndColumnPairs:
    """Test cases for Equal Row and Column Pairs problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
