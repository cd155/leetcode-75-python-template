"""
LeetCode 2390: Removing Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right: the closest character to the 1st star is
't', s becomes "lee*cod*e"; the closest character to the 2nd star is 'e', s becomes "lecod*e"; the
closest character to the 3rd star is 'd', s becomes "lecoe". There are no more stars.

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters and stars *.
- The operation above can be performed on s.
"""


class Solution:
    def removeStars(self, s):
        """
        Remove every star together with the closest non-star character to its left.

        Args:
            s: str - input string containing stars

        Returns:
            str - string after all stars have been removed

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.removeStars("leet**cod*e")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.removeStars("erase*****")
    print(f"Test 2: {result}")
