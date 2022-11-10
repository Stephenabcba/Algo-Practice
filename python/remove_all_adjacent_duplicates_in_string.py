# leetcode problem # 1047. Remove All Adjacent Duplicates In String

"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


"""
My Solution: Modify from leetcode solution of problem # 1544. Make The String Great

Using a stack, the string can be processed in one pass.

Iteratively process each letter:
- if the stack is empty or current letter is not the same as last item in the stack, push letter to the stack
- otherwise, pop from the stack.

The stack can be implemented in Python3 as a list.

After the letters have been processed, convert the stack into a string and return.

Runtime: O(N) where N is the number of letters in the string s
Space: O(N) where N is the number of letters in the string s
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for letter in s:
            if len(stack) == 0 or letter != stack[-1]:
                stack.append(letter)
            else:
                stack.pop()

        return "".join(stack)
