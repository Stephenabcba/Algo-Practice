# leetcode problem # 1155. Number of Dice Rolls With Target Sum

"""
You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10^9 + 7.

Constraints:
1 <= n, k <= 30
1 <= target <= 1000
"""

"""
My solution: dynamic programming

The number of ways to roll a target value can be found using a bottom-up approach:
1. Starting from the very first roll, find out the number of ways to roll values below target at every roll
2. At the end, return the number of ways to roll the target

Space Optimization: As each iteration only depends on the results of the previous iteration, the results of earlier
iteration can be removed
-> Only the result of 2 iterations needs to be saved at any given time, this reduces an O(N * T) matrix to an O(T) matrix

Runtime: O(N * M * T) where N is the number of dice, M is the max value of the dice, and T is the target
Space: O(T)
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0

        bigPrime = 1000000007

        dp = [0 for _ in range(target)]

        for value in range(min(k, target)):
            dp[value] = 1

        for roll in range(1, n):
            newdp = [0 for _ in range(target)]

            for idx in range(roll - 1, target):
                for new in range(1, k + 1):
                    if idx + new <= target - 1:
                        newdp[idx + new] += dp[idx] % bigPrime

            dp = newdp

        return dp[-1] % bigPrime
