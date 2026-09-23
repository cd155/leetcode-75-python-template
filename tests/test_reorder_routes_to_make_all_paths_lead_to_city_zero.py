"""
Tests for LeetCode 1466: Reorder Routes to Make All Paths Lead to the City Zero
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reorder_routes_to_make_all_paths_lead_to_city_zero", src_path / "graphs_dfs" / "reorder_routes_to_make_all_paths_lead_to_city_zero.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReorderRoutesToMakeAllPathsLeadToCityZero:
    """Test cases for Reorder Routes to Make All Paths Lead to the City Zero problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.minReorder(3, [[1, 0], [2, 0]]) == 0
