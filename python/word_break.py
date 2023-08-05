# leetcode problem # 139. Word Break

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

"""
My solution: DP

Idea: Break the problem down into smaller subproblems
- As long as len(s) >= 2, S can be split into two strings s1 and s2
    - s1 should be a word in wordDict
    - s2 would be the remaining letters in s
-> The problem becomes finding whether s2 can be composed of words in wordDict
    - repeat for all words that could match
- Create a boolean list "reachable", with each index corresponding to indeces in s
    - if words can be concatenated to match s up to index i, then i is considered reachable
        - set the reachable[i] to True
    - if the last index in reachable is True, then return True
        - otherwise, return False

To facilitate finding words that match, group words in wordDict by their initials.
- for any string s, only words that have the same initial as s could be matched at the start of s

Runtime: O(N * M * L) where N is the length of string s, M is the size of word dictionary, and L is the length of each
word in word dictionary
Space: O(M*L + N)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        newDict = {}
        for word in wordDict:
            if word[0] not in newDict:
                newDict[word[0]] = []
            newDict[word[0]].append(word)

        reachable = [False for _ in range(len(s) + 1)]

        for entry in newDict.values():
            entry.sort(key=lambda x:len(x), reverse=True)

        def recurse(start):
            if start > len(s) or reachable[start]:
                return
            reachable[start] = True
            if start == len(s):
                return

            for word in newDict.get(s[start], []):
                if start + len(word) <= len(s) and s[start:start + len(word)] == word:
                    recurse(start + len(word))

        recurse(0)

        return reachable[-1]