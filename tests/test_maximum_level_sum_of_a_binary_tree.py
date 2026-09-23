"""
Tests for LeetCode 1161: Maximum Level Sum of a Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_level_sum_of_a_binary_tree", src_path / "binary_tree_bfs" / "maximum_level_sum_of_a_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestMaximumLevelSumOfABinaryTree:
    """Test cases for Maximum Level Sum of a Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
        assert self.solution.maxLevelSum(root) == 2

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
        assert self.solution.maxLevelSum(root) == 2
