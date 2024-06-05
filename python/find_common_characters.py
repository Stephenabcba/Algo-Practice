# leetcode problem # 1002. Find Common Characters

"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

"""
My solution: Keep a list of common letters

In a list, keep a count of each common letter
- the value at index 0 is the number of common "a"s, index 1 the number of "b"s...
- The list gets update when each new word is encountered, and the total number of common letters can only maintain
its size or get smaller
    - When a new word is encountered, update the list of counts accordingly by comparing the new word's letters to
    the common letters
        - only the letters that exist in the list of common letters AND exist in the new word are kept

In the end, convert the list of count of common letters into a list of letters, with duplicate counts if needed


Runtime: O(M*N) where M is the number of words, and N is the length of each word
Space: O(N)
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []

        aOrd = ord("a")

        common = [0] * 26

        for letter in words[0]:
            common[ord(letter) - aOrd] += 1

        for word in words[1:]:
            newCommon = [0] * 26
            for letter in word:
                letterIdx = ord(letter) - aOrd
                if common[letterIdx] > 0:
                    common[letterIdx] -= 1
                    newCommon[letterIdx] += 1
            common = newCommon

        for idx in range(26):
            for freq in range(common[idx]):
                ans.append(chr(idx + aOrd))

        return ans
