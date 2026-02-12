"""
Tests for LeetCode 437: Path Sum III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_tree.path_sum_iii import Solution
from binary_tree.path_sum_iii import TreeNode

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



class TestPathSumIii:
    """Test cases for LeetCode 437: Path Sum III"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = list_to_tree([10,5,-3,3,2,None,11,3,-2,None,1])
        assert self.solution.pathSum(root, 8) == 3

    def test_example_2(self):
        root = list_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
        assert self.solution.pathSum(root, 22) == 3

