# leetcode problem # 516. Longest Palindromic Subsequence

"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

"""
My solution: Dynamic Programming

Intuition:
1. Try to "unwrap the onion", where if the first letter matches the last letter, the longest palindromic subsequence is 2 + the result 
of the "inner core", which is the rest of string s enclosed within the first and last letter
2. if the letters do not match, try removing 1 letter
- it is unknown which letter should be removed
-> try both possiblities

Using a memo, repeated cases can be eliminated

Recursion Logic:
- if the length is 0, there can't be any palindrome
- if the string is seen before, return the answer from the memo
    - the string can be identified by the starting index and length
    - the memo is initialized such that all strings of length 1 have a longest palindromic subsequence of 1
- if the first letter matches the last letter, return 2 + the "core", with start + 1 and length - 2
- otherwise, return the maximum of removing 1 letter from either end

Runtime: O(N^2) where N is the length of string s
Space: O(N^2)
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for _ in s] for __ in range(len(s) + 1)]
        for idx in range(len(s)):
            dp[0][idx] = 0
            dp[1][idx] = 1

        def recurse(start, length):
            if length <= 0:
                return 0
            if dp[length][start] >= 1:
                return dp[length][start]
            if s[start] == s[start + length - 1]:
                dp[length][start] = recurse(start + 1, length - 2) + 2
                return dp[length][start]
            else:
                dp[length][start] = max(
                    recurse(start, length - 1), recurse(start + 1, length - 1))
                return dp[length][start]
        return recurse(0, len(s))
