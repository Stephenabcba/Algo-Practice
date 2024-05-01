# leetcode problem # 2000. Reverse Prefix of Word

"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:
1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
"""

"""
My solution: Slicing

Logic:
1. Find the range to reverse the string (the index of ch)
2. Reverse the string using string slicing
    - if ch wasn't found, return the original word instead

Runtime: O(N) where N is the length of word
Space: O(1), memory usage does not depend on input
- the memory used to create the output is ignored
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chIdx = 0

        while chIdx < len(word) and word[chIdx] != ch:
            chIdx += 1

        return word if chIdx == len(word) else word[chIdx::-1] + word[chIdx + 1:]
