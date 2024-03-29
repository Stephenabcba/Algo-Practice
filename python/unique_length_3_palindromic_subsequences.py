# leetcode problem # 1930. Unique Length-3 Palindromic Subsequences

"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:
3 <= s.length <= 10^5
s consists of only lowercase English letters.
"""

"""
My solution: Find letters wrapped by two identical letters

For a 3-letter string to be a palindrome, the first and the last letter must be the same
    - the middle letter can be any letter
-> To find the unique palindromic subsequences, count the number of distinct letters wrapped between two identical letters

Runtime: O(N) where N is the length of string s
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        confirmedPalindrome = defaultdict(int)
        countingPalindrome = defaultdict(set)

        for letter in s:
            if letter in countingPalindrome:
                confirmedPalindrome[letter] = len(countingPalindrome[letter])
            for countingSet in countingPalindrome.values():
                countingSet.add(letter)
            countingPalindrome[letter]

        ans = 0

        for palindromeCount in confirmedPalindrome.values():
            ans += palindromeCount

        return ans
