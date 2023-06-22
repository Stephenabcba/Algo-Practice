# leetcode problem # 714. Best Time to Buy and Sell Stock with Transaction Fee

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
"""

"""
My solution: dynamic programming

Intuition: On any given day, there are two states available: owning a stock and not owning a stock
- If choosing not to own a stock, there are two options:
    1. continuing to not own the stock from the day before
    2. selling the stock from the day before
    -> choose the option that yields the highest profit
- If choosing to own a stock, there are three options:
    1. Buying a stock at a lower price than the day before, but continuing the price from owning the stock the day before
    2. Holding a stock from the day before, and continuing the price from owning the stock from the day before
    3. Buying a new stock, when there's no stock from the day before
    -> choose the option that yields the highest profit
        - if the day's stock prices are lower than previous day's stock prices, use the day's prices
        - if the day's stock prices are higher than the previous day's prices, decide whether holding the stock is better
            or buying new stock is better

In all cases, each day's state depends on the state of the day before, so DP is a good solution to use.

To account for the trading fee, incorporate the fee into the price when buying the stock

Improvement: Since the prices only depend on the day before, the logic only needs to keep track of 2 days of profits in total
-> Memory usage is reduced to constant space.

Runtime: O(N) where N is the length of prices list
Space: O(N)
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[[0,0], 0] for price in prices]
        dp[0][0][1] = prices[0] + fee

        for idx, price in enumerate(prices):
            if idx > 0:
                if price + fee <= dp[idx - 1][0][1]:
                    dp[idx][0][1] = price + fee
                    dp[idx][0][0] = max(dp[idx - 1][0][0], dp[idx - 1][1])
                else:
                    if dp[idx - 1][0][0] - dp[idx - 1][0][1] > dp[idx - 1][1] - price - fee:
                        dp[idx][0][0] = dp[idx - 1][0][0]
                        dp[idx][0][1] = dp[idx - 1][0][1]
                    else:
                        dp[idx][0][0] = dp[idx - 1][1]
                        dp[idx][0][1] = price + fee
                dp[idx][1] = max(dp[idx - 1][1], dp[idx - 1][0][0] + price - dp[idx - 1][0][1])
            

        return dp[-1][1]