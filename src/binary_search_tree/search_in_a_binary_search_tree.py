"""
LeetCode 700: Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that
node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a binary search tree.
- 1 <= val <= 10^7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        """
        Find the subtree rooted at the node with the given value.

        Args:
            root: TreeNode - root of the BST
            val: int - value to search for

        Returns:
            TreeNode - subtree rooted at the matching node, or None

        Time Complexity: O(h) where h is height
        Space Complexity: O(1) iterative, O(h) recursive
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = solution.searchBST(root, 2)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    result = solution.searchBST(root, 5)
    print(f"Test 2: {result.val if result else None}")
