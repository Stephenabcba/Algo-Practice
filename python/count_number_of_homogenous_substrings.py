# leetcode problem # 1759. Count Number of Homogenous Substrings

"""
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 10^9 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:
Input: s = "zzzzz"
Output: 15

Constraints:
1 <= s.length <= 10^5
s consists of lowercase letters.
"""

"""
My solution: Process each homogenous substring individually

Example: s = "aaaabcca"
- s should be treated as 4 separate sections
    1. "aaaa"
    2. "b"
    3. "cc"
    4. "a"
    - even though sections 1 and 4 both only contain "a"s, they cannot combine to create different substrings

Calculating the number of combinations:
- for a substring t of length N, there are N*(N+1)/ 2 ways to make substrings out of t

Logic:
1. set up relevant variables
2. Iterate to find the homogenous substrings in s
    - when the letter is different from the previous one, a new substring has started
        - calculate the combination for the previous substring
3. return the total number of homogenous substrings

Runtime: O(N) where N is the length of string s
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        largePrime = 1000000007

        prev = ""
        prevCount = 0

        for letter in s:
            if letter == prev:
                prevCount += 1
            else:
                if prevCount > 0:
                    ans += ((prevCount * (prevCount + 1)) // 2) % largePrime
                prev = letter
                prevCount = 1

        ans += ((prevCount * (prevCount + 1)) // 2) % largePrime

        return ans
