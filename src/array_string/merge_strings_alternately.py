"""
LeetCode 1768: Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the
end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1, word2):
        """
        Merge two strings by adding letters in alternating order.

        Args:
            word1: str - first string
            word2: str - second string

        Returns:
            str - merged string

        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.mergeAlternately("abc", "pqr")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.mergeAlternately("ab", "pqrs")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.mergeAlternately("abcd", "pq")
    print(f"Test 3: {result}")
