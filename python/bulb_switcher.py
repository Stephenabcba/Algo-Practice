# leetcode problem # 319. Bulb Switcher

"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.


Example 1:
https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 1


Constraints:
0 <= n <= 10^9
"""

"""
My solution: Derived from observation

Observation: the number of bulbs turned on remains the same
as n increases until n reaches the next perfect square, then
the number increments by 1

Explanation from leetcode solutions:
- All values except perfect squares have an even number of factors,
    where N = X * Y
- Perfect squares have an odd number of factors, as it includes
    1 set of factor where N = X * X, forming the perfect square
- When the switch is toggled an even amount of times, the lightbulb
    is off
- When the switch is toggled an odd amount of times, the lightbulb
    is on
-> the problem becomes counting the number of perfect squares from
    1 to N
    - this turns out to be the floor of square root of N
        - every whole number in the square root of N represents a
        perfect square


Runtime: O(1)
Space: O(1)
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return floor(n ** (1/2))
        # improved solution:
        # return int(sqrt(n))
