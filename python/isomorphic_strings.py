# leetcode problem # 205. Isomorphic Strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""

"""
My solution: Dictionary

Using a dictionary, the program can check if the mapping is consistent from one string
    to the other
To make sure that the mapping is 1:1 from both sides, 2 dictionaries are used

Runtime: O(N) where 
Space: O(1), memory usage does not depend on input
- even though the memory used is variable, the maximum memory is used when
    all 26 characters are mapped
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingS = {}
        mappingT = {}

        for idx in range(len(s)):
            if s[idx] in mappingS:
                if mappingS[s[idx]] != t[idx]:
                    return False
            else:
                mappingS[s[idx]] = t[idx]

            if t[idx] in mappingT:
                if mappingT[t[idx]] != s[idx]:
                    return False
            else:
                mappingT[t[idx]] = s[idx]

        return True
