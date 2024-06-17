# leetcode problem # 633. Sum of Square Numbers

"""
Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Constraints:
0 <= c <= 2^31 - 1
"""

"""
My solution: Improved Brute Force

Observation: The highest value that a or b can be is sqrt(c)
-> Only need to check values from 0 to sqrt(c)

Logic:
1. Initialize a to the largest integer below sqrt(c), and b to 0
    - throughout iteration, a >= b
        - although the problem allows b > a, the outcome is simply swapping the places of a and b
2. Iterate and check the sums of a ^ 2 + b ^ 2, until a < b (or the sum == c)
    - if the sum is smaller than c, increment b
    - if the sum is larger than c, decrement a
    - if the sum is c, return True
3. If none of the sums == c, return False

Runtime: O(N) where N is the integer c
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = math.floor(sqrt(c))
        b = 0
        while a >= b:
            curSum = a ** 2 + b ** 2
            if curSum == c:
                return True
            elif curSum < c:
                b += 1
            else:
                a -= 1
        return False


"""
Solution by leetcode: Binary Search

Runtime: O(sqrt(c) * log c) where c is the input integer c
Space: O(log c)
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binarySearch(s, e, n):
            if s > e:
                return False
            mid = (e + s) // 2
            if mid * mid == n:
                return True
            if mid * mid > n:
                return binarySearch(s, mid - 1, n)
            return binarySearch(mid + 1, e, n)

        for a in range(math.floor(sqrt(c)) + 1):
            b = c - a * a
            if binarySearch(0, b, b):
                return True
        return False
