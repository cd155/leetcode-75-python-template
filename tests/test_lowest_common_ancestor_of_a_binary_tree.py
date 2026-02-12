"""
Tests for LeetCode 236: Lowest Common Ancestor of a Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_tree.lowest_common_ancestor_of_a_binary_tree import Solution
from binary_tree.lowest_common_ancestor_of_a_binary_tree import TreeNode

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



class TestLowestCommonAncestorOfABinaryTree:
    """Test cases for LeetCode 236: Lowest Common Ancestor of a Binary Tree"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        assert self.solution.lowestCommonAncestor(root, p, q).val == 3

    def test_example_2(self):
        root = list_to_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        assert self.solution.lowestCommonAncestor(root, p, q).val == 5

