# leetcode problem # 91. Decode Ways

"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

"""
My solution: DP

From the bottom up, build the number of ways that the number string can be decoded.
- all single digit numbers except 0 can be decoded as a letter
- if the first digit is a 1 or 2 and overall value is less than or equal to 26, the two digits can be decoded as a letter
=> Find the number of ways to reach each index, then return the number of ways to reach the index after the last letter

Runtime: O(N) where N is the length of string s
Space: O(N)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1

        for idx in range(len(s)):
            if s[idx] != "0":
                dp[idx + 1] += dp[idx]
                if idx < len(s) - 1 and (int(s[idx]) == 1 or int(s[idx]) == 2 and int(s[idx + 1]) <= 6):
                    dp[idx + 2] += dp[idx]

        return dp[-1]
