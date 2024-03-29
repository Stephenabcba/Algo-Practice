# leetcode problem # 1318. Minimum Flips to Make a OR b Equal to c

"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:
https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0

Constraints:
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""

"""
My solution: convert to binary then check bit by bit

after converting all 3 integers to binary, check each bit to see if it needs to be changed
- if the bit in C is 0, corresponding bits in both A and B must be 0
    - at most 2 changes can be made at the bit
- if the bit in C is 1, at least 1 of the bits must be 1
    - at most 1 change can be made

keep track of the number of changes and return it at the end

pad the left side of the binary with 0's if needed to make all
binary values the same length

Runtime: O(logN) where N is the largest out of a, b, and c
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        largest = max(a, b, c)
        binaryLength = len(bin(largest)) - 2

        binA = bin(a)[2:].zfill(binaryLength)
        binB = bin(b)[2:].zfill(binaryLength)
        binC = bin(c)[2:].zfill(binaryLength)

        changeCount = 0

        for idx in range(binaryLength):
            if binC[idx] == '0':
                if binA[idx] == '1':
                    changeCount += 1
                if binB[idx] == '1':
                    changeCount += 1
            else:
                if binA[idx] == '0' and binB[idx] == '0':
                    changeCount += 1

        return changeCount