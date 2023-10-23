# leetcode problem # 342. Power of Four

"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""

"""
My solution: Keep dividing by 4

If x is a power of 4, x can be divided by 4 y times (with the result being 1), where 4^y == x
- using this idea, keep dividing any integer n by 4 until it is less than 4, then check if the result is 1

Edge case: If n < 1, n can never be a power of 4
- always return False in this case

Runtime: O(logN) where N is the input integer
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
            
        while not n % 4:
            n = n // 4
        return n == 1