"""
LeetCode 216: Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are
true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination
twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation: 1 + 2 + 4 = 7. There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation: 1 + 2 + 6 = 9, 1 + 3 + 5 = 9, 2 + 3 + 4 = 9. There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. Using 4 different numbers in the range [1,9], the
smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
- 2 <= k <= 9
- 1 <= n <= 60
"""


class Solution:
    def combinationSum3(self, k, n):
        """
        Find all combinations of k distinct numbers from 1 to 9 that sum to n.

        Args:
            k: int - number of values in each combination
            n: int - target sum

        Returns:
            List[List[int]] - all valid combinations

        Time Complexity: O(C(9, k) * k)
        Space Complexity: O(k) excluding the output
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.combinationSum3(3, 7)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.combinationSum3(3, 9)
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.combinationSum3(4, 1)
    print(f"Test 3: {result}")
