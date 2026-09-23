"""
LeetCode 1004: Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums, k):
        """
        Find the longest run of 1's after flipping at most k 0's.

        Args:
            nums: List[int] - binary array
            k: int - maximum number of 0's to flip

        Returns:
            int - maximum number of consecutive 1's

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    print(f"Test 2: {result}")
