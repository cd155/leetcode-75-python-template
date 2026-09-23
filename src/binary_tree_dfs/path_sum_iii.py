"""
LeetCode 437: Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum
of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e.,
traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are: 5 -> 3, 5 -> 2 -> 1 and -3 -> 11.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        """
        Count the downward paths whose values sum to targetSum.

        Args:
            root: TreeNode - root of the tree
            targetSum: int - target path sum

        Returns:
            int - number of paths that sum to targetSum

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    result = solution.pathSum(root, 8)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    result = solution.pathSum(root, 22)
    print(f"Test 2: {result}")
