"""
LeetCode 334: Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i <
j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def increasingTriplet(self, nums):
        """
        Check whether an increasing triplet subsequence exists.

        Args:
            nums: List[int] - array of integers

        Returns:
            bool - true if an increasing triplet exists

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.increasingTriplet([1, 2, 3, 4, 5])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.increasingTriplet([5, 4, 3, 2, 1])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.increasingTriplet([2, 1, 5, 0, 4, 6])
    print(f"Test 3: {result}")
