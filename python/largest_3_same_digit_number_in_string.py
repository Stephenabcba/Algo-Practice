# leetcode problem # 2264. Largest 3-Same-Digit Number in String

"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

Example 1:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

Constraints:
3 <= num.length <= 1000
num only consists of digits.
"""

"""
My solution: 1 pass iteration

Find consecutive numbers with legnths longer than 3, and save the value of the largest one.

Runtime: O(N) where N is the length of string num
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -1

        cur = -1
        curLen = 1

        for number in num:
            if int(number) == cur:
                curLen += 1
                if curLen == 3 and cur > largest:
                    largest = cur
                    if largest == 9:
                        return "999"
            else:
                cur = int(number)
                curLen = 1

        if largest >= 0:
            return str(largest) * 3

        return ""
