# leetcode problem # 844. Backspace String Compare

"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""

"""
My solution: Work backwards

When working from the back to the front, it can be determined which letters are kept
    - the characters not seen cannot affect the letters being processed
    - in comparison, when working from the front to the back, a letter processed now may be
        deleted by a "#" to the right of it
    - by doing so, the logic does not need to keep track of the past processed characters

Logic:
- process all the backspace characters encountered first until the current character is not "#"
    - if the current character is "#", skip the current character and the first non-"#" character to the left of it
    - if multiple "#" are encountered while skipping, skip as many characters as the "#" encountered
- if a string is fully processed while the other is not finished, the strings are not equal
    - process the "#" in the other string if needed
    - return False
- if the letters at the current indeces are not matching, the strings are not equal
    - return False
- if both strings finish at the same time, and no mismatched characters were found, the strings are equal
    - return True

Runtime: O(N) where N is the length of the longer of str s and str t
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sIdx = len(s) - 1
        sSkipCount = 0
        tIdx = len(t) - 1
        tSkipCount = 0

        while sIdx >= 0 and tIdx >= 0:
            while sIdx >= 0 and (sSkipCount > 0 or s[sIdx] == "#"):
                if s[sIdx] == "#":
                    sSkipCount += 1
                else:
                    sSkipCount -= 1
                sIdx -= 1

            while tIdx >= 0 and (tSkipCount > 0 or t[tIdx] == "#"):
                if t[tIdx] == "#":
                    tSkipCount += 1
                else:
                    tSkipCount -= 1
                tIdx -= 1

            if sIdx < 0 and tIdx < 0:
                return True
            elif sIdx < 0 or tIdx < 0:
                return False

            if s[sIdx] != t[tIdx]:
                return False
            sIdx -= 1
            tIdx -= 1


        while sIdx >= 0 and (sSkipCount > 0 or s[sIdx] == "#"):
            if s[sIdx] == "#":
                sSkipCount += 1
            else:
                sSkipCount -= 1
            sIdx -= 1

        while tIdx >= 0 and (tSkipCount > 0 or t[tIdx] == "#"):
            if t[tIdx] == "#":
                tSkipCount += 1
            else:
                tSkipCount -= 1
            tIdx -= 1

        if sIdx >= 0 or tIdx >= 0:
            return False

        return True