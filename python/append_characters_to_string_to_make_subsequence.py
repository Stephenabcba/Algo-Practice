# leetcode problem # 2486. Append Characters to String to Make Subsequence

"""
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Example 2:
Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

Example 3:
Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.

Constraints:
1 <= s.length, t.length <= 10^5
s and t consist only of lowercase English letters.
"""

"""
My solution: 2-Pointers

Find the subsequence in s that fits t
- This can be done with 2 pointers, one in s and one in t
- If the current letter in s matches with the current letter in t, increment the pointer in t
- Regardless of matches, increment the pointer in s

At the end, the remaining part of t needs to be appended to s to make t a subsequence of s

Runtime: O(N) where N is the length of s
Space: O(1) Memory usage does not depend on input
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sIdx = 0
        tIdx = 0

        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]:
                tIdx += 1
            sIdx += 1

        return len(t) - tIdx
