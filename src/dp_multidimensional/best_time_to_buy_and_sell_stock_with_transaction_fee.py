"""
LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an
integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you
need to pay the transaction fee for each transaction.

Note:
- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before
  you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by: buying at prices[0] = 1, selling at prices[3] =
8, buying at prices[4] = 4, selling at prices[5] = 9. The total profit is ((8 - 1) - 2) + ((9 - 4) -
2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
- 1 <= prices.length <= 5 * 10^4
- 1 <= prices[i] < 5 * 10^4
- 0 <= fee < 5 * 10^4
"""


class Solution:
    def maxProfit(self, prices, fee):
        """
        Find the maximum profit with a fee charged per transaction.

        Args:
            prices: List[int] - stock price on each day
            fee: int - transaction fee

        Returns:
            int - maximum profit

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxProfit([1, 3, 7, 5, 10, 3], 3)
    print(f"Test 2: {result}")
