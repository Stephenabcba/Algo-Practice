# leetcode problem # 746. Min Cost Climbing Stairs

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

"""
My solution: Dynamic Programming

To clarify from the problem description, the final step is the nth step, not n-1th step.
- ex: if there are 5 steps (indexed 0 to 4), ending up at the 4th step requires the user to pay the cost of climbing the 4th step to reach the 5th step

The cost of reach any step is based on the cost to reach the previous 2 steps and the cost to move up from those steps
Option 1: Start from 2 steps below and pay the cost to climb from 2 steps below
Option 2: Start from 1 step below and pay the cost to climb from 1 step below
-> Always choose the cheaper of two options
* as the problem allows for the option of starting from 0th or 1st step, both steps have costs of 0.
=> Find the cheapest cost of reach every step iteratively, then return the cost of reaching the nth step

Runtime: O(N) where N is the length of cost list
Space: O(N)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in cost]
        dp.append(0)

        for idx in range(2,len(cost) + 1):
            dp[idx] = min(dp[idx - 1] + cost[idx - 1], dp[idx - 2] + cost[idx - 2])

        return dp[-1]