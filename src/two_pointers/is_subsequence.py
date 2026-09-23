"""
LeetCode 392: Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
"""


class Solution:
    def isSubsequence(self, s, t):
        """
        Check whether s is a subsequence of t.

        Args:
            s: str - candidate subsequence
            t: str - source string

        Returns:
            bool - true if s is a subsequence of t

        Time Complexity: O(n) where n is the length of t
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isSubsequence("abc", "ahbgdc")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isSubsequence("axc", "ahbgdc")
    print(f"Test 2: {result}")
