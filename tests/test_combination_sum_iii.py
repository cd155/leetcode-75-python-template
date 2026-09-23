"""
Tests for LeetCode 216: Combination Sum III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combination_sum_iii", src_path / "backtracking" / "combination_sum_iii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinationSumIii:
    """Test cases for Combination Sum III problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert sorted(self.solution.combinationSum3(3, 7)) == [[1, 2, 4]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.combinationSum3(3, 9)) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

    def test_example_3(self):
        """Test case from example 3"""
        assert sorted(self.solution.combinationSum3(4, 1)) == []
