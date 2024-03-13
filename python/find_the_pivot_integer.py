# leetcode problem # 2485. Find the Pivot Integer

"""
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.


Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.


Constraints:
1 <= n <= 1000
"""

"""
My solution: Math

The relationship between the pivot X and the input N can be shown as the following:
X * (X+1) / 2 = N * (N+1) / 2 - X * (X+1) / 2 + X
- this makes use of the definition of the pivot by the problem, and the formula for
sum from 1 to any number M

After simplifying, the relationship is:
X = sqrt((N^2 + N) / 2)

From problem constraints (and logically from summing up integers), the pivot X
can only be an integer.
-> If the X derived from the relationship is a whole number, X is the pivot value
    - if X is not a whole number, N does not have a pivot

** This solution came up when trying to find inputs with pivot integers,
original plan was to implement a binary search
    - an input with pivot integer N must satisfy these conditions:
        1. N must be a perfect square or 2x a perfect square
        2. N + 1 must be 2x a perfect square or a perfect square
        - ex: N = 8: N is 2x 4, and N+1 is 9; 4 and 9 are perfect squares
        - ex2: N = 49: N is 49, and N+1 is 2x 25; 49 and 25 are perfect squares

Runtime: O(1), the runtime does not depend on input
Space: O(1)
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        a = sqrt((n ** 2 + n) / 2)
        if (a == int(a)):
            return int(a)
        return -1
