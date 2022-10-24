# leetcode problem # 1239. Maximum Length of a Concatenated String with Unique Characters

"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

"""
Solution from leetcode discussion by pniraj657

Keep a list of valid word concatenation strings
Keep track of the highest valid word length encountered
For each word in the arr array, check if the word can be concatenated to any valid string to create a longer valid string
- if the resulting string is still valid (no duplicated letters), add the result string to the list
    - to check if a word is valid, check if its length is equal to its length when converted to a set
        - as sets do not allow duplicates, the word is valid if the lengths are equal.


Runtime: O(M * N^2) where M is the maximum length of each word and N is the number of words in arr array
Space: O(M * N^2) where M is the maximum length of each word and N is the number of words in arr array
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        res = [""]

        op = 0

        for word in arr:
            for r in res:
                newRes = r + word
                if len(newRes) != len(set(newRes)):
                    continue
                res.append(newRes)
                op = max(op, len(newRes))
        return op
