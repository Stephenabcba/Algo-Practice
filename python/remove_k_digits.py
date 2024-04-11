# leetcode problem # 402. Remove K Digits

"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

"""
My solution: Use a stack

Observation: Reducing the value of larger digits has a greater effect in reducing the overall value
-> minimize the front of num as much as possible

Logic: Keep a stack of all the values to keep
- if values can still be removed, remove all values larger than the current value in the stack
- otherwise, add the value to the stack
* do not add leading 0's to the stack
=> The front of the stack should be non-decreasing, until no more values can be removed

Convert the stack to a string and return at the end

Runtime: O(N) where N is the length of num
Space: O(N)
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = [num[0]]
        removeCount = 0
        idx = 1
        while idx < len(num):
            while len(stack) > 0 and num[idx] < stack[-1] and removeCount < k:
                stack.pop()
                removeCount += 1
            if len(stack) > 0 or num[idx] != "0":
                stack.append(num[idx])
            idx += 1

        while removeCount < k and len(stack) > 0:
            stack.pop()
            removeCount += 1

        ans = "".join(stack)
        return ans if len(ans) > 0 else "0"
