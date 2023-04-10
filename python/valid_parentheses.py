# leetcode problem # 20. Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

"""
My solution: Use a stack

Observation:
When closing brackets in the correct order, the last opened bracketed must be closed first
-> This follows the same order as a stack: Last In First Out

A list is used here to function as a stack.

Logic:
1. Initiate the stack
2. Iterate through each bracket in s
    - if the bracket is an opening bracket, add it to the stack
    - otherwise:
        i. check that the stack is not empty
            - if the stack is empty, the order is invalid, return False
        ii. check that the top of the stack is the corresponding opening bracket
            - if the brackets do not match, the order is invalid, return False
        iii. if the brackets match, pop from the stack
3. Check the length of the stack at the end
    - if the stack is empty, return True
    - otherwise, there's unclosed brackets remaining, return False

Runtime: O(N) where N is the number of brackets in s
Space: O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def closeBracket(openBracket):
            if len(stack) == 0:
                return False
            if stack[-1] == openBracket:
                stack.pop()
                return True
            return False

        openBrackets = "({["

        for bracket in s:
            result = True
            if bracket in openBrackets:
                stack.append(bracket)
            elif bracket == ")":
                result = closeBracket("(")
            elif bracket == "]":
                result = closeBracket("[")
            elif bracket == "}":
                result = closeBracket("{")

            if not result:
                return False

        return len(stack) == 0
