# leetcode problem # 58. Length of Last Word

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

"""
My solution: Check from the back

Starting from the back, check the length of the last word
- skip all space characters, until the first non-space character
- count all non-space characters, until the next space appears
- return the counted characters

Runtime: O(N) where N is the length of sting s
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        while s[idx] == ' ':
            idx -= 1

        wordLength = 0
        while s[idx] != ' ' and idx >= 0:
            idx -= 1
            wordLength += 1

        return wordLength
