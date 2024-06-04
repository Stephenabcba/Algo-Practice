# leetcode problem  # 409. Longest Palindrome

"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

"""
My solution: Group with dictionary

Idea: Count all the pairs, and only count 1 singles
- In a palindrome, there can be at most 1 letter with an odd count
    - that letter must be in the center
    - all other letters must be in pairs

Logic:
1. Count all the letters using a dictionary
2. Include all pairs, and at most 1 single
    - use a boolean to check if a single has been counted
        - if none has been counted, set the boolean to True when the count of a letter is odd
        - if a single has been counted, -1 to the total when the count of a letter is odd
    - add all the letters to the total length
3. Return the total length

Runtime: O(N) where N is the length of string s
Space: O(N)
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCounts = defaultdict(int)

        for letter in s:
            letterCounts[letter] += 1

        longestLength = 0
        countedSingles = False

        for freq in letterCounts.values():
            if freq % 2:
                if not countedSingles:
                    countedSingles = True
                else:
                    longestLength -= 1
            longestLength += freq

        return longestLength
