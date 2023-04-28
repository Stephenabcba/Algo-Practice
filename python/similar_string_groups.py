# leetcode problem # 839. Similar String Groups

"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  
Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?


Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1

Constraints:
1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""

"""
My solution: DFS

Each similar string group can be seen as a graph of words, where the edges connect 2 words that are similar

Using DFS, the graph can be traversed to find all nodes in the group

DFS may need to be initiated multiple times to find all the groups
- every time DFS is initiated, a new group is created

Runtime: O(N ^ 2 * M) where N is the number of words in strs and M is the length of each word
Space: O(N)
"""


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ans = 0
        memo = [False for _ in strs]

        def dfs(idx):
            for otherWordIdx in range(len(strs)):
                if not memo[otherWordIdx]:
                    difference = 0
                    for letterIdx in range(len(strs[idx])):
                        if strs[idx][letterIdx] != strs[otherWordIdx][letterIdx]:
                            difference += 1
                            if difference > 2:
                                break
                    if difference <= 2:
                        memo[otherWordIdx] = True
                        dfs(otherWordIdx)

        for idx in range(len(strs)):
            if not memo[idx]:
                memo[idx] = True
                ans += 1
                dfs(idx)

        return ans
