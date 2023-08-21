# leetcode problem # 459. Repeated Substring Pattern

"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""

"""
My solution: Check all possible substrings

It is only possible to repeat a substring X to create S if len(S) % len(X) == 0
- Thus, it is only required to check substrings with lengths that meet the requirement above

Check if the substrings can be repeated to create S by checking every single letter against the substring
- If it is possible, return True
- Otherwise, move on to the next substring
- If none of the substrings can be repeated to create S, return False

Runtime: O(logN * N), where N is the length of string s
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for subStringLength in range(1, n // 2 + 1):
            if n % subStringLength == 0:
                isRepeatable = True
                for idx in range(subStringLength, n):
                    if s[idx] != s[idx % subStringLength]:
                        isRepeatable = False
                        break
                if isRepeatable:
                    return True
        return False