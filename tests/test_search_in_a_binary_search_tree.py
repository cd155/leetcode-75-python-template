"""
Tests for LeetCode 700: Search in a Binary Search Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_search_tree.search_in_a_binary_search_tree import Solution
from binary_search_tree.search_in_a_binary_search_tree import TreeNode

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



class TestSearchInABinarySearchTree:
    """Test cases for LeetCode 700: Search in a Binary Search Tree"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([4,2,7,1,3])
        result = self.solution.searchBST(root, 2)
        assert result.val == 2

    def test_example_2(self):
        root = list_to_tree([4,2,7,1,3])
        result = self.solution.searchBST(root, 5)
        assert result is None

