"""
Tests for LeetCode 199: Binary Tree Right Side View
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("binary_tree_right_side_view", src_path / "binary_tree_bfs" / "binary_tree_right_side_view.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestBinaryTreeRightSideView:
    """Test cases for Binary Tree Right Side View problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        assert self.solution.rightSideView(root) == [1, 3, 4]

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(1, None, TreeNode(3))
        assert self.solution.rightSideView(root) == [1, 3]

    def test_example_3(self):
        """Test case from example 3"""
        root = None
        assert self.solution.rightSideView(root) == []
