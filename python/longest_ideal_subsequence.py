# leetcode problem # 2370. Longest Ideal Subsequence

"""
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

Constraints:
1 <= s.length <= 10^5
0 <= k <= 25
s consists of lowercase English letters.
"""

"""
My solution: Connect to the previous longest

Idea: Try to connect the current letter to the longest ideal subsequence possible
- Whether the letter connects only depends on the letter and the last letter in the subsequence
Implementation:
- Keep a dictionary of the longest ideal subsequence ending in each letter up to the current
letter
- Keep track of the length of the absolute longest ideal subsequence up to the current letter
    - also keep track of which letter the longest ideal subsequence ends with
- Iterate through each letter in the string
    1. try to connect with the absolute longest ideal subsequence
    2. If step 1 is not possible, look for the longest connectable longest subsequence
        - the absolute difference between the current letter and the ending letter is less than or equal to k
    3. In both cases, record the length of the outcome in the dictionary
        - update the absolute longest subsequence if needed

Runtime: O(M * N) where N is the length of string s, and M is the input integer k
Space: O(1), memory usage does not depend on input
- regardless of the length of s, the dictionary will have at most 26 entries, one for each letter
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        history = defaultdict(int)
        aOrd = ord("a")

        ans = 0
        ansOrd = 100

        for letter in s:
            letterOrd = ord(letter) - aOrd
            if abs(letterOrd - ansOrd) <= k:
                ans += 1
                history[letterOrd] = ans
                ansOrd = letterOrd
            else:
                longest = 0
                for prevOrd in range(max(0, letterOrd - k), min(26, letterOrd + k + 1)):
                    longest = max(longest, history[prevOrd])
                history[letterOrd] = longest + 1
                if history[letterOrd] > ans:
                    ans = history[letterOrd]
                    ansOrd = letterOrd

        return ans
