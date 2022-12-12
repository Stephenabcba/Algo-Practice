# leetcode problem # 70. Climbing Stairs

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

"""
My solution: Dynamic Programming

Observation 1:
For any integer N where N > 2, there are 2 paths to reach N using the given premise.
1. start with 1, and there are x ways to reach 1 + (N - 1)
2. start with 2, and there are y ways to reach 2 + (N - 2)
Thus, there are x + y ways to reach N from 0
If working sequentialling finding the number of ways to reach all integers from 0 to N,
x and y are known when N is processed

Observation 2:
The pattern found in observation one closely resembles the fibonacci sequence
-> After comparing, the sequence perfectly follows the fibonacci sequence.
    - except the start, where fidonacci sequence begins with 0, 1, 1, 2, 3...

Processing everything iteratively from 1 to N, every value n where n > 2 is based on values
<= n, which makes it a good candidate to use dynamic programming on.

Runtime: O(N) where N is the input integer n
Space: O(N) where N is the input integer n
"""


class Solution:

    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n > len(dp):
            startIdx = len(dp)
            for idx in range(startIdx, n + 1):
                dp.append(dp[idx - 1] + dp[idx - 2])

        return dp[n - 1]
