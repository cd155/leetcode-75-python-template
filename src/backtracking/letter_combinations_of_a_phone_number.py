"""
LeetCode 17: Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.

2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        Generate all letter combinations for a string of phone digits.

        Args:
            digits: str - digits from 2 to 9

        Returns:
            List[str] - all possible letter combinations

        Time Complexity: O(4^n * n) where n is the number of digits
        Space Complexity: O(n) excluding the output
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.letterCombinations("23")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.letterCombinations("")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.letterCombinations("2")
    print(f"Test 3: {result}")
