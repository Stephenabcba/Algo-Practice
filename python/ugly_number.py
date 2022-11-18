# leetcode problem # 263. Ugly Number

"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.


Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 x 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
-2^31 <= n <= 2^31 - 1
"""

"""
My solution: divide by 2,3,5 as much as possible

By definition, a number A is a factor of another number B if B is fully divisible by A
- it is possible that B can be fully divided by A multiple times.

Thus, to check whether a number has any other prime factors, keep dividing the number
by 2, 3, or 5 as long as the quotient is a whole number.
- As 2, 3, and 5 are not factors of each other, it doesn't matter which value the number is divided by
    first.

Note: any value below (including) 0 is never an ugly number, and thus does not
need to processed through division.

Runtime: O(log N) where N is the input integer N
Space: O(1), memory usage should not scale with input.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n /= 2

        while n % 3 == 0:
            n /= 3

        while n % 5 == 0:
            n /= 5

        return n == 1
