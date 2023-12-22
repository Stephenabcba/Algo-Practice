# leetcode problem # 1422. Maximum Score After Splitting a String

"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3

Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""

"""
My solution: Two passes preprocessing

By counting the one's before running the main loop, the algorithm can keep track of the number of
one's on the right side of the split in O(1) time during iteration.

In the main loop, the split is placed after the number in the current iteration
* The split cannot be placed after the last number, as both sides need to be non-empty
    -> skip the last number during iteration
During iteration:
1. Increase the count of zero's when encountered
2. Decrease the count of one's when encountered
3. Keep track of the highest number of zero's and one's recorded

Runtime: O(N) where N is the length of string s
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maxScore(self, s: str) -> int:
        oneCount = 0
        zeroCount = 0
        ans = 0

        for num in s:
            if num == '1':
                oneCount += 1

        for num in s[:-1]:
            if num == '0':
                zeroCount += 1
            else:
                oneCount -= 1

            if zeroCount + oneCount > ans:
                ans = zeroCount + oneCount

        return ans
