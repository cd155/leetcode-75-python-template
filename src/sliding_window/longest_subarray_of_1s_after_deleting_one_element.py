"""
LeetCode 1493: Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return
0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value
of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""


class Solution:
    def longestSubarray(self, nums):
        """
        Find the longest subarray of 1's after deleting exactly one element.

        Args:
            nums: List[int] - binary array

        Returns:
            int - length of the longest subarray of 1's

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestSubarray([1, 1, 0, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.longestSubarray([1, 1, 1])
    print(f"Test 3: {result}")
