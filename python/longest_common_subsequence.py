# leetcode problem # 1143. Longest Common Subsequence

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

"""
Solution on Leetcode by eaglevn: Dynamic programming

Create a memo matrix where there the rows correspond to the length of text1
and the columns correspond to the length of text2

If the letters match, the longest subsequence increases by 1, otherwise, the longest subsequence is 
the longer of 1 fewer letter in text1 or text2

Runtime: O(N * M) where N and M are the lengths of text1 and text2, respectively
Space: O(N * M) where N and M are the lengths of text1 and text2, respectively
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Idea: memo[i][j] = memo[i-1][j-1] + 1 if text1[i] == text2[j] else max(memo[i][j-1], memo[i-1][j])
        memo = [[0 for _ in range(len(text2) + 1)]
                for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        return max((max(row) for row in memo))
        # alternatively, return memo[-1][-1]
