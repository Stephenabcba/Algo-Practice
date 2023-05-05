# leetcode problem # 1456. Maximum Number of Vowels in a Substring of Given Length

"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""

"""
My solution: sliding window

Using a sliding window, the algorithm can check every substring for the maximum number of
vowels for the given substring length, and it only takes O(1) time to check the next substring
from the current one
    - to check the next substring, check whether the first letter in the current substring is a vowel
    (since it is getting removed), and check if the next letter is a vowel (since it is getting added)

Runtime: O(N) where N is the length of string s
Space: O(1)
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cumulativeVowels = [0]
        vowels = "aeiou"
        curVowelCount = 0

        for letter in s:
            if letter in vowels:
                curVowelCount += 1
            cumulativeVowels.append(curVowelCount)
        print(cumulativeVowels)

        ans = 0
        for startIdx in range(len(s) - k + 1):
            if cumulativeVowels[startIdx + k] - cumulativeVowels[startIdx] > ans:
                ans = cumulativeVowels[startIdx + k] - \
                    cumulativeVowels[startIdx]

        return ans
