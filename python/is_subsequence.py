# leetcode problem # 392. Is Subsequence

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

"""
My solution: Two pointers

Idea: have two pointers, one for s and one for t
- if the current letter at s matches the current pointer at t, move on to the next letter in s
- move to the next letter in t regardless of whether the letters matched
- return if all letters in s have been matched at the end
    - iteration could end early if all letters in s have been matched

Runtime: O(N) where N is the length of string t
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIdx = 0
        tIdx = 0

        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]:
                sIdx += 1
            tIdx += 1

        return sIdx == len(s)

"""
Regarding the follow up: If there are a lot of s, then preprocessing could be done on t
- create a dictionary for each letter in t, where the dictionary holds the index for each of the next letter
    - i.e. there will be 26 entries in each dictionary, where key of "a" has value of the next index of "a" after the current
    letter
    - there will be len(t) dictionaries
    - it could be easier building the dictionary from the back of t to the front
        - have a dictionary holding on to the current next occurrence letters
            - make a copy for each letter in t
            - update the dictionary for each letter in t
- when processing each incoming s, traverse through the dictionary instead of checking each letter in s against t linearly
Resulting runtime: O(N + M * K) where N is length of string t, M is the max length of string s, and K is the number of incoming s
Space: O(N)
"""