# leetcode problem # 1768. Merge Strings Alternately

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

"""
My solution: 2 pointers

Using 2 pointers, the problem can be done by adding the letters at the pointer location
and incrementing the pointers.

Possible Optimization from leetcode: 1 pointer & single loop
- as the pointers move at the same pace, only 1 pointer is needed
- the logic can be done in 1 while loop, with 2 if statements in the loop

Runtime: O(M + N) where M is length of string word1 and N is length of string word2
Space: O(1), memory usage does not scale with input except the returned string
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = ""
        while i < len(word1) and j < len(word2):
            ans += word1[i] + word2[j]
            i += 1
            j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return ans
