# leetcode problem # 1903. Largest Odd Number in String

"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.


Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

Constraints:
1 <= num.length <= 10^5
num only consists of digits and does not contain any leading zeros.
"""

"""
My solution: Greedy Approach

Observations:
1. Whether a number is odd or even only depends on its ones digit
2. To maximize the value, include as many digits as possible without creating an even number

Logic:
1. Greedily assume that num is an odd number
2. If num is not an odd number, remove 1 digit from the right side
3. Repeat until num is an odd number
4. If num only contains even digits, return empty string

Runtime: O(logN) where N is the number represented by num
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        end = len(num) - 1

        while end >= 0 and int(num[end]) % 2 == 0:
            end -= 1

        if end < 0:
            return ""

        return num[:end+1]
