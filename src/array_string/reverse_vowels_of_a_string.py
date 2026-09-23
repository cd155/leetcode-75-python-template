"""
LeetCode 345: Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more
than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
"AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s):
        """
        Reverse only the vowels of a string.

        Args:
            s: str - input string

        Returns:
            str - string with its vowels reversed

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.reverseVowels("IceCreAm")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.reverseVowels("leetcode")
    print(f"Test 2: {result}")
