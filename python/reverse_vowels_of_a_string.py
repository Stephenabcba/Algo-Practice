# leetcode problem # 345. Reverse Vowels of a String

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""

"""
My solution: Find all the vowels

Logic:
1. Find all the vowels in the string and store them
2. Iterate through the letters in the string
- if the letter is not a vowel, directly add it to the answer string
- if the letter is a vowel, add a vowel from the back

Runtime: O(N) where N is the length of string s
- Technically, it takes time to check whether the letter is a vowel, but as the number of vowels is constant, it is not counted in the big O notation
Space: O(N) where N is the length of string s
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        reversedVowels = []
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for chara in s:
            if chara in vowels:
                reversedVowels.append(chara)

        ans = ""
        curVowel = len(reversedVowels) - 1

        for chara in s:
            if chara in vowels:
                ans += reversedVowels[curVowel]
                curVowel -= 1
            else:
                ans += chara

        return ans
