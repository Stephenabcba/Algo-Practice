# leetcode problem # 879. Profitable Schemes

"""
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.


Example 1:
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.

Example 2:
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

Constraints:
1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
"""

"""
Solution By Leetcode: Iterative DP (originally in Java)

The possible steps that can be taken is based on the state defined by the current number of people, profit made,
and the current crime index
    - regardless of the steps taken before, the possibile steps are always the same given the same state
-> memoization can be used to eliminate redundant processing

By using an iterative approach, there is no overhead in call stacks like the recursive approach.

Runtime: O(N * M * K) where N is the maximum number of members, M is the length of list group, and K is minProfit
Space: O(N * M * K)
"""


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        mod = 1000000007
        dp = [[[0 for _ in range(minProfit + 1)] for __ in range(n + 1)]
              for ___ in range(len(group) + 1)]

        for count in range(n + 1):
            dp[len(group)][count][minProfit] = 1

        for index in range(len(group) - 1, -1, -1):
            for count in range(n + 1):
                for profit in range(minProfit + 1):
                    dp[index][count][profit] = dp[index + 1][count][profit]
                    if count + group[index] <= n:
                        dp[index][count][profit] = (
                            dp[index][count][profit] + dp[index + 1][count + group[index]][min(minProfit, profit + profits[index])]) % mod

        return dp[0][0][0]
