"""
Tests for LeetCode 1161: Maximum Level Sum of a Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_tree_bfs.maximum_level_sum_of_a_binary_tree import Solution
from binary_tree_bfs.maximum_level_sum_of_a_binary_tree import TreeNode

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


class TestMaximumLevelSumOfABinaryTree:
    """Test cases for LeetCode 1161: Maximum Level Sum of a Binary Tree"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([1,7,0,7,-8,None,None])
        assert self.solution.maxLevelSum(root) == 2

    def test_example_2(self):
        root = list_to_tree([989,None,10250,98693,-89388,None,None,None,-32127])
        assert self.solution.maxLevelSum(root) == 2
