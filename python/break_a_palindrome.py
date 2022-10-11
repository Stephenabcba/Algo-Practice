# leetcode problem # 1328. Break a Palindrome

"""
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.


Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

"""
My solution: Follow observation

Observation 1: It seems that the algorithm should change the first non-"a" letter to "a"
Observation 2: Changing the center letter of a palindrome with length of an odd number would not break the palindrome

Resulting Logic:
* Edge case:
- If the palindrome is an empty string or has a length of 1, it is impossible to break the palindrome
    - return "" as the problem requires.

1. Iterate through the first half of the palindrome (excluding the center letter in odd-length palindromes)
    - Find the first letter that isn't an "a"
        - return the string with the found letter replaced with an "a"
2. If the iteration finished without returning, all letters (except the center letter of odd-length palindromes) must be "a"
- Replace the last letter with "b"

Modifying the palindrome: as strings are immutable, the string has to be rebuilt
- this can be done using string slicing and concatenation

Runtime: O(N) where N is the number of letters in the palindrome
- The iteration runs at most N/2 times
- The replacement process takes O(N) times due to slicing
    - This process will occur exactly once in every function call except for the edge case.
Space: O(N) where N is the number of letters in the palindrome
- The new string must be created to be returned
    - Strings are immutable
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        for idx in range(0, len(palindrome) // 2):
            if palindrome[idx] is "a":
                continue
            else:
                return palindrome[:idx] + "a" + palindrome[idx + 1:]
        return palindrome[:-1] + "b"
