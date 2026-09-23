"""
LeetCode 1466: Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to
travel between two different cities (this network form a tree). Last year, The ministry of transport
decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai
to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this
city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the
minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Reverse the roads [0,1], [1,3] and [4,5] so that each city can reach city 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Reverse the roads [1,2] and [3,4] so that each city can reach city 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:
- 2 <= n <= 5 * 10^4
- connections.length == n - 1
- connections[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
"""


class Solution:
    def minReorder(self, n, connections):
        """
        Count the minimum number of roads to reorient so every city can reach city 0.

        Args:
            n: int - number of cities
            connections: List[List[int]] - directed roads [from, to]

        Returns:
            int - minimum number of edges changed

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.minReorder(3, [[1, 0], [2, 0]])
    print(f"Test 3: {result}")
