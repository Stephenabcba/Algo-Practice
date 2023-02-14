# leetcode problem # 67. Add Binary

"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

"""
My solution: add bit by bit

Process the numbers from right to left, carrying the 1 in the sum when required.
If the numbers have different lengths, only process the longer number when the shorter number runs out of bits
If the carrying value is 1 when the longer number is also out of bits, just add 1 to the front of the current sum

Runtime: O(N) where N is the number of bits in the input numbers (length of the strings)
Space: O(N)
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        shorter = a
        longer = b
        if len(b) < len(a):
            shorter = b
            longer = a

        carryBit = 0

        for idx in range(len(shorter)):
            shorterNum = int(shorter[-idx - 1])
            longerNum = int(longer[-idx - 1])
            total = shorterNum + longerNum + carryBit
            carryBit = 0
            if total >= 2:
                carryBit = 1
            ans = str(total % 2) + ans

        lenDiff = len(longer) - len(shorter)

        while carryBit > 0:
            if lenDiff == 0:
                ans = "1" + ans
                break
            total = int(longer[lenDiff - 1]) + carryBit
            carryBit = 0
            if total >= 2:
                carryBit = 1
            ans = str(total % 2) + ans
            lenDiff -= 1

        ans = longer[:lenDiff] + ans

        return ans
