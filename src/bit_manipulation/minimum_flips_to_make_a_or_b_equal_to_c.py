"""
LeetCode 1318: Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to
make ( a OR b == c ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary
representation.

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0

Constraints:
- 1 <= a <= 10^9
- 1 <= b <= 10^9
- 1 <= c <= 10^9
"""


class Solution:
    def minFlips(self, a, b, c):
        """
        Count the bit flips needed so that a OR b equals c.

        Args:
            a: int - first number
            b: int - second number
            c: int - target number

        Returns:
            int - minimum number of flips

        Time Complexity: O(log max(a, b, c))
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minFlips(2, 6, 5)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minFlips(4, 2, 7)
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.minFlips(1, 2, 3)
    print(f"Test 3: {result}")
