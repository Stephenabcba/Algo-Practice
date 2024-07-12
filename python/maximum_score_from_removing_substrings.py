# leetcode problem # 1717. Maximum Score From Removing Substrings

"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:
1 <= s.length <= 10^5
1 <= x, y <= 10^4
s consists of lowercase English letters.
"""

"""
My Solution: Use a stack to manage the letters

Idea: Greedily choose the option yielding more points
- if x > y, remove "ab" first
- if y > x, remove "ba" first
- if x == y, it doesn't matter which one is removed first


* the below assumes x > y; if y > x, switch a and b
During iteration, choose the better option
- when the letter "a" appears: add it to the stack
- when the letter "b" appears:
    - if there's an "a" at the top of the stack:
        - remove the "a" and increase the score by x
    - otherwise, add it to the stack
- when a letter that is neither "a" nor "b" appears:
    - tally the worse option and clear the stack
    - when this happens, all the better options have been taken
        - if x > y, all the stack's "a"s come after "b"s
            - thus, only the worse option can be chosen
    - the score is increased by L * y
        - L is the lower of the counts of "a" and "b" in the stack
At the end of the iteration, tally the score for the worse option again
- the score is increased by L * y
    - L is the lower of the counts of "a" and "b" in the stack

Runtime: O(N) where N is the length of string s
Space: O(N)
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first = "a"
        second = "b"

        if y > x:
            first = "b"
            second = "a"
            x, y = y, x

        stack = []
        score = 0
        firstCount = 0
        secondCount = 0

        for letter in s:
            if letter == first:
                firstCount += 1
                stack.append(letter)
            elif letter == second:
                if len(stack) > 0 and stack[-1] == first:
                    firstCount -= 1
                    stack.pop()
                    score += x
                else:
                    secondCount += 1
                    stack.append(letter)
            else:
                score += min(firstCount, secondCount) * y
                stack = []
                firstCount = 0
                secondCount = 0

        score += min(firstCount, secondCount) * y
        return score
