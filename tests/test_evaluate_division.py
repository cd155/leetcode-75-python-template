"""
Tests for LeetCode 399: Evaluate Division
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph_dfs.evaluate_division import Solution


class TestEvaluateDivision:
    """Test cases for LeetCode 399: Evaluate Division"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.calcEquation(
            [["a","b"],["b","c"]], [2.0,3.0],
            [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
        assert result == [6.0, 0.5, -1.0, 1.0, -1.0]

