"""
LeetCode 605: Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers
cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        Check whether n new flowers can be planted without adjacent flowers.

        Args:
            flowerbed: List[int] - plots (0 is empty, 1 is planted)
            n: int - number of flowers to plant

        Returns:
            bool - true if all n flowers can be planted

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print(f"Test 2: {result}")
