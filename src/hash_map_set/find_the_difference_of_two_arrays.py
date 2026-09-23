"""
LeetCode 2215: Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def findDifference(self, nums1, nums2):
        """
        Find the distinct integers that appear in only one of the two arrays.

        Args:
            nums1: List[int] - first array
            nums2: List[int] - second array

        Returns:
            List[List[int]] - [values only in nums1, values only in nums2]

        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findDifference([1, 2, 3], [2, 4, 6])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
    print(f"Test 2: {result}")
