# leetcode problem # 5. Longest Palindromic Substring

"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
My solution: Build palindromes using DP

Observation:
A palindrome can either have a "core" of 1 or 2 letters
- if the core is 1 letter, the length of the palindrome must be odd
- if the core is 2 letters, the length of the palindrome must be even
    - the 2 letters in the core must be identical

Idea: Expand on palindromes that are valid
- all substrings with a length of 1 is a palindrome
- if a letter is followed by the same letter, it is a palindrome of size 2
- iterate for palindromes from size 3 to size n
    - the substring can only be a palindrome if its inner portion is a palindrome
        - the inner portion is the substring of size x - 2 (where x is the length of current subtring),
        and starts at i + 1 (where i is the start of the current substring)
        - this is known from previous iterations
        - if the inner portion is not a palindrome, the substring cannot be a palindrome
    - if the previous condition is true, check the first and last letter of the substring
        - if they are identical, the substring is a palindrome
        - otherwise, the substring is not a palindrome

Space Optimization: Only two dp lists are needed
- An odd dp, for substrings of size 1,3,5...
- An even dp, for substrings of size 2,4,6...
- after the current iteration is done, the results of smaller sized substrings are no longer relevant

Runtime: O(N^2) where N is the length of string s
space: O(N)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        dpOdd = [1 for _ in s]
        dpEven = [0 for _ in s]

        longestLength = 1
        longestPalindrome = s[0]

        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                dpEven[idx] = 1
                longestLength = 2
                longestPalindrome = s[idx:idx+2]

        for palindromeSize in range(3, len(s) + 1):
            for startIdx in range(len(s) - palindromeSize + 1):
                if palindromeSize % 2 == 1:
                    if dpOdd[startIdx + 1] == 1:
                        if s[startIdx] == s[startIdx + palindromeSize - 1]:
                            dpOdd[startIdx] = 1
                            longestLength = palindromeSize
                            longestPalindrome = s[startIdx:startIdx + palindromeSize]
                        else:
                            dpOdd[startIdx] = 0
                    else:
                        dpOdd[startIdx] = 0
                else:
                    if dpEven[startIdx + 1] == 1:
                        if s[startIdx] == s[startIdx + palindromeSize - 1]:
                            dpEven[startIdx] = 1
                            longestLength = palindromeSize
                            longestPalindrome = s[startIdx:startIdx + palindromeSize]
                        else:
                            dpEven[startIdx] = 0
                    else:
                        dpEven[startIdx] = 0

        return longestPalindrome
    

"""
Solution from Leetcode: Manacher's Algorithm
https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        
        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (i + 1 + palindrome_radii[i] < n and 
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]

        return longest_palindrome