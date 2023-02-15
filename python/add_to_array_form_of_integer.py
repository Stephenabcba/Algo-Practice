# leetcode problem # 989. Add to Array-Form of Integer

"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:
1 <= num.length <= 10^4
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 10^4
"""

"""
My solution: perform addition digit by digit

Intuition:
When performing addition by hand, start from the 1's place and perform
additions from right to left.
Carry values over to the next addition as needed

Runtime: O(N + logM) where N is the length of input list num and M is the input integer k
Space: O(N + logM)
"""


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        powerOf10 = 0
        carry = 0

        while k > 0 or carry > 0:
            val = k % 10
            k = k // 10
            if len(num) < powerOf10 + 1:
                num.insert(0, 0)
            powerOf10 += 1
            total = val + num[-powerOf10] + carry
            carry = 0
            if total >= 10:
                carry = 1
                total -= 10
            num[-powerOf10] = total

        return num
