# leetcode problem # 316. Remove Duplicate Letters

"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""

"""
My solution: stack with dictionary

Logic:
1. Create a dictionary that keeps track of the last occurrence index of each letter in s
2. Create a stack to hold the letters to be returned
3. Iterate through string s
    - skip the letter if it is already in the stack
    - remove the letter from the top of the stack if that letter fits the following conditions:
        1. has a higher value than the current letter, and
        2. has another instance of the letter further down the string s
            - this can be checked with the dictionary created before
4. Return the answer at the end, which is the stack converted into a string

Runtime: O(N) where N is the number of letters in s
Space: O(K) where K is the size of the available character set. It is a constant of 26 in this problem
    - it could be written as O(1)
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurrence = {}

        for idx in range(len(s)):
            lastOccurrence[s[idx]] = idx

        stack = []
        for idx in range(len(s)):
            if s[idx] not in stack:
                while len(stack) > 0 and s[idx] < stack[-1] and lastOccurrence[stack[-1]] > idx:
                    stack.pop()
                stack.append(s[idx])

        return "".join(stack)