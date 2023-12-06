# leetcode problem # 1716. Calculate Money in Leetcode Bank

"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
1 <= n <= 1000
"""

"""
My solution: Math

For every full week, Hercy deposits 28 + (week# - 1) * 7
    - on week 2, he deposits 2+3+4+5+6+7+8, which can be rewritten as (1+2+3+4+5+6+7) + (1+1+1+1+1+1+1)
        - this can be rewritten in the form above, where the first part always sums to 28, and the second part is 7 times the week # - 1
Using the summation formula, he deposits 28 * x + x * (x-1) / 2 for x full weeks

For the remaining days less than 1 week, the sum equals (remaining * (remaining + 1)) // 2 + remaining * weeks

By adding the amount from full weeks and from remaining days together, the total amount deposited can be found.

Runtime: O(1), runtime does not depend on input
Space: O(1)
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remaining = n % 7

        return 28 * weeks + 7 * (weeks * (weeks - 1)) // 2 + (remaining * (remaining + 1)) // 2 + remaining * weeks
