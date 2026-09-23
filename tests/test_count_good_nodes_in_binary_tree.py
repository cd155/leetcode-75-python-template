"""
Tests for LeetCode 1448: Count Good Nodes in Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("count_good_nodes_in_binary_tree", src_path / "binary_tree_dfs" / "count_good_nodes_in_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestCountGoodNodesInBinaryTree:
    """Test cases for Count Good Nodes in Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
        assert self.solution.goodNodes(root) == 4

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
        assert self.solution.goodNodes(root) == 3
