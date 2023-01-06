# leetcode problem # 1833. Maximum Ice Cream Bars

"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.


Constraints:
costs.length == n
1 <= n <= 10^5
1 <= costs[i] <= 10^5
1 <= coins <= 10^8
"""

"""
My solution: Sort then buy the cheapest icecream bars

Intuition: The boy can buy the most ice cream bars if he buys the cheapest ones available every time
To find the cheapest ones in a faster time, sort the ice cream bars according to their cost from lowest to highest

Runtime: O(N * logN) where N is the length of costs list
Space: O(1), memory usage does not depend on input (assuming sorting is done in-place)


"""


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        iceCreams = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                iceCreams += 1
            else:
                break

        return iceCreams
