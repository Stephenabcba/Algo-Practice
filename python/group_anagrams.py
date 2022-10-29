# leetcode problem # 49. Group Anagrams

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
My solution: Count then group

Basic idea:
As anagrams are identified by their count of letters regardless of order, they can be placed together based on
comparing two strings' count of each letter.

Pseudo Code:
1. Iterate through each string in the strs list
- For each string, get the count of their letters
    - ex: "aabc" has 2 a, 1 b, and 1 c
- Store the string in such a way that it could be easily retrieved by the letter counts
    - this could be done with a dictionary, using the counts as keys and the string as value
    - as the anagrams are grouped, the dictionary would actually have a list of strings as the value
2. Convert dictionary into a list
- each item in the list is a list that was a value in the dictionary.
3. Return the list created in step 2

Runtime: O(N*L) where N is the number of strings in list strs, and L is the Length of each string in list strs
Space: O(N) where N is the number of strings in list strs
- Each string is stored as a count of their letters, which would always be 26 places
    - this could be optimized by omitting the letters that do not exist in the string.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aIdx = ord("a")
        anagramGroups = {}
        for word in strs:
            chars = [0] * 26
            for letter in word:
                chars[ord(letter) - aIdx] += 1

            charsTuple = tuple(chars)
            if charsTuple not in anagramGroups:
                anagramGroups[charsTuple] = []
            anagramGroups[charsTuple].append(word)

        ans = []
        for group in anagramGroups.values():
            ans.append(group)
        return ans
