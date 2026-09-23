"""
LeetCode 443: String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input
character array chars. Note that group lengths that are 10 or longer will be split into multiple
characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: Return 6, and the first 6 characters of the input array should be:
["a","2","b","2","c","3"]

Example 2:
Input: chars = ["a"]
Output: 1
Explanation: Return 1, and the first character of the input array should be: ["a"]

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Constraints:
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""


class Solution:
    def compress(self, chars):
        """
        Compress a character array in-place.

        Args:
            chars: List[str] - array of characters

        Returns:
            int - new length of the array

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    result = solution.compress(chars)
    print(f"Test 1: {result}, {chars[:result]}")

    # Test case 2
    chars = ["a"]
    result = solution.compress(chars)
    print(f"Test 2: {result}, {chars[:result]}")

    # Test case 3
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result = solution.compress(chars)
    print(f"Test 3: {result}, {chars[:result]}")
