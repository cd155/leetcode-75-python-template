"""
Tests for LeetCode 450: Delete Node in a BST
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("delete_node_in_a_bst", src_path / "binary_search_tree" / "delete_node_in_a_bst.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestDeleteNodeInABst:
    """Test cases for Delete Node in a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        result = self.solution.deleteNode(root, 3)
        assert result.val == 5
        assert result.left.val in (2, 4)
        assert result.right.val == 6

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        result = self.solution.deleteNode(root, 0)
        assert result.val == 5
        assert result.left.val == 3
        assert result.right.val == 6
