"""
LeetCode 1431: Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i]
represents the number of candies the ith kid has, and an integer extraCandies, denoting the number
of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all
the extraCandies, they will have the greatest number of candies among all the kids, or false
otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Example 3:
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

Constraints:
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """
        Determine which kids can have the greatest number of candies.

        Args:
            candies: List[int] - candies each kid has
            extraCandies: int - number of extra candies

        Returns:
            List[bool] - whether each kid can have the most candies

        Time Complexity: O(n)
        Space Complexity: O(1) excluding the output
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.kidsWithCandies([4, 2, 1, 1, 2], 1)
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.kidsWithCandies([12, 1, 12], 10)
    print(f"Test 3: {result}")
