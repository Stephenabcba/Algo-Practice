# leetcode problem # 1052. Grumpy Bookstore Owner

"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

Constraints:
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 10^4
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
"""

"""
My solution: Sliding Window

Idea: Keep a sliding window of dissatisfied customers, and choose the window with the most number of dissatisfied customers
- If the storekeeper is not grumpy at x minute, all customers at x minute is satisfied, and do not contribute to the sliding window
- The size of the sliding window is determined by the input integer "minutes"

At the end, add the number of already satisfied customers to the largest window of dissatisfied customers to get the total value

Runtime: O(N) where N is the number of minutes the store is open
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfaction = 0
        maxPotential = 0

        potential = 0

        for idx in range(len(customers)):
            if not grumpy[idx]:
                satisfaction += customers[idx]
            else:
                potential += customers[idx]
            if idx >= minutes and grumpy[idx - minutes]:
                potential -= customers[idx - minutes]
            maxPotential = max(maxPotential, potential)

        return satisfaction + maxPotential
