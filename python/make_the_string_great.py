# leetcode problem # 1544. Make The String Great

"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.


Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"

Constraints:
1 <= s.length <= 100
s contains only lower and upper case English letters.
"""

"""
My solution: Repeatedly remove "bad" characters

Intuition: Find character pairs that make the string bad, and exclude them from the solution
If working from front to back, it is possible that characters are now next to each other that makes the string bad
    after the first pass, and thus the logic needs to be repeated until there are no bad character pairs

Runtime: O(N ^2) where N is the number of characters in input string s
Space: O(N) where N is the number of characters in input string s
"""


class Solution:
    def makeGood(self, s: str) -> str:
        ans = s
        oldString = ""

        while len(oldString) != len(ans):
            oldString = ans
            ans = ""
            i = 0

            while i < len(oldString) - 1:
                if abs(ord(oldString[i]) - ord(oldString[i+1])) == 32:
                    i += 1
                else:
                    ans += oldString[i]
                i += 1

            if i == len(oldString) - 1:
                ans += oldString[i]

        return ans


"""
Solution from leetcode solutions: Stack

Using a stack, the solution can be in O(N) runtime

If the current letter forms a bad pair with the top of the stack, pop from the stack
Otherwise, push the current letter to the stack

It is guaranteed that the letters in the stack always forms a good string.
- otherwise, the logic would've popped from the stack instead of pushing the character.

Runtime: O(N) where N is length of string s
Space: O(N) where N is length of string s
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for curr_char in list(s):
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)

        return "".join(stack)
