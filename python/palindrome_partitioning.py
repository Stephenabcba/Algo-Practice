# leetcode problem # 131. Palindrome Partitioning

"""

Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

"""
My solution: Iterative Dynamic Programming

The problem can be broken into subproblems, where each subproblem can be used to
solve a larger subproblem, eventually completing the main problem
    - The subproblems are finding all partitions ending at each index, starting at the
    first letter

Logic:
1. Iterate through Each index
    a. find every palindrome ending at the index i
    b. if a palindrome ending at i doesn't start at the first index of s:
        - find all partitions that end where the palindrome starts
            - a new partition is created by adding the current palindrome to the end
            of the partitions
            - add the partition to the list of partitions ending at i
    c. if the palindrome starts at the first index of s, add it as a partition ending at i
2. Return all partitions ending at the last index

Runtime: O(2 ^ N) where N is the length of string s
Space: O(2 ^ N)
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = [[] for _ in s]

        for endIdx in range(len(s)):
            curPalindromes = []
            for palindromeLen in range(1, endIdx + 2):
                startIdx = endIdx - palindromeLen + 1
                isPalindrome = True
                for offset in range(palindromeLen // 2):
                    if s[startIdx + offset] != s[endIdx - offset]:
                        isPalindrome = False
                        break
                if isPalindrome:
                    newPalindrome = s[endIdx - palindromeLen + 1: endIdx + 1]
                    curPalindromes.append(newPalindrome)
            for palindrome in curPalindromes:
                if endIdx - len(palindrome) >= 0:
                    for prevPalindrome in palindromes[endIdx - len(palindrome)]:
                        copied = prevPalindrome[:]
                        copied.append(palindrome)
                        palindromes[endIdx].append(copied)
                else:
                    palindromes[endIdx].append([palindrome])

        return palindromes[-1]
