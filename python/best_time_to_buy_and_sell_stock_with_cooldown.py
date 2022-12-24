# leetcode problem # 309. Best Time to Buy and Sell Stock with Cooldown

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

"""
My Attempt: Failed when prices keep increasing and decreasing

Greedy algorithm to always sell stock when price decreases, comparing prices
of selling 1 day earlier than the increase to gain more from doing so.

Runtime: O(N)
Space O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevIncrease = 0
        totalProfit = 0
        curPrice = prices[0]
        buyPrice = prices[0]
        earlySaleLoss = 0
        earlySaleBuyPrice = 0

        for idx, price in enumerate(prices):
            print(idx, totalProfit, earlySaleLoss, prevIncrease)
            if earlySaleLoss > 0:
                if price - earlySaleBuyPrice > earlySaleLoss:
                    prevIncrease = price - earlySaleBuyPrice
                    totalProfit += prevIncrease - earlySaleLoss
                    curPrice = earlySaleBuyPrice
                else:
                    curPrice = price
                earlySaleLoss = 0
            elif price > curPrice:
                prevIncrease = price - curPrice
                totalProfit += prevIncrease
                curPrice = price
            elif prevIncrease == 0:
                curPrice = price
            else:
                earlySaleLoss = prevIncrease
                prevIncrease = 0
                earlySaleBuyPrice = price

        return totalProfit


"""
Solution by fun4LeetCode in Solutions
General Logic for all buy/sell stock problems can be found here:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75924/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/

The problem depends on 3 variables: i, k, and m
where:
- i is the index of the day
- k is the maximum allowable trades
- m is the number of stocks owned currently

In this problem:
- i is between 0 and n-1
- k is + infinity; there is no limit on the number of stocks traded
- m is either 0 or 1; the problem only allows at most 1 stock owned at any time
* Added requirement that buying must occur 2 days after selling

3 general actions on each day
- buy
- sell
- rest(do nothing)

With limits on m, there is only 2 possible actions each day depending on whether
stock is currently held
Case 1: have stock-> can only rest or sell
Case 2: doesn't have stock -> can only rest or buy

General equation for no added requirement:
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i])

Modified equation for the 1 day cooldown requirement:
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - prices[i])

In both sets, T represents the maximum profit based on the state, where
T[i][k][m] represents maximum profit on day i holding m stocks
- as k is unlimited in this problem, it can be disregarded
- with cooldown, the buying price depends on the selling price from 2 days ago

Runtime: O(N) where N is the number of prices
Space: O(1), memory usage does not depend on input size
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t_ik0_pre = 0
        t_ik0 = 0
        t_ik1 = float("-inf")

        for price in prices:
            t_ik0_old = t_ik0
            t_ik0 = max(t_ik0, t_ik1 + price)
            t_ik1 = max(t_ik1, t_ik0_pre - price)
            t_ik0_pre = t_ik0_old

        return t_ik0
