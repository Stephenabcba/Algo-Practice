# leetcode problem # 946. Validate Stack Sequences

"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.


Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
"""

"""
My solution: Try to recreate the stack

Observations:
- At any given time, there's at most 2 options that the program can take: push or pop
- When the stack is empty, only push is available
- When all the values have been pushed, only pop is available
- Pop can only be done when the current value in the pop list matches with the top of the stack

Logic:
- Part 1: Push the values (pop if necessary)
    1. if the stack is empty, push a value to the stack
    2. if the top of the stack matches with the next value to pop, pop from the stack
    3. otherwise, push a value to the stack
- Part 2: Pop the values
    1. if the top of the stack matches with the next value to pop, pop from the stack
    2. if the values do not match, return False
- If the 2 parts complete successfully, return True

Note:
- A list can be used as a stack.

Runtime: O(N) where N is the length of pushed list
Space: O(N)
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIdx = 0
        popIdx = 0
        stack = []
        n = len(pushed)

        while pushIdx < n:
            if len(stack) > 0 and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1
            else:
                stack.append(pushed[pushIdx])
                pushIdx += 1

        while popIdx < n:
            if stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1
            else:
                return False

        return True
