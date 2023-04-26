# leetcode problem # 258. Add Digits

"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0


Constraints:
0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

"""
My solution: Modulus

Observation: when adding 1 to num, the answer also increases by 1
- unless answer is 9, then the answer becomes 1
    - the answer is 9 when num is a multiple of 9
* the answer is 0 if and only if num is 0
-> take num % 9, and add 9 if the result is 0

Leetcode calls this the digital root of a number

Runtime: O(1)
Space: O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        ans = num % 9
        if ans == 0:
            ans = 9
        return ans
