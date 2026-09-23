"""
Tests for LeetCode 236: Lowest Common Ancestor of a Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lowest_common_ancestor_of_a_binary_tree", src_path / "binary_tree_dfs" / "lowest_common_ancestor_of_a_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestLowestCommonAncestorOfABinaryTree:
    """Test cases for Lowest Common Ancestor of a Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 3

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.left.right.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 5
