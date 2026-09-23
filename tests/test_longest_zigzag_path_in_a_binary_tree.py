"""
Tests for LeetCode 1372: Longest ZigZag Path in a Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_zigzag_path_in_a_binary_tree", src_path / "binary_tree_dfs" / "longest_zigzag_path_in_a_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestLongestZigzagPathInABinaryTree:
    """Test cases for Longest ZigZag Path in a Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
        assert self.solution.longestZigZag(root) == 3

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
        assert self.solution.longestZigZag(root) == 4

    def test_example_3(self):
        """Test case from example 3"""
        root = TreeNode(1)
        assert self.solution.longestZigZag(root) == 0
