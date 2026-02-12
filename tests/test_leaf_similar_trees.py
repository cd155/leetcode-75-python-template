"""
Tests for LeetCode 872: Leaf-Similar Trees
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_tree.leaf_similar_trees import Solution
from binary_tree.leaf_similar_trees import TreeNode

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



class TestLeafSimilarTrees:
    """Test cases for LeetCode 872: Leaf-Similar Trees"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root1 = list_to_tree([3,5,1,6,2,9,8,None,None,7,4])
        root2 = list_to_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        assert self.solution.leafSimilar(root1, root2) == True

    def test_example_2(self):
        root1 = list_to_tree([1,2,3])
        root2 = list_to_tree([1,3,2])
        assert self.solution.leafSimilar(root1, root2) == False

