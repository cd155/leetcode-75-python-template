"""
Tests for LeetCode 450: Delete Node in a BST
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_search_tree.delete_node_in_a_bst import Solution
from binary_search_tree.delete_node_in_a_bst import TreeNode

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

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)



class TestDeleteNodeInABst:
    """Test cases for LeetCode 450: Delete Node in a BST"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([5,3,6,2,4,None,7])
        result = self.solution.deleteNode(root, 3)
        assert result is not None

    def test_example_2(self):
        root = list_to_tree([5,3,6,2,4,None,7])
        result = self.solution.deleteNode(root, 0)
        assert result is not None

