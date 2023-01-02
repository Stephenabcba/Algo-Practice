# leetcode problem # 520. Detect Capital

"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.


Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""

"""
My solution: follow instructions

To be a "right" word, the word must have all letters in upper case or upper case for
all letters after the first
"Right" Case 1: All words are capitals
"Right" Case 2: All words are lower case
"Right" Case 3: All words are lower case except the first, which is capital
-> To differentiate between the 3 cases, check the first 2 letters.
1. First letter capital -> check second letter
    - second letter capital: all letters must be capital
    - second letter capital: all letters after must be lowercase
2. First letter lower case -> all letters after must be lowercase

Runtime: O(N) where N is length of word
Space: O(1) memory usage doesn't depend on input
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowerCase = "abcdefghijklmnopqrstuvwxyz"

        wantedLetters = capitals

        if word[0] in lowerCase or word[0] in capitals and word[1] in lowerCase:
            wantedLetters = lowerCase

        for idx in range(1, len(word)):
            if word[idx] not in wantedLetters:
                return False

        return True
