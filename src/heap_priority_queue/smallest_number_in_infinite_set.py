"""
LeetCode 2336: Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:
- SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
- int popSmallest() Removes and returns the smallest integer contained in the infinite set.
- void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already
  in the infinite set.

Example 1:
Input: ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
       [[], [2], [], [], [], [1], [], [], []]
Output: [null, null, 1, 2, 3, null, 1, 4, 5]

Constraints:
- 1 <= num <= 1000
- At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:
    def __init__(self):
        """
        Initialize the set to contain all positive integers.

        Time Complexity: O(1)
        Space Complexity: O(n) where n is the number of integers added back
        """
        # TODO: Implement initialization
        pass

    def popSmallest(self):
        """
        Remove and return the smallest integer in the set.

        Returns:
            int - smallest integer in the set

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement popSmallest
        pass

    def addBack(self, num):
        """
        Add a positive integer back into the set.

        Args:
            num: int - integer to add back

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement addBack
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    smallestInfiniteSet = SmallestInfiniteSet()
    smallestInfiniteSet.addBack(2)
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 1
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 2
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 3
    smallestInfiniteSet.addBack(1)
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 1
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 4
    print(f"Pop: {smallestInfiniteSet.popSmallest()}")  # 5
