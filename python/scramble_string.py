# leetcode problem # 87. Scramble String

"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.


Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:
Input: s1 = "a", s2 = "a"
Output: true

Constraints:
s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.
"""

"""
Solution by leetcode: Dynamic Programming

As the problem is set up recursively where the strings are broken into smaller parts, DP can be used
to process the strings.

the DP matrix is set up with the following structure: dp[length][i][j]
where:
- length is the length of a given substring
- i is the substring of s1 beginning at index i with length length, call this substring s
- j is the substring of s2 beginning at index j with length length, call this substring t
dp[length][i][j] holds the value of whether t is a scrambled version of s
    - True if it is, False if it isn't
-> dp[n]][0][0] signifies whether s2 is a scrambled version of s1

iterate through each length from 1 to N, where N is the length of s1
-> by doing so, finding the dp of any given length takes O(1) time
    - all the substrings of the current string would have been processed

Runtime: O(N^4) where N is the length of s1 (which is the same as length of s2)
Space: O(N^3))
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)]
              for l in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for new_length in range(1, length):
                        dp1 = dp[new_length][i]
                        dp2 = dp[length-new_length][i+new_length]
                        dp[length][i][j] |= dp1[j] and dp2[j+new_length]
                        dp[length][i][j] |= dp1[j+length-new_length] and dp2[j]
        return dp[n][0][0]
