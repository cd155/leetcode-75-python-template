"""
LeetCode 283: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Move all zeroes to the end while keeping the order of non-zero elements.

        Args:
            nums: List[int] - array of integers

        Returns:
            None - modifies nums in-place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(f"Test 1: {nums}")

    # Test case 2
    nums = [0]
    solution.moveZeroes(nums)
    print(f"Test 2: {nums}")
