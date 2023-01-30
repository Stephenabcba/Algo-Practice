# leetcode problem # 1137. N-th Tribonacci Number

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

"""
My solution: Dynamic programming

As T_n depends on previous results when n >= 3, dynamic programming can be used
to iteratively build up an array of tribonacci numbers, up to T_n

Runtime: O(N) where N is the input integer n
Space: O(N)
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1]

        while n > len(tribonacci) - 1:
            tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])

        return tribonacci[n]
