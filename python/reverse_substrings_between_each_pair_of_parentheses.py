# leetcode problem # 1190. Reverse Substrings Between Each Pair of Parentheses

"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:
1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""

"""
My solution: Use a stack

A stack is used to manage the substrings
- reverse the substrings every time a "(" is reached

Runtime: O(N ^ 2) where N is the length of s
Space: O(N)
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curStart = 0
        curEnd = 0
        for idx, letter in enumerate(s):
            if letter == '(':
                prefix = ""
                if len(stack) > 0:
                    prefix = stack.pop()
                stack.append(prefix + s[curStart:curEnd])
                stack.append("")
                curStart, curEnd = idx + 1, idx + 1
            elif letter == ')':
                x = stack.pop()[::-1]
                stack.append(stack.pop() + s[curEnd - 1:curStart - 1:-1] + x)
                curStart, curEnd = idx + 1, idx + 1
            else:
                curEnd += 1
        if curEnd > curStart:
            prefix = ""
            if len(stack) > 0:
                prefix = stack.pop()
            stack.append(prefix + s[curStart:curEnd])
        return stack[0]


"""
Solution by leetcode: "Wormhole Technique"

Algorithm
- First Pass: Pair up parentheses
    - Initialize openParenthesesIndices stack and pair vector to establish "wormhole" connections.
    - For each character:
        -If '(', push its index to openParenthesesIndices to remember its position.
        -If ')', pop from openParenthesesIndices and link both indices in pair to create the "wormhole".
- Second Pass: Build the result string
    - Initialize result string, currIndex, and direction to traverse and build the result.
    -While currIndex < input length:
        -If '(' or ')', jump through the "wormhole" using pair and reverse direction to simulate reversal.
        -Otherwise, append the character to result to build the result.
        -Move currIndex by direction to continue traversal.
Return result as the final string with all reversals simulated.

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)
