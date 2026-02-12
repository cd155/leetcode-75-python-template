"""
Tests for LeetCode 199: Binary Tree Right Side View
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_tree_bfs.binary_tree_right_side_view import Solution
from binary_tree_bfs.binary_tree_right_side_view import TreeNode

from collections import deque

def list_to_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestBinaryTreeRightSideView:
    """Test cases for LeetCode 199: Binary Tree Right Side View"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([1,2,3,None,5,None,4])
        assert self.solution.rightSideView(root) == [1,3,4]

    def test_example_2(self):
        root = list_to_tree([1,None,3])
        assert self.solution.rightSideView(root) == [1,3]

    def test_example_3(self):
        root = list_to_tree([])
        assert self.solution.rightSideView(root) == []
