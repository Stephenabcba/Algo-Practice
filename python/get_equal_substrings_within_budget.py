# leetcode problem # 1208. Get Equal Substrings Within Budget

"""
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

Constraints:
1 <= s.length <= 10^5
t.length == s.length
0 <= maxCost <= 10^6
s and t consist of only lowercase English letters.
"""

"""
My solution: Sliding Window

One of the ways to check for the longest substrings is to check the longest substrings ending
at each index

The sliding window approach can quickly find the substrings above
- Iterate through every index in s (or t, they're the same length)
    - include a new letter to the window
        - the costs associated to the letter is added
    - shorten the window until the cost of everything in the window is below max cost
    - check if the length of the window is the longest seen so far
- Return the longest window length at the end

Runtime: O(N) where N is the length of s (or t)
Space: O(N)
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0
        q = deque()
        highest = 0

        for idx in range(len(s)):
            cost = abs(ord(s[idx]) - ord(t[idx]))
            q.append(cost)
            curCost += cost
            while curCost > maxCost:
                curCost -= q.popleft()
            highest = max(len(q), highest)

        return highest
