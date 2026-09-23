"""
LeetCode 1372: Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to
  the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: The longest ZigZag path is right -> left -> right.

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: The longest ZigZag path is left -> right -> left -> right.

Example 3:
Input: root = [1]
Output: 0

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root):
        """
        Find the length of the longest ZigZag path.

        Args:
            root: TreeNode - root of the tree

        Returns:
            int - length of the longest ZigZag path

        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
    result = solution.longestZigZag(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
    result = solution.longestZigZag(root)
    print(f"Test 2: {result}")

    # Test case 3
    root = TreeNode(1)
    result = solution.longestZigZag(root)
    print(f"Test 3: {result}")
