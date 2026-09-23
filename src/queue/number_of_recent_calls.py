"""
LeetCode 933: Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time
frame.

Implement the RecentCounter class:
- RecentCounter() Initializes the counter with zero recent requests.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and
  returns the number of requests that has happened in the past 3000 milliseconds (including the new
  request). Specifically, return the number of requests that have happened in the inclusive range [t
  - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
       [[], [1], [100], [3001], [3002]]
Output: [null, 1, 2, 3, 3]

Constraints:
- 1 <= t <= 10^9
- Each test case will call ping with strictly increasing values of t.
- At most 10^4 calls will be made to ping.
"""


class RecentCounter:
    def __init__(self):
        """
        Initialize the counter with zero recent requests.

        Time Complexity: O(1)
        Space Complexity: O(n) where n is the number of requests in the time window
        """
        # TODO: Implement initialization
        pass

    def ping(self, t):
        """
        Add a request at time t and count the recent requests.

        Args:
            t: int - time of the request in milliseconds

        Returns:
            int - number of requests in the inclusive range [t - 3000, t]

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        # TODO: Implement ping
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    recentCounter = RecentCounter()
    print(f"Ping 1: {recentCounter.ping(1)}")  # 1
    print(f"Ping 100: {recentCounter.ping(100)}")  # 2
    print(f"Ping 3001: {recentCounter.ping(3001)}")  # 3
    print(f"Ping 3002: {recentCounter.ping(3002)}")  # 3
